from funciones import *

ESTADOS = {
    "INICIO",
    "ESPERANDO_LEGAJO",
    "LEGAJO_VALIDADO",
    "CARGANDO_SOLICITUD",
    "PENDIENTE_APROBACION",
    "APROBADA",
    "RECHAZADA",
    "ERROR",
}

def transicionar(estado_actual: str, nuevo_estado: str) -> str:
    print(f"  [transición] {estado_actual} → {nuevo_estado}")
    return nuevo_estado

def main():
    estado = transicionar("—", "INICIO")
    empleados = []
    empleado = None

    try:
        empleados = cargarEmpleados()

        # ── Estado: ESPERANDO_LEGAJO ──────────────────────────────────────
        estado = transicionar(estado, "ESPERANDO_LEGAJO")
        # validarInputNumero ya maneja entradas inválidas internamente
        # (loop hasta recibir un entero positivo)
        legajo = validarInputNumero("Bienvenido. Ingrese su legajo: ")

        try:
            verificarLegajo(empleados, legajo)
            empleado = buscarEmpleado(empleados, legajo)
        except ValueError as e:
            # Legajo inexistente → transición directa a RECHAZADA
            estado = transicionar(estado, "RECHAZADA")
            print(f"Acceso denegado: {e}")
            return

        # ── Estado: LEGAJO_VALIDADO ───────────────────────────────────────
        estado = transicionar(estado, "LEGAJO_VALIDADO")
        print(f"Bienvenido, {empleado['Nombre']}. "
              f"Días disponibles: {empleado['DiasDisponibles']}\n")

        # ── Estado: CARGANDO_SOLICITUD ────────────────────────────────────
        estado = transicionar(estado, "CARGANDO_SOLICITUD")
        # validarInputNumero y validarFecha manejan entradas inválidas internamente
        dias = validarInputNumero(
            f"¿Cuántos días desea solicitar, {empleado['Nombre']}? "
        )
        fecha_inicio = validarFecha("Fecha de inicio (DD/MM): ")
        fecha_fin    = validarFecha("Fecha de fin   (DD/MM): ")
        fechas = [fecha_inicio, fecha_fin]

        # Verificar saldo antes de llegar al supervisor
        if not verificarSaldo(empleado, dias):
            estado = transicionar(estado, "RECHAZADA")
            print(f"Solicitud rechazada: no cuenta con {dias} días disponibles "
                  f"(disponibles: {empleado['DiasDisponibles']}).")
            return

        # ── Estado: PENDIENTE_APROBACION ──────────────────────────────────
        estado = transicionar(estado, "PENDIENTE_APROBACION")
        respuesta = validarInputTexto("¿El supervisor aprueba? (s/n): ").lower()

        if respuesta == "s":
            actualizarEmpleado(empleado, empleados, dias)
            cargarSolicitud(empleado, fechas, "APROBADA")
            estado = transicionar(estado, "APROBADA")
            print("Solicitud aprobada. RRHH registró la ausencia.")
        else:
            cargarSolicitud(empleado, fechas, "RECHAZADA")
            estado = transicionar(estado, "RECHAZADA")
            print("Solicitud rechazada por el supervisor.")

    except Exception as e:
        estado = transicionar(estado, "ERROR")
        print(f"Error inesperado en estado {estado}: {e}")

if __name__ == "__main__":
    main()