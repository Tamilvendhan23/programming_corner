The program must an integer N as the input. The program must print the count C of pairs of positive integers X and Y so that the sum of X and Y is equal to N.
Boundary Condition(s):
2 <= N <= 10^8
Input Format:
The first line contains N.
Output Format:
The first line contains C.
Example Input/Output 1:
Input:
6
Output:
5
Explanation:
All possible pairs of integers whose sum is equal to 6 are (1, 5), (2, 4), (3, 3), (4, 2) and (5, 1).
Here the count of pairs of integers is 5, so 5 is printed as the output.
Example Input/Output 2:
Input:
11
Output:
10
---------------------------solution--------------------------
n=int(input())
print(n-1)
