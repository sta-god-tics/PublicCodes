def chyr(n):
    if n%400==0 :
        print(n,'is a Leap Year')
    elif n%100==0 :
        print(n,'is not a Leap Year')
    elif n%4==0 :
        print(n,'is a Leap Year')
    else:
        print(n,'is not a Leap Year')
print('#'*30+' Check Leap Year '+'#'*30)
n=int(input('Enter Year:  '))
chyr(n)