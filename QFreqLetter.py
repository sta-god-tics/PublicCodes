def freq():
    data=str(input('Enter sentence: '))
    dtn=dict()
    for ch in data:
        if ch in dtn :
            dtn[ch]+=1
        else:
            dtn[ch]=1
    print(dtn)

print('#'*30+' Total Frequency of Letters '+'#'*30)
freq()