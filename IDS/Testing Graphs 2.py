class Tree(object):
    def __init__(self, name='root', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)

    def __repr__(self):
        return self.name

    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)


def generating_tree(node, current_depth):
    instances = 0
    count = 0
    # Checking if we are done doing the number of vertices and if so we just return the node we are at.
    if current_depth == 18:
        return node
    # iterate over the name
    for j in range(0, len(node.name)):
        # current implementation needs to be changed as this only works for 2 pancakes, because
        # when you have more than 2 pancakes you have to flip each time that it's not the top instance.
        # for instance if you had 3 pancakes with 3 sides and you are at state "12b3b" then it's children would be
        # "1b2b3b", "2bb1b3b", "3bb2bb1b"
        # so for now this will only work for 2 pancakes
        # This means we are at the first flip of the pancake so only doing 12 becoming 1b2
        if node.name[j] != "b" and instances == 0:
            # This just shows we are not at the first flip of the pancake
            instances += 1
            subname = node.name[j + 1:]
            for k in range(0, len(subname)):
                if subname[k] != "b":
                    break
                else:
                    count += 1
            if count == sides - 1:
                count = 0
                new_name = node.name[:j + 1] + node.name[j + sides:]
                new_name = Tree(new_name)
                new_name = generating_tree(new_name, current_depth + 1)
                node.add_child(new_name)
            else:
                count = 0
                new_name = node.name[:j + 1] + "b" + node.name[j + 1:]
                new_name = Tree(new_name)
                new_name = generating_tree(new_name, current_depth + 1)
                node.add_child(new_name)
        elif node.name[j] != "b" and instances != 0:
            subname = node.name[j + 1:]
            for k in range(0, len(subname)):
                if subname[k] != "b":
                    break
                else:
                    count += 1
            if count == sides - 1:
                # here
                new_name = node.name[:j + 1] + node.name[j + sides:]
                new_name = new_name[j:] + new_name[:j]
                count = 0
                subname = new_name[2:]
                for l in range(0, len(subname)):
                    if subname[l] != "b":
                        break
                    else:
                        count += 1
                if count == sides - 1:
                    # blarg
                    count = 0
                    new_name = new_name[:1 + 1] + new_name[1 + sides:]
                    new_name = Tree(new_name)
                    new_name = generating_tree(new_name, current_depth + 1)
                    node.add_child(new_name)
                else:
                    # thing
                    count = 0
                    new_name = new_name[:1 + 1] + "b" + new_name[1 + 1:]
                    new_name = Tree(new_name)
                    new_name = generating_tree(new_name, current_depth + 1)
                    node.add_child(new_name)
            else:
                # wow
                new_name = node.name[:j + 1] + "b" + node.name[j + 1:]
                new_name = new_name[j:] + new_name[:j]
                subname = new_name[count + 3:]
                j = count + 2
                count = 0
                for l in range(0, len(subname)):
                    if subname[l] != "b":
                        break
                    else:
                        count += 1
                if count == sides - 1:
                    # za
                    new_name = new_name[:-count]
                    count = 0
                    new_name = Tree(new_name)
                    new_name = generating_tree(new_name, current_depth + 1)
                    node.add_child(new_name)
                else:
                    # boy
                    count = 0
                    new_name = new_name[:1 + 1] + new_name[1 + 1:] + "b"
                    new_name = Tree(new_name)
                    new_name = generating_tree(new_name, current_depth + 1)
                    node.add_child(new_name)
    return node


def lengths(tree, lengthsdict, length, nodeslist, targetname):
    if targetname == tree.name:
        lengthsdict[length] = 1
            #if children not in nodeslist:
            #    nodeslist.append(children.name)
            #    lengths(children, lengthsdict, 0, nodeslist, children.name)
    else:
        for children in tree.children:
            lengths(children, lengthsdict, length + 1, nodeslist, targetname)
            #if children not in nodeslist:
            #    nodeslist.append(children.name)
            #    lengths(children, lengthsdict, 0, nodeslist, children.name)


def dicupdate(dict):
    if dictofLengths != dict:
        for i in range(0, len(dict)):
            if dictofLengths[i] == 0 and dict[i] == 1:
                dictofLengths[i] = dict[i]


def printingtree(tree, length):
    print(tree.name, "at length: ", length)
    for children in tree.children:
        print(children, "at length: ", length + 1)
    for children in tree.children:
        printingtree(children, length + 1)

def checkingvalues(tree, validvalues, length):
    if tree.name not in validvalues:
        print("ERROR, ERROR, We have an error at length: ", length)
    for children in tree.children:
        checkingvalues(children, validvalues, length + 1)
pancakes = 2 #input("Enter the number of pancakes: ")
sides = 3 #input("Enter the number of Sides per Pancake: ")
pancakes = int(pancakes)
sides = int(sides)

root = ""
for pancake in range(1, pancakes + 1):
    root = root + str(pancake)
root = Tree(root)
print(root.name)
side_count = 0
depth = 0
root = generating_tree(root, depth)


validvalues = ["12", "1b2", "1bb2", "2bb1bb", "2b1bb", "21bb", "12b", "2bb1b", "2b1b", "21b", "12bb", "1b2bb", "1bb2bb",
               "2b1", "21", "2bb1", "1b2b", "1bb2b"]
print(len(validvalues))
checkingvalues(root, validvalues, 0)

print(root.name == "12")
dictofLengths = {}
listofnodes = []
listofnodes.append(root.name)

for i in range(0, 18 + 1):
    dictofLengths[i] = 0


# Should be 3,4,6,8,9,10,12,13,14,15,18
#for children in root.children:
#    lengths(children, dictofLengths, 1, listofnodes, root.name)
# lengths(root, dictofLengths, 0, listofnodes, root.name)
#print(dictofLengths)
