##flowchat-question


start

Declare two integer variables X and Y

Read the values of X and Y

Check if X <= Y

Yes

Print the value of X

Increment the value of X by 1
Else no
--------------------------solution-------------------
x,y=map(int,input().split())
while(x<=y):
  print(x,end=" ")
  x+=1
