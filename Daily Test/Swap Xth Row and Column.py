The program must accept an integer matrix of size NxN and an integer X as the input. The program must swap the integers in the Xth row and the Xth column in the matrix. Then the program must print the modified matrix as the output.
Boundary Condition(s):
2 <= N <= 50
1 <= X <= N
Input Format:
The first line contains N.
The next N lines, each containing N integers separated by a space.
The (N+2)nd line contains X.
Output Format:
The first N lines, each containing N integers of the modified matrix.
Example Input/Output 1:
Input:
4
1 3 0 7
2 4 6 8
9 1 7 5
7 0 0 6
2
Output:
1 2 0 7 
3 4 1 0 
9 6 7 5 
7 8 0 6 
Explanation:
In the given 4x4 matrix, the integers in the 2nd row and the 2nd column are highlighted below.
1 3 0 7
2 4 6 8
9 1 7 5
7 0 0 6
After swapping the 2nd row and the 2nd column of the matrix, the matrix becomes
1 2 0 7 
3 4 1 0 
9 6 7 5 
7 8 0 6
Example Input/Output 2:
Input:
5
82 62 15 12 57
21 65 21 63 11
38 56 58 53 67
18 59 53 25 35
74 30 34 74 33
5
Output:
82 62 15 12 74 
21 65 21 63 30 
38 56 58 53 34 
18 59 53 25 74 
57 11 67 35 33

-------------------solution--------------------------------
def swap(matrix, X):

    for i in range(len(matrix)):
        matrix[i][X-1], matrix[X-1][i] = matrix[X-1][i], matrix[i][X-1]

    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    X = int(input())

    swap(matrix, X)

    for row in matrix:
        print(*row)

