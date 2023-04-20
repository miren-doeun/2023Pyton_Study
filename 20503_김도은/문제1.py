num=int(input("숫자 입력:"))

if num%3==0:
    if num%5==0:
        print("3과 5의 공배수")
    else:
        print("3의 배수")
else:
    print("3의 배수 아님")
