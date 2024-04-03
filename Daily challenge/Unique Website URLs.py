The program must accept N string values representing the website URLs and print the count of unique websites.
Boundary Condition(s):
2 <= N <= 50
5 <= Length of each string <= 50
Input Format:
The first line contains N.
The next N lines, each containing a string.
Output Format:
The first line contains the count of unique websites.
Example Input/Output 1:
Input:
6
www.skillrack.com
http://www.skillrack.com
https://www.skillrack.com
www.google.com
http://www.google.com
google.com
Output:
2
Explanation:
In the given 6 URLs, the unique websites are skillrack.com and google.com.
Hence the output is 2
Example Input/Output 2:
Input:
9
www.skillrack.com
http://www.skillrack.com
https://www.skillrack.com
www.google.com
http://www.google.com
google.com
www.google.in
skillrack.com
www.skillrack.in
Output:
4
-----------------------------------solution-----------------------------------------
  n=int(input())
l=[]
for i in range(n):
    a=input()
    l.append(a)
d=[]
for i in l:
    dd=i.split('www.')[-1]
    d.append(dd)
k=[i.rstrip("\r") for i in d]
c=set(k)
print(len(c))
