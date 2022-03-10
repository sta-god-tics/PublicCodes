import math as mt
x=0
print('#'*30+' Table for Sine, Cosine and Tangent Values '+'#'*30)
print('Value\t\tSine\t\tCosine\t\tTangent')
while x<=10 :
    print('{}\t\t{}\t\t{}\t\t{}'.format(round(x,2),round(mt.sin(x),4),round(mt.cos(x),4),round(mt.tan(x),4)))
    x+=0.2