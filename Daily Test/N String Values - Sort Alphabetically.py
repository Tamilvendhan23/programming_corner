
The program must accept N string values as the input. The program must print the number of unique string values K among the N string values. Then the program must print the unique string values in sorted order along with the positions that they have occurred as the output.
Boundary Condition(s):
2 <= N <= 1000
1 <= Length of each string <= 100
Input Format:
The first line contains N.
The next N lines each contain a string value.
Output Format:
The first line contains the number of unique string values K.
The next K lines, each containing a string value and the positions that they have occurred in the N string values.
Example Input/Output 1:
Input:
7
abcd
eabs
abcd
eabs
abcd
some
abcd
Output:
3
abcd 1 3 5 7
eabs 2 4
some 6
Explanation:
Here the number of unique string values is 3 (abcd, eabs and some).
After sorting the string values in alphabetical order, the string values become abcd, eabs and some.
The string abcd has occurred in the positions 1, 3, 5 and 7.
The string eabs has occurred in the positions 2 and 4.
The string some has occurred in the position 6.
Hence the output is
3
abcd 1 3 5 7
eabs 2 4
some 6
Example Input/Output 2:
Input:
4
stu
abc
xyz
ijk
Output:
4
abc 2
ijk 4
stu 1
xyz 3

----------------solution--------------

n=int(input())
a=[input().strip() for i in range(n)]
l=sorted(set(a))
print(len(l))
for i in range(len(l)):
    print(l[i],end=" ")
    for j in range(n):
        if a[j]==l[i]:
            print(j+1,end=" ")
    print()
