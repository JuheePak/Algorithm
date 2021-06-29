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

- `awk`: 파일로부터 레코드를 선택하고, 선택된 레코드에 포함된 값을 조작하거나 데이터화 함.

- 패턴, 분류, 텍스트, 조작, 연산, 액션 등 수행

- https://recipes4dev.tistory.com/171 참고.

- awk program에는 아래와 같은 키워드가 제공

  ``` bash
      BEGIN   delete  END     function    in      printf
      break   do      exit    getline     next    return
      continue        else    for         if      print      while
  ```

- awk program에는 새로운 변수를 선언하고 값을 할당하거나 참조할 수 있음.

  ``` bash
      ARGC        : ARGV 배열 요소의 갯수.
      ARGV        : command line argument에 대한 배열.
      CONVFMT     : 문자열을 숫자로 변경할 때 사용할 형식. (ex, "%.6g")
      ENVIRON     : 환경변수에 대한 배열.
      FILENAME    : 경로를 포함한 입력 파일 이름.
      FNR         : 현재 파일에서 현재 레코드의 순서 값.
      FS          : 필드 구분 문자. (기본 값 = space)
      NF          : 현재 레코드에 있는 필드의 갯수.
      NR          : 입력 시작 점에서 현재 레코드의 순서 값.
      OFMT        : 문자열을 출력할 때 사용할 형식.
      OFS         : 결과 출력 시 필드 구분 문자. (기본 값 = space)
      ORS         : 결과 출력 시 레코드 구분 문자. (기본 값 = newline)
      RLENGTH     : match 함수에 의해 매칭된 문자열의 길이.
      RS          : 레코드 구분 문자. (기본 값 = newline)
      RSTART      : match 함수에 의해 매칭된 문자열의 시작 위치.
  ```

  

