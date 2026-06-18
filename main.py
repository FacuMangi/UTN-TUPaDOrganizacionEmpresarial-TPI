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

		pedirDias = validarInputNumero(f"Cuantos dias desea solicitar, {empleado["Nombre"]}?\nIntroducir dias: ")
		estado = "Validando solicitud"
		print(f"Estado: {estado}\n")

		# la funcion verificarSaldo devuelve True o False, si devuelve True es que tiene dias suficientes
		if verificarSaldo(empleado, pedirDias):
			if validarInputTexto("Supervisor aprueba? (s/n)\nIntroducir respuesta: ").lower() == "s":
				actualizarEmpleado(empleado, empleados, pedirDias)
				print(f"RRHH esta registrando su ausencia.\nSu solicitud fue aprobada")
			else: print("Su solicitud fue rechazada.")
		else:
			print("No cuenta con la cantidad de dias suficiente.")
			estado = "Chat finalizado"		
			print(f"Estado: {estado}\n")

	except Exception as e:
		print(f'Error en estado: "{estado}".\nError: {e}\n')
		estado = "Chat finalizado"		
		print(f"Estado: {estado}\n")

if __name__ == "__main__":
    main()