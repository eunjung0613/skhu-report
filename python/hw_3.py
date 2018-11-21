coffie = 10

while True  :
    money = int(input("돈을 넣어주세요. : "))
    if money == 300:
        print("커피를 줍니다.")
        coffie -= 1
    elif money > 300:
        a = money - 300
        print("거스름돈 {}원을 돌려주고 커피를 줍니다.".format(a))
        coffie -= 1
    elif money < 300:
        b = 300 - money
        print("돈을 다시 돌려줍니다. {}원이 모자랍니다.".format(b))
        print("남은 커피는 {}잔입니다.".format(coffie))
    if coffie == 0:
        print("커피가 다 떨어졌습니다. 판매를 종료합니다.")
        break