
The program must accept a string S containing multiple words as the input. The program must print the desired pattern as shown in the Example Input/Output section.
Boundary Condition(s):
3 <= Length of S <= 100
Input Format:
The first line contains S.
Output Format:
The first line contains the desired pattern as shown in the Example Input/Output section.
Example Input/Output 1:
Input:
he is a good boy
Output:
+--+--+-+----+---+
|he|is|a|good|boy|
+--+--+-+----+---+
Example Input/Output 2:
Input:
stay home stay safe
Output:
+----+----+----+----+
|stay|home|stay|safe|
+----+----+----+----+
  -------------------------------------------solution-------------------------------------------

a=list(input().split())
x="|"
y="+"
for i in a:
    x+=i+"|"
    p=len(i)
    c="-"*p
    y+=c+"+"
    
print(y)
print(x)
print(y)
