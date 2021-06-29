### 195. Tenth Line

---

Given a text file `file.txt`, print just the 10th line of the file.

**Example:**

Assume that `file.txt` has the following content:

``` bash
Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10
```

Your script should output the tenth line, which is:

``` bash
Line 10
```

**Note:**

1. If the file contains less than 10 lines, what should you output?

2. There's at least three different solutions. Try to explore all possibilities.



A.

``` bash
# Read from the file file.txt and output the tenth line to stdout.
cat file.txt | awk 'BEGIN{}; { if(NR==10) {print;} }; END{};'
```

- awk: 파일로부터 레코드를 선택하고, 선택된 레코드에 포함된 값을 조작하거나 데이터화 함.
- 패턴, 분류, 텍스트, 조작, 연산, 액션 등 수행
- https://recipes4dev.tistory.com/171 참고.