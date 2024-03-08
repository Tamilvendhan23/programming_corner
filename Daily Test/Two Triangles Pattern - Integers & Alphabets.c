The program must accept an odd integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section.
Boundary Condition(s):
3 <= N <= 999
Input Format:
The first line contains N.
Output Format:
The lines containing the desired pattern as shown in the Example Input/Output section.
Example Input/Output 1:
Input:
5
Output:
1 * * * * a
2 3 * * b c
4 5 6 d e f
7 8 * * g h
9 * * * * i
Example Input/Output 2:
Input:
7
Output:
1 * * * * * * a
2 3 * * * * b c
4 5 6 * * d e f
7 8 9 10 g h i j
11 12 13 * * k l m
14 15 * * * * n o
16 * * * * * * p
Example Input/Output 3:
Input:
11
Output:
1 * * * * * * * * * * a 
2 3 * * * * * * * * b c 
4 5 6 * * * * * * d e f 
7 8 9 10 * * * * g h i j 
11 12 13 14 15 * * k l m n o 
16 17 18 19 20 21 p q r s t u 
22 23 24 25 26 * * v w x y z 
27 28 29 30 * * * * a b c d 
31 32 33 * * * * * * e f g 
34 35 * * * * * * * * h i 
36 * * * * * * * * * * j
-----------------------solution---------------
#include<stdio.h>
#include<stdlib.h>

int main()
{
int n,m=0;
scanf("%d",&n);
char a = 'a';
for(int i=0;i<n;i++){
    if(i <= n/2){
    for(int j=0;j<=i;j++){
        printf("%d ",++m);
    }for(int j = 0;j<(n-1)-(2*i);j++){
        printf("* ");
    }
    for(int j = 0;j<=i;j++){
        printf("%c ",a++);
        if(a >'z'){
            a='a';
        }
    }}
    else{
        for(int j=0;j<(n)-i;j++){
            printf("%d ",++m);
            }
        for(int j =0;j<(i-(n/2))*2;j++){
            printf("* ");
        }
        for(int j =0;j<(n)-i;j++){
            printf("%c ",a++);
            if(a>'z')
                a='a';
        }
    }
    printf("\n");
}
}

