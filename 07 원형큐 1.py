# 함수 선언부
def isQueueFull():
    global SIZE, queue, front, rear
    if ((rear+1) % SIZE == front):
        return True
    else:
        return False

def isQueueEmpty():
    global SIZE, queue, front, rear
    if (front == rear):
        return True
    else:
        return False

def enQueue(data):
    global SIZE, queue, front, rear
    if isQueueFull():
        return
    rear = (rear+1) % SIZE
    queue[rear] = data

def deQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        return
    front = (front+1) % SIZE
    data = queue[front]
    queue[front] = None
    return data

# 전역 변수부
SIZE = 5
queue = [None for _ in range(0, SIZE)]
front = rear = 0

# 메인 코드부
enQueue('a')
enQueue('b')
enQueue('c')
print(queue)
deQueue()
deQueue()
enQueue('A')
enQueue('B')
enQueue('D')
print(queue)
