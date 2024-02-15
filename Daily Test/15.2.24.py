N players are standing in a line and their country names are passed as the input. If any two adjacent players belong to the same country they are removed from the line. The program must print the final count C of the players who are standing in the line.

Boundary Condition(s): 1 <= N <= 50 4 <= Length of each country name <= 50

Input Format:
The first line contains N. The second line contains N country names separated by a space.

Output Format:
The first line contains C.

Example Input/Output 1:

Input: 5 India Australia India India Australia

Output: 1

Explanation:
The line contains India Australia India India Australia.
There are 2 players from India standing nearby. So they are removed from the line. Now, the line contains India Australia Australia. Again, there are 2 players from Australia standing nearby.So they are removed from the line. Now, the line contains India. Finally, only one player will remain in the line. Hence the output is 1

Example Input/Output 2:

Input:

7 
Bangladesh Germany Malaysia Germany Banglades

Output:

7


-------------------------------------------solution------------------------------
n=int(input())
con=list(map(int,input.split()))
a=[]
for i in con:
    if not a or a[-1]!=i:
	a.append(i)
    else:
	a.pop()
print(len(a))