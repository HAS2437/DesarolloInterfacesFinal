# -*- coding: utf-8 -*-
"""
Batería de pruebas funcionales del Gestor de Actividades Formativas.

Ejecuta sobre la aplicación real (sin pantalla) los casos de prueba de la
matriz de la UD1. Cada caso indica si se SUPERADA / NO SUPERADA y el motivo.

Uso:  py pruebas_funcionales.py
Salida: tabla por pantalla y archivo resultados_pruebas.json
"""

import json
import os
import sys
import traceback

# La aplicación se ejecuta sin pantalla para poder automatizar las pruebas.
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PySide6.QtCore import QDate                              # noqa: E402
from PySide6.QtWidgets import QApplication, QMessageBox      # noqa: E402

import main as modulo_main                                    # noqa: E402


# ----------------------------------------------------------------------
# Doble de QMessageBox: registra los mensajes y responde automáticamente.
# Permite probar la lógica sin ventanas modales reales.
# ----------------------------------------------------------------------
class DobleMensajes:
    StandardButton = QMessageBox.StandardButton

    registros = []   # [(tipo, titulo, texto), ...]
    respuestas = []  # respuestas en cola para question(); por defecto Yes

    @classmethod
    def limpiar(cls):
        cls.registros.clear()
        cls.respuestas.clear()

    @classmethod
    def information(cls, parent, titulo, texto, *args, **kwargs):
        cls.registros.append(("information", titulo, texto))
        return cls.StandardButton.Ok

    @classmethod
    def warning(cls, parent, titulo, texto, *args, **kwargs):
        cls.registros.append(("warning", titulo, texto))
        return cls.StandardButton.Ok

    @classmethod
    def about(cls, parent, titulo, texto, *args, **kwargs):
        cls.registros.append(("about", titulo, texto))

    @classmethod
    def question(cls, parent, titulo, texto, *args, **kwargs):
        cls.registros.append(("question", titulo, texto))
        if cls.respuestas:
            return cls.respuestas.pop(0)
        return cls.StandardButton.Yes


modulo_main.QMessageBox = DobleMensajes  # la app usa este nombre importado


# ----------------------------------------------------------------------
# Utilidades de preparación
# ----------------------------------------------------------------------
def nueva_ventana():
    """Crea una ventana limpia y registra los mensajes que produzca."""
    DobleMensajes.limpiar()
    return modulo_main.VentanaPrincipal()


def rellenar_formulario(ventana, nombre="Lucía Prueba", correo="lucia@prueba.com",
                        ciclo=1, actividad=1, condiciones=True):
    """Completa el formulario con datos válidos."""
    ventana.ui.txtNombre.setText(nombre)
    ventana.ui.txtCorreo.setText(correo)
    ventana.ui.cmbCiclo.setCurrentIndex(ciclo)
    ventana.ui.cmbActividad.setCurrentIndex(actividad)
    ventana.ui.chkCondiciones.setChecked(condiciones)


def sembrar(ventana, cantidad=3):
    """Inserta inscripciones de prueba directamente en la lista interna."""
    nombres = ["Ana Torres", "Bruno Diaz", "Carla Ruiz"]
    for i in range(cantidad):
        ventana.inscripciones.append({
            "nombre": nombres[i],
            "correo": f"persona{i}@centro.es",
            "ciclo": "Desarrollo de Aplicaciones Multiplataforma",
            "actividad": "Desarrollo de Interfaces",
            "fecha": "23/10/2026",
            "participantes": 1,
            "modalidad": "Presencial",
            "material": "No",
            "observaciones": "",
        })
    ventana.refrescar_tabla()


def mensajes_de_tipo(tipo):
    return [r for r in DobleMensajes.registros if r[0] == tipo]


def texto_de_ultimo_mensaje():
    if not DobleMensajes.registros:
        return ""
    return DobleMensajes.registros[-1][2]


# ----------------------------------------------------------------------
# Casos de prueba
# ----------------------------------------------------------------------
def PF01_ejecucion_inicial():
    """La aplicación se abre sin errores desde main.py."""
    ventana = nueva_ventana()
    paginas = ventana.ui.stackedPaginas.count()
    visible = ventana.ui.stackedPaginas.currentWidget()
    ok = (paginas == 4 and visible is ventana.ui.paginaInicio)
    return ok, (
        f"Ventana creada con {paginas} páginas; "
        f"página visible al arrancar: {visible.objectName()}"
    )


