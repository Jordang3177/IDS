import sys

sys.setrecursionlimit(30000)

def generate_graph(vertex, dict):
    if vertex in dict:
        return
    else:
        instances = 1
        children = []
        for flip in range(0 , pancakes):
            children.append(get_children(vertex, instances))
            instances = instances + 1
        dict[vertex] = children
        print(dict[vertex])
        print(len(dict))
        for items in dict[vertex]:
            generate_graph(items, dict)
    return dict


def get_children(nodes, instance):
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
        if len(temp_name) == sides:
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

pancakes = input("Enter the number of pancakes: ")
sides = input("Enter the number of Sides per Pancake: ")
while type(pancakes) != int:
    pancakes = input("")
pancakes = int(pancakes)
sides = int(sides)
root = ""
for pancake in range(1, pancakes + 1):
    root = root + str(pancake)

graphdict = {}
generate_graph(root, graphdict)
print(len(graphdict))
for items in graphdict:
    print(items)
    for y in graphdict[items]:
        print(items, "children :", y)

initial = []
paths = []
pathsss = []
paths.append(find_all_paths(graphdict, graphdict[root][0], root))
lendict = {}
for i in range(0, 19):
    lendict[i] = 0
for items in paths:
    for things in items:
        if lendict[len(things)] == 0:
            lendict[len(things)] = 1
print(root)
print(lendict)
