import random
import datetime
from pytz import timezone


print(random.random())

print(random.randrange(1,7))

print(random.randint(1,6))

print(random.choice([10,20,30]))

print("=========================================")



now = datetime.datetime.now(timezone('Asia/Seoul'))

if(now.hour<=12 and now.hour>=6):
    print("좋은 아침 입니다. 지금 시각은", now.hour,"시 입니다.")
    if(random.random==1):
        print("현제 날씨가 화창하지 않습니다.")
        print("종달새가 노래하지 않습니다.")
    else:
        print("현제 날씨가 화창합니다.")
        print("종달새가 노래합니다.")
if(now.hour>=13):
    print("이걸 이제서야 일어나누")
    
print("=========================================")


x=0
while x<3:
    print("안녕하세요")
    x+=1
print("=========================================")

student=1
while student <=3:
    print(student, "번 학생의 성적을 처리한다.")
    student+=1
print("=========================================")

m=0
while m<10:
    print("3 *", m,"=", 3*m)
    m+=1
print("=========================================")


num = 1
sum = 0
while sum<=50:
    sum += num
    print("num의 값 : %d => 합계:%d"%(num, sum))
    num+=1
print("=========================================")


num=150
sum=0
while num<=300:
    if(num%2==1):
        sum+=num
    num+=1
print("sum = ", sum)

print("=========================================")


s=-5
h=0
print("=============")
print("섭씨     화씨")
print("=============")
while(s<=5):
    print(s,"      ", s*9.0/5+32)
    s+=1
print("=========================================")

n=10
fact=1
while n>=1:
    fact *=n
    n-=1
    print('10! =',fact)
print("=========================================")


num=1
while num <=20:
    if num%2==0:
        print(num)
    num+=1
print("=========================================")

n=10
while n<=50:
    if n&3>=1:
        print(n, end=' ')
    n+=1

print("=========================================")

pw1=input("암호 입력:")
pw2=input("암호 입력:")
pw3=input("암호 입력:")

if pw1=='java' and pw2 == 'c' and pw3 == 'pyton':
    print("로그인 성공")
else:
    print("로그인 실패")
    
print("=========================================")
pw=''
while pw!='java':
    pw=input("암호 입력:")
while pw!='c':
    pw=input("암호 입력:")
while pw!='pyton':
    pw=input("암호 입력:")
print("로그인 성공")


print("=========================================")


answer=int(random.randrange(1,100))
print("정답:",answer)
print("1부터 100사이의 숫자를 맞추기")
guess=0
n=0
while guess != answer:
    n+=1
    guess=int(input("숫자를 맞춰 보세요:"))
    if guess>answer:
        print("높음")
    else:
        print("낮음")
print("축하합니다. 시도 횟수=",n)
