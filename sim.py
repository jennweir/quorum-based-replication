import time
import random

class Node:
    def __init__(self, name):
        self.name = name
        self.data = {}
        self.is_down = False

    def write(self, key, value):
        if self.is_down:
            return False
        # Simulate network & disk latency (10ms to 50ms)
        time.sleep(random.uniform(0.01, 0.05)) 
        self.data[key] = value
        print(f"   -> Node {self.name} successfully wrote {key}: {value}")
        return True

    def read(self, key):
        if self.is_down:
            return None
        # Simulate network & disk latency
        time.sleep(random.uniform(0.01, 0.05))
        return self.data.get(key)

class QuorumSystem:
    def __init__(self, nodes):
        self.nodes = nodes

    def write(self, key, value, write_quorum):
        start_time = time.time()
        success_count = 0
        
        # write quorum logic implementation
        # iterate through nodes calling write
        for node in self.nodes:
            if node.write(key, value):
                success_count += 1
            # keep track of successful writes and break when write quorum is reached
            if success_count >= write_quorum:
                break
        
        end_time = time.time()
        latency = end_time - start_time
        return success_count >= write_quorum, latency

    def read(self, key, read_quorum):
        start_time = time.time()
        read_values = {}
        # read quorum logic implementation
        # iterate through nodes calling read
        for node in self.nodes:
            node_value = node.read(key)
            # keep track of the number of times each node value is found
            if node_value is None:
                continue
            if node_value in read_values:
                read_values[node_value] += 1
            else:
                read_values[node_value] = 1
            # return the value that meets the read quorum threshold
            if read_values[node_value] >= read_quorum:
                end_time = time.time()
                latency = end_time - start_time
                return node_value, latency
        end_time = time.time()
        latency = end_time - start_time
        return None, latency

# 3 node cluster setup and testing different scenarios
nodes = [Node("A"), Node("B"), Node("C")]
system = QuorumSystem(nodes)

print("--- Scenario A: Strong Consistency (W=2, R=2) ---")
system.write("k1", "v0", 2)
value, latency = system.read("k1", 2)
print(f"Read value: {value}, Latency: {latency}")

print("\n--- Scenario B: Fast Writes, Slow Reads (W=1, R=3) ---")
system.write("k2", "v1", 3)
system.write("k2", "v2", 1)
value, latency = system.read("k2", 3)
print(f"Read value: {value}, Latency: {latency}")

print("\n--- Scenario C: Eventual Consistency (W=1, R=1) ---")
# test staleness by writing a value and then creating simulated node failure before reading
system.write("k3", "v4", 3)
system.write("k3", "v5", 1)
nodes[0].is_down = True
value, latency = system.read("k3", 1)
# proves R=1 can return stale data if the updated node is down
print(f"Read value: {value}, Latency: {latency}")