The program must accept an integer N as the input. The program must print the binary representation of the integers from 1 to N as the output.

Boundary Condition(s):
1 <= N <= 100

Input Format:
The first line contains N.

Output Format:
The first line contains the binary representation of the integers from 1 to N.

Example Input/Output 1:
Input:
8

Output:
1 10 11 100 101 110 111 1000

Explanation:
The binary representation of the integers from 1 to 8 are 1, 10, 11, 100, 101, 110, 111 and 1000.

Example Input/Output 2:
Input:
17

Output:
1 10 11 100 101 110 111 1000 1001 1010 1011 1100 1101 1110 1111 10000 10001





-------------------------solution-----------------------------
n=int(input())
for i in range(1,n+1):
    print(bin(i)[2:],end=' ')
