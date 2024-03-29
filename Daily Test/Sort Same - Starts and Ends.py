The program must accept N string values containing only lower case alphabets as the input. The program must sort the string values starting and ending with the same alphabet. Then the program must print the N modified string values as the output.
Boundary Condition(s):
2 <= N <= 50
2 <= Length of each string value <= 100
Input Format:
The first line contains N.
The next N lines, each containing a string.
Output Format:
The first N lines, each containing a string representing the N modified string values.
Example Input/Output 1:
Input:
5
rotator
madam
auto
bomb
travels
Output:
bomb
madam
auto
rotator
travels
Explanation:
The string values starting and ending with the same alphabet are rotator, madam and bomb.
After sorting those 3 string values in their positions, the string values become
bomb
madam
auto
rotator
travels
Example Input/Output 2:
Input:
6
river
steps
chair
libel
window
heath
Output:
heath
libel
chair
river
steps
window
----------------------------solution----------------------------------------
n=int(input());v=[];k=[];c=0
for i in range(n):
    s=input().strip()
    v.append(s)
    if s[0]==s[-1]:
        k.append(s)
k.sort()
for i in range(0,n):
    if v[i][0]==v[i][-1]:
        print(k[c])
        c=c+1
    else:
        print(v[i])  
