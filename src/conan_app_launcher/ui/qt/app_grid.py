# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\sw-dev\product\app_grid_conan\src\conan_app_launcher\ui\qt\app_grid.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(836, 633)
        MainWindow.setAcceptDrops(False)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.tabs.setObjectName("tabs")
        self.tab_1 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_1.sizePolicy().hasHeightForWidth())
        self.tab_1.setSizePolicy(sizePolicy)
        self.tab_1.setObjectName("tab_1")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_1)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tab_scroll_area = QtWidgets.QScrollArea(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_scroll_area.sizePolicy().hasHeightForWidth())
        self.tab_scroll_area.setSizePolicy(sizePolicy)
        self.tab_scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tab_scroll_area.setWidgetResizable(True)
        self.tab_scroll_area.setAlignment(QtCore.Qt.AlignCenter)
        self.tab_scroll_area.setObjectName("tab_scroll_area")
        self.tab_scroll_area_widgets = QtWidgets.QWidget()
        self.tab_scroll_area_widgets.setGeometry(QtCore.QRect(0, 0, 816, 437))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_scroll_area_widgets.sizePolicy().hasHeightForWidth())
        self.tab_scroll_area_widgets.setSizePolicy(sizePolicy)
        self.tab_scroll_area_widgets.setMinimumSize(QtCore.QSize(752, 359))
        self.tab_scroll_area_widgets.setBaseSize(QtCore.QSize(752, 359))
        self.tab_scroll_area_widgets.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tab_scroll_area_widgets.setObjectName("tab_scroll_area_widgets")
        self.tab1_grid_layout = QtWidgets.QGridLayout(self.tab_scroll_area_widgets)
        self.tab1_grid_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.tab1_grid_layout.setObjectName("tab1_grid_layout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tab1_grid_layout.addLayout(self.verticalLayout_4, 0, 1, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.app_button = QtWidgets.QLabel(self.tab_scroll_area_widgets)
        self.app_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.app_button.sizePolicy().hasHeightForWidth())
        self.app_button.setSizePolicy(sizePolicy)
        self.app_button.setText("")
        self.app_button.setPixmap(QtGui.QPixmap("../../assets/default_app_icon.png"))
        self.app_button.setScaledContents(False)
        self.app_button.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.app_button.setObjectName("app_button")
        self.verticalLayout_7.addWidget(self.app_button)
        self.app_name = QtWidgets.QLabel(self.tab_scroll_area_widgets)
        self.app_name.setAlignment(QtCore.Qt.AlignCenter)
        self.app_name.setObjectName("app_name")
        self.verticalLayout_7.addWidget(self.app_name)
        self.app_version = QtWidgets.QComboBox(self.tab_scroll_area_widgets)
        self.app_version.setObjectName("app_version")
        self.verticalLayout_7.addWidget(self.app_version)
        self.tab1_grid_layout.addLayout(self.verticalLayout_7, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tab1_grid_layout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tab1_grid_layout.addLayout(self.verticalLayout_5, 0, 2, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tab1_grid_layout.addLayout(self.verticalLayout_3, 2, 0, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tab1_grid_layout.addLayout(self.verticalLayout_6, 0, 3, 1, 1)
        self.tab1_grid_layout.setColumnMinimumWidth(0, 202)
        self.tab1_grid_layout.setColumnMinimumWidth(1, 202)
        self.tab1_grid_layout.setColumnMinimumWidth(2, 202)
        self.tab1_grid_layout.setColumnMinimumWidth(3, 202)
        self.tab1_grid_layout.setRowMinimumHeight(0, 146)
        self.tab1_grid_layout.setRowMinimumHeight(1, 146)
        self.tab1_grid_layout.setRowMinimumHeight(2, 146)
        self.tab1_grid_layout.setColumnStretch(0, 1)
        self.tab1_grid_layout.setColumnStretch(1, 1)
        self.tab1_grid_layout.setColumnStretch(2, 1)
        self.tab1_grid_layout.setColumnStretch(3, 1)
        self.tab1_grid_layout.setRowStretch(0, 1)
        self.tab1_grid_layout.setRowStretch(1, 1)
        self.tab1_grid_layout.setRowStretch(2, 1)
        self.tab_scroll_area.setWidget(self.tab_scroll_area_widgets)
        self.verticalLayout_8.addWidget(self.tab_scroll_area)
        self.tabs.addTab(self.tab_1, "")
        self.verticalLayout.addWidget(self.tabs)
        self.console = QtWidgets.QTextBrowser(self.centralwidget)
        self.console.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.console.setFrameShadow(QtWidgets.QFrame.Raised)
        self.console.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.console.setReadOnly(True)
        self.console.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:7.875pt;\"><br /></p></body></html>")
        self.console.setTabStopWidth(200)
        self.console.setObjectName("console")
        self.verticalLayout.addWidget(self.console)
        self.verticalLayout.setStretch(0, 4)
        self.verticalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menu_bar = QtWidgets.QMenuBar(MainWindow)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 836, 20))
        self.menu_bar.setObjectName("menu_bar")
        self.menu_help = QtWidgets.QMenu(self.menu_bar)
        self.menu_help.setObjectName("menu_help")
        self.menu_file = QtWidgets.QMenu(self.menu_bar)
        self.menu_file.setObjectName("menu_file")
        self.menuView = QtWidgets.QMenu(self.menu_bar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menu_bar)
        self.menu_about_action = QtWidgets.QAction(MainWindow)
        self.menu_about_action.setObjectName("menu_about_action")
        self.menu_open_config_file_action = QtWidgets.QAction(MainWindow)
        self.menu_open_config_file_action.setObjectName("menu_open_config_file_action")
        self.menu_set_display_versions = QtWidgets.QAction(MainWindow)
        self.menu_set_display_versions.setCheckable(True)
        self.menu_set_display_versions.setChecked(True)
        self.menu_set_display_versions.setObjectName("menu_set_display_versions")
        self.menu_set_display_channels = QtWidgets.QAction(MainWindow)
        self.menu_set_display_channels.setCheckable(True)
        self.menu_set_display_channels.setChecked(True)
        self.menu_set_display_channels.setObjectName("menu_set_display_channels")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionAuto_Install = QtWidgets.QAction(MainWindow)
        self.actionAuto_Install.setObjectName("actionAuto_Install")
        self.menu_help.addAction(self.menu_about_action)
        self.menu_file.addAction(self.menu_open_config_file_action)
        self.menuView.addAction(self.menu_set_display_versions)
        self.menuView.addAction(self.menu_set_display_channels)
        self.menuView.addSeparator()
        self.menu_bar.addAction(self.menu_file.menuAction())
        self.menu_bar.addAction(self.menuView.menuAction())
        self.menu_bar.addAction(self.menu_help.menuAction())

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Conan App Launcher"))
        self.app_name.setText(_translate("MainWindow", "TextLabel"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_1), _translate("MainWindow", "Basics"))
        self.menu_help.setTitle(_translate("MainWindow", "Help"))
        self.menu_file.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menu_about_action.setText(_translate("MainWindow", "About"))
        self.menu_open_config_file_action.setText(_translate("MainWindow", "Open Config File"))
        self.menu_set_display_versions.setText(_translate("MainWindow", "Display versions"))
        self.menu_set_display_channels.setText(_translate("MainWindow", "Display channels"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionAuto_Install.setText(_translate("MainWindow", "Auto Install"))
