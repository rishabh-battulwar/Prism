# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ExternalTask.ui'
#
# Created: Tue Feb 20 21:19:32 2018
#      by: pyside2-uic @pyside_tools_VERSION@ running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_dlg_ExternalTask(object):
    def setupUi(self, dlg_ExternalTask):
        dlg_ExternalTask.setObjectName("dlg_ExternalTask")
        dlg_ExternalTask.resize(627, 147)
        self.verticalLayout = QtWidgets.QVBoxLayout(dlg_ExternalTask)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(dlg_ExternalTask)
        self.widget.setObjectName("widget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout_5.addWidget(self.widget_2)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_3 = QtWidgets.QWidget(self.widget_4)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.w_taskName = QtWidgets.QWidget(self.widget_3)
        self.w_taskName.setObjectName("w_taskName")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.w_taskName)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.e_taskName = QtWidgets.QLineEdit(self.w_taskName)
        self.e_taskName.setObjectName("e_taskName")
        self.horizontalLayout_2.addWidget(self.e_taskName)
        self.horizontalLayout_3.addWidget(self.w_taskName)
        self.w_versionName = QtWidgets.QWidget(self.widget_3)
        self.w_versionName.setObjectName("w_versionName")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.w_versionName)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.w_versionName)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.e_versionName = QtWidgets.QLineEdit(self.w_versionName)
        self.e_versionName.setObjectName("e_versionName")
        self.horizontalLayout_4.addWidget(self.e_versionName)
        self.horizontalLayout_3.addWidget(self.w_versionName)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.w_taskPath = QtWidgets.QWidget(self.widget_4)
        self.w_taskPath.setObjectName("w_taskPath")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.w_taskPath)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.e_taskPath = QtWidgets.QLineEdit(self.w_taskPath)
        self.e_taskPath.setObjectName("e_taskPath")
        self.horizontalLayout.addWidget(self.e_taskPath)
        self.b_browseFile = QtWidgets.QPushButton(self.w_taskPath)
        self.b_browseFile.setMinimumSize(QtCore.QSize(70, 0))
        self.b_browseFile.setMaximumSize(QtCore.QSize(70, 16777215))
        self.b_browseFile.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_browseFile.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.b_browseFile.setObjectName("b_browseFile")
        self.horizontalLayout.addWidget(self.b_browseFile)
        self.b_browseFolder = QtWidgets.QPushButton(self.w_taskPath)
        self.b_browseFolder.setMinimumSize(QtCore.QSize(80, 0))
        self.b_browseFolder.setMaximumSize(QtCore.QSize(80, 16777215))
        self.b_browseFolder.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_browseFolder.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.b_browseFolder.setObjectName("b_browseFolder")
        self.horizontalLayout.addWidget(self.b_browseFolder)
        self.verticalLayout_2.addWidget(self.w_taskPath)
        self.horizontalLayout_5.addWidget(self.widget_4)
        self.verticalLayout.addWidget(self.widget)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(dlg_ExternalTask)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(dlg_ExternalTask)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), dlg_ExternalTask.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), dlg_ExternalTask.reject)
        QtCore.QMetaObject.connectSlotsByName(dlg_ExternalTask)

    def retranslateUi(self, dlg_ExternalTask):
        dlg_ExternalTask.setWindowTitle(QtWidgets.QApplication.translate("dlg_ExternalTask", "Create external task", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("dlg_ExternalTask", "Taskname:", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("dlg_ExternalTask", "External path:", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("dlg_ExternalTask", "Versionname:", None, -1))
        self.b_browseFile.setText(QtWidgets.QApplication.translate("dlg_ExternalTask", "...(file)", None, -1))
        self.b_browseFolder.setText(QtWidgets.QApplication.translate("dlg_ExternalTask", "...(folder)", None, -1))

