The program must accept an integer matrix of size NxN and an integer K as the input. The program must print yes if each KxK submatrix of the given matrix contains the same integer. Else the program must print no as the output.
Note: The integer N is always divisible by the integer K.
Boundary Condition(s):
2 <= K <= N <= 50
Input Format:
The first line contains N.
The next N lines, each containing N integers separated by a space.
The next (N+2)nd line contains K.
Output Format:
The first line contains yes or no.
Example Input/Output 1:
Input:
9
1 1 1 2 2 2 4 4 4
1 1 1 2 2 2 4 4 4
1 1 1 2 2 2 4 4 4
5 5 5 3 3 3 7 7 7
5 5 5 3 3 3 7 7 7
5 5 5 3 3 3 7 7 7
9 9 9 1 1 1 5 5 5
9 9 9 1 1 1 5 5 5
9 9 9 1 1 1 5 5 5
3
Output:
yes
Explanation:
In the 9x9 matrix, each 3x3 submatrix contains the same integer.
Hence the output is yes
Example Input/Output 2:
Input:
4
10 10 20 20
10 10 20 20
33 33 40 44
33 33 40 44
2
Output:
no
---------------------soluiton------------------------
x=int(input())
m=[]
f=0
for i in range(x):
    a=list(map(int,input().split()))
    m.append(a)
y=int(input())
for i in range(0,x,y):
    for j in range(0,x,y):
        n=m[i][j]
        for a in range(i,i+y):
            for b in range(j,j+y):
                if n!=m[a][b]:
                    f=1
                    break
print("yes" if f==0 else "no")
