The program must accept two integers M and N as the input. The program must print the position of the second 1 in the binary representation of the sum of M and N as the output. If there is no second 1 then the program must print 0 as the output.
Boundary Condition(s):
1 <= M, N <= 10^8
Input Format:
The first line contains M and N separated by a space.
Output Format:
The first line contains an integer value as per the given condition.
Example Input/Output 1:
Input:
13 5
Output:
4
Explanation:
Here M=13 and N=5.
The binary representation of 18 (13+5) is 10010.
The position of the second 1 in 10010 is 4, so 4 is printed as the output.
Example Input/Output 2:
Input:
20 12
Output:
0
      -----------------------solution----------------------
def second_one_position(M, N):
    # Calculate the sum of M and N
    total = M + N
    
    # Convert the sum to its binary representation
    binary_rep = bin(total)[2:]
    
    # Count the number of 1s in the binary representation
    count_ones = binary_rep.count('1')
    
    # If there are less than 2 ones, return 0
    if count_ones < 2:
        return 0
    
    # Otherwise, find the position of the second 1
    second_one_index = binary_rep.find('1', binary_rep.find('1') + 1)
    
    # Return the position (index + 1)
    return second_one_index + 1

# Input
M, N = map(int, input().split())

# Output
print(second_one_position(M, N))
