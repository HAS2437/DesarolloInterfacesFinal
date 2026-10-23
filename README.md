# Gestor de Actividades Formativas

## Autor

Héctor Alonso Pastor del Río

Módulo: 0488 - Desarrollo de Interfaces (2.º DAM)
Unidad didáctica: UD1 - Diseño y generación de interfaces gráficas

## Descripción

Aplicación de escritorio para gestionar las inscripciones del alumnado en las
actividades formativas de un centro educativo.

Permite registrar a un participante en una actividad (nombre, correo, ciclo,
actividad, fecha, número de participantes, modalidad, material y
observaciones), revisar el alta en una página de resumen y consultar todas las
inscripciones en un listado con búsqueda, edición y eliminación.

## Funcionalidades

- Navegación por páginas con `QStackedWidget`: Inicio, Formulario, Resumen y
  Listado, accesibles también desde el menú Archivo.
- Alta de inscripciones con validación en vivo del formulario: el nombre es
  obligatorio y **no puede contener números**, el correo se comprueba con una
  expresión regular, y hay que elegir ciclo, actividad y aceptar las
  condiciones.
- Página de resumen con los datos de la última inscripción registrada.
- Listado de inscripciones en tabla (`QTableWidget`) con contador de registros.
- Búsqueda por nombre, correo o actividad, sin distinguir mayúsculas.
- Edición de la inscripción seleccionada, cargando todos sus datos en el
  formulario y actualizando el mismo registro sin duplicarlo.
- Eliminación de la inscripción seleccionada con confirmación previa.
- Confirmación e información al usuario mediante `QMessageBox` en las
  operaciones de alta, edición y eliminación.
- Atajos de teclado: Ctrl+N (nueva), Ctrl+L (listado), Ctrl+I (inicio),
  Ctrl+Q (salir), Intro (Guardar) y Esc (cancelar edición).

## Requisitos

- Sistema operativo: Windows 10/11 (también funciona en Linux o macOS).
- Python 3.10 o superior (probada con Python 3.14.7).
- Bibliotecas: PySide6 6.12.0 (ver `requirements.txt`).

## Instalación

Abre una terminal en la carpeta del proyecto y crea el entorno virtual:

```
py -m venv .venv
```

Después instala las dependencias con **una** de estas dos formas:

- Con el entorno virtual activado (en `cmd`: `.venv\Scripts\activate`; en
  PowerShell: `.venv\Scripts\Activate.ps1`):

  ```
  python -m pip install -r requirements.txt
  ```

- Sin activarlo (funciona siempre, y es lo que se usó en la prueba de
  despliegue):

  ```
  .venv\Scripts\python.exe -m pip install -r requirements.txt
  ```

En Linux o macOS: `python3 -m venv .venv` y `source .venv/bin/activate`.

> Nota: en PowerShell puede aparecer el aviso
> *«running scripts is disabled on this system»* al activar. Es la política de
> ejecución de scripts de Windows; no afecta a la aplicación y se puede usar la
> segunda opción.

## Ejecución

```
.venv\Scripts\python.exe main.py
```

o, con el entorno virtual activado:

```
python main.py
```

## Estructura del proyecto

```
Alonso_Héctor_UD1_ProyectoFinal/
│
├── main.py                  # Lógica de la aplicación y clase VentanaPrincipal
├── principal.ui             # Diseño de la interfaz (fuente en Qt Designer)
├── ui_principal.py          # Código generado desde principal.ui (pyside6-uic)
├── pruebas_funcionales.py   # Batería de 18 casos de prueba automatizada
├── resultados_pruebas.json  # Resultado detallado de la última ejecución
├── README.md                # Este archivo
├── requirements.txt         # Dependencias del proyecto
│
└── documentacion/
    └── Alonso_Héctor_InformeFinal_UD1.pdf   # Informe final con capturas
```

`principal.ui` es el archivo de diseño original; `ui_principal.py` se genera
a partir de él con `pyside6-uic principal.ui -o ui_principal.py` y no debe
editarse a mano.

