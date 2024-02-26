The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section.
Note: N is always an odd integer.
Boundary Condition(s):
3 <= N <= 25
Input Format:
The first line contains N.
Output Format:
The lines containing the desired pattern as shown in the Example Input/Output section.
Example Input/Output 1:
Input:
5
Output:
5 4 3 2 1 2 3 4 5
4 4 3 2 1 2 3 4 4
3 3 3 2 1 2 3 3 3
2 2 2 2 1 2 2 2 2
1 1 1 1 1 1 1 1 1
2 2 2 2 1 2 2 2 2 
3 3 3 2 1 2 3 3 3
4 4 3 2 1 2 3 4 4
5 4 3 2 1 2 3 4 5
Example Input/Output 2:
Input:
3
Output:
3 2 1 2 3
2 2 1 2 2
1 1 1 1 1
2 2 1 2 2
3 2 1 2 3
--------------------------------solution-------------------------

x=int(input())
y=list(map(int,input().split()))
z=list(map(int,input().split()))
if z==y[::-1]:
    print(1)
else:
    print(0)
