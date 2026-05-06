import os
from sumo_rl import parallel_env

net = r"E:\Work\FPT University\#Documents\PhD\Paper 4 - Multi Agents\map\4x4.net.xml"
rou = r"E:\Work\FPT University\#Documents\PhD\Paper 4 - Multi Agents\map\4x4c1c2c1c2.rou.xml"

env = parallel_env(
    net_file=net,
    route_file=rou,
    fixed_ts=True,
    num_seconds=60,
    use_gui=False,
    delta_time=5,
    yellow_time=3,
)
obs, _ = env.reset(seed=0)
steps = 0
while True:
    actions = {a: 0 for a in obs.keys()}  # fixed phase 0
    obs, rew, term, trunc, info = env.step(actions)
    steps += 1
    if all({**term, **trunc}.values()):
        break
env.close()
print("SUMO smoke OK with steps:", steps)
