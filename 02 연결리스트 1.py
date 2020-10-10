class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNode(current):
    print(current.data, end='-->')
    while (current.link != None):
        current = current.link
        print(current.data, end='-->')
    print()

node1 = Node() # 빈 노드 생성
node1.data = '다현'

node2 = Node()
node2.data = '정연'
node1.link=node2

node3 = Node()
node3.data = '쯔위'
node2.link=node3


printNode(node1)

newNode = Node()
newNode.data = '주희'
newNode.link = node2.link
node2.link = newNode

printNode(node1)

# node1 첫 노드를 알려주는 시작점은 알아야 한다.
# print(node1.data, end='-->')
# print(node1.link.data, end='-->')
# print(node1.link.link.data, end='-->')
# print(node1.link.link.link.data)

# 주희 노드를 삭제
node2.link = node3
del(newNode)
printNode(node1)


