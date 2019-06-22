import sys
import math

import tarjan as tarjan
import timeit

sys.setrecursionlimit(30000)


def generate_graph(vertex, gdict, s, p):
    if vertex in gdict:
        return
    else:
        instances = 1
        children = []
        for flip in range(0, p):
            children.append(get_children(vertex, instances, s))
            instances = instances + 1
        gdict[vertex] = children
        for items in gdict[vertex]:
            generate_graph(items, gdict, s, p)
    return gdict


def get_children(nodes, instance, side):
    original_name = nodes
    end_name = ""
    count = 0
    for j in range(0, instance):
        for k in range(1, len(original_name)):
            if original_name[k] == 'b':
                count = count + 1
            else:
                break
        count = count + 1
        temp_name = original_name[0:count]
        original_name = original_name[count:]
        if len(temp_name) == side:
            temp_name = temp_name[0]
        else:
            temp_name = temp_name + 'b'
        end_name = temp_name + end_name
        count = 0
    end_name = end_name + original_name
    return end_name


def strongly_connected_components(graph):
    result = []
    stack = []
    low = {}

    def visit(node):
        if node in low: return

        num = len(low)
        low[node] = num
        stack_pos = len(stack)
        stack.append(node)

        for successor in graph[node]:
            visit(successor)
            low[node] = min(low[node], low[successor])

        if num == low[node]:
            component = tuple(stack[stack_pos:])
            del stack[stack_pos:]
            result.append(component)
            for item in component:
                low[item] = len(graph)

    for node in graph:
        visit(node)

    return result


def topological_sort(graph):
    count = {}
    for node in graph:
        count[node] = 0
    for node in graph:
        for successor in graph[node]:
            count[successor] += 1

    ready = [node for node in graph if count[node] == 0]

    result = []
    while ready:
        node = ready.pop(-1)
        result.append(node)

        for successor in graph[node]:
            count[successor] -= 1
            if count[successor] == 0:
                ready.append(successor)

    return result


def robust_topological_sort(graph):

    components = strongly_connected_components(graph)

    node_component = {}
    for component in components:
        for node in component:
            node_component[node] = component

    component_graph = {}
    for component in components:
        component_graph[component] = []

    for node in graph:
        node_c = node_component[node]
        for successor in graph[node]:
            successor_c = node_component[successor]
            if node_c != successor_c:
                component_graph[node_c].append(successor_c)

    return topological_sort(component_graph)

def main():
    sides = input("Enter the number of Sides per Permutation: ")
    pancakes = input("Enter the number of Permutations: ")
    while not sides.isdigit():
        sides = input("Please give an integer for the number of Sides per Permutation: ")
    while not pancakes.isdigit():
        pancakes = input("Please give an integer for the number of Permutations: ")
    start = timeit.default_timer()
    pancakes = int(pancakes)
    sides = int(sides)
    root = ""
    for pancake in range(1, pancakes + 1):
        root = root + str(pancake)

    graphdict = {}
    generate_graph(root, graphdict, sides, pancakes)
    path = []
    paths = []
    lendict = {}
    length = pow(sides, pancakes) * math.factorial(pancakes)
    for i in range(0, length + 1):
        lendict[i] = 0
    print(graphdict)
    stop = timeit.default_timer()
    print("Time: ", stop - start)
    # for i in range(0, len(graphdict[root])):
    #     paths.append(find_all_paths(graphdict, graphdict[root][i], root, path))
    # print(len(paths))
    # for items in paths:
    #     print(len(items))
    #     for things in items:
    #         if lendict[len(things)] == 0:
    #             lendict[len(things)] = 1
    #
    # print("For C_" + str(sides) + " w.p. S_" + str(pancakes) + ". The lengths is as follows below: ")
    # print(lendict)


if __name__ == "__main__":
    main()
