from funciones import *

def main():
	try:
		estado = "Chat inicializado"		
		print(f"Estado: {estado}\n")

		empleados = cargarEmpleados()
		
		legajo = validarInputNumero("Bienvenido. Ingrese su legajo: ")
		estado = verificarLegajo(empleados, legajo)
		print(f"Estado: {estado}\n")

		empleado = buscarEmpleado(empleados, legajo)

		pedirDias = validarInputNumero(f"Cuántos días desea solicitar, {empleado["Nombre"]}?\nIntroducir días: ")
		
		fechas = [] 
		fechas.append(validarFecha(f"Introduzca fecha de inicio (DD/MM): "))
		fechas.append(validarFecha(f"Introduzca fecha de fin (DD/MM): "))

		estado = "Validando solicitud"
		print(f"Estado: {estado}\n")

		# la funcion verificarSaldo devuelve True o False, si devuelve True es que tiene dias suficientes
		if verificarSaldo(empleado, pedirDias):

			# Decisión del supervisor
			if validarInputTexto("Supervisor aprueba? (s/n)\nIntroducir respuesta: ").lower() == "s":
				
				actualizarEmpleado(empleado, empleados, pedirDias)
				
				# Caso feliz: supervisor aprueba
				print(f"RRHH está registrando su ausencia.\nSu solicitud fue aprobada")

				cargarSolicitud(empleado, fechas, "APROBADA")

			else: 
				# Caso infeliz 3: supervisor rechaza
				print("Su solicitud fue rechazada.")
				cargarSolicitud(empleado, fechas, "RECHAZADA - SUPERVISOR")

		else:
			# Caso infeliz 2: saldo insuficiente 
			print("No cuenta con la cantidad de días suficiente.")
			cargarSolicitud(empleado, fechas, "RECHAZADA - SALDO INSUFICIENTE")

			estado = "Chat finalizado"		
			print(f"Estado: {estado}\n")

	except Exception as e:
		print(f'Error en estado: {estado}.\nError: {e}\n')
		estado = "Chat finalizado"		
		print(f"Estado: {estado}\n")

if __name__ == "__main__":
    main()
