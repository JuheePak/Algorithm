## Big-O

### `세번째로 큰 숫자 찾기`

### 0보다 큰 정수들의 배열이 주어졌다고 할 때 이 배열에서 세번째로 큰 숫자를 찾아내시오.

### 예를 들어, [2, 8, 19, 37, 4, 5, 12, 50, 1, 34, 23]이 입력되어 주어졌을 경우 가장 큰 수는 50, 두번째로 큰 수는 37, 세 번째로 큰 수는 34입니다. 따라서 34를 반환해야 한다.

### 시간복잡도를 고려하면서 여러가지 방법으로 문제를 풀어보자.

```python
def thirdMax(nums):
    nums.sort()
    return nums[-3]

def main():
    print(thirdMax([2, 8, 19, 37, 4, 5, 12, 50, 1, 34, 23])) # should return 34

if __name__ == "__main__":
    main()
```



### `단어 패턴`

### 문자열(패턴) 하나와 문자열의 배열 하나가 주어진다. 패턴 문자열의 각각의 문자 하나는 두번째 문자열 배열의 각각의 문자열 하나에 대응 될 수 있습니다. 해당 배열이 해당 패턴으로 표현되는지 아닌지의 여부를 확인하는 함수를 만들어보세요.

### 예를 들어서, `aabb` 와 `['elice', 'elice', 'alice', 'alice']` 가 주어졌을 경우에는 함수가 `True`를 반환해야 합니다. 이 경우에는 `a`가 `elice`에, `b`가 `alice`에 대응되도록 하면 배열을 해당 패턴으로 표현 하는 것이 가능하기 때문이죠.

### 반면, `aabb` 와 `['elice', 'alice', 'elice', 'alice']` 가 주어졌을 경우에는 함수가 `False`를 반환해야 합니다.

### ***단, 모든 문자는 영어 소문자라고 가정한다.***

```python
def wordPattern(pattern, strList):
    return len(set(pattern)) == len(set(zip(pattern, strList)))
def main():
    print(wordPattern("aabb", ["elice", "elice", "alice", "alice"])) # should return True
    print(wordPattern("abab", ["elice", "elice", "alice", "alice"])) # should return False
    

if __name__ == "__main__":
    main()
```



### `틀린 문자 찾기`

### 두 개의 문자열이 주어집니다. 이때 두번째 문자열은 첫번째 문자열에 하나의 문자를 추가 한 후, 그 순서를 랜덤하게 뒤섞은 문자입니다. 이때 추가된 문자를 찾아 보도록 합시다.

### 예를 들어서, `apple` 과 `azlppe` 가 주어졌을 경우 추가된 문자는 `z`입니다.

### 단, 추가된 문자는 하나라고 가정한다. 또 추가된 문자가 이미 리스트에 존재하던 문자일 수 있다.

``` python
def findDifference(str1, str2):
    for i in range(len(str2)):
        if str1.find(str2[i]) == -1:
            return str2[i]

def main():
    print(findDifference("pple", "zlppe"))


if __name__ == "__main__":
    main()

# 40점짜리.
# 이미 기존에 존재하는 문자를 찾아내는 알고리즘은 아직 진행중
# 어떻게 해야 기존에 있는 문자가 추가되는 것을 찾아낼 수 있을까?
```

