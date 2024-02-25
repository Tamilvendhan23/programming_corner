The program must accept two string values S1 and S2 containing only alphabets as the input. 
The program must print yes if all the upper case alphabets (A to Z) present only once in two string 
values. Else the program must print no as the output. 
Boundary Condition(s): 1 <= Length of S1, S2 <= 100 
Input Format: The first line contains S1. The second line contains S2.
Output Format: The first line contains yes or no. 
Example Input/Output 1:
Input:
ABCDEFGHIJKLMNO 
PQRSTUVWXYZ 
Output: yes
Explanation: Here all the upper case alphabets (A to Z) occur only once in two string values.
So yes is printed.
Example Input/Output 2:
Input: FEDCBA 
GHIJKLMNOPQRSTUVWXYZ 
Output: yes 
Example Input/Output 3:
Input: CBADEFGHIjkl
MNOPQRSTuvwXYZ 
Output: no
-------------------------------------solution-------------------
s1=input().strip()
s2=input().strip()
leng=len(s1)+len(s2)
if (s1.isupper() and s2.isupper() and leng==24):
    print("yes")
else:
    print("no")

