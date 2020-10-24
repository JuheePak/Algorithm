# 함수 선언부

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

def insert_node(findData, insertData):
    global head, pre, cur
    # 입력할 데이터가 제일 처음이 될 때
    if head.data == findData:
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return
    # 입력 데이터가 중간에 있을 때
    current = head
    # while True:
    #     if current.link == None: # 끝
    #         break
    # or
    while current.link != None: #끝
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return

    #findData 못찾음(못찾거나 없거나)
    node = Node()
    node.data = insertData
    current.link = node
    memory.append(node)


# 전역 변수부
memory = []
head, cur, pre = None, None, None # 시작노드, 현재노드, 앞노드
dataAry = ['다현', '정연', '쯔위', '주희', '별']

# 메인 코드부
if __name__=='__main__':
    node = Node() # 메인 임포트할때 pass 쓰면 실행되지 않고 데이터만 갖고 온다.
    node.data=dataAry[0]
    head = node
    memory.append(node)

    for data in dataAry[1:]: # 정연부터 끝까지. 다현이는 head니까
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

    printNode(head)
    insert_node('다현','화사')
    printNode(head)
    insert_node('쯔위','재남')
    printNode(head)
    insert_node('없다','막내')