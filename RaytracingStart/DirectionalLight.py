from Light import Light
from Point3D import Point3D
from Vector import Vector

class DirectionalLight(Light):
    def __init__(self, color:Vector, strength:float, direction:Vector):
        Light.__init__(self, color, strength)
        self.direction = direction