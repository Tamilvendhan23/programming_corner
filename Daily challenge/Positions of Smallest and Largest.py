The program must accept N distinct integers as the input. The program must print the positions of the smallest and the largest integer among the N integers as the output.
Boundary Condition(s):
2 <= N <= 100
1 <= Each integer value <= 1000
Input Format:
The first line contains N.
The second line contains N integers separated by a space.
Output Format:
The first line contains the positions of the smallest and the largest integer among the N integers.
Example Input/Output 1:
Input:
10
40 18 5 89 9 74 69 59 27 93
Output:
3 10
Explanation:
The smallest integer among the 10 integers is 5. The integer 5 is present in the 3rd position.
The largest integer among the 10 integers is 93. The integer 93 is present in the 10th position.
So 3 and 10 are printed.
Example Input/Output 2:
Input:
6
82 11 23 61 27 73
Output:
2 1
----------------------------solution---------------
  n=int(input())
  m=list(map(int,input().split()))
   s=min(m)
    l=max(m)
     ss=[]
       ll=[]
       for i in range(n):
            if s==m[i]:
                ss.append(i+1)
            if l==m[i]:
               ll.append(i+1)
  print(*(ss),end=' ')
       print(*(ll))
