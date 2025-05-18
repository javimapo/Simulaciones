import numpy as np

# Datos del problema
C0 = 100  # mg/L, concentración inicial
C = 10    # mg/L, concentración final
k = 0.25  # constante de velocidad de reacción

# Método analítico
# C = C0 * exp(-k * t)
# Resolviendo para t:
t_analitico = -np.log(C / C0) / k

# Método numérico: Bisección
def f(t):
    return C0 * np.exp(-k * t) - C

# Definimos los límites iniciales para la bisección
a = 0
b = 50  # Suposición inicial
tol = 1e-6
max_iter = 100

def bisection_method(f, a, b, tol, max_iter):
    for i in range(max_iter):
        c = (a + b) / 2
        if f(c) == 0 or (b - a) / 2 < tol:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c

t_biseccion = bisection_method(f, a, b, tol, max_iter)

t_analitico, t_biseccion
