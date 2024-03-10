Sum of ASCII Values
The program must accept a string S as the input. The program must print the sum of the ASCII values of all the characters in the string S.
Boundary Condition(s):
2 <= Length of S <= 100
Input Format:
The first line contains S.
Output Format:
The first line contains the sum of the ASCII values of all the characters in the string S.
Example Input/Output 1:
Input:
abcd
Output:
394
Explanation:
The ASCII value of a is 97.
The ASCII value of b is 98.
The ASCII value of c is 99.
The ASCII value of d is 100.
The sum of those ASCII values is 394.
Hence the output is 394
Example Input/Output 2:
Input:
LMLM
Output:
306
  ----------------------solution------------------------------
n=input()
res=sum(ord(i) for i in n)
  print(res)
