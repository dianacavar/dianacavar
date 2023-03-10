# -*- coding: utf-8 -*-
"""EJERCICIOCDT.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fwqQEgM8URDGL07GhpR08ekhVjSWmvyu
"""

def CDT(usuario:str, capital:int, tiempo:int):
  
  porcentaje_interes = 0.03
  porcentaje_a_perder = 0.02
  
  if tiempo > 2:
    valor_intereses = (capital * porcentaje_interes * tiempo)/12 
    valor_total = valor_intereses + capital
    return f"Para el usuario {usuario}",f"La cantidad de dinero a recibir, según el monto inicial {capital}",f"para un tiempo de {tiempo} meses es: {valor_total}"
  else:
    valor_a_perder = capital * porcentaje_a_perder
    valor_total_perdida = capital - valor_a_perder  
    return f"Para el usuario {usuario}",f"La cantidad de dinero a recibir, según el monto inicial {capital}",f"para un tiempo de {tiempo} meses es: {valor_total_perdida}"


usuario,capital,tiempo= CDT("AB1012",100000,2)
print(usuario,capital,tiempo)

def CDT(usuario:str, capital:int, tiempo:int):
  
  porcentaje_interes = 0.03
  porcentaje_a_perder = 0.02
  
  if tiempo > 2:
    valor_intereses = (capital * porcentaje_interes * tiempo)/12 
    valor_total = valor_intereses + capital
    return "Para el usuario {} La cantidad de dinero a recibir, según el monto inicial {} para un tiempo de {} meses es: {}".format(usuario,capital,tiempo,valor_total)
  else:
    valor_a_perder = capital * porcentaje_a_perder
    valor_total_perdida = capital - valor_a_perder  
    return "Para el usuario {} La cantidad de dinero a recibir, según el monto inicial {} para un tiempo de {} meses es: {}".format(usuario,capital,tiempo,valor_total_perdida)