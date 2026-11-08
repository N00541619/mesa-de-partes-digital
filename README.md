# Mesa de Partes Digital – Municipalidad Distrital de Los Olivos

**DEL ARCHIVADOR AL ALGORITMO, UN PROTOTIPO PARA LA MESA DE PARTES DIGITAL**
Curso CIIN1205P · Ingeniería de Sistemas Computacionales · Universidad Privada del Norte (UPN) · Lima, 2026

## Descripción

Prototipo de consola desarrollado en Python que simula una mesa de partes digital: permite registrar solicitudes de ciudadanos, agendar tickets de atención presencial, consultar trámites por código de seguimiento y gestionar expedientes desde un módulo interno, usando listas de Python y control de versiones con Git y GitHub.

Es un prototipo académico y no reemplaza los procedimientos oficiales de la municipalidad.

## Tecnologías

- Python 3 (biblioteca estándar: `random`, `time` y `os`)
- Programación orientada a objetos: clases `Ciudadano`, `Cita` y `Solicitud`
- Listas de Python para guardar, buscar, eliminar y ordenar (burbuja) las solicitudes
- Git y GitHub

## Funcionalidades

1. **Registrar nueva solicitud:** datos del ciudadano, tipo de trámite, área y asunto; se genera un código de seguimiento (`MUNI-2026-XXXX`).
2. **Agendar ticket de atención presencial:** fecha, hora y zona.
3. **Consultar trámite por código de seguimiento.**
4. **Gestión interna (personal):** con código de empleado se puede derivar, marcar como resuelto o eliminar un expediente; los expedientes se ordenan por código con el método burbuja.
5. **Salir:** muestra el total de operaciones realizadas en la sesión.

## Ejecución

```bash
python main.py
```

Código de empleado de prueba para la opción 4: `OLIVOS123`

## Estructura del repositorio

```
mesa-de-partes-digital/
├── main.py        (código fuente del prototipo)
├── capturas/      (capturas de pantalla de cada versión)
└── README.md
```

## Versiones

| Versión | Funcionalidad |
| --- | --- |
| v1.0 | Estructura inicial del proyecto |
| v1.1 | Clases Ciudadano, Cita y Solicitud |
| v1.2 | Funciones auxiliares y menú principal |
| v1.3 | Registro de solicitudes en la lista |
| v1.4 | Ticket de atención presencial |
| v1.5 | Consulta por código con `buscar_solicitud` |
| v1.6 | Gestión interna: derivar y finalizar |
| v1.7 | Eliminar con `eliminar_solicitud` y ordenar con burbuja |
| v1.8 | Resumen de operaciones al salir |
| v2.0 | Pruebas y correcciones (versión final estable) |

## Integrantes

- Fabricio Dominick Delgadillo Leyva
- Juan David Zelada Grau
- Jair Lincon Aron Mamani Vasquez
- Marlon Andersson Ramos Santiago
- Fabrizio Gabriel Rojas Torres (L)

Docente: Mg. Calderon Aquiño, Cinthia

## Repositorio

https://github.com/N00541619/mesa-de-partes-digital.git
