def isPalindrome(s):
    tmp = []
    for i in s:
        if 97 <= ord(i) < 123:
            tmp.append(i)
        elif 65 <= ord(i) <= 90:
            tmp.append(i.lower())

    for k in range(0, len(tmp)):
        if tmp[k] != tmp[-k]:
            return False
        else:
            return True


s = ["A man, a plan, a canal: Panama"]
print(isPalindrome(s))

# TypeError: ord() expected a character, but string of length 30 found
