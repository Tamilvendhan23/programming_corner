The program must accept an integer N as the input. A seven segment LED is used to display a single digit. The program must print the total number of segments to be turned ON to display the integer N as the output.

Boundary Condition(s): 1 <= N <= 10^8
Input Format: The first line contains N.
Output Format: The first line contains the total number of segments to be turned ON to display the integer N.

Example Input/Output 1:
Input: 31
Output: 7

Explanation:
To display the digit 3, 5 segments need to turn ON.
To display the digit 1, 2 segments need to turn ON.
The total number of segments to be turned ON to display the integer 31 is 7 (5+2). Hence the output is 7

Example Input/Output 2:
Input: 88
Output: 14


-------------------------solution-------------------------
def segments_required(digit):
    segments = {'0': 6, '1': 2, '2': 5, '3': 5, '4': 4, '5': 5, '6': 6, '7': 3, '8': 7, '9': 6}
    return segments[digit]

def total_segments(n):
    total = 0
    for digit in str(n):
        total += segments_required(digit)
    return total

N = int(input())
print(total_segments(N))
