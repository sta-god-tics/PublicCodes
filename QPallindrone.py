def palindrome():
    data=str(input('Enter string: '))
    datapal=''
    for i in range(len(data)-1,-1,-1):
        datapal+=data[i]
    if datapal==data :
        print(data,'is palindrome.')
    else:
        print(data,'is not palindrome.')

print('#'*30+' Test for Palindrome String '+'#'*30)
palindrome()