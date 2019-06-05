import sys
import math

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


def find_all_paths(graph, start, end, path):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    newpaths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
        for newpath in newpaths:
                if newpath not in paths:
                    paths.append(newpath)
    return paths


def main():
    sides = input("Enter the number of Sides per Permutation: ")
    pancakes = input("Enter the number of Permutations: ")
    while not sides.isdigit():
        sides = input("Please give an integer for the number of Sides per Permutation: ")
    while not pancakes.isdigit():
        pancakes = input("Please give an integer for the number of Permutations: ")
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
    for i in range(0, len(graphdict[root])):
        paths.append(find_all_paths(graphdict, graphdict[root][i], root, path))
    print(len(paths))
    for items in paths:
        print(len(items))
        for things in items:
            if lendict[len(things)] == 0:
                lendict[len(things)] = 1

    print("For C_" + str(sides) + " w.p. S_" + str(pancakes) + ". The lengths is as follows below: ")
    print(lendict)


if __name__ == "__main__":
    main()
