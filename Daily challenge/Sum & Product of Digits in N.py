
The program must accept an integer N as the input. The program must find the sum of digits S and the product of digits P in N. Then the program must print yes if the sum of S and P is equal to N. Else the program must print no as the output.
Boundary Condition(s):
10 <= N <= 100
Input Format:
The first line contains N.
Output Format:
The first line contains yes or no.
Example Input/Output 1:
Input:
59
Output:
yes
Explanation:
Here N = 59.
The sum of digits in 59 is 14 (5+9 = 14).
The product of digits in 59 is 45 (5*9 = 45).
The sum of 14 and 45 is 59 (14+45 = 59) which is equal to the given integer 59.
So yes is printed as the output.
Example Input/Output 2:
Input:
63
Output:
no

------------------------------solution----------------------
n=int(input())

s=str(n)

summ=0

prod=1

for i in range(len(s)):

      summ+=int(s[i])

      prod*=int(s[i])

if summ+prod==n:
  print('yes')

else: 
  print('no')
