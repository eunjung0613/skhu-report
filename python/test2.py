py1 = int(input("하나의 정수를 입력하세요. : "))
py2 = int(input("하나의 정수를 입력하세요. : ")) #정수 입력받음

def add (a,b):
    addresult = (a + b)
    return addresult

def min (a,b) :
    minresult = (a-b)
    return minresult  # 두개의 정수를 빼는 함수생성 및 뺀 값 반환

a = "더한 값은 {} 입니다.".format(add(py1,py2))
b = "뺀 값은 {}입니다.".format(min(py1,py2))  # 두 코드 모두 포맷 이용하여 더하고 뺀 값을 저장.

print (a) #더한 값 프린트
print (b) #뺀 값 프린트