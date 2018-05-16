point = [90,25,67,45,80]

number=0
for result in point:
    number = number+1
    if result <60:
        continue
    print("%d번 학생 축하합니다. 합격입니다."%number)

list = [1,2,3,4,5,6,66,90,100]

for i in list:
    if(i% 3==0):
        print(i)
        break

        #3에서 나눠지면 반복이 끝남. 만약 break를 지우면 나머지 다 나옴.