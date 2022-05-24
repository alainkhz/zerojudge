x = str(input("請輸入需解明的密碼"))
n = len(x)
for i in range(n):
    print(chr(ord(x[i])-7),end="")