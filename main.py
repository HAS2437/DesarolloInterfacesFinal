import re
import sys

from PySide6.QtCore import QDate, Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QTableWidgetItem,
)

from ui_principal import Ui_VentanaPrincipal

# Expresión regular sencilla de validación de correo
EXPRESION_CORREO = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]{2,}$")


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_VentanaPrincipal()
        self.ui.setupUi(self)

        self.inscripciones = []
        self.indice_edicion = None

        self.configurar_interfaz()
        self.conectar_eventos()
        self.mostrar_inicio()

    # ------------------------------------------------------------------
    # Configuración inicial
    # ------------------------------------------------------------------
    def configurar_interfaz(self):
        self.ui.dateFecha.setDate(QDate.currentDate())

        self.ui.spinParticipantes.setMinimum(1)
        self.ui.spinParticipantes.setMaximum(30)
        self.ui.spinParticipantes.setValue(1)

        self.ui.btnRegistrar.setEnabled(False)
        # Intro activa el botón Guardar sin necesidad del ratón (accesibilidad)
        self.ui.btnRegistrar.setDefault(True)

        self.ui.tablaInscripciones.setColumnCount(7)
        self.ui.tablaInscripciones.setHorizontalHeaderLabels([
            "Nombre",
            "Correo",
            "Ciclo",
            "Actividad",
            "Fecha",
            "Participantes",
            "Modalidad",
        ])
        self.ui.tablaInscripciones.horizontalHeader().setStretchLastSection(True)

        self.actualizar_contador([])
        self.ui.statusbar.showMessage("Aplicación Preparada.")

    def conectar_eventos(self):
        # Botones de navegación y acciones principales
        self.ui.btnComenzar.clicked.connect(self.mostrar_formulario)
        self.ui.btnLimpiar.clicked.connect(self.limpiar_formulario)
        self.ui.btnRegistrar.clicked.connect(self.registrar)
        self.ui.btnNueva.clicked.connect(self.nueva_inscripcion)
        self.ui.btnVerTodas.clicked.connect(self.mostrar_listado)
        self.ui.btnInicio.clicked.connect(self.mostrar_inicio)

        # Página de listado
        self.ui.btnNuevaListado.clicked.connect(self.nueva_inscripcion)
        self.ui.btnEditarListado.clicked.connect(self.editar_seleccion)
        self.ui.btnEliminarListado.clicked.connect(self.eliminar_seleccion)
        self.ui.btnInicioListado.clicked.connect(self.mostrar_inicio)
        self.ui.txtBuscar.textChanged.connect(self.aplicar_filtro)
        self.ui.btnLimpiarBusqueda.clicked.connect(self.limpiar_busqueda)

        # Menús
        self.ui.actionNueva.triggered.connect(self.nueva_inscripcion)
        self.ui.actionListado.triggered.connect(self.mostrar_listado)
        self.ui.actionInicio.triggered.connect(self.mostrar_inicio)
        self.ui.actionSalir.triggered.connect(self.close)
        self.ui.actionAcercaDe.triggered.connect(self.mostrar_acerca_de)

        # Validación en vivo del formulario
        self.ui.txtNombre.textChanged.connect(self.actualizar_estado)
        self.ui.txtCorreo.textChanged.connect(self.actualizar_estado)
        self.ui.cmbCiclo.currentIndexChanged.connect(self.actualizar_estado)
        self.ui.cmbActividad.currentIndexChanged.connect(self.actualizar_estado)
        self.ui.txtObservaciones.textChanged.connect(self.actualizar_estado)
        self.ui.chkCondiciones.toggled.connect(self.actualizar_estado)

    # ------------------------------------------------------------------
    # Navegación entre páginas
    # ------------------------------------------------------------------
    def mostrar_inicio(self):
        self.ui.stackedPaginas.setCurrentWidget(self.ui.paginaInicio)
        self.statusBar().showMessage("Página de inicio")

    def mostrar_formulario(self):
        self.ui.stackedPaginas.setCurrentWidget(self.ui.paginaFormulario)
        self.statusBar().showMessage("Página de Formulario")

    def mostrar_resumen(self):
        self.ui.stackedPaginas.setCurrentWidget(self.ui.paginaResumen)
        self.statusBar().showMessage("Página de Resumen")

    def mostrar_listado(self):
        self.ui.stackedPaginas.setCurrentWidget(self.ui.paginaListado)
        self.refrescar_tabla()
        self.statusBar().showMessage("Página de Listado")

    # ------------------------------------------------------------------
    # Validación del formulario
    # ------------------------------------------------------------------
    def correo_valido(self, correo: str) -> bool:
        """Un correo debe tener texto, @ y dominio con al menos 2 caracteres."""
        return bool(EXPRESION_CORREO.match(correo))

    @staticmethod
    def nombre_valido(nombre: str) -> bool:
        """Un nombre no puede estar vacío ni contener números."""
        if not nombre:
            return False
        return not any(caracter.isdigit() for caracter in nombre)

    @staticmethod
    def mensaje_nombre_con_numeros(nombre: str) -> bool:
        """True si el nombre escrito contiene cifras (para avisar al usuario)."""
        return bool(nombre) and any(c.isdigit() for c in nombre)

    def formulario_valido(self) -> bool:
        nombre = self.ui.txtNombre.text().strip()
        correo = self.ui.txtCorreo.text().strip()
        ciclo_idx = self.ui.cmbCiclo.currentIndex()
        actividad_idx = self.ui.cmbActividad.currentIndex()
        condiciones = self.ui.chkCondiciones.isChecked()

        nombre_valido = self.nombre_valido(nombre)
        correo_valido = self.correo_valido(correo)
        ciclo_valido = ciclo_idx > 0  # Índice 0 es "Selecciona un ciclo"
        actividad_valida = actividad_idx > 0  # Índice 0 es "Selecciona una actividad"

        return (
                nombre_valido
                and correo_valido
                and ciclo_valido
                and actividad_valida
                and condiciones
        )

    def actualizar_estado(self):
        if self.formulario_valido():
            self.ui.btnRegistrar.setEnabled(True)
            self.ui.lblEstado.setText("Formulario preparado para registrar")
            self.statusBar().showMessage("Formulario preparado para registrar")
        else:
            self.ui.btnRegistrar.setEnabled(False)
            nombre = self.ui.txtNombre.text().strip()
            if self.mensaje_nombre_con_numeros(nombre):
                mensaje = (
                    "El nombre no puede contener números: "
                    "corrígielo (por ejemplo, «Lucía Torres»)"
                )
            else:
                mensaje = (
                    "Revisa los datos obligatorios (nombre, correo, ciclo, "
                    "actividad y condiciones)"
                )
            self.ui.lblEstado.setText(mensaje)
            self.statusBar().showMessage(mensaje)

    # ------------------------------------------------------------------
    # Recogida y presentación de datos
    # ------------------------------------------------------------------
    def obtener_datos(self) -> dict:
        modalidad = "Presencial" if self.ui.radioPresencial.isChecked() else "Online"
        material = "Sí" if self.ui.chkMaterial.isChecked() else "No"

        return {
            "nombre": self.ui.txtNombre.text().strip(),
            "correo": self.ui.txtCorreo.text().strip(),
            "ciclo": self.ui.cmbCiclo.currentText(),
            "actividad": self.ui.cmbActividad.currentText(),
            "fecha": self.ui.dateFecha.date().toString("dd/MM/yyyy"),
            "participantes": self.ui.spinParticipantes.value(),
            "modalidad": modalidad,
            "material": material,
            "observaciones": self.ui.txtObservaciones.toPlainText().strip(),
        }

    def actualizar_resumen(self, datos: dict):
        self.ui.lblResumenNombre.setText(datos["nombre"])
        self.ui.lblResumenCorreo.setText(datos["correo"])
        self.ui.lblResumenCiclo.setText(datos["ciclo"])
        self.ui.lblResumenActividad.setText(datos["actividad"])
        self.ui.lblResumenFecha.setText(str(datos["fecha"]))
        self.ui.lblResumenParticipantes.setText(str(datos["participantes"]))
        self.ui.lblResumenModalidad.setText(datos["modalidad"])
        self.ui.lblResumenMaterial.setText(datos["material"])
        self.ui.lblResumenObservaciones.setText(
            datos["observaciones"] or "Sin observaciones"
        )

    # ------------------------------------------------------------------
    # Alta y edición de inscripciones
    # ------------------------------------------------------------------
    def registrar(self):
        if not self.formulario_valido():
            nombre = self.ui.txtNombre.text().strip()
            if self.mensaje_nombre_con_numeros(nombre):
                texto_aviso = (
                    "El nombre no puede contener números. "
                    "Escríbelo solo con letras (y espacios o guiones)."
                )
            else:
                texto_aviso = (
                    "Revisa los datos obligatorios: nombre, correo con formato "
                    "válido, ciclo, actividad y condiciones aceptadas."
                )
            QMessageBox.warning(
                self,
                "Formulario incompleto",
                texto_aviso,
            )
            return

        datos = self.obtener_datos()

        # ---- Modo edición: actualiza el registro cargado, sin duplicar ----
        if self.indice_edicion is not None:
            self.inscripciones[self.indice_edicion] = datos
            indice = self.indice_edicion
            self.indice_edicion = None
            self.limpiar_formulario()
            self.mostrar_listado()
            self.ui.tablaInscripciones.selectRow(indice)
            QMessageBox.information(
                self,
                "Edición completada",
                f"La inscripción de {datos['nombre']} ha sido actualizada correctamente"
            )
            return

        # ---- Modo alta: pide confirmación y añade el registro ----
        respuesta = QMessageBox.question(
            self,
            "Confirmar inscripción",
            (
                f"¿Deseas registrar a "
                f"{datos['nombre']} en "
                f"{datos['actividad']}?"
            ),
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if respuesta != QMessageBox.StandardButton.Yes:
            return

        self.inscripciones.append(datos)
        self.actualizar_resumen(datos)
        self.limpiar_formulario()
        self.mostrar_resumen()

    def indice_real_de_fila(self, fila: int) -> int:
        """Devuelve el índice real en la lista interna de una fila de la tabla.

        La tabla puede estar filtrada, por eso el índice se guarda en el
        propio elemento de la tabla (rol UserRole) al construirla.
        """
        item = self.ui.tablaInscripciones.item(fila, 0)
        if item is None:
            return -1
        return item.data(Qt.ItemDataRole.UserRole)

    def editar_seleccion(self):
        fila = self.ui.tablaInscripciones.currentRow()

        # Sin selección, currentRow() devuelve -1: se avisa y no se hace nada
        if fila < 0:
            QMessageBox.warning(
                self,
                "Sin selección",
                "Selecciona una fila de la tabla antes de pulsar Editar."
            )
            return

        indice = self.indice_real_de_fila(fila)
        datos = self.inscripciones[indice]
        self.indice_edicion = indice

        # Se cargan TODOS los datos del registro en el formulario
        self.ui.txtNombre.setText(datos["nombre"])
        self.ui.txtCorreo.setText(datos["correo"])
        self.ui.cmbCiclo.setCurrentText(datos["ciclo"])
        self.ui.cmbActividad.setCurrentText(datos["actividad"])

        fecha = QDate.fromString(datos["fecha"], "dd/MM/yyyy")
        if fecha.isValid():
            self.ui.dateFecha.setDate(fecha)

        self.ui.spinParticipantes.setValue(datos["participantes"])

        if datos["modalidad"] == "Presencial":
            self.ui.radioPresencial.setChecked(True)
        else:
            self.ui.radioOnline.setChecked(True)

        self.ui.chkMaterial.setChecked(datos.get("material") == "Sí")
        self.ui.txtObservaciones.setPlainText(datos["observaciones"])
        # Una inscripción guardada tuvo que aceptar las condiciones
        self.ui.chkCondiciones.setChecked(True)

        self.ui.lblTituloFormulario.setText("Editar inscripción")
        self.ui.lblSubtitulo.setText(
            f"Modificando el registro de {datos['nombre']}"
        )
        self.ui.btnRegistrar.setText("Guardar cambios")
        self.actualizar_estado()
        self.mostrar_formulario()

    def eliminar_seleccion(self):
        fila = self.ui.tablaInscripciones.currentRow()

        # Sin selección no se elimina nada (evita borrar la fila equivocada)
        if fila < 0:
            QMessageBox.warning(
                self,
                "Sin selección",
                "Selecciona una fila de la tabla antes de pulsar Eliminar."
            )
            return

        indice = self.indice_real_de_fila(fila)
        nombre = self.inscripciones[indice]["nombre"]

        respuesta = QMessageBox.question(
            self,
            "Confirmar eliminación",
            f"¿Deseas eliminar la inscripción de {nombre}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if respuesta != QMessageBox.StandardButton.Yes:
            return

        del self.inscripciones[indice]

        # Si se estaba editando ese registro, se cancela la edición
        if self.indice_edicion == indice:
            self.indice_edicion = None

        self.refrescar_tabla()
        QMessageBox.information(
            self,
            "Eliminación completada",
            f"La inscripción de {nombre} ha sido eliminada correctamente"
        )

    # ------------------------------------------------------------------
    # Listado, búsqueda y filtro
    # ------------------------------------------------------------------
    def inscripciones_filtradas(self):
        """Lista de registros que cumplen el filtro activo del buscador."""
        texto = self.ui.txtBuscar.text().strip().lower()
        if not texto:
            return list(self.inscripciones)

        return [
            inscripcion
            for inscripcion in self.inscripciones
            if texto in inscripcion["nombre"].lower()
            or texto in inscripcion["correo"].lower()
            or texto in inscripcion["actividad"].lower()
        ]

    def refrescar_tabla(self):
        filtradas = self.inscripciones_filtradas()

        self.ui.tablaInscripciones.setRowCount(0)

        for inscripcion in filtradas:
            # El índice real en la lista interna viaja en el primer item
            indice_real = self.inscripciones.index(inscripcion)

            fila = self.ui.tablaInscripciones.rowCount()
            self.ui.tablaInscripciones.insertRow(fila)

            item_nombre = QTableWidgetItem(inscripcion["nombre"])
            item_nombre.setData(Qt.ItemDataRole.UserRole, indice_real)
            self.ui.tablaInscripciones.setItem(fila, 0, item_nombre)
            self.ui.tablaInscripciones.setItem(
                fila, 1, QTableWidgetItem(inscripcion["correo"])
            )
            self.ui.tablaInscripciones.setItem(
                fila, 2, QTableWidgetItem(inscripcion["ciclo"])
            )
            self.ui.tablaInscripciones.setItem(
                fila, 3, QTableWidgetItem(inscripcion["actividad"])
            )
            self.ui.tablaInscripciones.setItem(
                fila, 4, QTableWidgetItem(inscripcion["fecha"])
            )
            self.ui.tablaInscripciones.setItem(
                fila, 5, QTableWidgetItem(str(inscripcion["participantes"]))
            )
            self.ui.tablaInscripciones.setItem(
                fila, 6, QTableWidgetItem(inscripcion["modalidad"])
            )

        self.actualizar_contador(filtradas)

    def actualizar_contador(self, filtradas):
        total = len(filtradas)
        # Singular / plural correcto según la cantidad mostrada
        sustantivo = "inscripción" if total == 1 else "inscripciones"
        self.ui.lblContadorListado.setText(f"Total: {total} {sustantivo}")

    def aplicar_filtro(self):
        self.refrescar_tabla()

    def limpiar_busqueda(self):
        self.ui.txtBuscar.clear()
        self.refrescar_tabla()

    # ------------------------------------------------------------------
    # Utilidades del formulario
    # ------------------------------------------------------------------
    def limpiar_formulario(self):
        self.ui.txtNombre.clear()
        self.ui.txtCorreo.clear()
        self.ui.cmbCiclo.setCurrentIndex(0)
        self.ui.cmbActividad.setCurrentIndex(0)
        self.ui.dateFecha.setDate(QDate.currentDate())
        self.ui.spinParticipantes.setValue(1)
        self.ui.radioPresencial.setChecked(True)
        self.ui.chkMaterial.setChecked(False)
        self.ui.txtObservaciones.clear()
        self.ui.chkCondiciones.setChecked(False)

        self.indice_edicion = None
        self.ui.lblTituloFormulario.setText("Formulario de matrícula")
        self.ui.lblSubtitulo.setText("Completa los datos para continuar")
        self.ui.btnRegistrar.setText("Guardar")

        self.actualizar_estado()

    def nueva_inscripcion(self):
        self.limpiar_formulario()
        self.mostrar_formulario()

    def mostrar_acerca_de(self):
        QMessageBox.about(
            self,
            "Acerca de",
            "Gestor de actividades formativas\n\n"
            "Aplicación desarrollada en Python con PySide6.\n"
            "Permite gestionar la matrícula de alumnado en actividades del centro."
        )

    # ------------------------------------------------------------------
    # Atajos de teclado (accesibilidad)
    # ------------------------------------------------------------------
    def keyPressEvent(self, event):
        """Esc cancela la edición en curso y vuelve al listado."""
        if (event.key() == Qt.Key.Key_Escape
                and self.indice_edicion is not None):
            self.indice_edicion = None
            self.limpiar_formulario()
            self.mostrar_listado()
            self.statusBar().showMessage("Edición cancelada", 3000)
            return
        super().keyPressEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = VentanaPrincipal()
    ventana.show()

    sys.exit(app.exec())
