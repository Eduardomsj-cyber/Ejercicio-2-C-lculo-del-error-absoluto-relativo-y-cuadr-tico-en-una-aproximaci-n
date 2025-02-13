#   Codigo que implementa un esquema numerico 
#   para determinar la aproximacion de Leibniz
# 
#           Autor:
#   Dr. Ivan de Jesus May-Cen
#   imaycen@hotmail.com
#   Version 1.0 : 29/01/2025
#


import numpy as np
import matplotlib.pyplot as plt  # Importamos librerías para cálculos numéricos y gráficos

# Función que calcula una aproximación de pi usando la serie de Leibniz
def leibniz_pi(n):
    return 4 * sum((-1)**k / (2*k + 1) for k in range(n))  # Fórmula de la serie de Leibniz

true_pi = np.pi  # Valor real de pi
N_values = [10, 100, 1000, 10000]  # Valores de N para probar la aproximación
errors_abs = []  # Lista para almacenar errores absolutos
errors_rel = []  # Lista para almacenar errores relativos

# Bucle que calcula la aproximación de pi y los errores para cada N
for N in N_values:
    approx_pi = leibniz_pi(N)  # Calcula pi con N términos
    error_abs = abs(true_pi - approx_pi)  # Error absoluto |pi_real - pi_aprox|
    error_rel = error_abs / true_pi  # Error relativo = error absoluto / pi_real
    errors_abs.append(error_abs)  # Guardamos error absoluto
    errors_rel.append(error_rel)  # Guardamos error relativo
    print(f"N={N}: Error absoluto={error_abs}, Error relativo={error_rel}")  # Mostramos los errores

# Graficamos los errores en función de N
plt.figure()
plt.plot(N_values, errors_abs, label='Error absoluto', marker='o')  # Gráfica del error absoluto
plt.plot(N_values, errors_rel, label='Error relativo', marker='s')  # Gráfica del error relativo
plt.xscale('log')  # Escala logarítmica en el eje X
plt.yscale('log')  # Escala logarítmica en el eje Y
plt.xlabel('N')  # Etiqueta del eje X
plt.ylabel('Error')  # Etiqueta del eje Y
plt.legend()  # Mostramos la leyenda
plt.title('Errores en la aproximación de pi')  # Título de la gráfica
plt.show()  # Mostramos la gráfica
