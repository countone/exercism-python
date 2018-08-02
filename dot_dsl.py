NODE, EDGE, ATTR = range(3)


class Node(object):
    def __init__(self, name, attrs={}):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge(object):
    def __init__(self, src, dst, attrs={}):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Graph(object):
    def __init__(self, data=[]):
        self.nodes=[]
        self.edges=[]
        self.attrs={}

        for items in data:
            if len(items)<1:
                raise TypeError('TypeError')
            if items[0]==NODE:
                try:
                    if len(items)==3 and type(items[1]) is str and type(items[2]) is dict:
                        self.nodes.append(Node(items[1],items[2]))
                    else:
                        raise ValueError('ValueError')
                except IndexError:
                    raise TypeError
            elif items[0]==EDGE:
                try:
                    if len(items)==4 and type(items[1]) is str and type(items[2]) is str and type(items[3]) is dict:
                        self.edges.append(Edge(items[1],items[2],items[3]))
                    else:
                        raise ValueError('ValueError')
                    
                except IndexError:
                    raise ValueError('ValueError')
            elif items[0]==ATTR:
                try:
                    if len(items)<3:
                        raise TypeError('ValueError')
                    if type(items[1]) is str and type(items[2]) is str:
                        self.attrs[items[1]]=items[2]
                    else:
                        raise ValueError('ValueError')
                    
                except IndexError:
                    raise TypeError('TypeError')
            else:
                if type(items[0]) is str:
                    raise TypeError('TypeError')
                elif type(items[0]) is int:
                    raise ValueError('ValueError')