class TreeNode(object):
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        fmt = 'TreeNode(data={}, left={}, right={})'
        return fmt.format(self.data, self.left, self.right)

    def insert(self, value):
        if value <=self.data:
            if self.left is None:
                self.left=TreeNode(value,None,None)
            else:
                self.left.insert(value)
        elif value > self.data:
            if self.right is None:
                self.right=TreeNode(value,None,None)
            else:
                self.right.insert(value)

    def sorted_data(self):

        if self.data is None:

            return []
        elif self.right is None and self.left is None:

            return [self.data]
        elif self.right is None:

            return self.left.sorted_data()+[self.data]
        elif self.left is None:

            return [self.data]+self.right.sorted_data()
        else:

            sorted=self.left.sorted_data()+[self.data]+self.right.sorted_data()
        
        return sorted

class BinarySearchTree(object):
    def __init__(self, tree_data):

        self.root=TreeNode(tree_data[0],None,None)
      
        for value in tree_data[1:]:
            
            self.root.insert(value)  


    def data(self):
        return self.root

    def sorted_data(self):

        return self.root.sorted_data()
    