def PF02_navegacion_completa():
    """Todas las páginas son accesibles y se puede volver al inicio."""
    ventana = nueva_ventana()
    recorrido = []

    ventana.ui.btnComenzar.click()
    recorrido.append(ventana.ui.stackedPaginas.currentWidget().objectName())

    ventana.ui.actionListado.trigger()
    recorrido.append(ventana.ui.stackedPaginas.currentWidget().objectName())

    ventana.ui.btnInicioListado.click()
    recorrido.append(ventana.ui.stackedPaginas.currentWidget().objectName())

    ventana.mostrar_resumen()
    recorrido.append(ventana.ui.stackedPaginas.currentWidget().objectName())

    esperado = ["paginaFormulario", "paginaListado", "paginaInicio", "paginaResumen"]
    return recorrido == esperado, f"Secuencia recorrida: {' -> '.join(recorrido)}"


def PF03_alta_con_datos_validos():
    """Alta completa: se crea, aparece en la tabla y se informa al usuario."""
    ventana = nueva_ventana()
    rellenar_formulario(ventana)
    ventana.ui.btnRegistrar.setEnabled(ventana.formulario_valido())
    ventana.registrar()

    creada = len(ventana.inscripciones) == 1
    confirmacion = len(mensajes_de_tipo("question")) == 1
    en_resumen = ventana.ui.stackedPaginas.currentWidget() is ventana.ui.paginaResumen

    # Tras el alta, "Nueva Inscripción" deja el formulario listo y limpio
    ventana.ui.btnNueva.click()
    formulario_limpio = (
        ventana.ui.txtNombre.text() == ""
        and ventana.ui.cmbCiclo.currentIndex() == 0
        and ventana.ui.chkCondiciones.isChecked() is False
    )

    ventana.mostrar_listado()
    aparece_en_tabla = (
        ventana.ui.tablaInscripciones.rowCount() == 1
        and ventana.ui.tablaInscripciones.item(0, 0).text() == "Lucía Prueba"
    )

    ok = creada and confirmacion and en_resumen and formulario_limpio and aparece_en_tabla
    return ok, (
        f"Registro creado: {creada}; confirmación mostrada: {confirmacion}; "
        f"resumen visible: {en_resumen}; formulario limpio tras alta: {formulario_limpio}; "
        f"aparece en la tabla: {aparece_en_tabla}"
    )


def PF04_campo_obligatorio_vacio():
    """Con un campo obligatorio vacío no se guarda y se explica el motivo."""
    ventana = nueva_ventana()
    rellenar_formulario(ventana, nombre="   ")  # nombre en blanco
    ventana.actualizar_estado()

    boton_desactivado = not ventana.ui.btnRegistrar.isEnabled()
    mensaje = ventana.ui.lblEstado.text()
    etiqueta_identifica = "Revisa" in mensaje

    # Aunque se intente forzar el guardado, no debe registrarse nada
    ventana.registrar()
    no_guardado = len(ventana.inscripciones) == 0

    ok = boton_desactivado and etiqueta_identifica and no_guardado
    return ok, (
        f"Botón Guardar desactivado: {boton_desactivado}; "
        f"mensaje mostrado: '{mensaje}'; registro no guardado: {no_guardado}"
    )


def PF05_formato_incorrecto():
    """Un correo con formato incorrecto debe detectarse y no guardarse."""
    ventana = nueva_ventana()
    rellenar_formulario(ventana, correo="alumno@centro")  # falta el dominio
    ventana.actualizar_estado()

    detectado = not ventana.ui.btnRegistrar.isEnabled()

    ventana.registrar()
    no_guardado = len(ventana.inscripciones) == 0

    ok = detectado and no_guardado
    return ok, (
        f"Correo 'alumno@centro' detectado como inválido: {detectado}; "
        f"registro no guardado: {no_guardado}"
    )


def PF06_busqueda_con_coincidencias():
    """La búsqueda solo muestra las coincidencias."""
    ventana = nueva_ventana()
    sembrar(ventana)
    ventana.ui.txtBuscar.setText("ana")  # "Ana Torres" pero no "Bruno Diaz"

    filas = ventana.ui.tablaInscripciones.rowCount()
    nombre = ventana.ui.tablaInscripciones.item(0, 0).text()
    contador = ventana.ui.lblContadorListado.text()

    ok = filas == 1 and nombre == "Ana Torres"
    return ok, (
        f"Filtro 'ana' -> {filas} fila(s) ('{nombre}'); contador: '{contador}'"
    )


