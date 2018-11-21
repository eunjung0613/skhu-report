"""
챕터: day4
주제: 반복문(while)문
문제:
사용자가 입력한 영문자를 아래와 같이 출력
(예)
BINGO
 INGO
  NGO
   GO
    O
작성자: 김은정
작성일: 2018. 9. 27
"""
num = input("영단어를 입력하세요. : ")
num1 = len(num)
for i in range(0,num1):
    c = ""
    for j in range(0,i):
        c = c +" "

    print(c+num[i:])