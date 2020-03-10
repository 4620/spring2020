from Vector import Vector

class Material:
    def __init__(self, diffuseColor:Vector, specularColor:Vector, specularStrength:float):
        self.diffuseColor = diffuseColor
        self.specularColor = specularColor
        self.specularStrength  = specularStrength