Please fill in the lines of code to implement the logic present in the flowchart.

** flow chart diagram has been given as a question ***
-------- solution----------
a=input().strip()
n=len(a);i=0
while i<n:
    if a[i]>='a':
        if a[i]<='j':
            print(a[i],end="")
        else:
            print("*",end="")
    else:
        print("*",end="")
    i+=1
