for i in range(1,10):
    print(i,"단")
    for j in range(1,10):
        print(i,"*",j,"=",i*j)
    print("")
print("===========================")
i=1
while i<10:
    print(i,"단")
    i+=1
    j=1
    while j<10:
        print(i,"*",j,"=",i*j)
        j+=1
    print("")
print("===========================")

i=0
j=0
for i in range(5):
    for j in range(i+1):
        print("*",end='')
    print("")
print("===========================")
i=0
j=0
for i in range(1,8):
    for j in range(1,8):
        if(i+4==0 or i==j or i+j==8):
            print("*",end='')
        else:
            print(" ",end='')
    print('')
print("===========================")
i=0
j=0
f=0
for i in range(1,6):
    for j in range(i,5):
        print("-",end="")
    for k in range(0,-i,-1):
        print("*",end='')
    print("")
    
print("===========================")
i=1
n=int(input("수 입력:"))
for i in range(2,n+1):
    p=True
    for j in range(2,i):
        if i%j==0:
            p=False
            break
    if p:
        print("%5d"%i, end="")
        
print("")
print("===========================")

price=[500,5000,8900,1800,2500]
fruit=['사과','파인애플','수박']
print(price, end=" ")
print(type(price))
print(fruit,end=" ")
print(type(fruit))
print("===========================")
fruitprice=['사과', 1500, '수박', 8900]
print(fruitprice)
print(type(fruitprice[0]), end=' ')
print(type(fruitprice[1]), end=' ')
print(type(fruitprice[2]), end=' ')
print(type(fruitprice[3]), end=' ')
print("")
print("===========================")

a=[]
b=list()
print(type(a), end=" ")
print(type(b))
print("===========================")

print(len(num))
print(lne(a))
