The program must accept an integer N as the input. The program must print the prime factors of N in ascending order as the output.
Boundary Condition(s):
10 <= N <= 10^5
Input Format:
The first line contains N.
Output Format:
The first line contains the prime factors of N in ascending order.
Example Input/Output 1:
Input:
100
Output:
2 5
Explanation:
The factors of 100 are 1, 2, 4, 5, 10, 20, 25, 50 and 100.
The prime factors of 100 are 2 and 5.
So 2 and 5 are printed as the output.
Example Input/Output 2:
Input:
150
Output:
2 3 5

----------------------solution---------------------------


def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors

N = int(input())
factors = prime_factors(N)
print(*sorted(set(factors)))


