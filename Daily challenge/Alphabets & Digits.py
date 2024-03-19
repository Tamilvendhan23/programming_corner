The program must accept a string S containing alphabets and digits as the input. The program must print all the alphabets in S. Then the program must print all the digits in S as the output.
Boundary Condition(s):
2 <= Length of S <= 1000
Input Format:
The first line contains S.
Output Format:
The first line contains all the alphabets followed by the digits in S.
Example Input/Output 1:
Input:
Pass123Lock456
Output:
PassLock123456
Explanation:
All the alphabets in the string Pass123Lock456 are printed.
Then all the digits in the string Pass123Lock456 are printed.
Example Input/Output 2:
Input:
3a6bd0v
Output:
abdv360

---------------------solution--------------------
n=input()
a=[]
b=[]
for i in range(len(n)):
  if n[i].isalpha():
    a.append(n[i])
else:
   b.append(n[i]))
print(''.join(a+b))