def PF07_busqueda_sin_coincidencias():
    """Sin coincidencias: tabla vacía, sin bloqueos y con información."""
    ventana = nueva_ventana()
    sembrar(ventana)
    ventana.mostrar_listado()
    ventana.ui.txtBuscar.setText("zzznoexiste")

    filas = ventana.ui.tablaInscripciones.rowCount()
    contador = ventana.ui.lblContadorListado.text()
    sigue_funcionando = ventana.ui.stackedPaginas.currentWidget() is ventana.ui.paginaListado

    ok = filas == 0 and sigue_funcionando and "0" in contador
    return ok, (
        f"Filtro sin coincidencias -> {filas} filas; contador: '{contador}'; "
        f"la aplicación sigue operativa: {sigue_funcionando}"
    )


def PF08_restauracion_del_listado():
    """Borrar el buscador restaura todos los registros."""
    ventana = nueva_ventana()
    sembrar(ventana)
    ventana.ui.txtBuscar.setText("ana")
    filtradas = ventana.ui.tablaInscripciones.rowCount()

    ventana.ui.btnLimpiarBusqueda.click()
    restauradas = ventana.ui.tablaInscripciones.rowCount()
    contador = ventana.ui.lblContadorListado.text()

    ok = filtradas == 1 and restauradas == 3
    return ok, (
        f"Con filtro: {filtradas} fila; tras limpiar búsqueda: {restauradas} filas; "
        f"contador: '{contador}'"
    )


def PF09_edicion_con_seleccion():
    """Editar una fila seleccionada actualiza el mismo registro, sin duplicados."""
    ventana = nueva_ventana()
    sembrar(ventana)
    ventana.mostrar_listado()
    ventana.ui.tablaInscripciones.selectRow(0)

    ventana.editar_seleccion()
    en_formulario = ventana.ui.stackedPaginas.currentWidget() is ventana.ui.paginaFormulario
    cargado = ventana.ui.txtNombre.text() == "Ana Torres"

    ventana.ui.txtNombre.setText("Ana Torres Editada")
    ventana.actualizar_estado()
    ventana.registrar()  # respuesta del doble: Yes

    sin_duplicados = len(ventana.inscripciones) == 3
    actualizada = ventana.inscripciones[0]["nombre"] == "Ana Torres Editada"
    informa = any("actualizada" in r[2].lower() or "confirmar" in r[1].lower()
                  for r in DobleMensajes.registros)

    ok = en_formulario and cargado and sin_duplicados and actualizada and informa
    return ok, (
        f"Formulario abierto: {en_formulario}; datos cargados: {cargado}; "
        f"registros tras guardar (sin duplicar): {len(ventana.inscripciones)}; "
        f"primera fila actualizada: {actualizada}; informa al usuario: {informa}"
    )


def PF10_edicion_sin_seleccion():
    """Editar sin seleccionar fila debe avisar y no tocar ningún registro."""
    ventana = nueva_ventana()
    sembrar(ventana)
    ventana.mostrar_listado()
    # Sin selección: currentRow() == -1

    ventana.editar_seleccion()

    aviso = len(mensajes_de_tipo("warning")) > 0
    sin_cambios = all(i["nombre"] in ("Ana Torres", "Bruno Diaz", "Carla Ruiz")
                      for i in ventana.inscripciones)
    sigue_en_listado = ventana.ui.stackedPaginas.currentWidget() is ventana.ui.paginaListado

    ok = aviso and sin_cambios and sigue_en_listado
    return ok, (
        f"Aviso mostrado: {aviso}; ningún registro modificado: {sin_cambios}; "
        f"permanece en el listado: {sigue_en_listado}"
    )


def PF11_eliminacion_cancelada():
    """Cancelar la confirmación no elimina nada."""
    ventana = nueva_ventana()
    sembrar(ventana)
    ventana.mostrar_listado()
    ventana.ui.tablaInscripciones.selectRow(1)

    DobleMensajes.respuestas.append(DobleMensajes.StandardButton.No)
    ventana.eliminar_seleccion()

    ok = len(ventana.inscripciones) == 3
    return ok, f"Registros tras cancelar: {len(ventana.inscripciones)} (esperados 3)"


