import os

guide = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}


def find_path(raw_data):
    data = raw_data.split(',')

    position = (0, 0)
    for point in data:
        direction = point[0]
        step = int(point[1:])

        for s in range(step):
            # add step to the current position and update it
            position = tuple(sum(x) for x in zip(position, guide[direction]))
            yield position


def find_dist(raw_data, target):
    data = raw_data.split(',')

    total_step = 0
    position = (0, 0)
    for point in data:
        direction = point[0]
        step = int(point[1:])

        for s in range(step):
            # add step to the current position and update it
            position = tuple(sum(x) for x in zip(position, guide[direction]))
            total_step += 1
            if position == target:
                return total_step


with open(os.getcwd() + '/data/task1.txt') as file:
    a, b = file.read().split('\n')

    path_a = set(i for i in find_path(a))
    path_b = set(i for i in find_path(b))

    # find all intersections b/w wire a and b
    intersections = list(path_a & path_b)
    # find all manhattan distance from the central port to each intersection
    man_dist = [abs(x)+abs(y) for x, y in intersections]
    print('What is the Manhattan distance:', min(man_dist))
    
    intersection_dist = [find_dist(a, i) + find_dist(b, i) for i in intersections]
    print('What is the fewest combined steps the wires must take to reach an intersection:', min(intersection_dist))
