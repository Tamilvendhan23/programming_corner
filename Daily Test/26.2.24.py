The program must accept an integer N as the input. The program must print the sum of prime integers from 1 to N ending with 7 as the output.

Boundary Condition(s): 10 <= N <= 10^8

Input Format:

The first line contains N.

Output Format: The first line contains the sum of prime integers from 1 to N ending with 7.

Example Input/Output 1:

Input: 42

Output: 61

Explanation:

The prime integers from 1 to 42 which ends with 7 are 7, 17 and 37.

The sum of 7, 17 and 37 is 61. Hence the output is 61

Example Input/Output 2:

Input: 156

Output: 643
------------------------------------solution-----------------------------

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def sum_of_primes_ending_with_7(N):
    prime_sum = 0
    for i in range(7, N+1):
        if is_prime(i) and str(i)[-1] == '7':
            prime_sum += i
    return prime_sum

N = int(input())
print(sum_of_primes_ending_with_7(N))
