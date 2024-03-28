The program must accept an integer N as the input. The program must print the number of ways to represent N as the sum of two prime integers.
Boundary Condition(s):
2 <= N <= 10^4
Input Format:
The first line contains N.
Output Format:
The first line contains the number of ways to represent N as the sum of two prime integers.
Example Input/Output 1:
Input:
18
Output:
2
Explanation:
The 2 possible ways are given below.
5 + 13 = 18
7 + 11 = 18
Example Input/Output 2:
Input:
100
Output:
6
------------------------solution-----------------------------
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def count_prime_pairs(N):
    count = 0
    for i in range(2, N // 2 + 1):
        if is_prime(i) and is_prime(N - i):
            count += 1
    return count

# Input
N = int(input())

# Output
print(count_prime_pairs(N))
