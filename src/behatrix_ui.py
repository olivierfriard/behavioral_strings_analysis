# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'behatrix.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(893, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_strings = QtWidgets.QWidget()
        self.tab_strings.setObjectName("tab_strings")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_strings)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.tab_strings)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_7.addWidget(self.label_2)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.pte_behav_strings = QtWidgets.QPlainTextEdit(self.tab_strings)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.pte_behav_strings.setFont(font)
        self.pte_behav_strings.setObjectName("pte_behav_strings")
        self.horizontalLayout_19.addWidget(self.pte_behav_strings)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pb_clear_behavioral_strings = QtWidgets.QPushButton(self.tab_strings)
        self.pb_clear_behavioral_strings.setObjectName("pb_clear_behavioral_strings")
        self.verticalLayout_3.addWidget(self.pb_clear_behavioral_strings)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_19.addLayout(self.verticalLayout_3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_17 = QtWidgets.QLabel(self.tab_strings)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_16.addWidget(self.label_17)
        self.le_behaviors_separator = QtWidgets.QLineEdit(self.tab_strings)
        self.le_behaviors_separator.setObjectName("le_behaviors_separator")
        self.horizontalLayout_16.addWidget(self.le_behaviors_separator)
        self.verticalLayout_7.addLayout(self.horizontalLayout_16)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leStringsFileName = QtWidgets.QLineEdit(self.tab_strings)
        self.leStringsFileName.setEnabled(False)
        self.leStringsFileName.setText("")
        self.leStringsFileName.setReadOnly(True)
        self.leStringsFileName.setObjectName("leStringsFileName")
        self.horizontalLayout.addWidget(self.leStringsFileName)
        self.pb_select_behav_strings_file = QtWidgets.QPushButton(self.tab_strings)
        self.pb_select_behav_strings_file.setObjectName("pb_select_behav_strings_file")
        self.horizontalLayout.addWidget(self.pb_select_behav_strings_file)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.cb_remove_repeated_behaviors = QtWidgets.QCheckBox(self.tab_strings)
        self.cb_remove_repeated_behaviors.setObjectName("cb_remove_repeated_behaviors")
        self.verticalLayout_7.addWidget(self.cb_remove_repeated_behaviors)
        self.label_4 = QtWidgets.QLabel(self.tab_strings)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pb_statistics = QtWidgets.QPushButton(self.tab_strings)
        self.pb_statistics.setObjectName("pb_statistics")
        self.horizontalLayout_5.addWidget(self.pb_statistics)
        self.pb_save_observed_matrix = QtWidgets.QPushButton(self.tab_strings)
        self.pb_save_observed_matrix.setObjectName("pb_save_observed_matrix")
        self.horizontalLayout_5.addWidget(self.pb_save_observed_matrix)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.label_13 = QtWidgets.QLabel(self.tab_strings)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_7.addWidget(self.label_13)
        self.pte_statistics = QtWidgets.QPlainTextEdit(self.tab_strings)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.pte_statistics.setFont(font)
        self.pte_statistics.setReadOnly(True)
        self.pte_statistics.setObjectName("pte_statistics")
        self.verticalLayout_7.addWidget(self.pte_statistics)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.pb_save_stats_results = QtWidgets.QPushButton(self.tab_strings)
        self.pb_save_stats_results.setObjectName("pb_save_stats_results")
        self.horizontalLayout_12.addWidget(self.pb_save_stats_results)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_12)
        self.label_4.raise_()
        self.label_13.raise_()
        self.pte_statistics.raise_()
        self.label_2.raise_()
        self.cb_remove_repeated_behaviors.raise_()
        self.tabWidget.addTab(self.tab_strings, "")
        self.tab_flow_diagram = QtWidgets.QWidget()
        self.tab_flow_diagram.setObjectName("tab_flow_diagram")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.tab_flow_diagram)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.vertical_splitter = QtWidgets.QSplitter(self.tab_flow_diagram)
        self.vertical_splitter.setOrientation(QtCore.Qt.Vertical)
        self.vertical_splitter.setObjectName("vertical_splitter")
        self.layoutWidget = QtWidgets.QWidget(self.vertical_splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_23.addWidget(self.label_8)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.rb_percent_after_behav = QtWidgets.QRadioButton(self.layoutWidget)
        self.rb_percent_after_behav.setChecked(True)
        self.rb_percent_after_behav.setObjectName("rb_percent_after_behav")
        self.horizontalLayout_10.addWidget(self.rb_percent_after_behav)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.sb_cutoff_transition_after_behav = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.sb_cutoff_transition_after_behav.setObjectName("sb_cutoff_transition_after_behav")
        self.horizontalLayout_4.addWidget(self.sb_cutoff_transition_after_behav)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.rb_percent_total_transitions = QtWidgets.QRadioButton(self.layoutWidget)
        self.rb_percent_total_transitions.setObjectName("rb_percent_total_transitions")
        self.horizontalLayout_18.addWidget(self.rb_percent_total_transitions)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.sb_cutoff_total_transition = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.sb_cutoff_total_transition.setObjectName("sb_cutoff_total_transition")
        self.horizontalLayout_8.addWidget(self.sb_cutoff_total_transition)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_8.addWidget(self.label_12)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.horizontalLayout_18.addLayout(self.horizontalLayout_8)
        self.verticalLayout_5.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_23.addLayout(self.verticalLayout_5)
        self.verticalLayout_8.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_18 = QtWidgets.QLabel(self.layoutWidget)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_17.addWidget(self.label_18)
        self.sb_decimals = QtWidgets.QSpinBox(self.layoutWidget)
        self.sb_decimals.setMaximum(6)
        self.sb_decimals.setProperty("value", 3)
        self.sb_decimals.setObjectName("sb_decimals")
        self.horizontalLayout_17.addWidget(self.sb_decimals)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_17)
        self.cb_plot_significativity = QtWidgets.QCheckBox(self.layoutWidget)
        self.cb_plot_significativity.setObjectName("cb_plot_significativity")
        self.horizontalLayout_9.addWidget(self.cb_plot_significativity)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem5)
        self.verticalLayout_8.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_16 = QtWidgets.QLabel(self.layoutWidget)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_14.addWidget(self.label_16)
        self.le_dot_path = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_dot_path.setObjectName("le_dot_path")
        self.horizontalLayout_14.addWidget(self.le_dot_path)
        self.pb_browse_dot_path = QtWidgets.QPushButton(self.layoutWidget)
        self.pb_browse_dot_path.setObjectName("pb_browse_dot_path")
        self.horizontalLayout_14.addWidget(self.pb_browse_dot_path)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem6)
        self.verticalLayout_8.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pb_graphviz_script = QtWidgets.QPushButton(self.layoutWidget)
        self.pb_graphviz_script.setObjectName("pb_graphviz_script")
        self.horizontalLayout_6.addWidget(self.pb_graphviz_script)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.horizontal_splitter = QtWidgets.QSplitter(self.vertical_splitter)
        self.horizontal_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.horizontal_splitter.setChildrenCollapsible(True)
        self.horizontal_splitter.setObjectName("horizontal_splitter")
        self.layoutWidget1 = QtWidgets.QWidget(self.horizontal_splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_4.addWidget(self.label_14)
        self.pte_gv = QtWidgets.QPlainTextEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.pte_gv.setFont(font)
        self.pte_gv.setObjectName("pte_gv")
        self.verticalLayout_4.addWidget(self.pte_gv)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.pb_save_gv = QtWidgets.QPushButton(self.layoutWidget1)
        self.pb_save_gv.setObjectName("pb_save_gv")
        self.horizontalLayout_13.addWidget(self.pb_save_gv)
        self.pb_flow_diagram = QtWidgets.QPushButton(self.layoutWidget1)
        self.pb_flow_diagram.setObjectName("pb_flow_diagram")
        self.horizontalLayout_13.addWidget(self.pb_flow_diagram)
        self.pb_clear_diagram = QtWidgets.QPushButton(self.layoutWidget1)
        self.pb_clear_diagram.setObjectName("pb_clear_diagram")
        self.horizontalLayout_13.addWidget(self.pb_clear_diagram)
        self.pb_save_png = QtWidgets.QPushButton(self.layoutWidget1)
        self.pb_save_png.setObjectName("pb_save_png")
        self.horizontalLayout_13.addWidget(self.pb_save_png)
        self.pb_save_svg = QtWidgets.QPushButton(self.layoutWidget1)
        self.pb_save_svg.setObjectName("pb_save_svg")
        self.horizontalLayout_13.addWidget(self.pb_save_svg)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem8)
        self.verticalLayout_4.addLayout(self.horizontalLayout_13)
        self.lb_flow_chart = QtWidgets.QLabel(self.horizontal_splitter)
        self.lb_flow_chart.setMinimumSize(QtCore.QSize(0, 100))
        self.lb_flow_chart.setText("")
        self.lb_flow_chart.setObjectName("lb_flow_chart")
        self.verticalLayout_13.addWidget(self.vertical_splitter)
        self.tabWidget.addTab(self.tab_flow_diagram, "")
        self.tab_randomization = QtWidgets.QWidget()
        self.tab_randomization.setObjectName("tab_randomization")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_randomization)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cb_block_first_behavior = QtWidgets.QCheckBox(self.tab_randomization)
        self.cb_block_first_behavior.setObjectName("cb_block_first_behavior")
        self.horizontalLayout_2.addWidget(self.cb_block_first_behavior)
        self.cb_block_last_behavior = QtWidgets.QCheckBox(self.tab_randomization)
        self.cb_block_last_behavior.setObjectName("cb_block_last_behavior")
        self.horizontalLayout_2.addWidget(self.cb_block_last_behavior)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.label_7 = QtWidgets.QLabel(self.tab_randomization)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.pte_excluded_transitions = QtWidgets.QPlainTextEdit(self.tab_randomization)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.pte_excluded_transitions.setFont(font)
        self.pte_excluded_transitions.setObjectName("pte_excluded_transitions")
        self.horizontalLayout_15.addWidget(self.pte_excluded_transitions)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pb_exclude_repetition = QtWidgets.QPushButton(self.tab_randomization)
        self.pb_exclude_repetition.setObjectName("pb_exclude_repetition")
        self.verticalLayout.addWidget(self.pb_exclude_repetition)
        self.pb_clear_excluded_transitions = QtWidgets.QPushButton(self.tab_randomization)
        self.pb_clear_excluded_transitions.setObjectName("pb_clear_excluded_transitions")
        self.verticalLayout.addWidget(self.pb_clear_excluded_transitions)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem10)
        self.horizontalLayout_15.addLayout(self.verticalLayout)
        self.verticalLayout_6.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.tab_randomization)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.leNumberRandomizations = QtWidgets.QLineEdit(self.tab_randomization)
        self.leNumberRandomizations.setObjectName("leNumberRandomizations")
        self.horizontalLayout_3.addWidget(self.leNumberRandomizations)
        self.label_3 = QtWidgets.QLabel(self.tab_randomization)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.sb_nb_cores = QtWidgets.QSpinBox(self.tab_randomization)
        self.sb_nb_cores.setMinimum(1)
        self.sb_nb_cores.setObjectName("sb_nb_cores")
        self.horizontalLayout_3.addWidget(self.sb_nb_cores)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pb_run_permutations_test = QtWidgets.QPushButton(self.tab_randomization)
        self.pb_run_permutations_test.setObjectName("pb_run_permutations_test")
        self.horizontalLayout_7.addWidget(self.pb_run_permutations_test)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem12)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.label_15 = QtWidgets.QLabel(self.tab_randomization)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_6.addWidget(self.label_15)
        self.pte_random = QtWidgets.QPlainTextEdit(self.tab_randomization)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.pte_random.setFont(font)
        self.pte_random.setReadOnly(True)
        self.pte_random.setObjectName("pte_random")
        self.verticalLayout_6.addWidget(self.pte_random)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pb_save_random = QtWidgets.QPushButton(self.tab_randomization)
        self.pb_save_random.setObjectName("pb_save_random")
        self.horizontalLayout_11.addWidget(self.pb_save_random)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem13)
        self.verticalLayout_6.addLayout(self.horizontalLayout_11)
        self.tabWidget.addTab(self.tab_randomization, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.pb_levenshtein = QtWidgets.QPushButton(self.tab)
        self.pb_levenshtein.setObjectName("pb_levenshtein")
        self.horizontalLayout_21.addWidget(self.pb_levenshtein)
        self.pb_needleman_wunsch = QtWidgets.QPushButton(self.tab)
        self.pb_needleman_wunsch.setObjectName("pb_needleman_wunsch")
        self.horizontalLayout_21.addWidget(self.pb_needleman_wunsch)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem14)
        self.verticalLayout_9.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_19 = QtWidgets.QLabel(self.tab)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_11.addWidget(self.label_19)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem15)
        self.horizontalLayout_22.addLayout(self.verticalLayout_11)
        self.pte_distances_results = QtWidgets.QPlainTextEdit(self.tab)
        self.pte_distances_results.setReadOnly(True)
        self.pte_distances_results.setObjectName("pte_distances_results")
        self.horizontalLayout_22.addWidget(self.pte_distances_results)
        self.verticalLayout_9.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.pb_save_distances = QtWidgets.QPushButton(self.tab)
        self.pb_save_distances.setObjectName("pb_save_distances")
        self.horizontalLayout_20.addWidget(self.pb_save_distances)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem16)
        self.verticalLayout_9.addLayout(self.horizontalLayout_20)
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 893, 22))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuHelp_2 = QtWidgets.QMenu(self.menubar)
        self.menuHelp_2.setObjectName("menuHelp_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionLoad_behavioral_sequences = QtWidgets.QAction(MainWindow)
        self.actionLoad_behavioral_sequences.setObjectName("actionLoad_behavioral_sequences")
        self.menuHelp.addAction(self.actionLoad_behavioral_sequences)
        self.menuHelp.addAction(self.actionQuit)
        self.menuHelp_2.addAction(self.actionAbout)
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuHelp_2.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bed intersection"))
        self.label_2.setText(_translate("MainWindow", "<b>Behavioral strings</b>"))
        self.pb_clear_behavioral_strings.setText(_translate("MainWindow", "Clear strings"))
        self.label_17.setText(_translate("MainWindow", "Behaviors separator"))
        self.pb_select_behav_strings_file.setText(_translate("MainWindow", "Load strings from file"))
        self.cb_remove_repeated_behaviors.setText(_translate("MainWindow", "Remove repeated behaviors"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Descriptive statistics</span></p></body></html>"))
        self.pb_statistics.setText(_translate("MainWindow", "Generate statistics"))
        self.pb_save_observed_matrix.setText(_translate("MainWindow", "Transition matrix"))
        self.label_13.setText(_translate("MainWindow", "Results"))
        self.pb_save_stats_results.setText(_translate("MainWindow", "Save results"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_strings), _translate("MainWindow", "Behavioral strings"))
        self.label_8.setText(_translate("MainWindow", "Set cut-off"))
        self.rb_percent_after_behav.setText(_translate("MainWindow", "% of transitions after behavior"))
        self.label_11.setText(_translate("MainWindow", "%"))
        self.rb_percent_total_transitions.setText(_translate("MainWindow", "% of total transitions"))
        self.label_12.setText(_translate("MainWindow", "%"))
        self.label_18.setText(_translate("MainWindow", "Decimals in edges labels"))
        self.cb_plot_significativity.setText(_translate("MainWindow", "Add significativity to edges (perform the permutations test before)"))
        self.label_16.setText(_translate("MainWindow", "Path to dot program (leave empty if dot is on the path)"))
        self.pb_browse_dot_path.setText(_translate("MainWindow", "Browse"))
        self.pb_graphviz_script.setText(_translate("MainWindow", "Generate GraphViz script"))
        self.label_14.setText(_translate("MainWindow", "GraphViz script"))
        self.pb_save_gv.setText(_translate("MainWindow", "Save script"))
        self.pb_flow_diagram.setText(_translate("MainWindow", "Generate flow diagram"))
        self.pb_clear_diagram.setText(_translate("MainWindow", "Clear diagram"))
        self.pb_save_png.setText(_translate("MainWindow", "Save diagram as PNG"))
        self.pb_save_svg.setText(_translate("MainWindow", "Save diagram as SVG"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_flow_diagram), _translate("MainWindow", "Flow diagram"))
        self.cb_block_first_behavior.setText(_translate("MainWindow", "Block first behavior"))
        self.cb_block_last_behavior.setText(_translate("MainWindow", "Block last behavior"))
        self.label_7.setText(_translate("MainWindow", "Excluded transitions"))
        self.pb_exclude_repetition.setText(_translate("MainWindow", "Exclude repeated behaviors"))
        self.pb_clear_excluded_transitions.setText(_translate("MainWindow", "Clear excluded transitions"))
        self.label.setText(_translate("MainWindow", "Number of permutations"))
        self.leNumberRandomizations.setText(_translate("MainWindow", "100"))
        self.label_3.setText(_translate("MainWindow", "Number of cores to use"))
        self.pb_run_permutations_test.setText(_translate("MainWindow", "Run random permutations test"))
        self.label_15.setText(_translate("MainWindow", "P-values matrix"))
        self.pb_save_random.setText(_translate("MainWindow", "Save results"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_randomization), _translate("MainWindow", "Random permutations test"))
        self.pb_levenshtein.setText(_translate("MainWindow", "Levenshtein distances"))
        self.pb_needleman_wunsch.setText(_translate("MainWindow", "Needleman-Wunsch identities"))
        self.label_19.setText(_translate("MainWindow", "Results"))
        self.pb_save_distances.setText(_translate("MainWindow", "Save results"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Behavioral sequences distances"))
        self.menuHelp.setTitle(_translate("MainWindow", "File"))
        self.menuHelp_2.setTitle(_translate("MainWindow", "Help"))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionLoad_behavioral_sequences.setText(_translate("MainWindow", "Open behavioral sequences"))


