Given a string S as the input, the program must print the mismatch alphabet (which is not in sequence) in the string.
Boundary Condition(s):
4 <= Length of S <= 10
Input Format:
The first line contains the string S.
Output Format:
The first line contains the mismatch alphabet in the string.
Example Input/Output 1:
Input:
aergc
Output:
r
Explanation:
Arrange the alphabets of the string in a series. Then find the mismatch alphabet so that the string has the series of alphabets (aceg).
Example Input/Output 2:
Input:
rpmsqut
Output:
m
---------------solution---------------------
s = list(map(ord, input().strip()))
h = {} ; s = sorted(s) 
if s[1] - s[0] != s[2] - s[1]:
    print(chr(s[0]))
else:
    print(chr(s[-1]))
 
