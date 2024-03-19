The program must accept an integer array of size N and Q queries as the input. Each query contains two integers representing the starting position S and the ending position E of a sub-array. For each query, the program must print the minimum integer in the subarray specified by the query as the output.
Boundary Condition(s):
1 <= N <= 100
1 <= Q <= 1000
1 <= S <= E <= N
Input Format:
The first line contains N and Q separated by a space.
The second line contains N integers separated by a space.
The next Q lines, each containing two integers (S and E) separated by a space.
Output Format:
The first Q lines, each containing the minimum integer in the sub-array specified by the query.
Example Input/Output 1:
Input:
6 3
9 5 3 4 6 2
1 3
2 6
3 5
Output:
3
2
3
Explanation:
Here N=6 and Q=3,
1st query: The integers in the sub-array are 9, 5 and 3. Here the minimum integer is 3, so 3 is printed.
2nd query: The integers in the sub-array are 5, 3, 4, 6 and 2. Here the minimum integer is 2, so 2 is printed.
3rd query: The integers in the sub-array are 3, 4 and 6. Here the minimum integer is 3, so 3 is printed.
Example Input/Output 2:
Input:
9 3
94 22 25 79 70 52 11 12 73
1 9
3 7
6 6
Output:
11
11
52
----------------------solution-------------------

N, Q = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(Q):
    S, E = map(int, input().split())
    print(min(arr[S-1:E]))
