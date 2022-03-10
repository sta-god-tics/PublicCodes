def check_duplicates(lst1):
    dupl={}
    flag=0
    for i in lst1 :
        if i not in dupl :
             dupl[i]=1
        else:
            dupl[i]+=1
            flag=1
    if flag==1 :
        for i in dupl :
            if dupl[i]>1 :
                print(i,'occurs',dupl[i],'times')
        return True

print('#'*30+' Checking Duplicate items in a List '+'#'*30)
l=list(map(str, input('Enter elements of the list separated by comma:  ').split(',')))
print(check_duplicates(l))