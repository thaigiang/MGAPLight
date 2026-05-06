import os, warnings
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"   # cho phép 2 runtime cùng tồn tại (workaround)
os.environ["MKL_SERVICE_FORCE_INTEL"] = "1"   # ép dùng Intel OMP nếu MKL xuất hiện
os.environ["OMP_NUM_THREADS"] = "1"           # tránh oversubscription (tùy chọn)
warnings.filterwarnings("ignore", category=DeprecationWarning)

from ray.rllib.algorithms.ppo import PPOConfig
from ray.tune.registry import register_env
from ray.rllib.env.wrappers.pettingzoo_env import ParallelPettingZooEnv
from sumo_rl import parallel_env as sumo_parallel

NET = r"E:\Work\FPT University\#Documents\PhD\Paper 4 - Multi Agents\map\4x4.net.xml"
ROU = r"E:\Work\FPT University\#Documents\PhD\Paper 4 - Multi Agents\map\4x4c1c2c1c2.rou.xml"

def make_env(cfg=None):
    cfg = dict(cfg or {})
    cfg.setdefault("net_file", NET)
    cfg.setdefault("route_file", ROU)
    cfg.setdefault("num_seconds", 120)
    cfg.setdefault("fixed_ts", False)
    cfg.setdefault("use_gui", False)
    cfg.setdefault("delta_time", 5)
    cfg.setdefault("yellow_time", 3)
    return sumo_parallel(**cfg)

def env_creator(env_config):
    return ParallelPettingZooEnv(make_env(env_config))

register_env("4x4grid", env_creator)

algo = (PPOConfig()
        .environment("4x4grid")
        .framework("torch")
        .resources(num_gpus=1)          # dùng GPU nếu có
        .rollouts(num_rollout_workers=0) # tránh worker từ xa
        .build())

# Train vài iteration ngắn
for i in range(2):
    res = algo.train()
    print(f"Iter {i} reward_mean:", res.get("episode_reward_mean"))

algo.cleanup()
print("RLlib smoke OK")
