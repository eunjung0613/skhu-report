"""
문제 : 백준 알고리즘 10871번 -
정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
작성자 : 김은정
작성일 : 2018 . 9 20
"""

a = input().split(" ")
X = int(a[1])
b = input().split(" ")
c = ""
for i in b :
    if (int(i)<X):
        c += i+" "
print(c)