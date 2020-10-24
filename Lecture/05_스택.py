# 함수 선언부
def isStackEmpty():
    if (top == top - SIZE):
        return True
    else:
        return False

def pop(data):
    if isStackEmpty():
        print("스택이 비어있음")
        return
    top -= 1
    stack[top] = data

def isStackFull():
    if (top == SIZE -1):
        return True
    else:
        return False

def push(data):
    global stack, top
    if isStackFull():
        print("스택 꽉 차있음")
        return
    top += 1
    stack[top] = data

# 전역 변수부
SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1

# 메인 코드부
