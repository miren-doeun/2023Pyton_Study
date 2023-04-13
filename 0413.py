for i in(1,2,3):
    print(i)
print("============================")
for i in range(10):
    print(i, end='')
print('')
print("============================")
for i in range(1,11):
    print(i, end='')
print("")
print("============================")

for i in range(1,10,2):
    print(i,end='')
print("")
print("============================")

for i in range(20,0,-2):
    print(i, end='')
print("")
print("============================")
for i in range(0,5):
    print("안녕하세요")
print("============================")
a=10
for num in range(1,5,2):
    a+=num
print(a)
print("============================")
for stu in range(1,4):
    print(stu,"번째 학생의 성적 처리")
print("============================")
for i in range(1,11):
    print(i*2, end=' ')
print("")
print("============================")
for i in range(1,10):
    print("2 x", i,"=",2*i)
print("============================")
num=0
for i in range(1,11):
    num+=i
    print("i의 값:",i,"=> 합계:",num)
print("============================")
sum=0
num=0
for sum in range(2,101):
    if(sum%2==0):
        num+=sum
print("sum=",num)
print("============================")
fac=int(input("값:"))
j=1
for i in range(1,fac+1):
    j=j*i
print(fac,end='! =')
print(j)
print("============================")
i=1
for i in range(i,8):
    print(5*i,end=' ')
print("")
for i in range(8,15):
    print(5*i,end=' ')
print("")
for i in range(15,21):
    print(5*i,end=' ')
print("")
print("============================")
n=int(input("정수를 입력하시오:"))
for i in range(1,n+1):
    if(n%i==0):
        print(i,end=' ')
print("")
print("============================")
i=0
j=1
n=0
print(i,j,end=" ")
for k in range(3,21):
    n=i+j
    print(n, end=" ")
    i=j
    j=n
print("")
print("============================")
i=0
for i in range(1,41):
    if(i%10==0):
        print("+",end='')
    if(i%10>=1):
        print("-",end="")
print("")
print("============================")
i=0
for i in range(1,40):
    if(i%5==0):
        print("+",end='')
    if(i%5>=0):
        print("-",end='')
print("")
print("============================")
print("")
print("----------------------------")
print("센치   인치    피트    야드")
print("----------------------------")
for cm in range(10,101,10):
    print(cm,"   ", round(cm*0.393701,1),"   ", round(cm*0.032808,1),"   ", round(cm*0.010936,1),"   ", end='')
    print("")
print("============================")
for i in range(1,1001):
    print(i,end='')
    if i==10:
        break
print("============================")
score=[92,86,68,120,56,72]
for s in score:
    if(s<0 or s>100):
        break
    print(s)
print("성적 처리 끝")
print("============================")
score=[92,86,68,120,56,72]
for s in score:
    if(s<0 or s>100):
        continue
    print(s)
print("성적 처리 끝")
print("============================")
print("3+4?")
while (1):
    a=int(input("정답을 입력하세요:"))
    if a==7:
        print("참 잘했어요")
        break
