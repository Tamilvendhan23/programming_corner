The program must accept N integers and an integer K as the input. The program must find the last occurrence of K in the given N integers and remove it. Then the program must print the remaining N-1 integers as the output. If K is not present in the given N integers, the program must print the N integers as it is.
Boundary Condition(s):
2 <= N <= 100
1 <= Each integer value, K <= 10^8
Input Format:
The first line contains N.
The second line contains N integers separated by a space.
The third line contains K.
Output Format:
The first line contains the integer value(s) separated by a space.
Example Input/Output 1:
Input:
5
50 86 2 86 45
86
Output:
50 86 2 45
Explanation:
Here K = 86.
So the last occurrence of 86 is removed and the remaining integers are printed.
Example Input/Output 2:
Input:
4
55 23 45 32
22
Output:
55 23 45 32
-------------------solution-------------

N = int(input().strip())
arr = list(map(int, input().strip().split()))
K = int(input().strip())
if k in arr:
        last_index = len(arr) - 1 - arr[::-1].index(k)
        arr.pop(last_index)
print(*arr)

