def fibbo(n):
    f=0
    s=1
    if n<=0:
        print('Number of Terms cannot be 0 or less than 0')
    elif n==1:
        print('Fibonacci Series : 0')
    elif n==2:
        print('Fibonacci Series : 0 1')
    else:
        print('Fibonacci Series : 0 1 ',end='')
        for i in range(3,n+1):           #first two terms 0,1 are pre defined
            t=f+s
            print(t,end=' ')
            f,s=s,t
print('#'*30+' Fint the Fibonacci series '+'#'*30)
n=int(input('Enter the Number of terms:  '))
fibbo(n)