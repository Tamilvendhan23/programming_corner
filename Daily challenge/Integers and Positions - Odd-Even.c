The program must accept N integers as the input. The program must print the odd integers which are present in the even positions and print the even integers which are present in the odd positions among the N integers. If there is no such integer, the program must print -1 as the output.
Boundary Condition(s):
1 <= N <= 100
-10^5 <= Each integer value <= 10^5
Input Format:
The first line contains N.
The second line contains N integers separated by a space.
Output Format:
The first line contains the integers or -1 as per the given condition.
Example Input/Output 1:
Input:
5
80 82 26 -27 25
Output:
80 26 -27
Explanation:
The integer 80 is even which is present in the odd position. So 80 is printed.
The integer 82 is even which is present in the even position. So 82 is NOT printed.
The integer 26 is even which is present in the odd position. So 26 is printed.
The integer -27 is odd which is present in the even position. So -27 is printed.
The integer 25 is odd which is present in the odd position. So 25 is NOT printed.
Example Input/Output 2:
Input:
4
1 2 3 8
Output:
-1
---------------------solution-----------------------
C 17-Mar-2024 02:52  KRISHNA CHOUDHARY H (458744) 0 0 867
#include<stdio.h>
#include<stdlib.h>

int main()
{
int a;
scanf("%d",&a);
int l[a];
int f=0;
for(int i=0;i<a;i++){
    scanf("%d",&l[i]);
}
for(int i=0;i<a;i++){
    if(i%2==0 && l[i]%2==0){
        printf("%d ",l[i]);
        f=1;
    }
    if(i%2!=0 && l[i]%2!=0){
        printf("%d ",l[i]);
        f=1;
    }
}
if(f==0){
    printf("-1");
}
}
C 17-Mar-2024 02:54  VENKADESH K (402932) 0 0 891
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int n;
    scanf("%d ",&n);
    int a[n];
    int k=0;
    for(int i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    for(int i=0;i<n;i++)
    {
        if(abs(a[i])%2==0 && i%2==0)
        {
            printf("%d ",a[i]);
            k=1;
        }
        if(abs(a[i])%2==1 && i%2==1)
        {
            k=1;
            printf("%d ",a[i]);
        }
    }
    if(k==0)
    {
        printf("-1");
    }
}
C 17-Mar-2024 02:55  JONES MARTIN A (458760) 0 0 510
#include<stdio.h>
#include<stdlib.h>

int main()
{
int a;
scanf("%d",&a);
int f=0;
int l[a];
for(int i=0;i<a;i++){
    scanf("%d",&l[i]);
}
for(int i=0;i<a;i++){
    if(i%2==0 && l[i]%2==0){
        printf("%d ",l[i]);
        f=1;
    }
    if(i%2!=0 && l[i]%2!=0){
        printf("%d ",l[i]);
        f=1;
    }
}
if(f==0){
    printf("-1");
}
}
  
