"""
챕터: day3
주제: 문자열 연습
작성자: 김은정
날짜: 2018. 9. 6

"""
"""
1. 이름을 입력 받는다.
2. 이름을 열 번 출력한다. (반복문을 사용하지 않는다.)
"""
name = input("이름을 입력하세요: ")
print(name*10)
"""
3. 나이를 정수형으로 입력받는다.
4. 이름과 나이를 다음 형식으로 s에 저장한다. 정수형인 나이를 문자열로 변환하여 연결한다.
예. "나의 이름은 홍길동이고, 21세 입니다."
5. s를 다섯 번 출력한다. 매번 줄바꿈이 포함되어야 한다.
"""
age = int(input("나이를 입력하세요: "))
s = "나의 이름은 "+name+"이고,"+str(age)+"세입니다.\n"
print(s*5)
"""
6. 입력을 받지 않고. 다음을 s1에 저장한다. 반드시 줄바꿈이 표현되어야 한다. \n을 사용하지 않는다. s1을 출력한다.
예:
나의 이름은 홍길동이고,
21세 입니다.
"""
s1 = """
나의 이름은 홍길동이고.
21세 입니다.
"""
print(s1)
