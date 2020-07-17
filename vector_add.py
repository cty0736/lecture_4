class Vector3D:
    def __init__(self,x,y,z): # 변수 x,y,z
        self.x=x #언더바 두개쓰면 외부에서 호출 못해요 self.__x 이런거
        self.y=y #생성자 만들기
        self.z=z

    def __str__(self): #문자열로 출력하려면 사용, 반환 어떻게 하는 지 만든 것
        return '({},{},{})'.format(self.x, self.y, self.z)

    # def add(self, other): #add 는 메소드, 변수 other
    #     return Vector3D(self.x + other.x, self.y + other.y,self.z + other.z) 

    def __add__(self, other): #__add__ 는 특수 메소드, 변수 other
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)    

# v1=Vector3D(10,20,30)
# v2=Vector3D(20,30,40)

# #v3 = v1.add(v2) # add 메소드로 계산, other입력
# v4 = v1+v2 # __add__로 계산,
# print(v4)