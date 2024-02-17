The program must accept N string values as the input. The program must print the length of the longest palindromic string among the N string values as the output.

Note:

Each string value contains only lower case alphabets.
- At least one palindromic string is always present in the given N string values.
Boundary Condition(s): 1 <= N <= 100
1 <= Length of each string <= 1000

Input Format:
The first line contains N. The next N lines, each containing a string value.
Output Format: The first line contains the length of the longest palindromic string among the N string values.

Example Input/Output 1:
Input:
5
abcdefg
eye
engine
madam
environment

Output: 5
Explanation:
Here, the palindromic string values are eye and madam is the longest palindromic string whose length is 5, so 5 is printed as the output.
madam.

Example Input/Output 2:
Input:
4
book
redder
rotor
WOW
Output:
6
--------------------------------------solution------------------------

def is_palindrome(s):
    return s == s[::-1]

N = int(input())
longest_palindrome_length = 0

for _ in range(N):
    string = input().strip()
    if is_palindrome(string):
        longest_palindrome_length = max(longest_palindrome_length, len(string))

print(longest_palindrome_length)
