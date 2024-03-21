The program must accept N integers in which all integers are repeated thrice except one integer X. The integer X has occurred only once in the given N integers. The program must find the integer X and print it as the output.
Boundary Condition(s):
4 <= N <= 100
1 <= Each integer value <= 1000
Input Format:
The first line contains N.
The second line contains N integers separated by a space.
Output Format:
The first line contains X.
Example Input/Output 1:
Input:
4
10 50 10 10
Output:
50
Explanation:
The integer 10 is repeated thrice.
The integer 50 has occurred once.
So 50 is printed as the output.
Example Input/Output 2:
Input:
7
7 2 4 4 4 2 2
Output:
7
------------------------solution--------------------
n = int(input())
m = list(map(int, input().split()))

for i in range(len(m)):
    if m.count(m[i]) == 1:
        print(m[i])
     

