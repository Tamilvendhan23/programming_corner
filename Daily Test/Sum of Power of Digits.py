  
The program must accept an integer N as the input. 
The program must print the sum of each digit raised to the power of the number of digits in N as the output. 

Boundary Condition(s): 1 <= N <= 10^8 

Input Format: The first line contains N.
Output Format: The first line contains the sum of each digit raised to the power of the number of digits in N.  
Example Input/Output 1:
Input: 2356 
Output: 2018
Explanation: The number of digits in 2356 is 4. (24 + 34 + 54 + 64) = (16 + 81 + 625 + 1296) = 2018
Hence the output is 2018

Example Input/Output 2: 
Input: 78100 
Output: 49576

======================solution=================

def res(N):
    num_digits = len(str(N))
    sum_of_powers = sum(int(digit) ** num_digits for digit in str(N))
    return sum_of_powers


N = int(input().strip())
print(res(N))
