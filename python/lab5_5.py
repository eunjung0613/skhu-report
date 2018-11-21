"""
챕터: day5
주제: min 함수 이용
문제:
작성자: 김은정
작성일: 2018. 10. 4
"""

"""
   I 변수에 [4,7,9,11,-5]를 저장한다.
   l에서 최소값, 최대값을 출력한다.
"""
# I변수에 리스트 저장
I = [4,7,9,11,-5] #iterable한 값
print(min(I)) #리스트 내에서 최소값 출력, min의 첫번째 매개변수는 iterable한 값을 넘긴다.
print(max(I)) #리스트 내에서 최대값 출력
"""
   fruits 변수에 "apple","orange","banana"를 tuple로 배정한다
   fruits에서 최소값과 최대값을 출력한다.
"""

fruits = ("apple","orange","banana")
print(min(fruits))
print(max(fruits))

"""
   fruits 변수에 orange를 Orange로 변경한다.
   frutis에서 최소값과 최대값을 출력한다.
"""
fruits = ("apple","Orange","banana") #대문자가 소문자보다 아스키코드값이 작다. 그렇기 때문에 대문자가 가장 작은 값으로 나옴
print(min(fruits))
print(max(fruits))

"""
   대소문자를 구분하지 않고 최대 최소를 얻기 위해
   min, max함수의 마지막 key 매개변수로 str.lower(모두 소문자로 바꾸어 비교)를 전달한다. (min(fruits,key=str.lower))
"""
fruits = ("apple","Orange","banana")
print(min(fruits,key=str.lower))
print(max(fruits,key=str.lower))

"""
   1부터 50까지의 수 중 최대, 최소값을 출력한다. (range 이용, min(range(1,51)))
"""
print(min(range(1,51)))
print(max(range(1,51)))

"""
   min 함수에 직접 1,3,6 값을 전달하여, 최소값 출력
"""
print(min(1,3,6))
