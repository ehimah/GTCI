from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = []
    if root is None:
        return result
    queue = deque()
    queue.appendleft(root)
    while queue:
        levelItems = []
        levelsize = len(queue)
        for _ in range(levelsize):
            item = queue.popleft()
            levelItems.append(item.val)
            if item.left is not None:
                queue.append(item.left)

            if item.right is not None:
                queue.append(item.right)
            # add children
        result.append(levelItems)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(traverse(root)))


main()
