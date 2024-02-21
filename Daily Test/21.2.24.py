'''The program must accept a string S and find the longest prefix, which when reversed is also the suffix. Then the program must remove this prefix and the reversed suffix from the string and print the remaining string value. If the remaining string is empty then print -1.
Boundary Condition(s):
2 <= Length of S <= 100

Input Format:
The first line contains S.
Output Format:
The first line contains the string as per the given condition or -1.

Example Input/Output 1:
Input:
abcdefgdcba
Output:
efg

Explanation:
The longest prefix is "abcd", which when reversed is also the suffix "dcba".
After removing the prefix "abcd" and the reversed suffix "dcba" from the string "abcdefgdcba", the string becomes "efg".
Hence the output is efg

Example Input/Output 2:
Input:
lkkl
Output:
-1
'''

---------------------------------solution--------------------------------

def result(string):
    length = len(string)
    for i in range(length // 2, 0, -1):
        prefix = string[:i]
        suffix = string[length - i:]
        if prefix == suffix[::-1]:
            return string[i:length - i]
    return -1
s = input().strip()
print(result(s))


