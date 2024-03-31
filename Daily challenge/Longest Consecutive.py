The program must accept a string S containing only 1's and 0's as the input.
The program must print the length of the longest consecutive 1’s in S as the output. If there are no such consecutive 1's then the program must print -1 as the output.
Boundary Condition(s):
2 <= Length of S <= 1000
Input Format:
The first line contains S.
Output Format:
The first line contains the length of the longest consecutive 1’s in S or -1.
Example Input/Output 1:
Input:
1011011101100011
Output:
3
Explanation:
The length of the longest consecutive 1's in the string 1011011101100011 is 3.
Hence the output is 3
Example Input/Output 2:
Input:
00101010100
Output:
-1
---------------------------solutioin------------------------
s = input().strip()

a = []

c = 0

for i in s:
    if i == '1':
        c += 1
        a.append(c)
    else:
        c = 0

print(max(a) if a else -1)

