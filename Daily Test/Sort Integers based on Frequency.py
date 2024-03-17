
The program must accept N integers as the input. The program must sort the integers based on the frequency (i.e., the number of occurrences). If more than one integers have the same frequency, then the program must sort those integers in ascending order. Finally, the program must print the sorted integers as the output.
Boundary Condition(s):
2 <= N <= 100
1 <= Each integer value <= 10^8
Input Format:
The first line contains N.
The second line contains N integers separated by a space.
Output Format:
The first line contains N integers representing the sorted integers.
Example Input/Output 1:
Input:
6
10 20 30 20 10 10
Output:
30 20 20 10 10 10
Explanation:
After sorting the 6 integers based on the frequency, the integers become 30, 20, 20, 10, 10 and 10.
Hence the output is 30 20 20 10 10 10
Example Input/Output 2:
Input:
9
880 91 880 91 91 1887 134 1887 880
Output:
134 1887 1887 91 91 91 880 880 880

---------------------------solution------------------------------
from collections import Counter 
def ntr(a):
    f=Counter(a)
    return sorted(a,key=lambda x:(f[x],x))
n=int(input())
l=list(map(int,input().split()))
l=ntr(l);print(*l)
