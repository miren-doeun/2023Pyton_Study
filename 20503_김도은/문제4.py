import random

answer=random.randint(1,100)

print(f"정답 : {answer}")
guess=0
p=0
print("1부터 100 사이의 숫자를 맞히기")
while (1):
    guess=int(input("숫자를 맞혀 보세요:"))
    p+=1
    if guess>answer:
        print("높음")
    elif guess<answer:
        print("낮음")
    else:
        break;
print(f"축하합니다. 시도횟수 = {p}")
