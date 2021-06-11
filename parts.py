'''This module stores all classes used to visualize robot frame'''

class object:
    '''Basic object'''
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def copyPos(self, posArray):
        '''Convenient assigning method'''
        self.x = posArray.x
        self.y = posArray.y
        self.z = posArray.z

class cylinder(object):
    '''Representation of rotational joint'''

    def __init__(self, direction):
        self.direction = direction
        
    lenght = 2          # Lenght of rotational joint
    radius = 1          # Width of rotational joint
    angle = 0           # Initial angle of rotational joint
    maxAngle = 115      # Max allowed angle of rotational joint

class ray(object):
    '''Representation of arm'''     
    radius = 0.1        # Width of ray

class end(object):
    '''Representation of end effector'''
    direction = []

class point(object):
    '''Point in space'''
    pass