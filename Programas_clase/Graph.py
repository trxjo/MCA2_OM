import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir el polinomio: 2x^4 + 3x^3y + 7x^2y^2 + 15xy^3 + y^4
def P(x, y):
    return 2*x**4 + 3*x**3*y + 7*x**2*y**2 + 15*x*y**3 + y**4

# Crear una malla de puntos x, y
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)

# Evaluar el polinomio en la malla
Z = P(X, Y)

# Crear la figura 3D
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Graficar la superficie
surf = ax.plot_surface(X, Y, Z, cmap='plasma', alpha=0.8, linewidth=0, antialiased=True)

# Etiquetas y título
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Gráfica de PH4(x,y) = 2x⁴ + 3x³y + 7x²y² + 15xy³ + y⁴')

# Agregar barra de colores
plt.colorbar(surf, shrink=0.5, aspect=5)

# Mostrar
plt.show()

#Deepseek. (2026). Código de ejemplo para graficar un polinomio homogéneo en Python 