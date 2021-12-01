yr = int(input())
if ((yr % 4 == 0) & (yr % 100 != 0)) | (yr % 400 == 0):
    print(1)
else:
    print(0)
