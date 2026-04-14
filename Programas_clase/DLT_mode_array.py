#Autor Trejo Garcia Ozkar Mauricio 
#Encontrar la homografia de la matriz a traves de puntos visibles de mi foto.
import numpy as np

#Puntos del mundo
pts_3D = [
    (0,0),
    (5,0),
    (5,6),
    (0,6),
    (2.5,3),
    (4,3),
]

#Puntos de la imagen 
pts_2D = [
    (650, 800),
    (900,780),
    (880, 500),
    (600, 520),
    (750, 650),
    (820, 600),
]

A = []

for (x,y),(u,v) in zip(pts_3D, pts_2D):

    A.append([x,y,1,0,0,0,-u*x,-u*y,-u])
    A.append([0,0,0,x,y,1,-v*x,-v*y,-v])

A = np.array(A)

# SVD
U, S, Vt = np.linalg.svd(A)

h = Vt[-1]   # menor valor singular
H = h.reshape(3,3)

# normalizar
H = H / H[2,2]

print(H)