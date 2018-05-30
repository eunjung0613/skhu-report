# 딕셔너리 함수
dic = {
    'name' : 'eunjung', 'age':'20'
}
print(dic)
del dic['name']
print(dic)

#using tuple
t= (1,2,3,4)
list = []
dic = {}

print(t)
# t[1]=(2) 로 바꿀 수 없음

"""주제 : url 라이브러리"""
"""import os
print(os.getcwd()) #현재 디렉토리 출력
try:
    n = os.mkdir((input("파일을 생성할 디렉토리 입력: ")))
except:
    if not os.mkdir(n):
        print("입력한디렉토리는 존재하지 않습니다.")
"""
import urllib.request
req = urllib.request
d = urllib.request.urlopen("https://forest.skhu.ac.kr/")
status = d.getheaders()
for s in status:
    print(s)