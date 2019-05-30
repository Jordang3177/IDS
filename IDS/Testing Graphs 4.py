import sys
import math

sys.setrecursionlimit(30000)


def generate_graph(vertex, gdict, s, p):
    if vertex in gdict:
        return
    else:
        instances = 1
        children = []
        for flip in range(0 , p):
            children.append(get_children(vertex, instances, s))
            instances = instances + 1
        gdict[vertex] = children
        for items in gdict[vertex]:
            generate_graph(items, gdict, s, p)
    return gdict


def get_children(nodes, instance, side):
    original_name = nodes
    temp_name = ""
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
        temp_name = ""
        count = 0
    end_name = end_name + original_name
    return end_name


def find_all_paths(graph, start, end, path = []):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    newpaths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
        for newpath in newpaths:
            paths.append(newpath)
    return paths


def main():
    sides = input("Enter the number of Sides per Permutation: ")
    pancakes = input("Enter the number of Permutations: ")
    while type(pancakes) != int:
        pancakes = input("Please give an integer for the number of Permutations")
    while type(sides) != int:
        sides = input("Please give an integer for the number of Sides per Permutation: ")
    pancakes = int(pancakes)
    sides = int(sides)
    root = ""
    for pancake in range(1, pancakes + 1):
        root = root + str(pancake)

    graphdict = {}
    generate_graph(root, graphdict, sides, pancakes)

    paths = []
    paths.append(find_all_paths(graphdict, graphdict[root][0], root))
    lendict = {}
    length = pow(sides, pancakes) * math.factorial(pancakes)
    for i in range(0, length + 1):
        lendict[i] = 0
    for items in paths:
        for things in items:
            if lendict[len(things)] == 0:
                lendict[len(things)] = 1

    print(lendict)


if __name__ == "__main__":
    main()