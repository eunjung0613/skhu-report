def pibo(num):
    a,b = 0,1
    for i in range (num):
        a,b=b,a+b
    return a

print(pibo(13))

str1 = "ㄱㄷ"
print(str1.find("ㅅ"))