# Day 3 연산자와 형변환 연습

a = 15.0
b = 4.0

print("%d + %d = %d"%(a,b,a+b)) #덧셈
print("%d - %d = %d"%(a,b,a-b)) #뺄셈
print("%d * %d = %d"%(a,b,a*b)) #곱셈
print("%f / %f = %f"%(a,b,a/b)) #나눗셈 %f로 출력
print("%d / %d = %d"%(a,b,a/b)) #나눗셈 %d로 출력
print("%f // %f = %f"%(a,b,a//b)) #나눗셈 %f로 출력 단, /가 더블 //
print("%d // %d = %d"%(a,b,a//b)) #나눗셈 %d로 출력 단, /가 더블 //
print("%d %% %d = %d"%(a,b,a%b)) #나머지
print("%d ** %d = %d"%(a,b,a**b)) #승수
# 더블 // 사용 경우 나눗셈의 소수점 부분이 잘려서 나타난다.