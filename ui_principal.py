# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'principal.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QDateEdit, QFormLayout, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStackedWidget, QStatusBar, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_VentanaPrincipal(object):
    def setupUi(self, VentanaPrincipal):
        if not VentanaPrincipal.objectName():
            VentanaPrincipal.setObjectName(u"VentanaPrincipal")
        VentanaPrincipal.resize(860, 640)
        VentanaPrincipal.setMinimumSize(QSize(640, 520))
        self.actionNueva = QAction(VentanaPrincipal)
        self.actionNueva.setObjectName(u"actionNueva")
        self.actionListado = QAction(VentanaPrincipal)
        self.actionListado.setObjectName(u"actionListado")
        self.actionInicio = QAction(VentanaPrincipal)
        self.actionInicio.setObjectName(u"actionInicio")
        self.actionSalir = QAction(VentanaPrincipal)
        self.actionSalir.setObjectName(u"actionSalir")
        self.actionAcercaDe = QAction(VentanaPrincipal)
        self.actionAcercaDe.setObjectName(u"actionAcercaDe")
        self.centralwidget = QWidget(VentanaPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.stackedPaginas = QStackedWidget(self.centralwidget)
        self.stackedPaginas.setObjectName(u"stackedPaginas")
        self.paginaInicio = QWidget()
        self.paginaInicio.setObjectName(u"paginaInicio")
        self.horizontalLayout_3 = QHBoxLayout(self.paginaInicio)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.LayoutInicio = QVBoxLayout()
        self.LayoutInicio.setObjectName(u"LayoutInicio")
        self.verticalSpacerSuperior = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.LayoutInicio.addItem(self.verticalSpacerSuperior)

        self.lblTituloInicio = QLabel(self.paginaInicio)
        self.lblTituloInicio.setObjectName(u"lblTituloInicio")
        self.lblTituloInicio.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.LayoutInicio.addWidget(self.lblTituloInicio)

        self.lblDescripcionInicio = QLabel(self.paginaInicio)
        self.lblDescripcionInicio.setObjectName(u"lblDescripcionInicio")
        self.lblDescripcionInicio.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.LayoutInicio.addWidget(self.lblDescripcionInicio)

        self.btnComenzar = QPushButton(self.paginaInicio)
        self.btnComenzar.setObjectName(u"btnComenzar")

        self.LayoutInicio.addWidget(self.btnComenzar)

        self.verticalSpacerInferior = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.LayoutInicio.addItem(self.verticalSpacerInferior)


        self.horizontalLayout_3.addLayout(self.LayoutInicio)

        self.stackedPaginas.addWidget(self.paginaInicio)
        self.paginaFormulario = QWidget()
        self.paginaFormulario.setObjectName(u"paginaFormulario")
        self.verticalLayout_2 = QVBoxLayout(self.paginaFormulario)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lblTituloFormulario = QLabel(self.paginaFormulario)
        self.lblTituloFormulario.setObjectName(u"lblTituloFormulario")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lblTituloFormulario.setFont(font)
        self.lblTituloFormulario.setCursor(QCursor(Qt.CursorShape.UpArrowCursor))

        self.verticalLayout_2.addWidget(self.lblTituloFormulario)

        self.lblSubtitulo = QLabel(self.paginaFormulario)
        self.lblSubtitulo.setObjectName(u"lblSubtitulo")

        self.verticalLayout_2.addWidget(self.lblSubtitulo)

        self.formLayoutDatos = QFormLayout()
        self.formLayoutDatos.setObjectName(u"formLayoutDatos")
        self.formLayoutDatos.setVerticalSpacing(6)
        self.lblNombre = QLabel(self.paginaFormulario)
        self.lblNombre.setObjectName(u"lblNombre")

        self.formLayoutDatos.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblNombre)

        self.txtNombre = QLineEdit(self.paginaFormulario)
        self.txtNombre.setObjectName(u"txtNombre")

        self.formLayoutDatos.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtNombre)

        self.lblCorreo = QLabel(self.paginaFormulario)
        self.lblCorreo.setObjectName(u"lblCorreo")

        self.formLayoutDatos.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblCorreo)

        self.txtCorreo = QLineEdit(self.paginaFormulario)
        self.txtCorreo.setObjectName(u"txtCorreo")

        self.formLayoutDatos.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtCorreo)

        self.dateFecha = QDateEdit(self.paginaFormulario)
        self.dateFecha.setObjectName(u"dateFecha")
        self.dateFecha.setCalendarPopup(True)

        self.formLayoutDatos.setWidget(5, QFormLayout.ItemRole.FieldRole, self.dateFecha)

        self.lblFecha = QLabel(self.paginaFormulario)
        self.lblFecha.setObjectName(u"lblFecha")

        self.formLayoutDatos.setWidget(5, QFormLayout.ItemRole.LabelRole, self.lblFecha)

        self.spinParticipantes = QSpinBox(self.paginaFormulario)
        self.spinParticipantes.setObjectName(u"spinParticipantes")
        self.spinParticipantes.setMinimum(1)
        self.spinParticipantes.setMaximum(30)

        self.formLayoutDatos.setWidget(6, QFormLayout.ItemRole.FieldRole, self.spinParticipantes)

        self.lblParticipantes = QLabel(self.paginaFormulario)
        self.lblParticipantes.setObjectName(u"lblParticipantes")

        self.formLayoutDatos.setWidget(6, QFormLayout.ItemRole.LabelRole, self.lblParticipantes)

        self.lblCiclo = QLabel(self.paginaFormulario)
        self.lblCiclo.setObjectName(u"lblCiclo")

        self.formLayoutDatos.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblCiclo)

        self.cmbCiclo = QComboBox(self.paginaFormulario)
        self.cmbCiclo.addItem("")
        self.cmbCiclo.addItem("")
        self.cmbCiclo.addItem("")
        self.cmbCiclo.addItem("")
        self.cmbCiclo.addItem("")
        self.cmbCiclo.setObjectName(u"cmbCiclo")

        self.formLayoutDatos.setWidget(2, QFormLayout.ItemRole.FieldRole, self.cmbCiclo)

        self.lblActividad = QLabel(self.paginaFormulario)
        self.lblActividad.setObjectName(u"lblActividad")

        self.formLayoutDatos.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblActividad)

        self.cmbActividad = QComboBox(self.paginaFormulario)
        self.cmbActividad.addItem("")
        self.cmbActividad.addItem("")
        self.cmbActividad.addItem("")
        self.cmbActividad.addItem("")
        self.cmbActividad.addItem("")
        self.cmbActividad.addItem("")
        self.cmbActividad.setObjectName(u"cmbActividad")

        self.formLayoutDatos.setWidget(3, QFormLayout.ItemRole.FieldRole, self.cmbActividad)


        self.verticalLayout_2.addLayout(self.formLayoutDatos)

        self.groupModalidad = QFrame(self.paginaFormulario)
        self.groupModalidad.setObjectName(u"groupModalidad")
        self.groupModalidad.setFrameShape(QFrame.Shape.StyledPanel)
        self.groupModalidad.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.groupModalidad)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioPresencial = QRadioButton(self.groupModalidad)
        self.radioPresencial.setObjectName(u"radioPresencial")

        self.horizontalLayout.addWidget(self.radioPresencial)

        self.layoutModalidad = QHBoxLayout()
        self.layoutModalidad.setObjectName(u"layoutModalidad")
        self.radioOnline = QRadioButton(self.groupModalidad)
        self.radioOnline.setObjectName(u"radioOnline")

        self.layoutModalidad.addWidget(self.radioOnline)


        self.horizontalLayout.addLayout(self.layoutModalidad)


        self.verticalLayout_2.addWidget(self.groupModalidad)

        self.chkMaterial = QCheckBox(self.paginaFormulario)
        self.chkMaterial.setObjectName(u"chkMaterial")

        self.verticalLayout_2.addWidget(self.chkMaterial)

        self.txtObservaciones = QPlainTextEdit(self.paginaFormulario)
        self.txtObservaciones.setObjectName(u"txtObservaciones")

        self.verticalLayout_2.addWidget(self.txtObservaciones)

        self.chkCondiciones = QCheckBox(self.paginaFormulario)
        self.chkCondiciones.setObjectName(u"chkCondiciones")

        self.verticalLayout_2.addWidget(self.chkCondiciones)

        self.lblEstado = QLabel(self.paginaFormulario)
        self.lblEstado.setObjectName(u"lblEstado")

        self.verticalLayout_2.addWidget(self.lblEstado)

        self.layoutBotonesFormulario = QHBoxLayout()
        self.layoutBotonesFormulario.setObjectName(u"layoutBotonesFormulario")
        self.horizontalSpacer = QSpacerItem(208, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layoutBotonesFormulario.addItem(self.horizontalSpacer)

        self.btnLimpiar = QPushButton(self.paginaFormulario)
        self.btnLimpiar.setObjectName(u"btnLimpiar")

        self.layoutBotonesFormulario.addWidget(self.btnLimpiar)

        self.btnRegistrar = QPushButton(self.paginaFormulario)
        self.btnRegistrar.setObjectName(u"btnRegistrar")
        self.btnRegistrar.setEnabled(False)

        self.layoutBotonesFormulario.addWidget(self.btnRegistrar)


        self.verticalLayout_2.addLayout(self.layoutBotonesFormulario)

        self.stackedPaginas.addWidget(self.paginaFormulario)
        self.paginaResumen = QWidget()
        self.paginaResumen.setObjectName(u"paginaResumen")
        self.verticalLayout = QVBoxLayout(self.paginaResumen)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayoutResumen = QFormLayout()
        self.formLayoutResumen.setObjectName(u"formLayoutResumen")
        self.lblResumenNombre = QLabel(self.paginaResumen)
        self.lblResumenNombre.setObjectName(u"lblResumenNombre")

        self.formLayoutResumen.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblResumenNombre)

        self.lblResumenCorreo = QLabel(self.paginaResumen)
        self.lblResumenCorreo.setObjectName(u"lblResumenCorreo")

        self.formLayoutResumen.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblResumenCorreo)

        self.lblResumenCiclo = QLabel(self.paginaResumen)
        self.lblResumenCiclo.setObjectName(u"lblResumenCiclo")

        self.formLayoutResumen.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblResumenCiclo)

        self.lblResumenActividad = QLabel(self.paginaResumen)
        self.lblResumenActividad.setObjectName(u"lblResumenActividad")

        self.formLayoutResumen.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblResumenActividad)

        self.lblResumenFecha = QLabel(self.paginaResumen)
        self.lblResumenFecha.setObjectName(u"lblResumenFecha")

        self.formLayoutResumen.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblResumenFecha)

        self.lblResumenParticipantes = QLabel(self.paginaResumen)
        self.lblResumenParticipantes.setObjectName(u"lblResumenParticipantes")

        self.formLayoutResumen.setWidget(5, QFormLayout.ItemRole.LabelRole, self.lblResumenParticipantes)

        self.lblResumenModalidad = QLabel(self.paginaResumen)
        self.lblResumenModalidad.setObjectName(u"lblResumenModalidad")

        self.formLayoutResumen.setWidget(6, QFormLayout.ItemRole.LabelRole, self.lblResumenModalidad)

        self.lblResumenMaterial = QLabel(self.paginaResumen)
        self.lblResumenMaterial.setObjectName(u"lblResumenMaterial")

        self.formLayoutResumen.setWidget(7, QFormLayout.ItemRole.LabelRole, self.lblResumenMaterial)

        self.lblResumenObservaciones = QLabel(self.paginaResumen)
        self.lblResumenObservaciones.setObjectName(u"lblResumenObservaciones")

        self.formLayoutResumen.setWidget(8, QFormLayout.ItemRole.LabelRole, self.lblResumenObservaciones)


        self.verticalLayout.addLayout(self.formLayoutResumen)

        self.layoutBotonesResumen = QHBoxLayout()
        self.layoutBotonesResumen.setObjectName(u"layoutBotonesResumen")
        self.btnNueva = QPushButton(self.paginaResumen)
        self.btnNueva.setObjectName(u"btnNueva")

        self.layoutBotonesResumen.addWidget(self.btnNueva)

        self.btnVerTodas = QPushButton(self.paginaResumen)
        self.btnVerTodas.setObjectName(u"btnVerTodas")

        self.layoutBotonesResumen.addWidget(self.btnVerTodas)

        self.btnInicio = QPushButton(self.paginaResumen)
        self.btnInicio.setObjectName(u"btnInicio")

        self.layoutBotonesResumen.addWidget(self.btnInicio)


        self.verticalLayout.addLayout(self.layoutBotonesResumen)

        self.stackedPaginas.addWidget(self.paginaResumen)
        self.paginaListado = QWidget()
        self.paginaListado.setObjectName(u"paginaListado")
        self.verticalLayoutListado = QVBoxLayout(self.paginaListado)
        self.verticalLayoutListado.setObjectName(u"verticalLayoutListado")
        self.lblTituloListado = QLabel(self.paginaListado)
        self.lblTituloListado.setObjectName(u"lblTituloListado")
        self.lblTituloListado.setFont(font)

        self.verticalLayoutListado.addWidget(self.lblTituloListado)

        self.layoutBusqueda = QHBoxLayout()
        self.layoutBusqueda.setObjectName(u"layoutBusqueda")
        self.lblBuscar = QLabel(self.paginaListado)
        self.lblBuscar.setObjectName(u"lblBuscar")

        self.layoutBusqueda.addWidget(self.lblBuscar)

        self.txtBuscar = QLineEdit(self.paginaListado)
        self.txtBuscar.setObjectName(u"txtBuscar")

        self.layoutBusqueda.addWidget(self.txtBuscar)

        self.btnLimpiarBusqueda = QPushButton(self.paginaListado)
        self.btnLimpiarBusqueda.setObjectName(u"btnLimpiarBusqueda")

        self.layoutBusqueda.addWidget(self.btnLimpiarBusqueda)


        self.verticalLayoutListado.addLayout(self.layoutBusqueda)

        self.tablaInscripciones = QTableWidget(self.paginaListado)
        if (self.tablaInscripciones.columnCount() < 7):
            self.tablaInscripciones.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tablaInscripciones.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablaInscripciones.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablaInscripciones.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tablaInscripciones.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tablaInscripciones.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tablaInscripciones.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tablaInscripciones.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tablaInscripciones.setObjectName(u"tablaInscripciones")
        self.tablaInscripciones.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tablaInscripciones.setAlternatingRowColors(True)
        self.tablaInscripciones.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tablaInscripciones.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tablaInscripciones.setColumnCount(7)

        self.verticalLayoutListado.addWidget(self.tablaInscripciones)

        self.lblContadorListado = QLabel(self.paginaListado)
        self.lblContadorListado.setObjectName(u"lblContadorListado")

        self.verticalLayoutListado.addWidget(self.lblContadorListado)

        self.layoutBotonesListado = QHBoxLayout()
        self.layoutBotonesListado.setObjectName(u"layoutBotonesListado")
        self.horizontalSpacerListado = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layoutBotonesListado.addItem(self.horizontalSpacerListado)

        self.btnNuevaListado = QPushButton(self.paginaListado)
        self.btnNuevaListado.setObjectName(u"btnNuevaListado")

        self.layoutBotonesListado.addWidget(self.btnNuevaListado)

        self.btnEditarListado = QPushButton(self.paginaListado)
        self.btnEditarListado.setObjectName(u"btnEditarListado")

        self.layoutBotonesListado.addWidget(self.btnEditarListado)

        self.btnEliminarListado = QPushButton(self.paginaListado)
        self.btnEliminarListado.setObjectName(u"btnEliminarListado")

        self.layoutBotonesListado.addWidget(self.btnEliminarListado)

        self.btnInicioListado = QPushButton(self.paginaListado)
        self.btnInicioListado.setObjectName(u"btnInicioListado")

        self.layoutBotonesListado.addWidget(self.btnInicioListado)


        self.verticalLayoutListado.addLayout(self.layoutBotonesListado)

        self.stackedPaginas.addWidget(self.paginaListado)

        self.horizontalLayout_2.addWidget(self.stackedPaginas)

        VentanaPrincipal.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(VentanaPrincipal)
        self.statusbar.setObjectName(u"statusbar")
        VentanaPrincipal.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(VentanaPrincipal)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 860, 33))
        self.menuArchivo = QMenu(self.menuBar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuAyuda = QMenu(self.menuBar)
        self.menuAyuda.setObjectName(u"menuAyuda")
        VentanaPrincipal.setMenuBar(self.menuBar)
#if QT_CONFIG(shortcut)
        self.lblNombre.setBuddy(self.txtNombre)
        self.lblCorreo.setBuddy(self.txtCorreo)
        self.lblFecha.setBuddy(self.dateFecha)
        self.lblCiclo.setBuddy(self.cmbCiclo)
        self.lblActividad.setBuddy(self.cmbActividad)
        self.lblBuscar.setBuddy(self.txtBuscar)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.txtNombre, self.txtCorreo)
        QWidget.setTabOrder(self.txtCorreo, self.cmbCiclo)
        QWidget.setTabOrder(self.cmbCiclo, self.cmbActividad)
        QWidget.setTabOrder(self.cmbActividad, self.dateFecha)
        QWidget.setTabOrder(self.dateFecha, self.spinParticipantes)
        QWidget.setTabOrder(self.spinParticipantes, self.radioPresencial)
        QWidget.setTabOrder(self.radioPresencial, self.radioOnline)
        QWidget.setTabOrder(self.radioOnline, self.chkMaterial)
        QWidget.setTabOrder(self.chkMaterial, self.txtObservaciones)
        QWidget.setTabOrder(self.txtObservaciones, self.chkCondiciones)
        QWidget.setTabOrder(self.chkCondiciones, self.btnLimpiar)
        QWidget.setTabOrder(self.btnLimpiar, self.btnRegistrar)
        QWidget.setTabOrder(self.btnRegistrar, self.btnNueva)
        QWidget.setTabOrder(self.btnNueva, self.btnVerTodas)
        QWidget.setTabOrder(self.btnVerTodas, self.btnInicio)
        QWidget.setTabOrder(self.btnInicio, self.txtBuscar)
        QWidget.setTabOrder(self.txtBuscar, self.btnLimpiarBusqueda)
        QWidget.setTabOrder(self.btnLimpiarBusqueda, self.tablaInscripciones)
        QWidget.setTabOrder(self.tablaInscripciones, self.btnNuevaListado)
        QWidget.setTabOrder(self.btnNuevaListado, self.btnEditarListado)
        QWidget.setTabOrder(self.btnEditarListado, self.btnEliminarListado)
        QWidget.setTabOrder(self.btnEliminarListado, self.btnInicioListado)
        QWidget.setTabOrder(self.btnInicioListado, self.btnComenzar)

        self.menuBar.addAction(self.menuArchivo.menuAction())
        self.menuBar.addAction(self.menuAyuda.menuAction())
        self.menuArchivo.addAction(self.actionNueva)
        self.menuArchivo.addAction(self.actionListado)
        self.menuArchivo.addAction(self.actionInicio)
        self.menuArchivo.addAction(self.actionSalir)
        self.menuAyuda.addAction(self.actionAcercaDe)

        self.retranslateUi(VentanaPrincipal)

        self.stackedPaginas.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(VentanaPrincipal)
    # setupUi

    def retranslateUi(self, VentanaPrincipal):
        VentanaPrincipal.setWindowTitle(QCoreApplication.translate("VentanaPrincipal", u"Gestor de Actividades Formativas", None))
        self.actionNueva.setText(QCoreApplication.translate("VentanaPrincipal", u"Nueva inscripci\u00f3n", None))
