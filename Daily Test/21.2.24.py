'''The program must accept a string S and find the longest prefix, which when reversed is also the suffix. Then the program must remove this prefix and the reversed suffix from the string and print the remaining string value. If the remaining string is empty then print -1.
Boundary Condition(s):
2 <= Length of S <= 100

Input Format:
The first line contains S.
Output Format:
The first line contains the string as per the given condition or -1.

Example Input/Output 1:
Input:
abcdefgdcba
Output:
efg

Explanation:
The longest prefix is "abcd", which when reversed is also the suffix "dcba".
After removing the prefix "abcd" and the reversed suffix "dcba" from the string "abcdefgdcba", the string becomes "efg".
Hence the output is efg

Example Input/Output 2:
Input:
lkkl
Output:
-1
'''

---------------------------------solution--------------------------------

a=input().strip()
b=a[::-1]
l=len(a)
for i in range(l):
    if a[i]!=b[i]:
        break
t=(a[i:l-i])
if len(t)==0:
    print("-1")
else:
    print(t)

