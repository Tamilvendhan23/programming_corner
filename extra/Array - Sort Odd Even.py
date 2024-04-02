Given an array of N integers, the program must sort the integers present in the odd positions if N is odd. Else if N is even the program must sort the integers present in the even positions. The sorting must be in ascending order.
Boundary Condition(s):
1 <= N <= 99999
Input Format:
The first line contains N.
The second line contains N integers separated by space.
Output Format:
The first line contains N integers separated by space.
Example Input/Output 1:
Input:
7
12 45 14 21 57 12 9
Output:
9 45 12 21 14 12 57
Example Input/Output 2:
Input:
10
78 121 34 56 12 34 89 18 33 90
Output:
78 18 34 34 12 56 89 90 33 121

solution
----------------------------------------------------------------------
def sort_odd_even_positions(array):
    if len(array) % 2 == 0:
        positions = [array[i] for i in range(len(array)) if i % 2 == 1]
    else:
        positions = [array[i] for i in range(len(array)) if i % 2 == 0]
    positions.sort()
    if len(array) % 2 == 0:
        for i in range(len(array)):
            if i % 2 == 1:
                array[i] = positions.pop(0)
    else:
        for i in range(len(array)):
            if i % 2 == 0:
                array[i] = positions.pop(0)
    return array

# Input
N = int(input())
array = list(map(int, input().split()))

# Sorting odd/even positions depending on N
sorted_array = sort_odd_even_positions(array)

# Output
print(*sorted_array)
