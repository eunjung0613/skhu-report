"""
성적 조회하기
국,영,수,과 성적 딕셔너리 생성
key = name, value = point
이름 입력받아서 국영수과 점수 출력 없는 이름 입력하면
"""

korea = {'오상원' : 50, '박찬우':90, '김문수':57 } #국어 딕셔너리 생성
english = {'오상원' : 70, '박찬우':100, '김문수':80 } #영어 딕셔너리 생성
math = {'오상원' : 90, '박찬우':100, '김문수':100 } #수학 딕셔너리 생성
science = {'오상원' : 50, '박찬우': 93 , '김문수': 87 }  #과학 딕셔너리 생성

def exam (name): #e딕셔너리에 있는 점수 조회 함수생성
    if name in korea.keys():
        print(korea[name])
    elif name not in korea.keys():
        print("점수를 입력하지 않았습니다.")
    if name in english.keys():
        print(english[name])
    elif name not in english.keys():
        print("점수를 입력하지 않았습니다.")
    if name in math.keys():
        print(math[name])
    elif name not in math.keys():
        print("점수를 입력하지 않았습니다.")
    if name in science.keys():
        print(science[name])
    elif name not in science.keys():
        print("점수를 입력하지 않았습니다.")
while True:
    print("1. 조회 2. 추가 3.삭제 4.종료")
    num = int(input("숫자를 입력하세요: "))
    if (num == 1):
        name = str(input("이름을 입력하세요: "))
        exam(name)
    elif (num==2):
        play = input("과목을 입력해주세요. : ")
        if (play == '국어'):
            ko = input("이름을 입력해주세요. : ")
            po = int(input("점수를 입력해주세요. : "))
            korea[ko]=po
        elif (play == '수학'):
            ko = input("이름을 입력해주세요. : ")
            po = int(input("점수를 입력해주세요. : "))
            math[ko]=po
        elif (play == '영어'):
            ko = input("이름을 입력해주세요. : ")
            po = int(input("점수를 입력해주세요. : "))
            english[ko]=po
        elif (play == '과학'):
            ko = input("이름을 입력해주세요. : ")
            po = int(input("점수를 입력해주세요. : "))
            science[ko]=po
    elif (num==3):
        play = input("과목을 입력해주세요. : ")
        if (play == '국어'):
            ko = input("이름을 입력해주세요. : ")
            del(korea[ko])
        elif (play == '수학'):
            ko = input("이름을 입력해주세요. : ")
            del (math[ko])
        elif (play == '영어'):
            ko = input("이름을 입력해주세요. : ")
            del (english[ko])
        elif (play == '과학'):
            ko = input("이름을 입력해주세요. : ")
            del (science[ko])
        else:
            print("없는 값입니다!")
    elif(num==4):
        print("프로그램을 종료합니다.")
        break
