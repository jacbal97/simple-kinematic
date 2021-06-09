class object:
    '''Basic object'''
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

class cylinder(object):
    '''Representation of rotational joint'''

    def __init__(self, direction):
        self.direction = direction
        
    lenght = 2
    radius = 1
    angle = 0
    maxAngle = 115

class ray(object):
    '''Representation of arm'''
    distance = 1
    radius = 0.1

class end(object):
    '''Representation of end effector'''
    direction = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]