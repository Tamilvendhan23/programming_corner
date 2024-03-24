The program must accept a string S as the input. The program must print YES if the first half of S is equal to the second half of S after removing exactly one character from S. Else the program must print NO as the output.
Note: The length of S is always odd.
Boundary Condition(s):
3 <= Length of S <= 999
Input Format:
The first line contains S.
Output Format:
The first line contains YES or NO.
Example Input/Output 1:
Input: 
meome
Output:
YES
Explanation:
After removing the middle character in the string "meome", the string becomes "meme".
Now the first half "me" is equal to the second half "me".
So YES is printed as the output.
Example Input/Output 2:
Input:
5#sdf#sdf
Output:
YES
Example Input/Output 3:
Input:
LioeLin
Output:
NO
-----------------------------solution-----------------------------
def f(a):
 l=len(a)
 for i in range(l):
  b=a[:i]+a[i+1:]
  if b[:l//2]==b[l//2:]:
      return "YES"
 return "NO"
print(f(input().strip()))
