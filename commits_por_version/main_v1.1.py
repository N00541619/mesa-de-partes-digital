import random

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
