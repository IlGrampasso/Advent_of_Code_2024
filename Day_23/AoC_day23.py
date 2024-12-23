from collections import defaultdict
import time


# Function to load input from the file
def load_input(filename):
    with open(filename, 'r') as file:
        return [line.strip().split('-') for line in file.readlines()]


# Function to build the graph from the connections
def build_graph(connections):
    graph = defaultdict(list)
    pairs = set()
    for n1, n2 in connections:
        graph[n1].append(n2)
        graph[n2].append(n1)
        pairs.add((n1, n2))
    return graph, pairs


# Function to find all sets of three interconnected computers
def find_triads(graph, pairs):
    triads = set()
    for n1 in graph:
        for n2, n3 in pairs:
            if n1[0] == "t" or n2[0] == "t" or n3[0] == "t":
                if n1 in graph[n2] and n1 in graph[n3]:
                    triads.add(tuple(sorted([n1, n2, n3])))
    return triads


# Function to find the largest LAN (all directly connected)
def find_largest_clique(graph):
    largest_network = set()
    for k, v in graph.items():
        for i1 in range(len(v)):
            lan = {k, v[i1]}
            for i2 in range(i1 + 1, len(v)):
                if all(v[i2] in graph[s] for s in lan):
                    lan.add(v[i2])
            if len(lan) > len(largest_network):
                largest_network = lan
    return largest_network


# Measure elapsed time for the script execution
start = time.process_time()

# Load connections from input file
filename = 'input1.txt'
connections = load_input(filename)

# Build the graph
graph, pairs = build_graph(connections)

# Find all sets of three interconnected computers (triads)
triads = find_triads(graph, pairs)
print("Part 1: Number of triads with at least one computer name starting with 't':", len(triads))

# Find the largest clique in the graph (LAN party)
largest_clique = find_largest_clique(graph)
lan_party_password = ','.join(sorted(largest_clique))
print("Part 2: LAN party password:", lan_party_password)

# Print the elapsed time
elapsed_time = (time.process_time() - start) * 1000
print("Elapsed time: %fms" % elapsed_time)
