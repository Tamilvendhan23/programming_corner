The program must accept an integer matrix of size RxC as the input. If any cell is 0 in the matrix, the program must replace the entire row and column of the cell with zero. Finally, the program must print the modified matrix as the output.

Boundary Conditon(s):
2 <= R, C <= 50
0 <= Each integer value <= 1000

Input Format:
The first line contains R and C separated by a space.
The next R lines, each containing C integers separated by a space.

Output Format:
The first R lines, each containing C integers separated by a space.

Example Input/Output 1:
Input:
2 3
1 0 1
1 1 1

Output:
0 0 0
1 0 1

Explanation:
In the given 2x3 matrix, the 0 is present in the first row and second column.
So the entire first row and the entire second column are replaced with zero. Now, the matrix becomes
0 0 0
1 0 1

Example Input/Output 2:
Input:
3 4
3 8 3 8
0 5 7 8
6 0 4 8

Output:
0 0 3 8
0 0 0 0
0 0 0 0


____________________________solution________________________

def replace_zero(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    zero_rows = set()
    zero_cols = set()

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    for i in range(rows):
        for j in range(cols):
            if i in zero_rows or j in zero_cols:
                matrix[i][j] = 0

    return matrix

# Input
R, C = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(R)]

# Output
modified_matrix = replace_zero(matrix)
for row in modified_matrix:
    print(*row)
