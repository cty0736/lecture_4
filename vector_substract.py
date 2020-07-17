#unsupported operand type(s) for -: 'Vector3D' and 'Vector3D' 빼기 함수 직접 만들거나, __sub__이용

class Vector3D:
    def __init__(self,x,y,z): # 변수 x,y,z
        self.x=x #언더바 두개쓰면 외부에서 호출 못해요 self.__x 이런거
        self.y=y #생성자 만들기
        self.z=z


    def __str__(self): #문자열로 출력하려면 사용, 반환 어떻게 하는 지 만든 것
        return '({},{},{})'.format(self.x, self.y, self.z)

    def sub(self, other):
        return Vector3D(self.x -other.x,self.y -other.y,self.z -other.z)

    def __sub__(self, other): # 특수 메소드
        return Vector3D(self.x -other.x,self.y -other.y,self.z -other.z)    
    

v1 = Vector3D(10,20,30)
v2 = Vector3D(15,25,35)
v4=v1-v2
v3 = v1.sub(v2)
print(v3)
print(v4)

