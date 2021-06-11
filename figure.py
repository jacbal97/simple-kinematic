import math
import parts

def matrix3x3(M1, M2):
    '''3x3 Matrix multiplication'''
    result = []

    for i in range(len(M1)):
        for j in range(len(M2[0])):
            for k in range(len(M2)):
                result[i][j] += M1[i][k] * M2[k][j]

    return result

def rotationZ(angle):
    '''Calculate rotational matrix'''
    rad = math.radians(angle)
    return [[math.cos(rad), -1*math.sin(rad), 0], [math.sin(rad), math.cos(rad), 0], [0 , 0, 1]]

def dispMatrix(frame, displacement):
    '''Calculate position'''
    return [frame[0][0]*displacement[0]+frame[0][1]*displacement[1]+frame[0][2]*displacement[2], 
        frame[1][0]*displacement[0]+frame[1][1]*displacement[1]+frame[1][2]*displacement[2], 
        frame[2][0]*displacement[0]+frame[2][1]*displacement[1]+frame[2][2]*displacement[2]]

def frameMatrix(angle, frame):
    '''Calculate frame coordinate'''
    return matrix3x3(rotationZ(angle), frame)

class figure:
    '''Creating object to handle calculations'''
    rotZ = []                           # Dont know if I need it, but I let it live
    frames = []                         # Coordinates frames according to Denavit–Hartenberg, I hope I will use at least this one
    displacement = [4, 7.3, 4, 4.8]     # List of spacing between joints

    endEffector = parts.end()

    def __init__(self, lista):
        '''Initialize joints, rays and create coordinates frames'''
        self.lista = lista

    # Forward kinematics
    def shift(self, angle, index):
        '''Calculate the shift from rotation'''
        rad = math.radians(angle)
        return (self.displacement[index]*math.sin(rad), self.displacement[index]*math.cos(rad), 0)

    def displacement(self):
        '''Calculate displacement and direction''' 
        for index in len(self.lista)-1:
            lista[index+1].copyPos(dispMatrix(self.lista[index], self.shift(lista[index].angle, index)))        # Calculate position
            lista[index+1].direction = frameMatrix(lista[index].angle, lista[index+1].direction)                # Calculate coordinate frame

    def endFrame(self):
        '''Copy frame to end effector'''
        index = len(self.lista)
        self.endEffector.copyPos(dispMatrix(self.lista[index], self.shift(lista[index].angle, index)))          # Calculate position of end effector
        self.endEffector.direction = self.lista[index].direction                                                # Copy coordinate frame

    # Inverse kinematic
    def setEnd(self, pos):
        '''Set position of end effector'''
        self.endEffector.copyPos(pos)
        