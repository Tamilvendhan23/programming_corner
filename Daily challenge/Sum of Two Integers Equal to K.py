The program must accept N integers and an integer K as the input. The program must print yes if the sum of any two integers among the N integers is equal to K. Else the program must print no as the output.
Boundary Condition(s):
2 <= N <= 100
1 <= K, Each integer value <= 10^8
Input Format:
The first line contains N and K separated by a space.
The second line contains N integers separated by a space.
Output Format:
The first line contains yes or no.
Example Input/Output 1:
Input:
5 10
2 5 8 4 7
Output:
yes
Explanation:
The sum of 2 and 8 is 10. So yes is printed.
Example Input/Output 2:
Input:
4 25
12 24 15 11
Output:
no

-------------------------------solution------------------------------------------
n,m=map(int(input().split()))
a=list(map(int,input().split()))
k=0
 for i in range(n):
    for j in range(i+1,n):
      if a[i]+a[j]==m:
        k=1
if k==1:
  print('yes')
else:
  print('no')
