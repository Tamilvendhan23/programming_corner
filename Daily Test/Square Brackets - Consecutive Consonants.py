
The program must accept a string S containing only alphabets as the input. The program must enclose the consecutive consonants in the string S within the square brackets (possibly 1 consonant). Then the program must print the modified string S as the output. If there is no consonant in the string S, the program must print the same string as it is.

Boundary Condition(s):
1 <= Length of S <= 1000

Input Format:
The first line contains S.

Output Format:
The first line contains the modified string S.

Example Input/Output 1:
Input:
skillrack

Output:
[sk]i[llr]a[ck]

Explanation:
The consecutive consonants in the string skillrack are sk, llr and ck.
So they are enclosed within the square brackets.
Hence the output is [sk]i[llr]a[ck]

Example Input/Output 2:
Input:
CardGames

Output:
[C]a[rdG]a[m]e[s]

Example Input/Output 3:
Input:
Aeiou

Output:
Aeiou

-------------------------solution-------------------------------

s=input().strip()
v='AEIOUaeiou';c=0
for i in range(len(s)):
    if s[i] not in v:
        c+=1
        if c==1:
            print("["+s[i],end="")
        else:
            print(s[i],end="")
        if i==len(s)-1:
            print("]",end="")
    else:
        if c>=1:
            print("]"+s[i],end="")
        else:
            print(s[i],end="")
        c=0
