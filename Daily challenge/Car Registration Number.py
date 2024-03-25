The program must accept the registration number N of a car as the input. The program must print the sum of digits in N as the output.
Boundary Condition(s):
9 <= Length of N <= 13
Input Format:
The first line contains N.
Output Format:
The first line contains the sum of digits in N.
Example Input/Output 1:
Input:
TN-76 AC-1234
Output:
23
Explanation:
The digits in the registration number TN-76 AC-1234 are 7, 6, 1, 2, 3 and 4.
So their sum 23 is printed as the output.
Example Input/Output 2:
Input:
TN-13 AD-9051
Output:
19
  ----------------------------solutionn----------------------
  s=input()
  a=[]
  for i in range(len(s)):
      if s[i].isdigit():
          a.append(s[i])
print(sum(a))
