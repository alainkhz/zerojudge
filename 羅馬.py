inp = input("輸入2羅馬數字").split(" ")
l1 = inp[0]
l2 = inp[1]
n1 = 0
n2 = 0
for i in range(len(l1)):
    x=l1[i]
    if(x=='I'):
        n1+=1
    elif(x=='V'):
        n1+=5
    elif(x=='X'):
        n1+=10
    elif(x=='L'):
        n1+=50
    elif(x=='C'):
        n1+=100
    elif(x=='D'):
        n1+=500
    elif(x=='M'):
        n1+=1000
for i in range(len(l2)):
    x=l2[i]
    if(x=='I'):
        n2+=1
    elif(x=='V'):
        n2+=5
    elif(x=='X'):
        n2+=10
    elif(x=='L'):
        n2+=50
    elif(x=='C'):
        n2+=100
    elif(x=='D'):
        n2+=500
    elif(x=='M'):
        n2+=1000
c=abs(n2-n1)
c2 =c
s = ""
list = [[1000,'M'],[900,'CM'],[500,'D'],[400,'CD'],[100,'C'],[90,'XC'],[50,'L'],[40,'XL'],[10,'X'],[9,'IX'],[5,'V'],[4,'IV'],[1,'I']]

for i in list:
    if(c%i[0]!=0):
        s += i[1]*(c//i[0])
    elif(i[0]==1):
        s += i[1]*(c//i[0])
    c = c%i[0]
if(c2==0):
    print("zero")
else:
    print(s)
