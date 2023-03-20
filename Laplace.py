# Biblioteca para geração dos polinômios
import numpy as np
from numpy.polynomial import Polynomial

# Biblioteca para criação do gráfico
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Recebe os valores para criar o polinômio no numerador da função de transferência
n = list(map(int,input("\nEntre com os valores do polinômio do numerador\nExemplo: 1 2 3 gera s²+2s+3\nInsira os valores:").strip().split()))
num = np.poly1d(n)

# Calcula os zeros da função de transferência
zeros = np.roots(num)

# Recebe os valores para criar o polinômio no denominador da função de transferência
d = list(map(int,input("\nEntre com os valores do polinômio do denominador : ").strip().split()))
den = np.poly1d(d)

# Calcula os polos da função de transferência
polos = np.roots(den)


#================================================Criação do gráfico 3D de amplitude=====================================

# Criação dos eixos do plano cartesiano
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)

# Criação da variável 's'
s = X+Y*1j

# Troca de variável dos polinômios de 'x' (padrão) para 's'
num1 = np.polyval(num, s)
den1 = np.polyval(den, s)

# Cálculo da magnitude de H
H = abs(num1/den1)

# Mudando o nome dos eixos
ax.set_xlabel('Re')
ax.set_ylabel('Im')
ax.set_zlabel('|H|')
# Função que gera o gráfico 3D
surf = ax.plot_surface(X, Y, H, cmap=cm.inferno, linewidth=0, antialiased=False)

plt.show()


#================================================Criação do diagrama de polos e zeros===================================
# Plot dos polos e zeros no plano Real x Imaginário
plt.plot(zeros.real, zeros.imag, 'o')
plt.xlabel('Parte real de S')
plt.plot(polos.real, polos.imag, 'x')
plt.ylabel('Parte imaginária de S')
plt.show()


#================================================Criação do gráfico para sigma = 0======================================

# Criação da variável complexa 'im'
im = Y*1j

# Criação de polinômio sem parte real sigma = 0
num2 = np.polyval(num, im)
den2 = np.polyval(den, im)
    
# Cálculo de H para sigma = 0
H2 = abs(num2/den2)

plt.plot(Y, H2)
plt.xlabel('Eixo Imaginário')
plt.ylabel('Magnitude de H')

plt.show()
