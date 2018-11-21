#12
def max (*a):
    tab = a[0]
    for i in range(1,len(a)):
        if tab < a[i]:
            tab = a[i]
    return tab

print("최대값: %d" %max(6,8,9,-10,4))

#14
list_name = []
while True:
    for i in range(0,len(list_name)):
        print(list_name[i])
    print("대기자 추가: A")
    print("대기자 호출: C")
    play = input("명령어(A/C): ")
    if (play == 'A'):
        name = input("대기자 성명: ")
        list_name.append(name)
    elif (play == 'C'):
        print("호출 고객: %s" %list_name[0])
        del list_name[0]
    elif (play == ''):
        break
    else:
        print("A 또는 C를 입력해주세요. 마치려면 아무 것도 입력하지 말고 엔터를 쳐주세요.")
#13

fin = input("입력하세요: ")
we = "bob"
if we in fin:
    print(fin.count(we))