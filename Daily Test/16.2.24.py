The program must accept a string S containing only alphabets as the input. The program must remove the repeated alphabets in the string S and print the modified string as the output. Note: At least one unique alphabet is always present in the string S.

Boundary Condition(s): 1 <= Length of S <= 1000
Input Format:
The first line contains S.

Output Format: The first line contains the modified string S.

Example Input/Output 1:
Input: engine
Output: gi

Explanation:
Here the string is engine,
The alphabets e and n are repeated in the string engine, so they are removed from the string. Now the string becomes gi, so gi is printed as the output.

Example Input/Output 2:
Input:
fireFighter
Output:
fFght
--------------------------------solution-----------------------------

s=input()
for i in range(0,len(s)):
	if s.count(s[i])<2:
		print(s[i],end="")