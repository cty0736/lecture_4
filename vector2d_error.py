
#ERROR unsuportted operand type for +: Vector2D and Vector2D
# +를 할 수 없음, 메소드로 손수 만들어서 수행 
class Vector2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
v1 = Vector2D(1,2)
v2 = Vector2D(3,4)

v3 = v1+v2