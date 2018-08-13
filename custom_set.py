class CustomSet(object):
    def __init__(self, elements=[]):
        self.elements=set(elements)

    def isempty(self):
        return not self.elements

    def __contains__(self, element):
        return element in self.elements

    def issubset(self, other):
        return self.elements <=other.elements

    def isdisjoint(self, other):
        for value in list(self.elements):
            if value in other.elements:
                return False
        else:
            return True

    def __eq__(self, other):
        return self.elements==other.elements

    def add(self, element):
        self.elements=list(self.elements)
        self.elements.append(element)
        self.elements=set(self.elements)

    def intersection(self, other):
        intersection=[]
        for value in self.elements:
            if value in other.elements:
                intersection.append(value)

        return CustomSet(intersection)

    def __sub__(self,other):
        return self.difference(other)

    def difference(self, other):

        difference=list(self.elements)
        for value in other.elements:
            if value in self.elements:
                difference.remove(value)

        return CustomSet(difference)
    
    def __add__(self,other):
        return self.union(other)
    
    def union(self, other):
        return CustomSet(list(self.elements)+list(other.elements))