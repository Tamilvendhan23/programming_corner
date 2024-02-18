The program must accept an integer N as the input. The program must print yes if the sum of the first and third digits is present in N. Else the program must print no as the output.

Boundary Condition(s): 100 <= N <= 10^8

Input Format:
The first line contains N.
Output Format: The first line contains yes or no.

Example Input/Output 1:
Input: 96817
Output: yes

Explanation:
The sum of the first and third digits in 968172 is 17.
The sum 17 is present in the integer 968172. Hence the output is yes

Example Input/Output 2:
Input: 747134
Output:
no 
-----------------------------------solutionn-------------------------

def check_sum_present(N):
    first_digit = int(str(N)[0])
    third_digit = int(str(N)[2])
    sum_digits = first_digit + third_digit
    return "yes" if str(sum_digits) in str(N) else "no"

N = int(input())
print(check_sum_present(N))
