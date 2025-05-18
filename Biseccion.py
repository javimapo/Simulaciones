import streamlit as st
import numpy as np

# Título y descripción
st.title('Cálculo del Tiempo de Reacción: Método Analítico vs. Bisección')
st.write('Este programa calcula el tiempo necesario para que una concentración inicial disminuya a una concentración final utilizando el método analítico y el método numérico de bisección.')

# Entrada de datos
C0 = st.number_input('Concentración inicial (mg/L)', value=100.0, min_value=0.1)
C = st.number_input('Concentración final (mg/L)', value=10.0, min_value=0.1, max_value=C0)
k = st.number_input('Constante de velocidad de reacción', value=0.25, min_value=0.01)
tol = st.number_input('Tolerancia para bisección', value=1e-6, format='%e')
max_iter = st.number_input('Iteraciones máximas para bisección', value=100, min_value=1, step=1)

# Método analítico
if C > 0 and C0 > C:
    t_analitico = -np.log(C / C0) / k
    st.write(f'Tiempo (Analítico): {t_analitico:.6f} s')
else:
    st.warning('La concentración final debe ser menor que la concentración inicial.')

# Método numérico: Bisección
def f(t):
    return C0 * np.exp(-k * t) - C

# Definimos los límites iniciales para la bisección
a = 0
b = 50

# Método de bisección
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

# Ejecutar el método de bisección
t_biseccion = bisection_method(f, a, b, tol, max_iter)
st.write(f'Tiempo (Bisección): {t_biseccion:.6f} s')
