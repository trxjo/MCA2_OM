import numpy as np
import cv2
import matplotlib.pyplot as plt

# ==============================
# 1. Cargar imagen
# ==============================
img = cv2.imread("imagen.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# ==============================
# 2. Puntos (los que definimos)
# ==============================
pts_img = np.array([
    [650, 800],
    [900, 780],
    [880, 500],
    [600, 520],
    [750, 650],
    [820, 600]
], dtype=float)

pts_world = np.array([
    [0, 0],
    [5, 0],
    [5, 6],
    [0, 6],
    [2.5, 3],
    [4, 3]
], dtype=float)

# ==============================
# 3. Normalización (CLAVE)
# ==============================
def normalize_points(pts):
    mean = np.mean(pts, axis=0)
    std = np.std(pts)

    T = np.array([
        [1/std, 0, -mean[0]/std],
        [0, 1/std, -mean[1]/std],
        [0, 0, 1]
    ])

    pts_h = np.hstack((pts, np.ones((pts.shape[0],1))))
    pts_norm = (T @ pts_h.T).T

    return pts_norm, T

pts_img_n, T_img = normalize_points(pts_img)
pts_world_n, T_world = normalize_points(pts_world)

# ==============================
# 4. Construcción matriz A
# ==============================
A = []

for (x,y,_),(u,v,_) in zip(pts_world_n, pts_img_n):

    A.append([0,0,0,-x,-y,-1, v*x, v*y, v])
    A.append([x,y,1,0,0,0, -u*x, -u*y, -u])

A = np.array(A)

# ==============================
# 5. SVD (Fusiello style)
# ==============================
U, S, Vt = np.linalg.svd(A)

h = Vt[-1]  # menor valor singular
H_norm = h.reshape(3,3)

# ==============================
# 6. Desnormalizar
# ==============================
H = np.linalg.inv(T_img) @ H_norm @ T_world

# Normalizar
H = H / H[2,2]

print("Homografía:\n", H)

# ==============================
# 7. Validación
# ==============================
def project(H, pts):
    pts_h = np.hstack((pts, np.ones((pts.shape[0],1))))
    proj = (H @ pts_h.T).T
    proj = proj[:, :2] / proj[:, 2:]
    return proj

proj_pts = project(H, pts_world)

# ==============================
# 8. Visualización
# ==============================
plt.imshow(img)
plt.scatter(pts_img[:,0], pts_img[:,1], label="Real")
plt.scatter(proj_pts[:,0], proj_pts[:,1], marker='x', label="Proyectado")
plt.legend()
plt.title("DLT estilo Fusiello")
plt.show()