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
    if current_depth == 5:
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
                # Error in here somewhere with 2bb1b flipping the second time.
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


pancakes = input("Enter the number of pancakes: ")
sides = input("Enter the number of Sides per Pancake: ")
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

print(root)
print(root.children)
print(root.children[0])
print(root.children[0].children)
print(root.children[1])
print(root.children[1].children)
print(root.children[0].children[0])
print(root.children[0].children[0].children)
print(root.children[0].children[1])
print(root.children[0].children[1].children)
print(root.children[1].children[0])
print(root.children[1].children[0].children)
print(root.children[1].children[1])
print(root.children[1].children[1].children)
print(root.children[0].children[0].children[0])
print(root.children[0].children[0].children[0].children)
print(root.children[0].children[0].children[1])
print(root.children[0].children[0].children[1].children)
print(root.children[0].children[1].children[0])
print(root.children[0].children[1].children[0].children)
print(root.children[0].children[1].children[1])
print(root.children[0].children[1].children[1].children)
print(root.children[1].children[0].children[0])
print(root.children[1].children[0].children[0].children)
print(root.children[1].children[0].children[1])
print(root.children[1].children[0].children[1].children)
print(root.children[1].children[1].children[0])
print(root.children[1].children[1].children[0].children)
print(root.children[1].children[1].children[1])
print(root.children[1].children[1].children[1].children)
