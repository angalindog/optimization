# Importar las librerías necesarias
import pulp

# Definir el problema de equilibrio
modelo = pulp.LpProblem("Equilibrio", pulp.LpMaximize)

# Definir las variables de decisión
S = pulp.LpVariable('S', lowBound=0)  # Cantidad de sillas
M = pulp.LpVariable('M', lowBound=0)  # Cantidad de mesas

# Función objetivo (encontrar el equilibrio)
modelo += 0

# Agregar las restricciones
modelo +=0.4 * S - 0.2 * M == 40 # Equlibrio de sillas
modelo +=-0.1* S + 0.5 * M == 20 # Equilibrio de mesas

# Resolver el problema
modelo.solve(pulp.PULP_CBC_CMD(msg=0))

# Imprimir los resultados
print(f"Cantidad de sillas (S): {S.varValue}")
print(f"Cantidad de mesas (M): {M.varValue}")


# Resultados:
'''
Cantidad de sillas (S): 133.33333
Cantidad de mesas (M): 66.666667
'''