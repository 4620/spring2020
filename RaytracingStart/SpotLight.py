from Light import Light
from Vector import Vector
from Point3D import Point3D

class SpotLight(Light):
    def __init__(self, color:Vector, strength:float, position:Point3D, direction:Point3D, fov:float, isCircular:bool):
        Light.__init__(self, color, strength)
        self.position = position
        self.direction = direction
        self.fov = fov
        self.isCircular = isCircular