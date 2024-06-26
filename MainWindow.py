# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Sort_VF_Window(object):
    def setupUi(self, Sort_VF_Window):
        Sort_VF_Window.setObjectName("Sort_VF_Window")
        Sort_VF_Window.resize(765, 360)
        Sort_VF_Window.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        Sort_VF_Window.setWindowFlags(
            QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowCloseButtonHint)
        Sort_VF_Window.setFixedSize(765, 360)
        self.centralwidget = QtWidgets.QWidget(Sort_VF_Window)
        self.centralwidget.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(1, 1, 761, 351))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.ButtonExit = QtWidgets.QPushButton(self.widget)
        self.ButtonExit.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.ButtonExit.setFont(font)
        self.ButtonExit.setObjectName("ButtonExit")
        self.gridLayout.addWidget(self.ButtonExit, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.ListLog = QtWidgets.QListWidget(self.widget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(183, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(183, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.ListLog.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ListLog.setFont(font)
        self.ListLog.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.ListLog.setTabKeyNavigation(False)
        self.ListLog.setProperty("showDropIndicator", True)
        self.ListLog.setDragEnabled(False)
        self.ListLog.setAlternatingRowColors(False)
        self.ListLog.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.ListLog.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.ListLog.setProperty("isWrapping", False)
        self.ListLog.setResizeMode(QtWidgets.QListView.Fixed)
        self.ListLog.setWordWrap(True)
        self.ListLog.setObjectName("ListLog")
        self.setup_context_menu()
        self.gridLayout.addWidget(self.ListLog, 0, 0, 1, 2)
        Sort_VF_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Sort_VF_Window)
        self.ButtonExit.clicked.connect(Sort_VF_Window.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Sort_VF_Window)

    def setup_context_menu(self):
        self.context_menu = QtWidgets.QMenu(self.ListLog)
        copy_action = QtWidgets.QAction("Копіювати", self.context_menu)
        copy_action.triggered.connect(self.copy_selected_text)
        self.context_menu.addAction(copy_action)
        self.ListLog.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ListLog.customContextMenuRequested.connect(self.show_context_menu)

    def copy_selected_text(self):
        selected_item = self.ListLog.currentItem()
        if selected_item:
            clipboard = QtWidgets.QApplication.clipboard()
            clipboard.setText(selected_item.text())

    def show_context_menu(self, pos):
        self.context_menu.exec_(self.ListLog.mapToGlobal(pos))

    def retranslateUi(self, Sort_VF_Window):
        _translate = QtCore.QCoreApplication.translate
        Sort_VF_Window.setWindowTitle(_translate("Sort_VF_Window", "Сортування по верифікації"))
        self.ButtonExit.setText(_translate("Sort_VF_Window", "Вихід"))
