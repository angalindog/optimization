# Importamos las librerías necesarias
import pulp

# Definimos el problema de optimización
modelo = pulp.LpProblem("Maximizar_Utilidad", pulp.LpMaximize)

# Definimos las variables de decisión
x1 = pulp.LpVariable('x1', lowBound=0)
x2 = pulp.LpVariable('x2', lowBound=0)

# Definimos la función objetivo - Ganancias
modelo += 180 * x1 + 220 * x2 

# Definimos las restricciones 
modelo += 3*x1 + 4*x2 <= 120 # Compuesto A
modelo += 2*x1 + 1*x2 <= 80 # Compuesto B
modelo += 5*x1 + 3*x2 <= 150 # Compuesto C

# Resolvemos el problema
modelo.solve()
# Imprimimos los resultados
print(f"Cantidad de producto 1 (x1): {x1.varValue}")
print(f"Cantidad de producto 2 (x2): {x2.varValue}")
print(f"Utilidad máxima: {pulp.value(modelo.objective)}")

## Resultados:
'''
Cantidad de producto 1 (x1): 21.818182
Cantidad de producto 2 (x2): 13.636364
Utilidad máxima: 6927.27284
'''