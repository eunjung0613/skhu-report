"""
챕터: day3
주제: 여러 타입을 포함한 리스트
작성일: 2018. 9. 13
작성자: 김은정

"""
#l 에 [1,2,[3,'john',4],'hi'] 를 저장한다.
l = [1,2,[3,'John',4],'Hi']
#l에 3번째 요소를 출력한다.
print(l[3])

#l의 2번째 요소를 출력한다
print(l[2])

#2라는 값이 있는 위치 출력
print(l.index(2))

#l의 2번째 요소의 1번째 요소를 출력한다.
print(l[2][1])

#l의 2번째 요소와 1번째 요소의 앞의 세글자만 출력한다.
print(l[2][1][0:3])

#in 연산 연습
print(2 in l)

# l에 3이 있으면 True 아니면, False를 출력하라.
print(3 in l) # l안에 [3,john,4] 라는 리스트가 들어간거지 3이 직접적으로 들어가지 않는다.

# l의 2번째 요소 안에 3 있으면 True 아니면, False를 출력하라.
print(3 in l[2])

l[1] = 8 #mutable 하다. list는 mutable한 데이터 타입이다.
print(l)

