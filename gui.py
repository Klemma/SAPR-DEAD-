# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1148, 865)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tab_widget_main = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.tab_widget_main.setFont(font)
        self.tab_widget_main.setObjectName("tab_widget_main")
        self.preprocessor_tab = QtWidgets.QWidget()
        self.preprocessor_tab.setObjectName("preprocessor_tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.preprocessor_tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.preprocessor_layout = QtWidgets.QGridLayout()
        self.preprocessor_layout.setObjectName("preprocessor_layout")
        self.add_bar_btn = QtWidgets.QPushButton(self.preprocessor_tab)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.add_bar_btn.setFont(font)
        self.add_bar_btn.setObjectName("add_bar_btn")
        self.preprocessor_layout.addWidget(self.add_bar_btn, 2, 0, 1, 1)
        self.figure_view = QtWidgets.QGraphicsView(self.preprocessor_tab)
        self.figure_view.setObjectName("figure_view")
        self.preprocessor_layout.addWidget(self.figure_view, 3, 0, 1, 3)
        self.add_force_btn = QtWidgets.QPushButton(self.preprocessor_tab)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.add_force_btn.setFont(font)
        self.add_force_btn.setObjectName("add_force_btn")
        self.preprocessor_layout.addWidget(self.add_force_btn, 2, 2, 1, 1)
        self.forces_table = ForcesTableWidget(self.preprocessor_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.forces_table.sizePolicy().hasHeightForWidth())
        self.forces_table.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.forces_table.setFont(font)
        self.forces_table.setAlternatingRowColors(False)
        self.forces_table.setObjectName("forces_table")
        self.forces_table.setColumnCount(2)
        self.forces_table.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.forces_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.forces_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.forces_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.forces_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.forces_table.setItem(0, 1, item)
        self.forces_table.horizontalHeader().setCascadingSectionResizes(False)
        self.forces_table.horizontalHeader().setStretchLastSection(True)
        self.preprocessor_layout.addWidget(self.forces_table, 1, 2, 1, 1)
        self.bar_nodal_loads = QtWidgets.QLabel(self.preprocessor_tab)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.bar_nodal_loads.setFont(font)
        self.bar_nodal_loads.setAlignment(QtCore.Qt.AlignCenter)
        self.bar_nodal_loads.setObjectName("bar_nodal_loads")
        self.preprocessor_layout.addWidget(self.bar_nodal_loads, 0, 2, 1, 1)
        self.del_bar_btn = QtWidgets.QPushButton(self.preprocessor_tab)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.del_bar_btn.setFont(font)
        self.del_bar_btn.setObjectName("del_bar_btn")
        self.preprocessor_layout.addWidget(self.del_bar_btn, 2, 1, 1, 1)
        self.bars_table = QtWidgets.QTableWidget(self.preprocessor_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bars_table.sizePolicy().hasHeightForWidth())
        self.bars_table.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.bars_table.setFont(font)
        self.bars_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.bars_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.bars_table.setAutoScroll(True)
        self.bars_table.setGridStyle(QtCore.Qt.SolidLine)
        self.bars_table.setObjectName("bars_table")
        self.bars_table.setColumnCount(5)
        self.bars_table.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.bars_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bars_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bars_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.bars_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.bars_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.bars_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        self.bars_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bars_table.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.bars_table.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.bars_table.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.bars_table.setItem(0, 4, item)
        self.bars_table.horizontalHeader().setDefaultSectionSize(130)
        self.bars_table.horizontalHeader().setStretchLastSection(True)
        self.preprocessor_layout.addWidget(self.bars_table, 1, 0, 1, 2)
        self.bar_label = QtWidgets.QLabel(self.preprocessor_tab)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.bar_label.setFont(font)
        self.bar_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bar_label.setObjectName("bar_label")
        self.preprocessor_layout.addWidget(self.bar_label, 0, 0, 1, 2)
        self.gridLayout_3.addLayout(self.preprocessor_layout, 0, 0, 1, 1)
        self.termination_layout = QtWidgets.QHBoxLayout()
        self.termination_layout.setObjectName("termination_layout")
        self.left_termination = QtWidgets.QRadioButton(self.preprocessor_tab)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.left_termination.setFont(font)
        self.left_termination.setObjectName("left_termination")
        self.terminations_btn_group = QtWidgets.QButtonGroup(MainWindow)
        self.terminations_btn_group.setObjectName("terminations_btn_group")
        self.terminations_btn_group.addButton(self.left_termination)
        self.termination_layout.addWidget(self.left_termination)
        self.both_terminations = QtWidgets.QRadioButton(self.preprocessor_tab)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.both_terminations.setFont(font)
        self.both_terminations.setChecked(True)
        self.both_terminations.setObjectName("both_terminations")
        self.terminations_btn_group.addButton(self.both_terminations)
        self.termination_layout.addWidget(self.both_terminations, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.right_termination = QtWidgets.QRadioButton(self.preprocessor_tab)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.right_termination.setFont(font)
        self.right_termination.setObjectName("right_termination")
        self.terminations_btn_group.addButton(self.right_termination)
        self.termination_layout.addWidget(self.right_termination, 0, QtCore.Qt.AlignRight)
        self.gridLayout_3.addLayout(self.termination_layout, 1, 0, 1, 1)
        self.tab_widget_main.addTab(self.preprocessor_tab, "")
        self.postprocessor_tab = QtWidgets.QWidget()
        self.postprocessor_tab.setEnabled(True)
        self.postprocessor_tab.setObjectName("postprocessor_tab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.postprocessor_tab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.postprocessor_layout = QtWidgets.QGridLayout()
        self.postprocessor_layout.setObjectName("postprocessor_layout")
        self.postprocessor_tab_widget = QtWidgets.QTabWidget(self.postprocessor_tab)
        self.postprocessor_tab_widget.setObjectName("postprocessor_tab_widget")
        self.computations_tab = QtWidgets.QWidget()
        self.computations_tab.setObjectName("computations_tab")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.computations_tab)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.computations_table = QtWidgets.QTableWidget(self.computations_tab)
        self.computations_table.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.computations_table.setFont(font)
        self.computations_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.computations_table.setObjectName("computations_table")
        self.computations_table.setColumnCount(5)
        self.computations_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.computations_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.computations_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.computations_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.computations_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.computations_table.setHorizontalHeaderItem(4, item)
        self.computations_table.horizontalHeader().setDefaultSectionSize(205)
        self.computations_table.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_7.addWidget(self.computations_table, 3, 0, 1, 5)
        self.discrete_values_btn = QtWidgets.QPushButton(self.computations_tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.discrete_values_btn.setFont(font)
        self.discrete_values_btn.setObjectName("discrete_values_btn")
        self.gridLayout_7.addWidget(self.discrete_values_btn, 1, 1, 1, 1)
        self.extreme_values_btn = QtWidgets.QPushButton(self.computations_tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.extreme_values_btn.setFont(font)
        self.extreme_values_btn.setObjectName("extreme_values_btn")
        self.gridLayout_7.addWidget(self.extreme_values_btn, 2, 1, 1, 1)
        self.table_label = QtWidgets.QLabel(self.computations_tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.table_label.setFont(font)
        self.table_label.setAlignment(QtCore.Qt.AlignCenter)
        self.table_label.setObjectName("table_label")
        self.gridLayout_7.addWidget(self.table_label, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem, 1, 2, 1, 1)
        self.compute_section_btn = QtWidgets.QPushButton(self.computations_tab)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.compute_section_btn.setFont(font)
        self.compute_section_btn.setObjectName("compute_section_btn")
        self.gridLayout_7.addWidget(self.compute_section_btn, 2, 3, 1, 1)
        self.section_label = QtWidgets.QLabel(self.computations_tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.section_label.setFont(font)
        self.section_label.setAlignment(QtCore.Qt.AlignCenter)
        self.section_label.setObjectName("section_label")
        self.gridLayout_7.addWidget(self.section_label, 0, 3, 1, 1)
        self.section_input = QtWidgets.QLineEdit(self.computations_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.section_input.sizePolicy().hasHeightForWidth())
        self.section_input.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.section_input.setFont(font)
        self.section_input.setAlignment(QtCore.Qt.AlignCenter)
        self.section_input.setObjectName("section_input")
        self.gridLayout_7.addWidget(self.section_input, 1, 3, 1, 1)
        self.Nx_section_label = QtWidgets.QLabel(self.computations_tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Nx_section_label.setFont(font)
        self.Nx_section_label.setObjectName("Nx_section_label")
        self.gridLayout_7.addWidget(self.Nx_section_label, 0, 4, 1, 1)
        self.Ux_section_label = QtWidgets.QLabel(self.computations_tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Ux_section_label.setFont(font)
        self.Ux_section_label.setObjectName("Ux_section_label")
        self.gridLayout_7.addWidget(self.Ux_section_label, 1, 4, 1, 1)
        self.Sx_section_label = QtWidgets.QLabel(self.computations_tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Sx_section_label.setFont(font)
        self.Sx_section_label.setObjectName("Sx_section_label")
        self.gridLayout_7.addWidget(self.Sx_section_label, 2, 4, 1, 1)
        self.paimon_label = QtWidgets.QLabel(self.computations_tab)
        self.paimon_label.setText("")
        self.paimon_label.setPixmap(QtGui.QPixmap("paimon.png"))
        self.paimon_label.setAlignment(QtCore.Qt.AlignCenter)
        self.paimon_label.setObjectName("paimon_label")
        self.gridLayout_7.addWidget(self.paimon_label, 0, 0, 3, 1)
        self.postprocessor_tab_widget.addTab(self.computations_tab, "")
        self.epures_tab = QtWidgets.QWidget()
        self.epures_tab.setObjectName("epures_tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.epures_tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.epures_layout = QtWidgets.QGridLayout()
        self.epures_layout.setObjectName("epures_layout")
        self.epures_tab_widget = QtWidgets.QTabWidget(self.epures_tab)
        self.epures_tab_widget.setObjectName("epures_tab_widget")
        self.epure_nx_tab = QtWidgets.QWidget()
        self.epure_nx_tab.setObjectName("epure_nx_tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.epure_nx_tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Nx_epure_layout = QtWidgets.QVBoxLayout()
        self.Nx_epure_layout.setObjectName("Nx_epure_layout")
        self.gridLayout_2.addLayout(self.Nx_epure_layout, 0, 0, 1, 1)
        self.epures_tab_widget.addTab(self.epure_nx_tab, "")
        self.epure_ux_tab = QtWidgets.QWidget()
        self.epure_ux_tab.setObjectName("epure_ux_tab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.epure_ux_tab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.Ux_epure_layout = QtWidgets.QVBoxLayout()
        self.Ux_epure_layout.setObjectName("Ux_epure_layout")
        self.gridLayout_6.addLayout(self.Ux_epure_layout, 0, 0, 1, 1)
        self.epures_tab_widget.addTab(self.epure_ux_tab, "")
        self.epure_sx_tab = QtWidgets.QWidget()
        self.epure_sx_tab.setObjectName("epure_sx_tab")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.epure_sx_tab)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.Sx_epure_layout = QtWidgets.QVBoxLayout()
        self.Sx_epure_layout.setObjectName("Sx_epure_layout")
        self.gridLayout_8.addLayout(self.Sx_epure_layout, 0, 0, 1, 1)
        self.epures_tab_widget.addTab(self.epure_sx_tab, "")
        self.epures_layout.addWidget(self.epures_tab_widget, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.epures_layout, 0, 0, 1, 1)
        self.postprocessor_tab_widget.addTab(self.epures_tab, "")
        self.postprocessor_layout.addWidget(self.postprocessor_tab_widget, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.postprocessor_layout, 0, 0, 1, 1)
        self.tab_widget_main.addTab(self.postprocessor_tab, "")
        self.gridLayout.addWidget(self.tab_widget_main, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1148, 21))
        self.menubar.setObjectName("menubar")
        self.file_menu = QtWidgets.QMenu(self.menubar)
        self.file_menu.setObjectName("file_menu")
        self.processor_menu = QtWidgets.QMenu(self.menubar)
        self.processor_menu.setObjectName("processor_menu")
        MainWindow.setMenuBar(self.menubar)
        self.open_action = QtWidgets.QAction(MainWindow)
        self.open_action.setObjectName("open_action")
        self.save_action = QtWidgets.QAction(MainWindow)
        self.save_action.setObjectName("save_action")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.compute_action = QtWidgets.QAction(MainWindow)
        self.compute_action.setObjectName("compute_action")
        self.save_table_action = QtWidgets.QAction(MainWindow)
        self.save_table_action.setEnabled(False)
        self.save_table_action.setObjectName("save_table_action")
        self.file_menu.addAction(self.open_action)
        self.file_menu.addAction(self.save_action)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.save_table_action)
        self.processor_menu.addAction(self.compute_action)
        self.menubar.addAction(self.file_menu.menuAction())
        self.menubar.addAction(self.processor_menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tab_widget_main.setCurrentIndex(0)
        self.postprocessor_tab_widget.setCurrentIndex(0)
        self.epures_tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SAPR"))
        self.add_bar_btn.setText(_translate("MainWindow", "Добавить стержень"))
        self.add_force_btn.setText(_translate("MainWindow", "Добавить нагрузку"))
        self.forces_table.setSortingEnabled(False)
        item = self.forces_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.forces_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Номер узла"))
        item = self.forces_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "F"))
        __sortingEnabled = self.forces_table.isSortingEnabled()
        self.forces_table.setSortingEnabled(False)
        item = self.forces_table.item(0, 0)
        item.setText(_translate("MainWindow", "-"))
        item = self.forces_table.item(0, 1)
        item.setText(_translate("MainWindow", "-"))
        self.forces_table.setSortingEnabled(__sortingEnabled)
        self.bar_nodal_loads.setText(_translate("MainWindow", "Узловые нагрузки"))
        self.del_bar_btn.setText(_translate("MainWindow", "Удалить последний стержень"))
        self.bars_table.setSortingEnabled(False)
        item = self.bars_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.bars_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "E"))
        item = self.bars_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "L"))
        item = self.bars_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "A"))
        item = self.bars_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "S"))
        item = self.bars_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "q"))
        __sortingEnabled = self.bars_table.isSortingEnabled()
        self.bars_table.setSortingEnabled(False)
        item = self.bars_table.item(0, 0)
        item.setText(_translate("MainWindow", "1"))
        item = self.bars_table.item(0, 1)
        item.setText(_translate("MainWindow", "1"))
        item = self.bars_table.item(0, 2)
        item.setText(_translate("MainWindow", "1"))
        item = self.bars_table.item(0, 3)
        item.setText(_translate("MainWindow", "1"))
        item = self.bars_table.item(0, 4)
        item.setText(_translate("MainWindow", "0"))
        self.bars_table.setSortingEnabled(__sortingEnabled)
        self.bar_label.setText(_translate("MainWindow", "Стержни"))
        self.left_termination.setText(_translate("MainWindow", "Заделка слева"))
        self.both_terminations.setText(_translate("MainWindow", "Заделки с обеих сторон"))
        self.right_termination.setText(_translate("MainWindow", "Заделка справа"))
        self.tab_widget_main.setTabText(self.tab_widget_main.indexOf(self.preprocessor_tab), _translate("MainWindow", "Препроцессор"))
        self.computations_table.setSortingEnabled(True)
        item = self.computations_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Стержень"))
        item = self.computations_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "x"))
        item = self.computations_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "N(x)"))
        item = self.computations_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "U(x)"))
        item = self.computations_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "S(x)"))
        self.discrete_values_btn.setText(_translate("MainWindow", "Дискретизированные значения"))
        self.extreme_values_btn.setText(_translate("MainWindow", "Только краевые значения"))
        self.table_label.setText(_translate("MainWindow", "Отобразить в таблице"))
        self.compute_section_btn.setText(_translate("MainWindow", "Рассчитать"))
        self.section_label.setText(_translate("MainWindow", "Компоненты в точке (глобально)"))
        self.Nx_section_label.setText(_translate("MainWindow", "N(x)"))
        self.Ux_section_label.setText(_translate("MainWindow", "U(x)"))
        self.Sx_section_label.setText(_translate("MainWindow", "S(x)"))
        self.postprocessor_tab_widget.setTabText(self.postprocessor_tab_widget.indexOf(self.computations_tab), _translate("MainWindow", "Результаты расчетов"))
        self.epures_tab_widget.setTabText(self.epures_tab_widget.indexOf(self.epure_nx_tab), _translate("MainWindow", "N(x)"))
        self.epures_tab_widget.setTabText(self.epures_tab_widget.indexOf(self.epure_ux_tab), _translate("MainWindow", "U(x)"))
        self.epures_tab_widget.setTabText(self.epures_tab_widget.indexOf(self.epure_sx_tab), _translate("MainWindow", "S(x)"))
        self.postprocessor_tab_widget.setTabText(self.postprocessor_tab_widget.indexOf(self.epures_tab), _translate("MainWindow", "Эпюры"))
        self.tab_widget_main.setTabText(self.tab_widget_main.indexOf(self.postprocessor_tab), _translate("MainWindow", "Постпроцессор"))
        self.file_menu.setTitle(_translate("MainWindow", "Файл"))
        self.processor_menu.setTitle(_translate("MainWindow", "Процессор"))
        self.open_action.setText(_translate("MainWindow", "Открыть файл проекта"))
        self.save_action.setText(_translate("MainWindow", "Сохранить файл проекта"))
        self.action_3.setText(_translate("MainWindow", "Сохранить как"))
        self.compute_action.setText(_translate("MainWindow", "Провести расчет"))
        self.save_table_action.setText(_translate("MainWindow", "Сохранить таблицу расчетов"))
from ForcesTableWidget import ForcesTableWidget
