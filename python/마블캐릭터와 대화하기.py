from datetime import *
print("다음 마블 캐릭터 중 하나를 입력해 주세요.")
print("토르, 로키, 아이언맨, 자비스, 타노스 ")
PL = input()

if (PL=='토르'):
    print("만나서 반갑네 나는 아스가르드의 토르라고 하네.\n 토르가 당신의 손을 잡고 흔들었습니다.")
elif (PL == '로키'):
    print("로키를 마주쳤다.\n로키가 당신을 바라본다.\n이에 당신히 할 행동은?")
    print("▶때린다\n▶숨는다\n▶인사한다\n선택지를 골라 입력해주세요.")
    sl = input()
    if (sl == '때린다'):
        print("당신은 로키를 때렸습니다.\n로키는 화가나 당신을 죽였습니다.\n유다희...")
    elif (sl=='숨는다'):
        print("로키는 당신을 가소로워 합니다.\n로키가 그대로 지나쳐 갑니다.\n목숨은 부지했네요^^")
    elif (sl=='인사한다'):
        print("나는 아스가르드의 로키다.\n미개한 미드가르드인.\nKneel down!\n당신은 로키 앞에서 무릎을 강제로 꿇었다.")
elif (PL =='아이언맨'):
    print("오 나는 정말 바빠서 다른 사람한테 놀아달라고 해 honey.")
elif (PL =='자비스'):
    today = datetime.now()
    print("안녕하십니까 sir. 저를 선택해 주셔서 감사합니다. 지금 시간은 {}입니다.".format(today))
elif(PL == '타노스'):
    print("당신은 타노스와 마주치자 마자 죽었습니다^^.")