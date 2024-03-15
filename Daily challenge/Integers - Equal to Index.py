
The program must accept N integers and print the integers which are equal to their index value as the output. If there is no such integer, the program must print -1 as the output.
Boundary Condition(s):
1 <= N <= 100
Input Format:
The first line contains N.
The second line contains N integers separated by a space.
Output Format:
The first line contains the integer value(s) or -1 based on the given conditions.
Example Input/Output 1:
Input:
6
5 4 2 3 6 5
Output:
2 3 5
Explanation:
Here 2, 3 and 5 are the integers equal to their index value.
Example Input/Output 2:
Input:
4
2 3 1 4
Output:
-1
==============================solution=================================
n=int(input())
num=list(map(int,input().split()))
flag=0
for i in range(n):
    if i==n[i]:
      print(i,end=' ')
      flag=1
if flag==0:
  print(-1)
