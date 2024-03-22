The program must accept an integer array of size N as the input. The program must print the length of the longest increasing sequence in the given array as the output.
Boundary Condition(s):
1 <= N <= 100
1 <= Each integer value <= 10^5
Input Format:
The first line contains N.
The second line contains N integers separated by a space.
Output Format:
The first line contains the length of the longest increasing sequence in the given array.
Example Input/Output 1:
Input:
8
12 79 6 7 10 24 21 68
Output:
5
Explanation:
Here the longest increasing sequences are given below.
6 7 10 24 68
6 7 10 21 68
The length of the longest increasing sequence is 5, so 5 is printed as the output.
Example Input/Output 2:
Input:
5
58 50 50 41 24
Output:
1

-------------------------------------solution---------
def res(arr):
    n = len(arr)
    lis = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    return max(lis)

# Read input
n = int(input())
arr = list(map(int, input().split()))
print(res(arr))
