from funciones import *

try:
	legajo = validarInputNumero("Bienvenido. Ingrese su legajo: ")
	
	empleado = verificarLegajo(legajo, cargarEmpleados())
	
	print("Empleado encontrado.")
	
	pedirDias = validarInputNumero(f"Cuantos dias se va a solicitar?\nIntroducir dias: ")
	
	if verificarSaldo(empleado, pedirDias):
		if validarInputTexto("Supervisor aprueba? (s/n)").lower() == "s":
			print(f"RRHH registro su ausencia.\nSu solicitud fue aprobada")
		else: print("Su solicitud fue rechazada.")

except Exception as e:
	print(e)