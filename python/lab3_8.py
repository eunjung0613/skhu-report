"""
챕터: day3
주제: Dictionary
작성일: 2019. 9 .13
작성자: 김은정
"""

# fruits = {'a':'사과', 'b': '배', 'c':'복숭아', 'd':'딸기'}
fruits = {'a':'사과', 'b': '배', 'c':'복숭아', 'd':'딸기'}
print(fruits)
# 키가 'a'인 경우의 값을 출력하라.
print(fruits['a'])

# get() 함수는 키가 존재하지 않는 경우, None을 반환
print(fruits.get('k'))

#키가 'b'인 경우의 값을 '체리' 로 수정하라.
fruits['b'] = '체리'
print(fruits)

#키가 'f'인 값 '아보카도' 를 추가하라.
fruits['f'] = '아보카도'
print(fruits)

#fruits에서 키가 'a'인 경우의 값의 길이를 출력하라
print(len(fruits['a']))

#fruits의 모든 key 출력
print(fruits.keys())

#fruits의 모든 key 출력
print(fruits.values())

#fuits 안에 'a' 라는 키가 있으면 True, 없으면 False를 출력하라.
print('a' in fruits)
print('체리' in fruits) # in은 key값에 존재하는 지에 대한 boolean 값. '체리' 는 key가 아님. 따라서 False.
print('a' in fruits.keys())

# furits의 values 중에 '복숭아'가 있으면 True, 없으면 False를 출력하라.
print('복숭아' in fruits.values())

f = sorted(fruits) #key 순서에 따라 정렬된 key의 리스트를 반환.
print(fruits)
print(f)

#value 를 정렬된 순서의 list로 출력
fv = sorted(fruits.values())
print(fv)

# 키와 값을 튜플의 리스트로 만들어 출력하라.(.items())
print(fruits.items())

#삭제 (del 사용)
#'c' 라는 키를 가지는 fruits를 삭제하라.
del(fruits['c'])
print(fruits)