def PF12_eliminacion_confirmada():
    """Confirmar la eliminación quita el registro y actualiza la tabla."""
    ventana = nueva_ventana()
    sembrar(ventana)
    ventana.mostrar_listado()
    ventana.ui.tablaInscripciones.selectRow(1)  # Bruno Diaz

    DobleMensajes.respuestas.append(DobleMensajes.StandardButton.Yes)
    ventana.eliminar_seleccion()

    quedan = len(ventana.inscripciones)
    nombres = [i["nombre"] for i in ventana.inscripciones]
    filas_tabla = ventana.ui.tablaInscripciones.rowCount()
    informa = len(mensajes_de_tipo("information")) > 0

    ok = quedan == 2 and "Bruno Diaz" not in nombres and filas_tabla == 2 and informa
    return ok, (
        f"Registros restantes: {quedan}; nombres: {nombres}; "
        f"filas en tabla: {filas_tabla}; mensaje de confirmación: {informa}"
    )


def PF13_operaciones_con_filtro_activo():
    """Editar o eliminar con el filtro activo debe afectar al registro correcto."""
    ventana = nueva_ventana()
    sembrar(ventana)  # Ana Torres, Bruno Diaz, Carla Ruiz
    ventana.mostrar_listado()
    ventana.ui.txtBuscar.setText("carla")  # solo queda Carla Ruiz (fila 0 de la tabla)
    ventana.ui.tablaInscripciones.selectRow(0)

    DobleMensajes.respuestas.append(DobleMensajes.StandardButton.Yes)
    ventana.eliminar_seleccion()

    nombres = [i["nombre"] for i in ventana.inscripciones]
    ok = nombres == ["Ana Torres", "Bruno Diaz"]
    return ok, (
        f"Con filtro 'carla' se eliminó la fila 0 de la tabla; "
        f"registros restantes: {nombres}"
    )


def PF14_limites_del_spinbox():
    """El contador de participantes respeta sus límites."""
    ventana = nueva_ventana()
    spin = ventana.ui.spinParticipantes

    spin.setValue(0)
    minimo = spin.value()
    spin.setValue(999)
    maximo = spin.value()
    spin.setValue(1)

    ok = minimo == 1 and maximo == 30
    return ok, f"Valor mínimo permitido: {minimo}; valor máximo permitido: {maximo}"


def PF15_navegacion_por_teclado():
    """El foco recorre los campos en orden y Intro activa Guardar."""
    ventana = nueva_ventana()
    ventana.mostrar_formulario()

    ventana.ui.txtNombre.setFocus()
    ventana.focusNextChild()
    foco_tras_tab = ventana.focusWidget()

    orden_ok = foco_tras_tab is ventana.ui.txtCorreo

    # La tecla Intro debe activar el botón Guardar (botón por defecto)
    rellenar_formulario(ventana)
    ventana.actualizar_estado()
    intro_guarda = ventana.ui.btnRegistrar.isDefault()

    ok = orden_ok and intro_guarda
    return ok, (
        f"Tras Tab desde Nombre el foco va a {foco_tras_tab.objectName() if foco_tras_tab else 'ninguno'}; "
        f"Intro activa Guardar (botón por defecto): {intro_guarda}"
    )


def PF16_redimensionado_y_titulo():
    """La ventana identifica la aplicación y no se encoge hasta hacerse inservible."""
    ventana = nueva_ventana()
    titulo = ventana.windowTitle()
    minimo = ventana.minimumSize()

    titulo_ok = titulo == "Gestor de Actividades Formativas"
    minimo_ok = minimo.width() >= 600 and minimo.height() >= 480

    ok = titulo_ok and minimo_ok
    return ok, (
        f"Título de la ventana: '{titulo}'; tamaño mínimo: "
        f"{minimo.width()}x{minimo.height()}"
    )


