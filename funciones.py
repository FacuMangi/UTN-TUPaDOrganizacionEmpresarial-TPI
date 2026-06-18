import csv

# ========== VALIDACIONES ==========

# Funcion que recibe un mensaje que luego usa para crear un input
# luego valida ese input como string en un loop while

def validarInputTexto(mensaje: str):
	while True:
		v = input(mensaje).strip()
		if v and v.replace(" ", "").isalpha():
			return v
		print("Entrada vacía o no es texto valido. Intente de nuevo.")

# Funcion que recibe un mensaje que luego usa para crear un input
# luego valida ese input como integer en un loop while (devuelve string)
def validarInputNumero(mensaje: str):
	while True:
		s = input(mensaje).strip()
		if s == "":
			print("Entrada vacía. Intente de nuevo.")
			continue
		try:
			v = int(s)
		except ValueError:
			print("Entrada no es un número entero válido. Intente de nuevo.")
			continue
		if v <= 0:
			print("Ingrese un número positivo (mayor que 0).")
			continue
		return v

# 
def inputInt(mensaje, minimum=None, maximum=None):
	while True:
		try:
			v = int(input(mensaje))
		except ValueError:
			print("Entrada inválida. Ingrese un número entero.")
			continue
		if minimum is not None and v < minimum:
			print(f"El número debe ser >= {minimum}.")
			continue
		if maximum is not None and v > maximum:
			print(f"El número debe ser <= {maximum}.")
			continue
		return v

# Funcion que recibe una fecha en formato DD/MM
# valida que dia y mes sean numericos y esten dentro de rangos validos
def validarFecha(mensaje):
	while True:
		fecha = input(mensaje).strip()

		partes = fecha.split("/")

		if len(partes) == 2:
			dia, mes = partes

			if dia.isdigit() and mes.isdigit():
				dia = int(dia)
				mes = int(mes)

				if 1 <= dia <= 31 and 1 <= mes <= 12:
					return fecha
		
		print("Formato esperado: DD/MM")

# ========== FUNCIONES ==========

# funcion que devuelve filas de csv como lista de diccionarios con dupla key-value
def cargarEmpleados():
    with open("datosEmpleados.csv", "r", encoding="utf-8") as archivo:
        # devuelve lista de todos los datos de la fila del archivo como strings, asociados a su columna como par key-value
        listaDic = list(csv.DictReader(archivo))
        
        # se convierten valores numericos de string a int
        for empleado in listaDic:
            empleado["Legajo"] = int(empleado["Legajo"])
            empleado["DiasDisponibles"] = int(empleado["DiasDisponibles"])

        return(listaDic)
	
# funcion que toma lista de diccionarios y modifica csv con sus datos
def guardarCambios(empleados: list):
    if not empleados:
        raise ValueError("Error: no hay empleados cargados.")
        
    columnas = ["Legajo","Nombre","Departamento","DiasDisponibles"]

    with open("datosEmpleados.csv", "w", newline="", encoding="utf-8") as archivo:
        escritorDict = csv.DictWriter(archivo, fieldnames=columnas)
        escritorDict.writeheader()
        escritorDict.writerows(empleados)

# funcion que verifica si el legajo introducido pertenece a un empleado
# si el legajo pertenece a un empleado
# so no pertenece a un empleado devuelve un error 		
def verificarLegajo(empleados: list, legajoUsuario: int):
    if not empleados:
        raise ValueError("Error: no hay empleados cargados.")

    encontrado = False
	
    for empleado in empleados:
        if empleado["Legajo"] == legajoUsuario:
            return("Empleado validado")

	# caso infeliz 1: legajo inexistente
    if not encontrado:
        raise ValueError(f'Error: no se encontro empleado para el legajo introducido.')
	
def buscarEmpleado(empleados: list, legajoEmpleado: int):
	if not empleados: raise ValueError("Error: no hay empleados cargados.")
	
	encontrado = False
		
	for empleado in empleados:
		if empleado["Legajo"] == legajoEmpleado:
			return(empleado)
	
	if not encontrado:
		raise ValueError(f'Error: no se encontro empleado para el legajo introducido.')


# funcion que verifica que el empleado tenga suficientes dias disponibles
def verificarSaldo(empleado: dict, diasPedidos: int):
	if not empleado:
		raise ValueError("Error: no hay empleado cargado.")
	
	return(diasPedidos <= empleado["DiasDisponibles"])

# funcion que actualiza datos del epmleado, restando sus dias disponibles con los dias pedidos
def actualizarEmpleado(empleadoCargado: dict, empleados: list, diasPedidos: int):
	if not empleadoCargado:
		raise ValueError("Error: no hay empleado cargado.")
	if not empleados:
		raise ValueError("Error: no hay empleados cargados.")
	if not diasPedidos:
		raise ValueError("Error: no hay días pedidos.")
	
	empleadoCargado["DiasDisponibles"] -= diasPedidos

	for empleado in empleados:
		if empleado["Legajo"] == empleadoCargado["Legajo"]:
			empleado.update(empleadoCargado)
	
	guardarCambios(empleados)

# funcion que recibe empleado y se le registra el pedido de vacaciones
def cargarSolicitud(empleado: dict, fechas: list, estado: str):
	columnas = ["Legajo","Nombre","Vacaciones", "Estado"]

	try:
		# Intenta abrir el modo lectura para saber si existe
		with open("solicitudes.csv", "r", encoding="utf-8") as archivo:
			existe = True
	except FileNotFoundError:
		existe = False

	# Si no existe, lo crea con encabezados
	if not existe:
		with open("solicitudes.csv", "w", newline="", encoding="utf-8") as archivo:
			escritor = csv.DictWriter(archivo, fieldnames=columnas)
			escritor.writeheader()
			escritor.writerow({
				"Legajo": empleado["Legajo"],
				"Nombre": empleado["Nombre"],
				"Vacaciones": f"{fechas[0]} - {fechas[1]}",
				"Estado": estado
			})
	
	else:
		# Si ya existe, solo agrega una nueva fila
		with open("solicitudes.csv", "a", newline="", encoding="utf-8") as archivo:
			escritor = csv.DictWriter(archivo, fieldnames=columnas)
			escritor.writerow({
				"Legajo": empleado["Legajo"],
				"Nombre": empleado["Nombre"],
				"Vacaciones": f"{fechas[0]} - {fechas[1]}",
				"Estado": estado
			})