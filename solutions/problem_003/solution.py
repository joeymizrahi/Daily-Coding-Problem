"""
Given the root to a binary tree, implement serialize(root), which:
    serializes the tree into a string
and deserialize(s), which:
    deserializes the string back into the tree.

"""
import json  # using json as it knows how to turn dict to string and then back to dict
import pprint


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        """to represent the node as a string.
        """
        return '{}'.format(
            repr((self.val, self.left, self.right)))


def serialize(root):
    # base case
    if not root:
        return None

    serialized = {}
    left = serialize(root.left)
    right = serialize(root.right)

    serialized['data'] = root.val

    if left:
        serialized["left"] = left
    if right:
        serialized["right"] = right

    return json.dumps(serialized, indent=4)


def deserialize(s):
    serialized = json.loads(s)
    root = Node(serialized["data"])
    if "left" in serialized.keys():
        root.left = deserialize(serialized["left"])
    if "right" in serialized.keys():
        root.right = deserialize(serialized["right"])

    return root


node = Node('root', Node('left', Node('left.left')), Node('right'))
serialized = serialize(node)
assert deserialize(serialize(node)).left.left.val == 'left.left'
