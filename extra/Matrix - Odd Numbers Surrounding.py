A matrix of size R*C is passed as input. The surrounding elements of each element in the matrix are said to be the elements present immediately to the left, right, top or bottom of the element. The program must print only the elements which are surrounded by odd numbers.
Note: For element not having all four surrounding elements, consider only the available elements surrounding it.
Boundary Condition(s):
1 <= R, C <= 100
Input Format:
The first line contains R and C separated by space(s).
The next R lines contain C elements each separated by space(s).
Output Format:
The first line contains integers which are surrounded by odd numbers separated by a space.
Example Input/Output 1:
Input:
3 3
1 7 3
4 5 9
7 8 9
Output:
7 3 4 9 8
Example Input/Output 2:
Input:
4 3
12 38 38 
43 40 65 
74 47 18 
65 10 59
Output:
74 18 10


solution
---------------------------------------------------------------------------------
def is_odd(n):
    return n % 2 != 0

def surrounded_by_odd(matrix, i, j):
    rows, cols = len(matrix), len(matrix[0])
    surroundings = [
        (i-1, j), (i+1, j), (i, j-1), (i, j+1)
    ]
    for x, y in surroundings:
        if 0 <= x < rows and 0 <= y < cols and not is_odd(matrix[x][y]):
            return False
    return True

def print_odd_surrounded_elements(matrix):
    odd_surrounded_elements = []
    rows, cols = len(matrix), len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if surrounded_by_odd(matrix, i, j):
                odd_surrounded_elements.append(matrix[i][j])
    print(' '.join(map(str, odd_surrounded_elements)))

# Input
R, C = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(R)]

# Output
print_odd_surrounded_elements(matrix)
