class SimpleTreeNode:
    
    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов
    
class SimpleTree:

    def __init__(self, root):
        self.Root = root; # корень, может быть None
    
    def AddChild(self, ParentNode, NewChild):
        ParentNode.Children.append(NewChild)
        NewChild.Parent = ParentNode
        pass # ваш код добавления нового дочернего узла существующему ParentNode
  
    def DeleteNode(self, NodeToDelete):
        node = NodeToDelete
        if node is not self.Root:
            node.Parent.Children.remove(node)
            node.Parent = None
        pass # ваш код удаления существующего узла NodeToDelete

    def GetAllNodes(self):
        number = 0
        node = self.Root
        result = []
        while True:
            if node not in result:
                result.append(node)
            if number < len(node.Children):
                node = node.Children[number]
                number = 0
            else:
                if node.Parent is not None:
                    number = node.Parent.Children.index(node) + 1
                    node = node.Parent
                else:
                    break
        # ваш код выдачи всех узлов дерева в определённом порядке
        return result

    def FindNodesByValue(self, val):
        result = []
        node = self.Root
        number = 0
        while node.NodeValue is not None:
            if node not in result and node.NodeValue == val:
                result.append(node)
            if number < len(node.Children):
                node = node.Children[number]
                number = 0
            else:
                if node.Parent is not None:
                    number = node.Parent.Children.index(node) + 1
                    node = node.Parent
                else:
                    break
        # ваш код поиска узлов по значению
        return result
   
    def MoveNode(self, OriginalNode, NewParent):
        if OriginalNode is not self.Root:
            self.DeleteNode(OriginalNode)
            self.AddChild(NewParent, OriginalNode)
        # ваш код перемещения узла вместе с его поддеревом -- 
        # в качестве дочернего для узла NewParent
   
    def Count(self):
        count_nodes = self.GetAllNodes()
        # количество всех узлов в дереве
        return len(count_nodes)

    def LeafCount(self):
        number = 0
        for i in self.GetAllNodes():
            if len(i.Children) == 0:
                number += 1
        # количество листьев в дереве
        return number

    def EvenTrees(self):
        #  Метод разбивает дерево на максимальное количество минимальных четных деревьев
        #  на выходе будет список объектов SimpleTreeNode, между которыми нужно разорвать связь
        result = []
        def count_DFS(root):
            nonlocal result
            nodes = 1
            for child in root.Children:
                subtree_length = count_DFS(child)
                nodes += subtree_length
            if not root.Children:
                return 1
            if nodes % 2 == 0:
                if root.Parent:
                    result.append(root.Parent)
                    result.append(root)
                return 0
            return nodes
        count_DFS(self.Root)
        return result

    def Print_all_Nodes(self):
        # печать значений элементов
        all_Nodes=self.GetAllNodes()
        all_Nodes_for_print=[]
        for i in range(self.Count()):
            all_Nodes_for_print.append(all_Nodes[i].NodeValue)
        print(all_Nodes_for_print)