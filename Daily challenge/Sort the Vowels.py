The program must accept a string S as the input. The program must arrange the vowels in the string S in sorted order. Finally, the program must print the modified string S as the output.

Boundary Condition(s):
3 <= Length of S <= 100

Input Format:
The first line contains S.

Output Format:
The first line contains the modified string S.

Example Input/Output 1:
Input:
skillrack

Output:
skallrick

Explanation:
After arranging the vowels in the string skillrack in sorted order, the string becomes skallrick.
Hence the output is skallrick

Example Input/Output 2:
Input:
PROGRAMMING

Output:
PRAGRIMMONG

  =====================================solution=================================
  def sort_vowels(S):
    vowels = "aeiouAEIOU"
    sorted_vowels = sorted([char for char in S if char in vowels])
    result = ""
    index = 0
    for char in S:
        if char in vowels:
            result += sorted_vowels[index]
            index += 1
        else:
            result += char
    return result

# Reading input
S = input().strip()

# Sorting vowels and printing the modified string
print(sort_vowels(S))

