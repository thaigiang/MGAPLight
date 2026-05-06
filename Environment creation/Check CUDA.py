import torch, os
print("Torch:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("CUDA runtime:", torch.version.cuda)
    print("GPU:", torch.cuda.get_device_name(0))
print("SUMO_HOME:", os.environ.get("SUMO_HOME"))


from sumo_rl import parallel_env
import os
env = parallel_env(
    net_file=r"E:\Work\FPT University\#Documents\PhD\Paper 4 - Multi Agents\map\4x4.net.xml",
    route_file=r"E:\Work\FPT University\#Documents\PhD\Paper 4 - Multi Agents\map\4x4c1c2c1c2.rou.xml",
    use_gui=False,
    num_seconds=60,
    fixed_ts=True,          # run fixed-time
    delta_time=5,
    yellow_time=3,
)
obs, _ = env.reset(seed=0)
for _ in range(12):         # 12 steps x 5s = 60s
    actions = {a: 0 for a in obs.keys()}  # action dummy
    obs, rew, term, trunc, info = env.step(actions)
env.close()
print("Smoke test OK")
