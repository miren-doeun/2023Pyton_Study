max=0
num=0
maxi=0
maxj=0
j=100
for i in range(1,101):
    j-=1
    num=i*j
    if num>max:
        max=num
        maxi=i
        maxj=j
print(f"최대가 되는 경우 : {maxi} * {maxj} = {max}")
