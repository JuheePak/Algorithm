# 빈 배열 준비
# 카톡 친구라고 가정한다.

katok = []

# 배열 제일 뒤에 친구 추가하는 함수
def add_data(friend):
    katok.append(None) # 빈칸 추가
    kLen = len(katok)
    katok[kLen-1] = friend

# 중간에 삽입
def insert_data(position, friend): # 위치와 데이터
    katok.append(None)
    kLen = len(katok)
    for i in range(kLen-1, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None
    katok[position] = friend

# 중간 데이터 삭제
def delete_data(position):
    kLen = len(katok)
    katok[position] = None # 우선 position에 위치한 데이터 지움
    for i in range(position+1, kLen):
        katok[i-1]=katok[i]
        katok[i] = None
    del(katok[kLen-1]) # 땡겨서 비워진 가장 마지막 칸 지우기



add_data("다현")
add_data("정연")
add_data("쯔위")
print(katok)

insert_data(1, "사나")
print(katok)

delete_data(2) # 정연 삭제
print(katok)