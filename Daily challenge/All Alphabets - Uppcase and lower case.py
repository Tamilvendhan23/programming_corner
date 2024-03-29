The program must accept two string values S1 and S2 containing only alphabets as the input. The program must print yes if all the 26 alphabets (case insensitive) are present across the string values S1 and S2. Else the program must print no as the output.
Boundary Condition(s):
1 <= Length of S1, S2 <= 100
Input Format:
The first line contains S1.
The second line contains S2.
Output Format:
The first line contains yes or no.
Example Input/Output 1:
Input:
abcdEFGHIJk
LMNOpqrstuvwwxxxYYYzzz
Output:
yes
Explanation:
All the 26 alphabets (case insensitive) are present across the string values S1 and S2.
So yes is printed.
Example Input/Output 2:
Input:
zzzxyyWvvUUUTTSr
qponmllkjihgfedcba
Output:
yes
Example Input/Output 3:
Input:
ABCDEF
jklmnopqrst
Output:
no
--------------------------solution--------------------------
# Accepting input
s1 = input().strip()
s2 = input().strip()

# Create a set to store the alphabets present
alphabet_set = set()

# Convert both strings to lowercase for case insensitivity
s1 = s1.lower()
s2 = s2.lower()

# Add all characters from both strings to the set
for char in s1:
    if char.isalpha():
        alphabet_set.add(char)

for char in s2:
    if char.isalpha():
        alphabet_set.add(char)

# Check if the set contains all 26 alphabets
if len(alphabet_set) == 26:
    print("yes")
else:
    print("no")
