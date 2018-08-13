from json import dumps


class Tree(object):
    def __init__(self, label, children=[]):
        self.label = label
        self.children = children

    def __dict__(self):
        return {self.label: [c.__dict__() for c in sorted(self.children)]}

    def __str__(self, indent=None):
        return dumps(self.__dict__(), indent=indent)

    def __lt__(self, other):
        return self.label < other.label

    def __eq__(self, other):
        return self.__dict__() == other.__dict__()

    def from_pov(self, from_node):
        
        
        if self.label == from_node:
            return self
        for i in range(len(self.children)):
            if self.children[i].label == from_node:
                x = self.children[i]
                current = i
                y= Tree(self.label)
                if self.children:
                    for j in range(len(self.children)):
                        if j != current:
                            y.children = y.children+ [self.children[j]]
                x.children = x.children + [y]
                return x
            else:
                try:
                    x = self.children[i].from_pov(from_node)
                    current = i
                    y= Tree(self.label)
                    if self.children:
                        for j in range(len(self.children)):
                            if j != current:
                                y.children = y.children+ [self.children[j]]
                    x.add_tree(self.children[current].label,y)
                    return x
                except ValueError :
                    pass
                

        else:
            raise ValueError('ValueError')
        
    def add_tree(self,label, subtree):
        
        for i in range(len(self.children)):
           
            if label == self.children[i].label:
                self.children[i].children = self.children[i].children + [subtree]
            else:
                z = self.children[i].add_tree(label,subtree)
                if z is None:
                    continue



    def path_to(self, from_node, to_node):
        
        node_tree = self.from_pov(from_node)
        
        for child in node_tree.children:

            if child.label == to_node:
                
                return [from_node,child.label]
            else:
                try:
                    y= child.path_to(child.label,to_node)

                except ValueError:
                    pass
                else:
                    return [from_node]+ y

        else:
            raise ValueError('ValueError')
