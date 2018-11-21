"""
챕터: day3
주제: set
작성일: 2019. 9 .13
작성자: 김은정
"""

s = {7,8,9,7} #원래 집합은 순서 의미가 없고 중복을 허용하지 않는다.
fruits = {'a':'사과', 'b': '배', 'c':'복숭아', 'd':'딸기'}
print(s)
# 딕셔너리를 set으로 변환하기
print(set(fruits)) # key값만 set으로 변환된다.

# [3,4,5]를 set으로 형변환하여 s에 저장하고, 이를 출력하라.
list =  [3,4,5]
s = set(list)
print(s)

#인덱스를 사용할 수 없음. 위치가 의미가 없기 때문에 add를 이용하여 하나 추가해야 한다.
s.add(10)
print(s)

#remove로 삭제
s.remove(10)
print(s)

#정렬한 결과가 넘어옴
print(sorted(s))