The program must accept an integer M as the input. The program must print the number of days in the month M if it is valid. Else the program must print Invalid as the output.
Note: The number of days in each month will be considered from a non-leap year.

Boundary Condition(s):
1 <= M <= 50

Input Format:
The first line contains M.

Output Format:
The first line contains the number of days in the month M or Invalid.

Example Input/Output 1:
Input:
5

Output:
31

Explanation:
In a non-leap year, there are 31 days in the 5th month.
So 31 is printed.

Example Input/Output 2:
Input:
2

Output:
28

Example Input/Output 3:
Input:
15
-----------------------Solution------------------
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int num;scanf("%d",&num);
    switch(num)
    {
        case 1:
        case 3:
        case 5:
        case 7:
        case 8:
        case 10:
        case 12:
        printf("31");break;
        case 2:
        printf("28");break;
        case 4:
        case 6:
        case 9:
        case 11:printf("30");break;
        default:printf("Invalid");
    }
}

