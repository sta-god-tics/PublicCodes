#initiaL AREA
area=0

#area of floors
def floor():
    global area
    k=int(input('Enter no. of floors: '))
    l=float(input('Enter the length of 1 floor: '))
    b=float(input('Enter the breadth of 1 floor: '))
    h=float(input('Enter the height of 1 floor: '))
    area=k*(2*(b*h+h*l))

 #area of doors
def door():
    global area
    k=int(input('Enter no. of doors: '))
    b=float(input('Enter the breadth of 1 door: '))
    h=float(input('Enter the height of 1 door: '))
    area-=(k*b*h)

#area of windows
def wind():
    global area
    k=int(input('Enter no. of Windows: '))
    b=float(input('Enter the breadth of 1 window: '))
    h=float(input('Enter the height of 1 window: '))
    area-=(k*b*h)

#area of vents
def vent():
    global area
    k=int(input('Enter no. of Vents: '))
    b=float(input('Enter the breadth of 1 vent: '))
    h=float(input('Enter the height of 1 vent: '))
    area-=(k*b*h)

print('#'*30+' Calculate the area of a building '+'#'*30)
print('Please enter all measurements in Meter')

floor()
print('OK')

ans=str(input('Do building have Doors (Y/N): '))
if ans=='y' or ans=='Y' :
    door()
    print('OK')
else:
    print('OK')

ans=str(input('Do building have Windows (Y/N): '))
if ans=='y' or ans=='Y' :
    wind()
    print('OK')
else:
    print('OK')

ans=str(input('Do building have Air Vents (Y/N): '))
if ans=='y' or ans=='Y' :
    vent()
    print('OK')
else:
    print('OK')

print('Area of the building of mentioned specification is',area,'sqr meter.')
print('#'*100)
