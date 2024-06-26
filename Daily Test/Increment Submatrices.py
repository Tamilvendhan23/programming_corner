The program must accept the size of an integer matrix RxC and Q queries as the input. Each query contains four integers representing the positions of the top-left and the bottom-right cell of a submatrix. The program must form an integer matrix of size RxC with 0's. For each query, the program must increment the values of the integers in the submatrix specified by the query. Finally, the program must print the modified matrix as the output.
Boundary Condition(s):
2 <= R, C <= 50
1 <= Q <= 100
Input Format:
The first line contains R and C separated by a space.
The second line contains Q.
The next Q lines, each containing four integers separated by a space.
Output Format:
The first R lines, each containing C integers separated by a space.
Example Input/Output 1:
Input:
4 4
2
1 1 3 2
2 2 3 3
Output:
1 1 0 0
1 2 1 0
1 2 1 0
0 0 0 0
Explanation:
Initially, the value of each cell in the 4x4 matrix is 0.
After incrementing the values in the first submatrix, the matrix becomes
1 1 0 0
1 1 0 0
1 1 0 0
0 0 0 0
After incrementing the values in the second submatrix, the matrix becomes
1 1 0 0
1 2 1 0
1 2 1 0
0 0 0 0
Example Input/Output 2:
Input:
5 6
3
2 1 4 4
2 1 4 4
3 3 5 5
Output:
0 0 0 0 0 0
2 2 2 2 0 0
2 2 3 3 1 0
2 2 3 3 1 0
0 0 1 1 1 0
-----------------------------------solution--------------------
#Your code below
r,c=map(int,input().split())
n=int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
m=[[0 for i in range(c)] for j in range(r)]
for u in l:
    for i in range(u[0]-1,u[2]):
        for j in range(u[1]-1,u[3]):
            m[i][j]+=1
for i in m:
    print(*i)
