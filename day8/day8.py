import re
from math import lcm


class Vertex:

    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class Graph:

    def __init__(self):
        self.first = None
        self.vertices = []

    def get_vertex_if_exists(self, name):
        return next((v for v in self.vertices if v.name == name), None)

    def get_vertices(self, endswith=None):
        return [v for v in self.vertices if v.name[::-1].startswith(endswith)]

    def remove_vertex(self, v):
        self.vertices.remove(v)


def part1(input_file):
    values = [line for line in input_file.read().strip().split('\n') if line.strip()]
    dirs = values.pop(0)

    graph = Graph()
    for line in values:
        v_info = [val.strip() for val in re.split(r'[=,()]', line) if val.strip()]

        curr_v = graph.get_vertex_if_exists(v_info[0])

        if curr_v:
            vertex = curr_v
        else:
            vertex = Vertex(v_info[0])

        left_v = graph.get_vertex_if_exists(v_info[1])

        if not left_v:
            new_v = Vertex(v_info[1])
            vertex.left = new_v
            graph.vertices.append(new_v)
        else:
            vertex.left = left_v

        right_v = graph.get_vertex_if_exists(v_info[2])

        if not right_v:
            new_v = Vertex(v_info[2])
            vertex.right = new_v
            graph.vertices.append(new_v)
        else:
            vertex.right = right_v

        if curr_v:
            graph.remove_vertex(curr_v)

        graph.vertices.append(vertex)

    graph.first = graph.get_vertex_if_exists('AAA')
    curr_visited = graph.first

    i = 0
    while curr_visited.name != 'ZZZ':
        where_to_go = dirs[i % len(dirs)]

        if where_to_go == 'L':
            curr_visited = curr_visited.left

        if where_to_go == 'R':
            curr_visited = curr_visited.right

        i += 1

    return i


def part2(input_file):
    values = [line for line in input_file.read().strip().split('\n') if line.strip()]
    dirs = values.pop(0)

    graph = Graph()
    for line in values:
        v_info = [val.strip() for val in re.split(r'[=,()]', line) if val.strip()]

        curr_v = graph.get_vertex_if_exists(v_info[0])

        if curr_v:
            vertex = curr_v
        else:
            vertex = Vertex(v_info[0])

        left_v = graph.get_vertex_if_exists(v_info[1])

        if not left_v:
            new_v = Vertex(v_info[1])
            vertex.left = new_v
            graph.vertices.append(new_v)
        else:
            vertex.left = left_v

        right_v = graph.get_vertex_if_exists(v_info[2])

        if not right_v:
            new_v = Vertex(v_info[2])
            vertex.right = new_v
            graph.vertices.append(new_v)
        else:
            vertex.right = right_v

        if curr_v:
            graph.remove_vertex(curr_v)

        graph.vertices.append(vertex)

    local_walks = []
    for vertex in graph.get_vertices('A'):

        walks = 0
        while vertex.name[-1] != 'Z':
            where_to_go = dirs[walks % len(dirs)]

            if where_to_go == 'L':
                vertex = vertex.left

            if where_to_go == 'R':
                vertex = vertex.right
            walks += 1

        local_walks.append(walks)

    return lcm(*local_walks)


input_file = open("day8in.txt", "r")
# print("Part 1:", part1(input_file))
input_file.seek(0)
print("Part 2:", part2(input_file))
