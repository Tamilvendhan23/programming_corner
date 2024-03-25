The program must accept two integer arrays of size M and N as the input. The program must print the integers in the first array which are also present in the second array in the same order of occurrence as in the second array. Then the program must print the remaining integers in the first array in descending order as the output.
Note: The integers in the second array are always unique.
Boundary Condition(s):
2 <= M, N <= 100
1 <= Each integer value <= 10^5
Input Format:
The first line contains M and N separated by a space.
The second line contains M integers separated by a space.
The third line contains N integers separated by a space.
Output Format:
The first line contains M integers based on the give conditions.
Example Input/Output 1:
Input:
15 4
50 10 2 5 7 10 1 9 3 6 8 8 10 10 50
50 10 8 9
Output:
50 50 10 10 10 10 8 8 9 7 6 5 3 2 1
Explanation:
The integers in the first array, which are also present in the second array are 50 10 10 9 8 8 10 10 50. 
So the integers 50 10 10 9 8 8 10 10 50 are printed in the same order of occurrence as in the second array 50 50 10 10 10 10 8 8 9.
Then the remaining integers in the first array 2 5 7 1 3 6 are printed in descending order 7 6 5 3 2 1.
Example Input/Output 2:
Input:
7 8
3 8 7 10 5 2 7
8 3 5 11 17 14 23 16
Output:
8 3 5 10 7 7 2

----------------------------------------solution-------------------------------------------
 def main():
    # Accepting input
    m, n = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # Creating a dictionary to store the indices of elements in the second array
    idx = {}
    for i, x in enumerate(b):
        idx[x] = i

    common = []
    remaining = []

    # Loop through the first array
    for x in a:
        # If the element is present in the second array
        if x in idx:
            common.append((x, idx[x]))  # Store the element and its index
        else:
            remaining.append(x)  # Store the element if it's not common

    # Sorting the common elements based on their indices in the second array
    common.sort(key=lambda y: y[1])

    # Printing the common elements in the same order of occurrence as in the second array
    for x, _ in common:
        print(x, end=' ')

    # Printing the remaining elements in descending order
    remaining.sort(reverse=True)
    for x in remaining:
        print(x, end=' ')


if __name__ == "__main__":
    main()
 
