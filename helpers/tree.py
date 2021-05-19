# Definition for a binary tree node from Leetcode.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def getLeftChildIndex(index: int) -> int:
    return (index + 1) * 2 - 1


def getRightChildIndex(index: int) -> int:
    return (index + 1) * 2


def createNode(index, l: List) -> TreeNode:
    if index < len(l) and l[index] != None:
        return TreeNode(val=l[index],
                        left=createNode(getLeftChildIndex(index), l),
                        right=createNode(getRightChildIndex(index), l)
                        )
    else:
        return None


def createTreeFromList(l: List) -> TreeNode:
    return createNode(0, l)
