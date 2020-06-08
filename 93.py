### Problem

# Good morning! Here's your coding interview problem for today.

# This problem was asked by Apple.

# Given a tree, find the largest tree/subtree that is a BST.

# Given a tree, return the size of the largest tree/subtree that is a BST.


### Solution

class Tree:

    def __init__(self, value, left=None, right=None):
        self._value = value
        self._left = left
        self._right = right
        self._is_bst_cache = None

    def is_bst(self):
        if self._is_bst_cache is None:
            self._is_bst_cache = self._is_bst()
        return self._is_bst_cache

    def _is_bst(self):
        if self.has_left() and \
                self.get_left().get_value() > self.get_value():
            return False

        if self.has_right() and \
                self.get_right().get_value() < self.get_value():
            return False

        if self.has_left() and \
                BST.MaximumValue(self.get_left()) > self.get_value():
            return False

        if self.has_right() and \
                BST.MinimumValue(self.get_right()) < self.get_value():
            return False

        if self.has_left() and \
                not self.get_left()._is_bst():
            return False

        if self.has_right() and \
                not self.get_right()._is_bst():
            return False

        return True

    def get_left(self):
        return self._left

    def set_left(self, left):
        self._is_bst_cache = None
        self._left = left

    def has_left(self):
        return self._left is not None

    def get_right(self):
        return self._right

    def set_right(self, right):
        self._is_bst_cache = None
        self._right = right

    def has_right(self):
        return self._right is not None

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._is_bst_cache = None
        self._value = value


class BST:

    @staticmethod
    def MinimumValue(root):
        node = root
        while node.has_left():
            node = node.get_left()
        return node.get_value()

    @staticmethod
    def MaximumValue(root):
        node = root
        while node.has_right():
            node = node.get_right()
        return node.get_value()


def MaxSubBST(root):

    leftIsBST, leftCount = False, 1
    if root.has_left():
        leftIsBST = root.get_left().is_bst()
        leftCount = MaxSubBST(root.get_left())

    rightIsBST, rightCount = False, 1
    if root.has_right():
        rightIsBST = root.get_right().is_bst()
        rightCount = MaxSubBST(root.get_right())

    if root.is_bst() and leftIsBST and rightIsBST:
        return leftCount + rightCount + 1

    return max([leftCount, rightCount])


if __name__ == "__main__":
    tc1 = Tree(10,
        left=Tree(5,
            left=Tree(3),
            right=Tree(9)),
        right=Tree(15,
            left=Tree(9),
            right=Tree(17)))

    print('''Test Case:
         10
       /    \\
      5      15
     / \\    /  \\
    3   9  9   17
    Is BST? {}
    max BST count {}'''.format(tc1.is_bst(), MaxSubBST(tc1)))
