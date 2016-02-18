#-*- coding: utf-8 -*-
import random
# piedra papel o python
opciones = ["PIEDRA", "PAPEL", "PYTHON"]
print("Vamos a jugar!\n")
usuario_op = input("¿Qué escoges? (Piedra, papel o python): ")
usuario_op = usuario_op.upper()

pc_op = opciones[random.randint(0,2)]

if usuario_op == pc_op:
	print("Empate")
elif usuario_op == "PIEDRA" and pc_op == "PAPEL":
	print("Perdiste")
elif usuario_op == "PAPEL" and pc_op == "PYTHON":
	print("Perdiste")
elif usuario_op == "PYTHON" and pc_op == "PIEDRA":
	print("Perdiste")
else:
	print("¡Ganaste!")


