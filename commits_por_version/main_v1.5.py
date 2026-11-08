import random
import time
import os

def buscar_solicitud(lista, codigo):

    for solicitud in lista:
        if solicitud.codigo.upper() == codigo.upper():
            return solicitud
    return None


class Ciudadano:
    def __init__(self, dni, nombre, correo, telefono):
        self.dni = dni
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

class Cita:
    def __init__(self):
        self.fecha = f"{random.randint(1, 30)}/{random.randint(10, 12)}/2026"
        self.hora = f"{random.randint(8, 16)}:{random.randint(0, 59):02d}"
        self.zona = "Ventanilla Principal (Mesa de Partes)"

class Solicitud:
    def __init__(self, ciudadano, tramite, area, asunto, cita=None):
        self.ciudadano = ciudadano
        self.tramite = tramite
        self.area = area
        self.asunto = asunto
        self.cita = cita
        self.codigo = "MUNI-2026-" + str(random.randint(1000, 9999))
        self.estado = "En revisión (Mesa de Partes)"

    def detalle_completo(self):
        info_cita = f"Cita programada: {self.cita.fecha} a las {self.cita.hora}" if self.cita else "Sin cita presencial"
        return (f"---------------------------------------------\n"
                f"Código: {self.codigo}\n"
                f"Ciudadano: {self.ciudadano.nombre} (DNI: {self.ciudadano.dni})\n"
                f"Trámite: {self.tramite} | Área: {self.area}\n"
                f"Estado Actual: [{self.estado}]\n"
                f"{info_cita}\n"
                f"---------------------------------------------")


operaciones_realizadas = 0  

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def incrementar_operacion():
    global operaciones_realizadas
    operaciones_realizadas += 1

def leer_entero(minimo, maximo, mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            print(f"Error: Ingrese un valor entre {minimo} y {maximo}.")
        except ValueError:
            print("Error: Ingrese un número entero válido.")

def simular_carga(texto):
    print(texto, end="", flush=True)
    for _ in range(10):
        print("*", end="", flush=True)
        time.sleep(0.15)
    print(" ] Completado")

def main():
    lista_tramites = []
    areas_disponibles = ["Licencias", "Secretaría General", "Rentas", "Desarrollo Urbano", "Fiscalización"]
    opcion = 0

    while opcion != 5:
        limpiar_pantalla()
        print("==========================================")
        print(" MUNICIPALIDAD DISTRITAL DE LOS OLIVOS")
        print("==========================================")
        print("1. Registrar nueva solicitud")
        print("2. Agendar ticket de atención presencial")
        print("3. Consultar / Buscar trámite por código")
        print("4. Módulo de gestión interna (Personal)")
        print("5. Salir del sistema")
        
        opcion = leer_entero(1, 5, "Seleccione una opción (1-5)  ")

        if opcion == 1:
            limpiar_pantalla()
            print("=== REGISTRO DE SOLICITUD ===")
            dni = input("Ingrese número de DNI: ")
            nombre = input("Ingrese nombre completo o Razón Social: ")
            correo = input("Ingrese correo electrónico: ")
            telefono = input("Ingrese teléfono de contacto: ")

            print("\nTipos de trámite:")
            print("1. Solicitud simple")
            print("2. Pago de arbitrios / impuesto predial")
            print("3. Certificación de copias")
            opc_tramite = leer_entero(1, 3, "Seleccione opción  ")
            
            tipos = ["Solicitud simple", "Pago de arbitrios / impuesto predial", "Certificación de copias"]
            tipo_tram = tipos[opc_tramite - 1]

            asunto = input("Describa su consulta o asunto: ")
            
            print("Áreas disponibles:")
            for i in range(len(areas_disponibles)):
                print(f"{i + 1}. {areas_disponibles[i]}")
            opc_area = leer_entero(1, len(areas_disponibles), "Seleccione área  ")
            area_elegida = areas_disponibles[opc_area - 1]

            cita_obj = None
            req_cita = input("¿Requiere cita presencial? (S/N)  ").strip().upper()
            if req_cita == "S":
                cita_obj = Cita()

            nuevo_ciudadano = Ciudadano(dni, nombre, correo, telefono)
            nueva_solicitud = Solicitud(nuevo_ciudadano, tipo_tram, area_elegida, asunto, cita_obj)

            print("\n[ ", end="", flush=True)
            simular_carga("Creando la solicitud")
            
            lista_tramites.append(nueva_solicitud)
            incrementar_operacion()

            limpiar_pantalla()
            print("==========================================")
            print(" SOLICITUD REGISTRADA EXITOSAMENTE")
            print("==========================================")
            print(nueva_solicitud.detalle_completo())
            print("==========================================")
            input("Presione Enter para regresar al menú...")

        elif opcion == 2:
            limpiar_pantalla()
            print("=== GENERAR TICKET DE ATENCIÓN PRESENCIAL ===")
            nombre = input("Ingrese nombres del ciudadano: ")
            simular_carga("Buscando fechas y horas disponibles [ ")
            
            cita_presencial = Cita()
            print("\nCITA DISPONIBLE AGENDADA")
            print("==========================================")
            print(f"Ciudadano: {nombre}")
            print(f"Programada para el: {cita_presencial.fecha} a las {cita_presencial.hora}")
            print(f"Zona: {cita_presencial.zona}")
            print("Por favor, acuda con su DNI en físico.")
            print("==========================================")
            incrementar_operacion()
            input("Presione Enter para regresar al menú...")

        elif opcion == 3:
            limpiar_pantalla()
            print("=== SEGUIMIENTO DE TRÁMITE ===")
            if len(lista_tramites) == 0:
                print("No hay trámites registrados en el sistema.")
            else:
                buscado = input("Ingrese el código de seguimiento (Ej: MUNI-2026-XXXX)  ")
                simular_carga("Buscando expediente [ ")
                
                resultado = buscar_solicitud(lista_tramites, buscado)
                if resultado:
                    print("\n¡EXPEDIENTE ENCONTRADO!")
                    print(resultado.detalle_completo())
                else:
                    print("Error: No se encontró ningún trámite con ese código.")
            incrementar_operacion()
            input("\nPresione Enter para regresar al menú...")

        elif opcion == 5:
            print("Saliendo del sistema...")

        else:
            print("Opción en construcción.")
            input("Presione Enter para regresar al menú...")

if __name__ == "__main__":
    main()
