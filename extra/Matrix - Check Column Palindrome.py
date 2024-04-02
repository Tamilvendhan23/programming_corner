A matrix of size N*N is passed as input containing integers. The program must print yes if there is at least one column in the matrix which is a palindrome. Else the program must print no.
Boundary Condition(s):
1 <= N <= 100
Input Format:
The first line contains N.
The next N lines contain N elements each separated by space(s).
Output Format:
The first line contains yes or no
Example Input/Output 1:
Input:
3
45 23 67
98 13 67
67 25 84
Output:
no
Example Input/Output 2:
Input:
4
34 56 14 93
76 93 76 20
86 93 16 30
34 56 14 93
Output:
yes

solution


def is_palindrome(column):
    return column == column[::-1]

# Input
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

# Checking for palindrome column
found_palindrome = False
for j in range(N):
    column = [matrix[i][j] for i in range(N)]
    if is_palindrome(column):
        found_palindrome = True
        break

# Output
if found_palindrome:
    print('yes')
else:
    print('no')
