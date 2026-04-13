import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Definimos el polinomio
def P(x,y):
    return 23*x**4 + 28*x**3*y + 51*x**2*y**2 + 92*x*y**3

#Creamos una maya de puntos x ,y
x = np.linspace(-2, 2 , 100)
y = np.linspace(-2, 2 , 100)
X, Y = np.meshgrid(x, y)

Z = P(X,Y)

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Graficar la superficie
surf = ax.plot_surface(X, Y, Z, cmap='inferno', alpha=0.8, linewidth=0, antialiased=True)

# Etiquetas y título
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Gráfica de Ph4(x,y) = Ejemplo 2')

# Agregar barra de colores
plt.colorbar(surf, shrink=0.5, aspect=5)

# Mostrar
plt.show()