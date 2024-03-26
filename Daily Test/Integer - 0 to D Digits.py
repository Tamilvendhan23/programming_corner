The program must accept an integer N and a digit D as the input. The program must print yes if N has all the digits from 0 to D. Else the program must print no as the output.
Boundary Condition(s):
10 <= N <= 10^17
1 <= D <= 9
Input Format:
The first line contains N and D separated by a space.
Output Format:
The first line contains yes or no.
Example Input/Output 1:
Input:
102435 4
Output:
yes
Explanation:
Here N = 102435 and D = 4.
The integer 102435 contains all the digits from 0 to 4. So yes is printed as the output.
Example Input/Output 2:
Input:
21342 3
Output:
no
--------------------solution-------------------
def has_all_digits(number, digit):
    for i in range(int(digit) + 1):
        if str(i) not in number:
            return False
    return True

# Accepting input
N, D = input().split()

# Checking if N has all digits from 0 to D
result = "yes" if has_all_digits(N, D) else "no"

# Printing the result
print(result)
