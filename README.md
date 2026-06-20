# Quorum-Based Replication

## Run the Simulation

The simulation is a single python script that can be executed with `python3 sim.py`.

## Tests

R - read quorum
W - write quorum
N - number of nodes in the cluster

Running the simulation above will include 3 test scenarios demonstrating the effects of various read and write quorums in a 3 node cluster (N = 3).

- Scenario A: `R + W > N` where `R = 2` and `W = 2` for balanced / strong consistency
- Scenario B: `R = 3` and `W = 1` for fast writes, slow reads
- Scenario C: `R + W ≤ N` where `R = 1` and `W = 1` for eventual consistency
