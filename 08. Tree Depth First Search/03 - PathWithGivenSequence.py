class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_sequence(element, sequence, depth):
    if element is None:
        return False

    sequenceLength = len(sequence)

    if depth >= sequenceLength or element.val != sequence[depth]:
        return False

    # if it's leaf and we have found the path return true
    if element.right is None and element.left is None and depth == sequenceLength - 1:
        return True

    return find_sequence(element.right, sequence, depth + 1) or \
        find_sequence(element.left, sequence, depth + 1)


def find_path(root, sequence):
    return find_sequence(root, sequence, 0)


def main():

    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()
