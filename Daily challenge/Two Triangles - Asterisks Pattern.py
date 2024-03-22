The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section.
Note: The value of N is always odd.
Boundary Condition(s):
3 <= N <= 99
Input Format:
The first line contains N.
Output Format:
The lines containing the desired pattern as shown in the Example Input/Output section.
Example Input/Output 1:
Input:
5
Output:
*   *
** **
*****
** **
*   *
Example Input/Output 2:
Input:
7
Output:
*     *
**   **
*** ***
*******
*** ***
**   **
*     *
  -------------------------------------------solution---------------------------------------------
  
n = int(input())
lis = [' ' for _ in range(n)]
ans = []
for i in range(n//2 + 1):
    lis[i] = lis[-i-1] = '*'
    print(*lis, sep='')
    ans.append(lis[:])
for i in ans[:-1][::-1]:
    print(*i, sep='')
