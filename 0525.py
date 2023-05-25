score=[88,95,70,100,99]
print(score[0], end='')
print(score[1], end='')
print(score[2], end='')
print(score[3], end='')
print()
print(score[-1], end='')
print(score[-2], end='')
print(score[-3], end='')
print(score[-4], end='')
print()
print('=================================')
score=[88,95,70,100,99]
score[0]=10
score[2]=30

score[-2]=40
score[-1]=50

print(score)
print('=================================')
# animals=['토끼','거북이','사자','호랑이']
# i=0
# while i<5:
#     print(animals[i])
#     i+=1
# print('=================================')
nums=[0,1,2,3,4,5,6,7,8,9]
print(nums[2:5:1])
print(nums[1:7:2])
print(nums[0:5:2])
print('=================================')
nums=[0,1,2,3,4,5,6,7,8,9]
print(nums[:5:1])
print(nums[:7:2])
print(nums[:5:2])
print('=================================')
nums=[0,1,2,3,4,5,6,7,8,9]
print(nums[2::1])
print(nums[1::9])
print(nums[7:10:1])
print('=================================')
nums=[0,1,2,3,4,5,6,7,8,9]
print(nums[2:5])
print(nums[1:7])
print(nums[0:5])
print('=================================')
fruits=['사과','오렌지','딸기','포도','감','키위','멜론','수박']
print(fruits)
print(fruits[0])
print(fruits[1:4])
print(fruits[2:])
print(fruits[-1])
print(fruits[-4:-2])
print(fruits[-3:])
print('=================================')
my_list=list("PytonIsFun!")
print(my_list)
print(my_list[5:11])
print(my_list[-5:-2])
print(my_list[:4])
print(my_list[8:])
print('=================================')
s="pyton"
print(s[2])
print(s[-2])
print(s[1:4])
print('=================================')
file="20210505-104830.jpg"
print("활영 날짜:"+file[4:6]+"월"+file[6:8]+"일")
print("활영 시간:"+file[9:11]+"시"+file[11:13]+"분")
print("확장자:"+file[16:])
print('=================================')
s='차종:코란도C,제조사:쌍용,배기량:1998'
print(s[12:14])
print('=================================')
jumir='901231-1914983'
year=jumir[0:2]
if int(jumir[8])%2==0:
    gender="여자"
else:
    gender="남자"
print("{}년생 {}입니다.".format(year,gender))
print('=================================')
nums=[1,2,3,4]
nums.append(5)
print(nums)

nums.insert(2,99)
print(nums)
print('=================================')
list1=[1,2,3,4,5]
list2=[10,11]
list1.extend(list2)
print(list1)
print('=================================')
# score=[88,95,70,100,99]
# print("100의 위치 :",score.index(100)+1)
# print(score.pop())
# print(score.pop())
# print(score.pop(1))
# print(score)
# print('=================================')
# score=[88,95,70,100,99]
# score.remove(99)
# print("99삭제 후 :",score)
# score.sort()
# print("리스트 정렬 후:",score)
# score.sort(reverse=True)
# print("거꾸로 정렬:",score)
# score.clear()
# print("리스트 삭제:",score)
# print('=================================')
list1=['a','bb','c','d','aaa','c','ddd','aaa','b','cc','d','aaa',]
length=list1.count('aaa')

print(length)
print('=================================')
mylist=['사과','바나나','파인애플']
mylist.append('키위')
mylist.append("배")
for a in mylist:
    print(a)
print('=================================')
scores=[]
while True:
    score=int(input("성적을 입력하세요(종료:-1):"))
    if score==-1:
        break
    else:
        scores.append(score)
        
print(scores)
print('=================================')
num=[]
for i in range(5):
    num.append(int(input("숫자를 입력하시오:")))
num.sort()
print(num)
print('=================================')
emails=[["kim","naver.com"],["hwang","hanmail.net"],["lee","korea.com"],["choi","gmail.com"]]
email_new=[]
for email in emails:
    email_new.append(email[0]+"@"+email[1])
print(email_new)
print('=================================')
fruits=['apple','orange','banana']
for fruit in fruits:
    print(fruit)
print('=================================')
s="Hello"
for i in s:
    print(i,end='')
print("")
print('=================================')
colors=["빨간색","파란색","노란색","초록색"]
for color in colors:
    print("나는 %s을 좋아한다" %color)
print('=================================')

numbers=[7,9,15,18,30,-3,7,12,-16,-12]
sum=0
for number in numbers:
    sum=sum+number
print("합계", sum)
print('=================================')
score=[1,3,5,7,9,11,13]
cnt=0
for num in score:
    if num<10:
        cnt+=1
        print(num,end=' ')
print("\n10보다 작은 수의 개수:",cnt)
print('=================================')
questions=['tr_in','b_s','_axi', 'air_lane']
answers=['a','u','t','p']
count=0
for i in range():
    q='%s에서 밑줄(_) 안에 들어갈 알파벳은?'%questions
    ans=input(q)
    if ans==answers:
        print("정답입니다!")
        count +=1
    else:
        print('틀렸습니다!')
print("당신의 점수는 %d/4 입니다."%count)