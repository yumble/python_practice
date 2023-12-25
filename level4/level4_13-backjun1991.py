n = int(input())
dic = dict()
def preorder_traversal(key):
    global dic
    if key != '.':
        print(key, end='')
        preorder_traversal(dic[key][0])
        preorder_traversal(dic[key][1])
def inorder_traversal(key):
    global dic
    if key != '.':
        inorder_traversal(dic[key][0])
        print(key, end='')
        inorder_traversal(dic[key][1])
def postorder_traversal(key):
    global dic
    if key != '.':
        postorder_traversal(dic[key][0])
        postorder_traversal(dic[key][1])
        print(key, end='')

for _ in range(n):
    node, left, right = map(str, input().split())
    dic[node] = [left, right]


preorder_traversal('A')
print()
inorder_traversal('A')
print()
postorder_traversal('A')