## Instrucciones de uso

1. Al abrir la aplicación aparece la página de Inicio con el título y una
   descripción. Pulsa **Comenzar** para ir al formulario.
2. Completa los campos obligatorios: nombre, correo, ciclo y actividad, y
   marca la aceptación de las condiciones. Mientras falte algo, el botón
   **Guardar** permanece desactivado y el mensaje inferior indica qué revisar.
3. Pulsa **Guardar** y confirma la inscripción. Se muestra la página de
   Resumen con los datos registrados.
4. Pulsa **Ver todas** (o Archivo > Ver listado, Ctrl+L) para ver todas las
   inscripciones en la tabla.
5. En el listado puedes escribir en el buscador para filtrar por nombre,
   correo o actividad; **Limpiar búsqueda** restaura el listado completo.
6. Selecciona una fila y pulsa **Editar** para cargar sus datos en el
   formulario y modificarlos (Esc cancela la edición) o **Eliminar** para
   borrar el registro tras confirmarlo.
7. **Volver al Inicio** regresa siempre a la primera página.

## Pruebas realizadas

Se han ejecutado 18 casos de prueba automatizados con `pruebas_funcionales.py`
(ejecuta la aplicación real sin pantalla). Resultado final: **18/18
superadas**.

| ID    | Funcionalidad              | Estado final             |
|-------|----------------------------|--------------------------|
| PF01  | Ejecución inicial          | SUPERADA TRAS CORRECCIÓN |
| PF02  | Navegación completa        | SUPERADA                 |
| PF03  | Alta con datos válidos     | SUPERADA                 |
| PF04  | Campo obligatorio vacío    | SUPERADA TRAS CORRECCIÓN |
| PF05  | Formato incorrecto (correo)| SUPERADA TRAS CORRECCIÓN |
| PF06  | Búsqueda con coincidencias | SUPERADA                 |
| PF07  | Búsqueda sin coincidencias | SUPERADA TRAS CORRECCIÓN |
| PF08  | Restauración del listado   | SUPERADA                 |
| PF09  | Edición con selección      | SUPERADA TRAS CORRECCIÓN |
| PF10  | Edición sin selección      | SUPERADA TRAS CORRECCIÓN |
| PF11  | Eliminación cancelada      | SUPERADA                 |
| PF12  | Eliminación confirmada     | SUPERADA                 |
| PF13  | Operaciones con filtro     | SUPERADA TRAS CORRECCIÓN |
| PF14  | Límites del contador       | SUPERADA                 |
| PF15  | Navegación con teclado     | SUPERADA TRAS CORRECCIÓN |
| PF16  | Redimensionado y título    | SUPERADA TRAS CORRECCIÓN |
| PF17  | Esc cancela edición        | SUPERADA                 |
| PF18  | Nombre con números         | SUPERADA TRAS CORRECCIÓN |

La primera pasada se realizó con 16 casos y obtuvo **9/16**; el caso PF18
(nombre con números) tampoco pasó a la primera y se corrigió. El detalle de las
incidencias detectadas y sus correcciones está en el informe final.

## Limitaciones conocidas

- Los datos se mantienen en memoria: al cerrar la aplicación se pierden las
  inscripciones, ya que la persistencia no forma parte de la UD1.
- La búsqueda no distingue entre mayúsculas y minúsculas a propósito, pero no
  permite combinar varios criterios a la vez.
- Solo se puede editar o eliminar una inscripción cada vez (selección simple).

## Autoría y recursos

- Código, diseño de la interfaz y documentación: autoría propia.
- La interfaz se diseñó en Qt Designer (incluido con PySide6) y se generó
  `ui_principal.py` con `pyside6-uic`.
- No se han utilizado iconos, imágenes ni fuentes de terceros: la aplicación
  usa el aspecto nativo del sistema y los estándares de Qt.
- PySide6 se distribuye bajo licencia LGPL/Qt.
