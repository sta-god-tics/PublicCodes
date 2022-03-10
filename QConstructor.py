from mimetypes import init

class rectangle():
    
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        a=self.length*self.breadth
        print(a)
    def perimeter(self):
        p=2*(self.length+self.breadth)
        print(p)

r=rectangle(4,2)
r.area()
r.perimeter()