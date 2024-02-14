You must implement the function getSecondLargestDigit (int N) which accepts an integer N as the input. The function must return the second largest digit in N. If there is no such digit in N, the function must return -1.
Boundary Condition(s): 10 <= N <= 10 ^ n * 8

Example Input/Output 1:

Input: 24324

Output: Second Largest Digit: 3

Explanation: The 2 ^ (nd) largest digit in 24324 is 3.

Example Input/Output 2:

Input: 22

Output: Second Largest Digit: -1

---------------------------------------solution------------------------------------

def result(N):
    digits = [int(digit) for digit in str(N) if digit.isdigit()]
    unique_digits = sorted(set(digits), reverse=True)
    
    if len(unique_digits) < 2:
        return -1
    else:
        return unique_digits[1]

# Input from user
N = int(input())
print("Second Largest Digit:", result(N))

