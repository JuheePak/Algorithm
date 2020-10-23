queue = [None for _ in range(0, 3)]
front = rear = -1

rear += 1
queue[rear]='A'
rear += 1
queue[rear]='B'
rear += 1
queue[rear]='C'
print(queue)

front += 1
print(queue[front])
queue[front] = None # 지워주기

front += 1
print(queue[front])
queue[front] = None # 지워주기

front += 1
print(queue[front])
queue[front] = None # 지워주기
print(queue)

# rear += 1
# queue[rear]='D'
# print(queue) 삽입안됨.



