# UTN-TUPaDOrganizacionEmpresarial-TPI
Requisitos
Python 3.x
Ejecución
Clonar el repositorio:
git clone <repo-url>
Desde el proyecto ejecutar la aplicación:
python main.py
Funcionamiento

El bot permite:

Identificar al empleado mediante su legajo
Consultar disponibilidad de días
Crear solicitudes de vacaciones
Escalar la solicitud al supervisor
Registrar aprobaciones o rechazos
Actualizar el saldo de días
Base de datos simulada

El sistema trabaja con:

empleados.csv → datos de empleados y días disponibles

solicitudes.csv → historial de solicitudes

Flujo:

El flujo sigue la lógica definida en el diagrama BPMN:

Empleado → Chatbot → Supervisor → RRHH → Chatbot → Empleado
