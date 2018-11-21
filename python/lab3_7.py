"""
챕터: day3
주제 : tuple( immutable)
작성일: 2018. 9. 13
작성자: 김은정
"""
#튜플 t 정의
t = (2, 4, 6, 8, 10) #튜플을 정의할 때는 ()이용
print(t[2]) # 요소를 나타낼 때는 []를 이용
# t[2] = 100 TypeError가 발생한다. 튜플은 요소를 변경할 수 없다. (immutable)

#10 이라는 값이 있는 위치 출력
print(t.index(10))

# t의 길이 출력
print(len(t))

# 2부터 마지막 앞까지 슬라이싱하여 출력하라.
print(t[2:-1])

# t를 처음부터 1번쨰 앞까지 슬라이싱하여 출력하라.
print(t[0:1])

