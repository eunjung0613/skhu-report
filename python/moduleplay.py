import mymodule

a = int(input("정수를 입력하세요. : "))
b = int(input("또 다른 정수를 입력하세요. : "))
print("다음 덧셈의 결과입니다.")
print(mymodule.sum(a, b))
print("다음 뺄샘의 결과입니다.")
print(mymodule.min(a, b))
print("다음 곱셈의 결과입니다.")
print(mymodule.mul(a, b))
print("다음 나눗셈의 결과입니다.")
print(mymodule.div(a, b))


