The program must accept two integer arrays of size M and N as the input. The program must print the distinct integers in the two arrays in sorted order as the output.
Boundary Condition(s):
2 <= M, N <= 100
1 <= Each integer value <= 1000
Input Format:
The first line contains M and N separated by a space.
The second line contains M integers separated by a space.
The third line contains N integers separated by a space.
Output Format:
The first line contains the distinct integers in the two arrays in sorted order.
Example Input/Output 1:
Input:
10 5
50 40 60 20 20 50 10 50 60 40
45 45 45 50 60
Output:
10 20 40 45 50 60
Explanation:
The distinct integers are 50 40 60 20 10 45.
After sorting the distinct integers, the integers become 10 20 40 45 50 60.
Hence the output is 10 20 40 45 50 60
Example Input/Output 2:
Input:
4 5
2 2 1 1
5 6 7 3 4
Output:
1 2 3 4 5 6 7
  -------------------------------solution--------------------------------
m,n=map(int(input().split()))
f=list(map(int,input().split()))
l=list(map(int,input().split()))
a=f+l
s=list(set(a))
 s.sort(s)
 print(s)
