from SimpleTreeNode import SimpleTree, SimpleTreeNode
import unittest

class ls2_test(unittest.TestCase):

    def setUp(self):
        pass

    def test_lesson_example(self):
        a_tree = SimpleTree(None)
        root_node = SimpleTreeNode(1, None)
        a_tree.Root = root_node

        two = SimpleTreeNode(2, None)
        a_tree.AddChild(a_tree.Root, two)
        five = SimpleTreeNode(5, None)
        a_tree.AddChild(two, five)
        seven = SimpleTreeNode(7, None)
        a_tree.AddChild(two, seven)

        three = SimpleTreeNode(3, None)
        a_tree.AddChild(a_tree.Root, three)
        four = SimpleTreeNode(4, None)
        a_tree.AddChild(three, four)

        six = SimpleTreeNode(6, None)
        a_tree.AddChild(a_tree.Root, six)
        eight = SimpleTreeNode(8, None)
        a_tree.AddChild(six, eight)
        nine = SimpleTreeNode(9, None)
        a_tree.AddChild(eight, nine)
        ten = SimpleTreeNode(10, None)
        a_tree.AddChild(eight, ten)
        self.assertEqual(a_tree.EvenTrees(), [a_tree.Root, three, a_tree.Root, six])

    def test_another_example(self):
        a_tree = SimpleTree(None)
        root_node = SimpleTreeNode(1, None)
        a_tree.Root = root_node

        nine = SimpleTreeNode(9, None)
        a_tree.AddChild(a_tree.Root, nine)

        two = SimpleTreeNode(2, None)
        a_tree.AddChild(a_tree.Root, two)
        four = SimpleTreeNode(4, None)
        a_tree.AddChild(two, four)

        three = SimpleTreeNode(3, None)
        a_tree.AddChild(a_tree.Root, three)
        five = SimpleTreeNode(5, None)
        a_tree.AddChild(three, five)
        six = SimpleTreeNode(6, None)
        a_tree.AddChild(five, six)

        self.assertEqual(a_tree.EvenTrees(), [a_tree.Root, two, three, five])

    def tearDown(self):
        pass


unittest.main()