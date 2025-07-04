class TreeNode:
    def __init__(self,Val):
        self.Val=Val
        self.Children=[]

class Tree:
    def __init__(self):
        self.root=None
    def Recursive(self,node):
        print(node.Val)
        for i in node.Children:

            self.Recursive(i)




tree=Tree()
node1=TreeNode(1)
node2=TreeNode(2)
node3=TreeNode(3)
node4=TreeNode(4)
node5=TreeNode(5)
node6=TreeNode(6)
node7=TreeNode(7)
tree.root=node1
node1.Children=[node2,node3]
node2.Children=[node4,node5]
node4.Children=[node6,node7]

tree.Recursive(node1)


