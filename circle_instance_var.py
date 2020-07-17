import math
class Circle:
    PI=math.pi #클래스 변수
    def __init__(self,name,radius,PI):
        self.name=name #인스턴스 변수
        self.radius=radius
        self.PI=PI
    def area(self):
        return self.PI*self.radius**2
    def __del__(self):
        pass
PI=Circle.PI #클래스 변수 가져오기
c1 = Circle('C1',7,PI)
c2 = Circle('C2',10,PI)

print('C1의 면적은 {}'.format(c1.area()))

print(c1.__dict__) #딕셔너리 표시하기
