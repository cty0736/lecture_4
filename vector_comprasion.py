
class Vector3D:
    def __init__(self,x,y,z): # 변수 x,y,z
        self.x=x #언더바 두개쓰면 외부에서 호출 못해요 self.__x 이런거
        self.y=y #생성자 만들기
        self.z=z

    def __str__(self): #문자열로 출력하려면 사용, 반환 어떻게 하는 지 만든 것
        return '({},{},{})'.format(self.x, self.y, self.z)
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return 'Vectors are identical'
        else :
            return 'Vectors are different'

v1=Vector3D(1,2,3)
v2=Vector3D(1,2,4)

print(v1==v2)