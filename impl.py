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
        
        # TODO: Implement Write Quorum Logic here. 
        # Hint: Iterate through self.nodes. Call node.write(). 
        # Keep track of successes and break when write_quorum is reached.
        
        end_time = time.time()
        latency = end_time - start_time
        return success_count >= write_quorum, latency

    def read(self, key, read_quorum):
        start_time = time.time()
        read_values = {}
        
        # TODO: Implement Read Quorum Logic here.
        # Hint: Iterate through self.nodes. Call node.read().
        # Keep track of how many times each value is returned. 
        # Return the value that meets the read_quorum threshold.
        
        end_time = time.time()
        latency = end_time - start_time
        return None, latency # Replace None with the actual value

# --- Example Evaluation Setup ---
nodes = [Node("A"), Node("B"), Node("C")]
system = QuorumSystem(nodes)

print("--- Scenario A: Strong Consistency (W=2, R=2) ---")
# TODO: Write your tests here to measure latency

print("\n--- Scenario C: Eventual Consistency (W=1, R=1) ---")
# To test staleness, write a value, then fail the node that has the latest data!
# nodes[0].is_down = True
# TODO: Write a test that proves R=1 can return stale data if the updated node is down.