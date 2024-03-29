"The program must accept a string S containing multiple words as the input. The program must print yes if the last character of each word is equal to the first character of its previous word. Else the program must print no as the output.
Note: The alphabets in the string S is always case insensitive.

Boundary Condition(s):
5 <= Length of S <= 1000

Input Format:
The first line contains S.

Output Format:
The first line contains yes or no.

Example Input/Output 1:
Input:
Apple Guava Fig

Output:
yes

Explanation:
In the given string Apple Guava Fig, the last character of each word is equal to the first character of its previous word.
So yes is printed.

Example Input/Output 2:
Input:
A thing begun is half done

Output:
no
------------------------------solution-----------------------------
#Your code below
s = input().strip().split()

for i in range(1,len(s)):
    if s[i][-1].lower() != s[i-1][0].lower():
        print("no")
        break
else:
    print("yes")
