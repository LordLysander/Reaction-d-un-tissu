class Vec3f:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0


    def dot(self, vec):
        return self.x*vec.x + self.y*vec.y + self.z*vec.z


    def cross(self, vec):
        ret = Vec3f()
        ret.x = self.y*vec.z-vec.y*self.z
        ret.y = self.z*vec.x-vec.z*self.x
        ret.z = self.x*vec.y-vec.x*self.y
        return ret


    def add(self, vec):
        ret = Vec3f()
        ret.x, ret.y, ret.z = self.x + vec.x, self.y + vec.y, self.z + vec.z
        return ret


    def mult(self , scal):
        self.x *= scal   # a*=l <=> a = a * l   marche aussi avec | & && || << >> < > ! % + -  / // **
        self.y *= scal
        self.z *= scal
        
    def __str__(self):
        return "x : " + str(self.x) + " | y : " + str(self.y) + " | z : " + str(self.z)
    
    def __add__(self, vec):
        ret = Vec3f()
        ret.x, ret.y, ret.z = self.x + vec.x, self.y + vec.y, self.z + vec.z
        return ret
        
    def __mul__(self,scal):
        ret = Vec3f()
        ret.x, ret.y, ret.z = self.x*scal, self.y*scal, self.z*scal
        return ret
        
        
    def __sub__(self, vec):
        ret = Vec3f()
        ret.x, ret.y, ret.z = self.x - vec.x, self.y - vec.y, self.z - vec.z
        return ret