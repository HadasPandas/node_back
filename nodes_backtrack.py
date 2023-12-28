class LinkedList:
    def __init__(self, val, nextNode=None):
        self.val = val
        self.nextNode = nextNode

    def print_linked(self) -> None:
        cur = self.val
        res = []
        while cur:
            res.append(cur)
            cur = cur.nextNode
        print(res)

def rev_list_rec(lst):
    return rev_helper(lst, [])

def rev_helper(lis, new_lis):
    if not lis:
        return new_lis
    temp = lis.pop()
    if type(temp) == list:
        temp_lst = []
        temp = rev_helper(temp, temp_lst)
    new_lis.append(temp)
    return rev_helper(lis, new_lis)

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def equal_trees(x: TreeNode, y: TreeNode) -> bool:
    res_bool = True
    if not x and not y:
        return res_bool
    return res_bool

def stain_size(mat, place):
    return stain_size_helper(mat, place, set())

def stain_size_helper(mat, place, visited):
    if (not 0 <= place[0] < len(mat)) or (not 0 <= place[1] < len(mat[0])):
        return 0
    if mat[place[0]][place[1]] == 0 or tuple[place] in visited: #check it
        return 0
    counter = 1 #the easiest way will be to change the matrix itself cause they didnt tell us we cant:)
    visited.add(tuple(place))

    for i in range(-1, 2):
        for j in range(-1, 2):
            counter += stain_size_helper(mat, place[0]+i, place[1]+j)