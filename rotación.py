import numpy as np

def rot_x(x, y, z, theta):
    '''
    Rota un punto en el espacio 3D alrededor del eje X.
    Parameters:
        x (float): coordenada x del punto a rotar
        y (float): coordenada y del punto a rotar
        z (float): coordenada z del punto a rotar
        theta (float): ángulo de rotación en radianes
    Returns:
        numpy.ndarray: vector rotado con las nuevas coordenadas
    '''
    p = np.array([x, y, z])
    R = np.array([
        [1, 0, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta), np.cos(theta)]
    ])
    return np.dot(R, p)

def rot_y(x, y, z, theta):
    '''
    Rota un punto en el espacio 3D alrededor del eje Y.
    Parameters:
        x (float): coordenada x del punto a rotar
        y (float): coordenada y del punto a rotar
        z (float): coordenada z del punto a rotar
        theta (float): ángulo de rotación en radianes
    Returns:
        numpy.ndarray: vector rotado con las nuevas coordenadas
    '''
    p = np.array([x, y, z])
    R = np.array([
        [np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])
    return np.dot(R, p)

def rot_z(x, y, z, theta):
    '''
    Rota un punto en el espacio 3D alrededor del eje Z.
    Parameters:
        x (float): coordenada x del punto a rotar
        y (float): coordenada y del punto a rotar
        z (float): coordenada z del punto a rotar
        theta (float): ángulo de rotación en radianes
    Returns:
        numpy.ndarray: vector rotado con las nuevas coordenadas
    '''
    p = np.array([x, y, z])
    R = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])
    return np.dot(R, p)

def rotar(x, y, z, theta, axis):
    '''
    Rota un punto en el espacio 3D alrededor del eje especificado.
    Parameters:
        x (float): coordenada x del punto a rotar
        y (float): coordenada y del punto a rotar
        z (float): coordenada z del punto a rotar
        theta (float): ángulo de rotación en radianes
        axis (string): eje de rotacion; puede tomar valor 'x', 'y' o 'z'.
    Returns:
        numpy.ndarray: vector rotado con las nuevas coordenadas
    '''
    if axis.lower() == 'x':
        return rot_x(x, y, z, theta)
    elif axis.lower() == 'y':
        return rot_y(x, y, z, theta)
    elif axis.lower() == 'z':
        return rot_z(x, y, z, theta)
    else:
        raise ValueError("El eje debe ser 'x', 'y' o 'z'")