def PF17_esc_cancela_edicion():
    """La tecla Esc cancela la edición y vuelve al listado sin tocar datos."""
    ventana = nueva_ventana()
    sembrar(ventana)
    ventana.mostrar_listado()
    ventana.ui.tablaInscripciones.selectRow(0)
    ventana.editar_seleccion()
    en_edicion = ventana.indice_edicion == 0

    from PySide6.QtCore import QEvent, Qt
    from PySide6.QtGui import QKeyEvent
    evento = QKeyEvent(QEvent.Type.KeyPress, Qt.Key_Escape,
                       Qt.KeyboardModifier.NoModifier)
    ventana.keyPressEvent(evento)

    cancelada = ventana.indice_edicion is None
    en_listado = ventana.ui.stackedPaginas.currentWidget() is ventana.ui.paginaListado
    sin_cambios = ventana.inscripciones[0]["nombre"] == "Ana Torres"

    ok = en_edicion and cancelada and en_listado and sin_cambios
    return ok, (
        f"Modo edición activado: {en_edicion}; edición cancelada con Esc: {cancelada}; "
        f"vuelve al listado: {en_listado}; registro intacto: {sin_cambios}"
    )


def PF18_nombre_con_numeros():
    """Un nombre que contiene números no debe dejar guardar ni crear registro."""
    ventana = nueva_ventana()
    rellenar_formulario(ventana, nombre="Lucía 123")
    ventana.actualizar_estado()

    boton_desactivado = not ventana.ui.btnRegistrar.isEnabled()

    # Se intenta guardar igual (llamada directa, como haría Intro)
    ventana.registrar()

    aviso = "número" in texto_de_ultimo_mensaje().lower()
    sin_registro = len(ventana.inscripciones) == 0

    ok = boton_desactivado and aviso and sin_registro
    return ok, (
        f"Guardar desactivado con nombre numérico: {boton_desactivado}; "
        f"aviso específico sobre números: {aviso}; "
        f"ningún registro creado: {sin_registro}"
    )


PRUEBAS = [
    ("PF01", "Inicio", PF01_ejecucion_inicial),
    ("PF02", "Navegación", PF02_navegacion_completa),
    ("PF03", "Alta válida", PF03_alta_con_datos_validos),
    ("PF04", "Validación", PF04_campo_obligatorio_vacio),
    ("PF05", "Validación", PF05_formato_incorrecto),
    ("PF06", "Búsqueda", PF06_busqueda_con_coincidencias),
    ("PF07", "Búsqueda", PF07_busqueda_sin_coincidencias),
    ("PF08", "Búsqueda", PF08_restauracion_del_listado),
    ("PF09", "Edición", PF09_edicion_con_seleccion),
    ("PF10", "Edición", PF10_edicion_sin_seleccion),
    ("PF11", "Eliminación", PF11_eliminacion_cancelada),
    ("PF12", "Eliminación", PF12_eliminacion_confirmada),
    ("PF13", "Edición/Eliminación con filtro", PF13_operaciones_con_filtro_activo),
    ("PF14", "Formulario", PF14_limites_del_spinbox),
    ("PF15", "Teclado", PF15_navegacion_por_teclado),
    ("PF16", "Redimensionado", PF16_redimensionado_y_titulo),
    ("PF17", "Teclado (Esc)", PF17_esc_cancela_edicion),
    ("PF18", "Validación (nombre)", PF18_nombre_con_numeros),
]


def ejecutar_todas():
    app = QApplication.instance() or QApplication(sys.argv)
    resultados = []

    print("=" * 100)
    print("MATRIZ DE PRUEBAS FUNCIONALES - Gestor de Actividades Formativas")
    print("=" * 100)

    for codigo, funcion, funcion_prueba in PRUEBAS:
        try:
            ok, detalle = funcion_prueba()
            estado = "SUPERADA" if ok else "NO SUPERADA"
        except Exception:
            ok = False
            estado = "NO SUPERADA"
            detalle = "Excepción: " + traceback.format_exc(limit=1).strip().replace(
                "\n", " | "
            )

        resultados.append({
            "id": codigo,
            "funcionalidad": funcion,
            "estado": estado,
            "detalle": detalle,
        })
        marca = "OK " if ok else "XX "
        print(f"[{marca}] {codigo} ({funcion}): {detalle}")

    superadas = sum(1 for r in resultados if r["estado"] == "SUPERADA")
    print("-" * 100)
    print(f"RESULTADO: {superadas}/{len(resultados)} pruebas superadas")

    salida = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          "resultados_pruebas.json")
    with open(salida, "w", encoding="utf-8") as fh:
        json.dump(resultados, fh, ensure_ascii=False, indent=2)
    print(f"Detalle guardado en: {salida}")

    return resultados


if __name__ == "__main__":
    ejecutar_todas()
