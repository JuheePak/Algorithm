# def recursion():
#     print("나 불렀음?")
#     recursion()
#

#recursion()

# 5! = 5*4*3*2*1
# 5! = 5*4!
# 5! = 5*4*3!
# 5! = 5*4*3*2!
# 5! = 5*4*3*2*1

def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num-1)

print(factorial(5))
print(factorial(10))