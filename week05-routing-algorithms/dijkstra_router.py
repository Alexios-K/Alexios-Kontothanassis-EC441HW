import heapq
import copy

def dijkstra(graph, start):
    """Calculates shortest paths from the start node to all other nodes."""
    # Initialize distances and previous nodes
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    
    # Priority queue to hold (distance, node)
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # If we found a shorter path to this node already, skip it
        if current_distance > distances[current_node]:
            continue
            
        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # If we found a shorter path to the neighbor, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
                
    return distances, previous_nodes

def get_path(previous_nodes, start, target):
    """Reconstructs the shortest path from start to target."""
    path = []
    current_node = target
    while current_node != start:
        if current_node is None:
            return None # No path exists
        path.append(current_node)
        current_node = previous_nodes[current_node]
    path.append(start)
    return path[::-1] # Reverse the path to get start -> target

def print_routing_table(graph, start):
    """Prints the routing table in a readable format."""
    distances, previous_nodes = dijkstra(graph, start)
    print(f"Routing table for {start}:")
    print(f"{'Destination':<15} | {'Cost':<5} | {'Path'}")
    print("-" * 55)
    for node in graph:
        if node != start:
            path = get_path(previous_nodes, start, node)
            cost = distances[node]
            path_str = " -> ".join(path) if path else "Unreachable"
            cost_str = str(cost) if cost != float('infinity') else "inf"
            print(f"{node:<15} | {cost_str:<5} | {path_str}")
    print()

def main():
    # Define the initial network topology as an adjacency list
    # Costs could represent latency in ms or inverse bandwidth
    network = {
        'Home': {'RouterA': 10, 'RouterB': 5},
        'RouterA': {'Home': 10, 'RouterB': 2, 'RouterC': 1},
        'RouterB': {'Home': 5, 'RouterA': 2, 'RouterD': 3},
        'RouterC': {'RouterA': 1, 'RouterD': 9, 'Destination': 4},
        'RouterD': {'RouterB': 3, 'RouterC': 9, 'Destination': 2},
        'Destination': {'RouterC': 4, 'RouterD': 2}
    }
    
    print("--- Initial Network Topology ---\n")
    print_routing_table(network, 'Home')
    
    # Simulate Link Failure
    print("--- Simulating Link Failure ---\n")
    print("[!] Link between RouterB and RouterD goes down!\n")
    
    # Create a deepcopy of the network to simulate the new state
    updated_network = copy.deepcopy(network)
    
    # Remove the link between RouterB and RouterD (must remove both directions)
    del updated_network['RouterB']['RouterD']
    del updated_network['RouterD']['RouterB']
    
    print_routing_table(updated_network, 'Home')

if __name__ == "__main__":
    main()