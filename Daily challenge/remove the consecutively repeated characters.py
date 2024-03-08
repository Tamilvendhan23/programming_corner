The program must accept a string S as the input. The program must remove the consecutively repeated characters in the string S. Then the program must print the modified string S as the output.
Note: At least one consecutively non-repeated character is always present in the string S.
Boundary Condition(s):
3 <= Length of S <= 1000
Input Format:
The first line contains S.
Output Format:
The first line contains the modified string S.
Example Input/Output 1:
Input:
bookkeeping
Output:
bping
Explanation:
The consecutively repeated characters in the string bookkeeping are o, k and e.
After removing the characters o, k and e from the string, the string becomes bping.
Hence the output is bping 
Example Input/Output 2:
Input:
#5#C5C#5
Output:
#5#C5C#5
-------------------------solution---------------

Your code below
a=input()
if a[0]!=a[1]:
    print(a[0],end="")
for i in range(1,len(a)-1):
    if a[i]==a[i-1] or a[i]==a[i+1]:
        continue
    else:
        print(a[i],end="")
if a[-1]!=a[-2]:
    print(a[-1])
