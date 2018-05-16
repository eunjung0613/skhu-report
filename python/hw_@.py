"""2주차 모범 답안"""

from random import*

def rsp(p2):
    com = randint(1,3)

    if p2 == com:
        print("무승부입니다.")

    elif (p2 ==1 and com ==3) or (p2==2 and com==1) or(p2==3 and com==2):
        print("이겼습니다.")

    else:
        print("졌습니다.")

p1 = input ("가위, 바위, 보 중 하나를 입력하세요. : ")

if p1 == "가위":
    rsp(1)
elif p1 == "바위":
    rsp(2)
elif p1 == "보":
    rsp(3)
else:
    print("가위, 바위, 보 중에 입력해주세요.")




