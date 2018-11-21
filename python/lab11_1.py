"""
챕터: day6
주제: class
문제: 정수 집합 클래스
1. intSet 클래스는 정수들의 집합이다. 정수들을 관리하는 리스트 self.vals를 애트리튜브로 가진다.
2. 새로운 정수 e를 추가하는 insert 메쏘드, 해당 요소가 이미 있다면 추가하지 않음
3. e가 정수집합에 포함되어 있는지 확인하는 메쏘드인 involve정의(True,False 반환)
4. e를 제거하는 remove 메쏘드
5. 단, e가 해당 집합에 없다면 적당한 오류 메세지를 출력
6. 집합 형식의 문자열로 변환시켜주는 __str__메쏘드. 단, 정수들은 정렬되어 반환되어야 한다.

작성자: 김은정
작성일: 2018.11.1
"""

class intSet():
    #생성자 메쏘드(초기화)
    def __init__(self):
        self.vals = [] #정수들을 관리하는 리스트

    #새로운 정수 e를 추가하는 메쏘드
    def insert(self,e):
        if e in self.vals: #e가 리스트 안에 있는지 검사
            return self.vals #있다면 e를 포함하지 않은 vals리스트 반환
        else: #만약 e가 없다면
            return self.vals.append(e) #리스트에 e를 추가 후 반환

    #e가 정수집합에 포함되어 있는지 확인하는 메쏘드
    def involve(self,e):
        if e in self.vals: #e가 리스트 안에 존재하면
            return True #True 반환
        else: #아니면
            return False #False반환

    #e를 제거하는 메쏘드
    def remove(self,e):
        if e in self.vals: #e가 리스트에 존재한다면
            self.vals.remove(e) #리스트 안에 e를 지우고
            return self.vals #지워진 리스트를 반환
        else: #존재하지 않을 경우
            return print("해당 집합에 %d가 존재하지 않습니다." %e) #오류메세지 반환

    #집합 형식의 문자열로 변환시켜주는 메쏘드
    def __str__(self):
        self.vals.sort() #리스트 정렬
        v= "" #문자열로 만들기 위한 변수 v 정의
        for i in range(0,len(self.vals)): #for문을 리스트안에 숫자만큼 돌려서
            v += str(self.vals[i])+" " #v에 i번째 리스트 값을 문자열화
        return v #만들어진 문자열v를 반환


#실행부분
"""
A. intSet을 저장하는 변수 s를 정의
B. s에 insert를 이용하여 하나씩 5,3,7을 삽입
C. s를 정렬하여 출력
D. s에 8이 있는지 결과 출력
E. s에 3이 있는지 결과 출력
F. s에서 3을 제거
G. s에서 4를 제거
H. s를 정렬하여 출력
"""

s = intSet() #intSet을 저장하는 변수 s를 정의

s.insert(5) #s에 insert를 이용하여 5를 삽입
s.insert(3) #s에 insert를 이용하여 3,7를 삽입
s.insert(7) #s에 insert를 이용하여 7를 삽입
print(s) #s를 정렬하여 출력

print(s.involve(8)) #s에 8이 있는지 결과 출력
print(s.involve(3)) #s에 3이 있는지 결과 출력

s.remove(3) #s에서 3을 제거
s.remove(4) #s에서 4를 제거

print(s) #s를 정렬하여 출력