#if QT_CONFIG(statustip)
        self.actionNueva.setStatusTip(QCoreApplication.translate("VentanaPrincipal", u"Abre un formulario de inscripci\u00f3n vac\u00edo", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionNueva.setShortcut(QCoreApplication.translate("VentanaPrincipal", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionListado.setText(QCoreApplication.translate("VentanaPrincipal", u"Ver listado", None))
#if QT_CONFIG(statustip)
        self.actionListado.setStatusTip(QCoreApplication.translate("VentanaPrincipal", u"Muestra el listado de inscripciones", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionListado.setShortcut(QCoreApplication.translate("VentanaPrincipal", u"Ctrl+L", None))
#endif // QT_CONFIG(shortcut)
        self.actionInicio.setText(QCoreApplication.translate("VentanaPrincipal", u"Ir al inicio", None))
#if QT_CONFIG(statustip)
        self.actionInicio.setStatusTip(QCoreApplication.translate("VentanaPrincipal", u"Muestra la p\u00e1gina de Inicio", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionInicio.setShortcut(QCoreApplication.translate("VentanaPrincipal", u"Ctrl+I", None))
#endif // QT_CONFIG(shortcut)
        self.actionSalir.setText(QCoreApplication.translate("VentanaPrincipal", u"Salir", None))
#if QT_CONFIG(statustip)
        self.actionSalir.setStatusTip(QCoreApplication.translate("VentanaPrincipal", u"Cierra la aplicaci\u00f3n", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionSalir.setShortcut(QCoreApplication.translate("VentanaPrincipal", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionAcercaDe.setText(QCoreApplication.translate("VentanaPrincipal", u"Acerca de", None))
#if QT_CONFIG(statustip)
        self.actionAcercaDe.setStatusTip(QCoreApplication.translate("VentanaPrincipal", u"Muestra informaci\u00f3n sobre la aplicaci\u00f3n", None))
#endif // QT_CONFIG(statustip)
        self.lblTituloInicio.setText(QCoreApplication.translate("VentanaPrincipal", u"Gestor de Actividades Formativas", None))
        self.lblDescripcionInicio.setText(QCoreApplication.translate("VentanaPrincipal", u"Registra la participaci\u00f3n del alumnado en las actividades del centro", None))
        self.btnComenzar.setText(QCoreApplication.translate("VentanaPrincipal", u"Comenzar", None))
        self.lblTituloFormulario.setText(QCoreApplication.translate("VentanaPrincipal", u"Formulario de matr\u00edcula", None))
        self.lblSubtitulo.setText(QCoreApplication.translate("VentanaPrincipal", u"Completa los datos para continuar", None))
        self.lblNombre.setText(QCoreApplication.translate("VentanaPrincipal", u"&Nombre:", None))
        self.txtNombre.setText("")
        self.txtNombre.setPlaceholderText(QCoreApplication.translate("VentanaPrincipal", u"Nombre completo", None))
        self.lblCorreo.setText(QCoreApplication.translate("VentanaPrincipal", u"&Correo:", None))
        self.txtCorreo.setText("")
        self.txtCorreo.setPlaceholderText(QCoreApplication.translate("VentanaPrincipal", u"correo@ejemplo.com", None))
        self.lblFecha.setText(QCoreApplication.translate("VentanaPrincipal", u"&Fecha:", None))
        self.lblParticipantes.setText(QCoreApplication.translate("VentanaPrincipal", u"Participantes:", None))
        self.lblCiclo.setText(QCoreApplication.translate("VentanaPrincipal", u"&Ciclo:", None))
        self.cmbCiclo.setItemText(0, QCoreApplication.translate("VentanaPrincipal", u"Selecciona un ciclo", None))
        self.cmbCiclo.setItemText(1, QCoreApplication.translate("VentanaPrincipal", u"Desarrollo de Aplicaciones Multiplataforma", None))
        self.cmbCiclo.setItemText(2, QCoreApplication.translate("VentanaPrincipal", u"Desarrollo de Aplicaciones Web", None))
        self.cmbCiclo.setItemText(3, QCoreApplication.translate("VentanaPrincipal", u"Administraci\u00f3n de Sistemas Inform\u00e1ticos en Red", None))
        self.cmbCiclo.setItemText(4, QCoreApplication.translate("VentanaPrincipal", u"Sistemas Microinform\u00e1ticos y Redes", None))

        self.lblActividad.setText(QCoreApplication.translate("VentanaPrincipal", u"&Actividad:", None))
        self.cmbActividad.setItemText(0, QCoreApplication.translate("VentanaPrincipal", u"Selecciona una actividad", None))
        self.cmbActividad.setItemText(1, QCoreApplication.translate("VentanaPrincipal", u"Desarrollo de Interfaces", None))
        self.cmbActividad.setItemText(2, QCoreApplication.translate("VentanaPrincipal", u"Programaci\u00f3n con Python", None))
        self.cmbActividad.setItemText(3, QCoreApplication.translate("VentanaPrincipal", u"Bases de datos", None))
        self.cmbActividad.setItemText(4, QCoreApplication.translate("VentanaPrincipal", u"Inteligencia Artificial", None))
        self.cmbActividad.setItemText(5, QCoreApplication.translate("VentanaPrincipal", u"Ciberseguridad", None))

        self.radioPresencial.setText(QCoreApplication.translate("VentanaPrincipal", u"Presencial", None))
        self.radioOnline.setText(QCoreApplication.translate("VentanaPrincipal", u"Online", None))
        self.chkMaterial.setText(QCoreApplication.translate("VentanaPrincipal", u"Material", None))
        self.txtObservaciones.setPlainText("")
        self.txtObservaciones.setPlaceholderText(QCoreApplication.translate("VentanaPrincipal", u"Observaciones", None))
        self.chkCondiciones.setText(QCoreApplication.translate("VentanaPrincipal", u"Acepto las condiciones de participaci\u00f3n", None))
        self.lblEstado.setText(QCoreApplication.translate("VentanaPrincipal", u"Completa los datos obligatorios", None))
#if QT_CONFIG(tooltip)
        self.btnLimpiar.setToolTip(QCoreApplication.translate("VentanaPrincipal", u"Borra todos los campos", None))
#endif // QT_CONFIG(tooltip)
        self.btnLimpiar.setText(QCoreApplication.translate("VentanaPrincipal", u"Limpiar", None))
#if QT_CONFIG(tooltip)
        self.btnRegistrar.setToolTip(QCoreApplication.translate("VentanaPrincipal", u"Guarda la matr\u00edcula", None))
#endif // QT_CONFIG(tooltip)
        self.btnRegistrar.setText(QCoreApplication.translate("VentanaPrincipal", u"Guardar", None))
        self.lblResumenNombre.setText(QCoreApplication.translate("VentanaPrincipal", u"TextLabel", None))
        self.lblResumenCorreo.setText(QCoreApplication.translate("VentanaPrincipal", u"TextLabel", None))
        self.lblResumenCiclo.setText(QCoreApplication.translate("VentanaPrincipal", u"TextLabel", None))
        self.lblResumenActividad.setText(QCoreApplication.translate("VentanaPrincipal", u"TextLabel", None))
        self.lblResumenFecha.setText(QCoreApplication.translate("VentanaPrincipal", u"TextLabel", None))
        self.lblResumenParticipantes.setText(QCoreApplication.translate("VentanaPrincipal", u"TextLabel", None))
        self.lblResumenModalidad.setText(QCoreApplication.translate("VentanaPrincipal", u"TextLabel", None))
        self.lblResumenMaterial.setText(QCoreApplication.translate("VentanaPrincipal", u"TextLabel", None))
        self.lblResumenObservaciones.setText(QCoreApplication.translate("VentanaPrincipal", u"TextLabel", None))
        self.btnNueva.setText(QCoreApplication.translate("VentanaPrincipal", u"Nueva Inscripci\u00f3n", None))
        self.btnVerTodas.setText(QCoreApplication.translate("VentanaPrincipal", u"Ver todas", None))
        self.btnInicio.setText(QCoreApplication.translate("VentanaPrincipal", u"Volver al Inicio", None))
        self.lblTituloListado.setText(QCoreApplication.translate("VentanaPrincipal", u"Listado de inscripciones", None))
        self.lblBuscar.setText(QCoreApplication.translate("VentanaPrincipal", u"Buscar:", None))
#if QT_CONFIG(tooltip)
        self.txtBuscar.setToolTip(QCoreApplication.translate("VentanaPrincipal", u"Filtra por nombre, correo o actividad", None))
#endif // QT_CONFIG(tooltip)
        self.txtBuscar.setPlaceholderText(QCoreApplication.translate("VentanaPrincipal", u"Nombre, correo o actividad", None))
        self.btnLimpiarBusqueda.setText(QCoreApplication.translate("VentanaPrincipal", u"Limpiar b\u00fasqueda", None))
        ___qtablewidgetitem = self.tablaInscripciones.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("VentanaPrincipal", u"Nombre", None))
        ___qtablewidgetitem1 = self.tablaInscripciones.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("VentanaPrincipal", u"Correo", None))
        ___qtablewidgetitem2 = self.tablaInscripciones.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("VentanaPrincipal", u"Ciclo", None))
        ___qtablewidgetitem3 = self.tablaInscripciones.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("VentanaPrincipal", u"Actividad", None))
        ___qtablewidgetitem4 = self.tablaInscripciones.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("VentanaPrincipal", u"Fecha", None))
        ___qtablewidgetitem5 = self.tablaInscripciones.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("VentanaPrincipal", u"Participantes", None))
        ___qtablewidgetitem6 = self.tablaInscripciones.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("VentanaPrincipal", u"Modalidad", None))
        self.lblContadorListado.setText(QCoreApplication.translate("VentanaPrincipal", u"Total: 0 inscripciones", None))
        self.btnNuevaListado.setText(QCoreApplication.translate("VentanaPrincipal", u"Nueva Inscripci\u00f3n", None))
#if QT_CONFIG(tooltip)
        self.btnEditarListado.setToolTip(QCoreApplication.translate("VentanaPrincipal", u"Carga la fila seleccionada en el formulario", None))
#endif // QT_CONFIG(tooltip)
        self.btnEditarListado.setText(QCoreApplication.translate("VentanaPrincipal", u"Editar", None))
#if QT_CONFIG(tooltip)
        self.btnEliminarListado.setToolTip(QCoreApplication.translate("VentanaPrincipal", u"Elimina la fila seleccionada", None))
#endif // QT_CONFIG(tooltip)
        self.btnEliminarListado.setText(QCoreApplication.translate("VentanaPrincipal", u"Eliminar", None))
        self.btnInicioListado.setText(QCoreApplication.translate("VentanaPrincipal", u"Volver al Inicio", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("VentanaPrincipal", u"Archivo", None))
        self.menuAyuda.setTitle(QCoreApplication.translate("VentanaPrincipal", u"Ayuda", None))
    # retranslateUi

