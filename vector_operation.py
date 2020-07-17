import vector_mod
import vector_comprasion
import vector_substract
import vector_add   

class Vector3D:

    def __init__(self,x,y,z):
        self.x =x
        self.y =y
        self.z=z
    def __add__(self,other):
        return vector_add.Vector3D.__add__(self,other)
    def __eq__(self, other):
        return vector_comprasion.Vector3D.__eq__(self,other)
    def __mod__(self,other):
        return vector_mod.Vector3D.__mod__(self,other)
    def __sub__(self, other): # 특수 메소드
        return vector_substract.Vector3D.__sub__(self,other)            