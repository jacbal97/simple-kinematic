import math

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
    rotZ = []           # Dont know if I need it, but I let it live
    frames = []         # Coordinates frames according to Denavit–Hartenberg, I hope I will use at least this one
    displacement = []   # Probably will be useful when spacing between servo will be used. Update useless variable

    def __init__(self, lista, distance = 7.3):
        '''Initialize joints, rays and create coordinates frames'''
        self.lista = lista
        self.distance = distance

    def shift(self, angle):
        '''Calculate the shift from rotation'''
        rad = math.radians(angle)
        return (self.distance*math.sin(rad), self.distance*math.cos(rad), 0)

    def displacement(self):
        '''Calculate displacement and direction''' 
        first = lista[0]
        for index in len(self.lista)-1:
            second = first
            first = lista[index+1]

        second.x, second.y, second.z = dispMatrix(first.direction, self.shift(first.angle))         # Calculate position
        second.direction = frameMatrix(first.angle, second.direction)                               # Calculate coordinate frame

            
            
    
