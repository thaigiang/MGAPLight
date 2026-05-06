# MGAPLight: Multi-Agent Graph Attention PPO for Adaptive Traffic Signal Control

This repository contains the official implementation of **MGAPLight**, a decentralized multi-agent reinforcement learning framework for adaptive traffic signal control in mixed-traffic urban networks.

MGAPLight combines:

- Ego-graph observation construction
- Multi-head graph attention for neighborhood encoding
- Shared-parameter multi-agent PPO
- Decentralized execution for multi-intersection traffic signal control
- SUMO-based microscopic traffic simulation

The framework is designed for traffic networks where multiple signalized intersections interact through upstream–downstream traffic propagation and where heterogeneous vehicle types coexist, including bikes, passenger cars, buses, and trucks.

---

## Paper

**MGAPLight: A Decentralized Multi-Agent PPO Framework with Graph Attention for Adaptive Traffic Signal Control in Mixed-Traffic Networks**

Authors:

- Do Thai Giang
- Phan Duy Hung
- Truong Cong Doan

This work studies decentralized adaptive traffic signal control under mixed-traffic conditions. Each intersection is modeled as an agent that observes local traffic states and neighboring intersection information through an ego-graph representation. A multi-head graph attention encoder is used to aggregate neighborhood information before the actor and critic heads make traffic signal control decisions.

---

## Key Features

- **Decentralized multi-agent control**  
  Each traffic light agent selects actions based on its own ego-graph observation.

- **Graph-aware observation design**  
  Each intersection augments its local observation with neighboring observations and relative positional offsets.

- **Multi-head graph attention encoder**  
  The model learns adaptive attention weights over neighboring intersections.

- **Shared-parameter PPO**  
  All agents share the same actor–critic network parameters, improving scalability and sample efficiency.

- **Mixed-traffic simulation**  
  The simulation includes heterogeneous vehicle types such as bikes, passenger cars, buses, and trucks.

- **SUMO-based evaluation**  
  Experiments are conducted using SUMO, TraCI, SUMO-RL, PettingZoo, Ray RLlib, and PyTorch.

---

## Experimental Scenarios

The experiments are conducted on a 4×4 grid traffic network under five representative traffic scenarios:

1. Low demand
2. Medium demand
3. High demand
4. Directional imbalance
5. Time-varying demand

The main evaluation metric is **total waiting time**, with additional analysis of step-wise waiting time and PPO training metrics such as reward mean, policy loss, value-function loss, entropy, and KL divergence.

---

## Compared Methods

The repository supports experiments with the following learning-based controllers:

- `MAPPO-Base`  
  Local-observation-only MAPPO without graph-based neighborhood aggregation.

- `Cooperative agents with MAPPO`  
  A cooperative neighborhood-based variant used as an auxiliary comparison.

- `Single-head Graph Attention PPO`  
  A graph-aware PPO variant using a single attention head.

- `MGAPLight / Multi-head Graph Attention PPO`  
  The proposed method using ego-graph observation and multi-head graph attention.

A fixed-time controller can also be used as a contextual baseline.

---

## Repository Structure

```text
MGAPLight/
│
├── configs/                  # Training and evaluation configuration files
├── envs/                     # SUMO-RL and PettingZoo environment wrappers
├── models/                   # PPO and graph-attention model definitions
├── networks/                 # SUMO network files
├── routes/                   # Mixed-traffic route files for different scenarios
├── scripts/                  # Training, testing, and plotting scripts
├── results/                  # Experimental logs and evaluation outputs
├── figures/                  # Generated figures for analysis
├── requirements.txt          # Python dependencies
└── README.md
