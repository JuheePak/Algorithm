def isPalindrome(s) -> bool:
    tmp = []
    for i in s:
        if 97 <= ord(i) < 123:  # 소문자
            tmp.append(i)
        elif 65 <= ord(i) <= 90:  # 대문자
            tmp.append(i.lower())
        elif 48 <= ord(i) <= 57:  # 숫자
            tmp.append(i)

    checkList = []
    for k in range(0, len(tmp)):
        if tmp[k] != tmp[-(k + 1)]:
            checkList.append(tmp[k])

    if len(checkList) >= 1:
        return False
    else:
        return True

s = ["A man, a plan, a canal: Panama"]
ss = ["race a car"]
print(isPalindrome(s))
print(isPalindrome(ss))


