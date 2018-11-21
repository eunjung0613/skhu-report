a = int(input("숫자입력: "))
list = []
for i in range(0, 101):
    if(i % 3 == 0):
        list.append(i)
        i += 1
print(list)