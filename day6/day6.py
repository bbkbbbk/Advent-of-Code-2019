import os


def create_graph(filename):
    graph = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.rstrip()
            planet_a, planet_b = line.split(')')

            if planet_a not in graph:
                graph[planet_a] = [planet_b]
            else:
                graph[planet_a].append(planet_b)

            # add connection b/w planet a and b since the graph is bidirectional
            if planet_b in graph:
                if planet_a not in graph[planet_b]:
                    graph[planet_b].append(planet_a)
            else:
                graph[planet_b] = [planet_a]
    return graph


def find_path(graph, start, end, path=[]):
    # exclude destination from the path
    if start == end:
        return path

    path = path + [start]

    if start not in graph:
        return None

    for node in graph[start]:
        if node not in path:
            new_path = find_path(graph, node, end, path)
            if new_path:
                return new_path
    return None


filename_1 = os.getcwd() + '/data/task1.txt'
graph_1 = create_graph(filename_1)

total_orbits = 0
for key in graph_1.keys():
    total_orbits += len(find_path(graph_1, key, 'COM'))
print('What is the total number of direct and indirect orbits:', total_orbits)


filename_2 = os.getcwd() + '/data/task2.txt'
graph_2 = create_graph(filename_2)

# minus 2 to remove the transfer b/w YOU - object YOU is orbiting and SAN - object SAN is orbiting
minimum_transfer = len(find_path(graph_2, 'YOU', 'SAN')) - 2
print('What is the minimum number of orbital transfers required:', minimum_transfer)
