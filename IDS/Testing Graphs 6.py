from collections import defaultdict
import sys
import math
import timeit


def simple_cycles(G):
    # Yield every elementary cycle in python graph G exactly once
    # Expects a dictionary mapping from vertices to iterables of vertices
    def _unblock(thisnode, blocked, B):
        stack = set([thisnode])
        while stack:
            node = stack.pop()
            if node in blocked:
                blocked.remove(node)
                stack.update(B[node])
                B[node].clear()

    G = {v: set(nbrs) for (v, nbrs) in G.items()}  # make a copy of the graph
    sccs = strongly_connected_components(G)
    while sccs:
        scc = sccs.pop()
        startnode = scc.pop()
        path = [startnode]
        blocked = set()
        closed = set()
        blocked.add(startnode)
        B = defaultdict(set)
        stack = [(startnode, list(G[startnode]))]
        while stack:
            thisnode, nbrs = stack[-1]
            if nbrs:
                nextnode = nbrs.pop()
                if nextnode == startnode:
                    yield path[:]
                    closed.update(path)
                elif nextnode not in blocked:
                    path.append(nextnode)
                    stack.append((nextnode, list(G[nextnode])))
                    closed.discard(nextnode)
                    blocked.add(nextnode)
                    continue
            if not nbrs:
                if thisnode in closed:
                    _unblock(thisnode, blocked, B)
                else:
                    for nbr in G[thisnode]:
                        if thisnode not in B[nbr]:
                            B[nbr].add(thisnode)
                stack.pop()
                path.pop()
        remove_node(G, startnode)
        H = subgraph(G, set(scc))
        sccs.extend(strongly_connected_components(H))


def strongly_connected_components(graph):
    # Tarjan's algorithm for finding SCC's
    # Robert Tarjan. "Depth-first search and linear graph algorithms." SIAM journal on computing. 1972.
    # Code by Dries Verdegem, November 2012
    # Downloaded from http://www.logarithmic.net/pfh/blog/01208083168

    index_counter = [0]
    stack = []
    lowlink = {}
    index = {}
    result = []

    def _strong_connect(node):
        index[node] = index_counter[0]
        lowlink[node] = index_counter[0]
        index_counter[0] += 1
        stack.append(node)

        successors = graph[node]
        for successor in successors:
            if successor not in index:
                _strong_connect(successor)
                lowlink[node] = min(lowlink[node], lowlink[successor])
            elif successor in stack:
                lowlink[node] = min(lowlink[node], index[successor])

        if lowlink[node] == index[node]:
            connected_component = []

            while True:
                successor = stack.pop()
                connected_component.append(successor)
                if successor == node:
                    break
            result.append(connected_component[:])

    for node in graph:
        if node not in index:
            _strong_connect(node)

    return result


def remove_node(G, target):
    # Completely remove a node from the graph
    # Expects values of G to be sets
    del G[target]
    for nbrs in G.values():
        nbrs.discard(target)


def subgraph(G, vertices):
    # Get the subgraph of G induced by set vertices
    # Expects values of G to be sets
    return {v: G[v] & vertices for v in vertices}


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
    lengths = tuple(simple_cycles(graphdict))
    for items in lengths:
        if lendict[len(items)] == 0:
            lendict[len(items)] = 1
    print(lendict)
    stop = timeit.default_timer()
    print("Time: ", stop - start)


if __name__ == "__main__":
    main()
