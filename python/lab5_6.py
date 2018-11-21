"""
챕터: day5
주제: sum 함수 이용
문제:
작성자: 김은정
작성일: 2018. 10. 4
"""

"""
   1에서 30까지의 합 출력 sum(range(1,31))
"""
print(sum(range(1,31)))
"""
   1,3,5,7을 list로, tuple로, set으로 전달하여 합 출력
"""
list1 = [1,3,5,7]
two = (1,3,5,7)
three={1,3,5,7}
print(sum(list1))
print(sum(two))
print(sum(three))
"""
   50에 1,3,5,7의 합을 더하여 출력
"""
l = [1,3,5,7]
print(sum(l,50))