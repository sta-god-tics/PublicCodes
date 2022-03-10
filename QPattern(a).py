def pattern(n):
    for j in range(1,n+1):                         #for rows
        for i in range(j,0,-1):                    #for columns
            print(i,end='')
        print()                                    #next line
print('#'*30+' Program to print definite Pattern '+'#'*30)
n=int(input('Enter the no. of rows to be printed:  '))
pattern(n)