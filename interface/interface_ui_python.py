# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'material_statEbhVZW.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(632, 851)
        font = QFont()
        font.setBold(False)
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        MainWindow.setTabShape(QTabWidget.TabShape.Triangular)
        MainWindow.setDockOptions(QMainWindow.DockOption.AllowTabbedDocks|QMainWindow.DockOption.AnimatedDocks|QMainWindow.DockOption.VerticalTabs)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.side_v_layout = QVBoxLayout()
        self.side_v_layout.setSpacing(0)
        self.side_v_layout.setObjectName(u"side_v_layout")
        self.storage_status_btn = QPushButton(self.centralwidget)
        self.storage_status_btn.setObjectName(u"storage_status_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.storage_status_btn.sizePolicy().hasHeightForWidth())
        self.storage_status_btn.setSizePolicy(sizePolicy)
        self.storage_status_btn.setMinimumSize(QSize(56, 0))
        self.storage_status_btn.setStyleSheet(u"background-color: rgba(175, 227, 255, 0);\n"
"border-color: rgba(255, 255, 255, 0);")

        self.side_v_layout.addWidget(self.storage_status_btn)

        self.recipe_btn = QPushButton(self.centralwidget)
        self.recipe_btn.setObjectName(u"recipe_btn")
        sizePolicy.setHeightForWidth(self.recipe_btn.sizePolicy().hasHeightForWidth())
        self.recipe_btn.setSizePolicy(sizePolicy)
        self.recipe_btn.setMinimumSize(QSize(56, 0))
        self.recipe_btn.setStyleSheet(u"background-color: rgba(175, 227, 255, 0);\n"
"border-color: rgba(255, 255, 255, 0);")

        self.side_v_layout.addWidget(self.recipe_btn)

        self.show_help_btn = QPushButton(self.centralwidget)
        self.show_help_btn.setObjectName(u"show_help_btn")
        sizePolicy.setHeightForWidth(self.show_help_btn.sizePolicy().hasHeightForWidth())
        self.show_help_btn.setSizePolicy(sizePolicy)
        self.show_help_btn.setMinimumSize(QSize(56, 0))
        font1 = QFont()
        font1.setPointSize(30)
        font1.setBold(False)
        self.show_help_btn.setFont(font1)
        self.show_help_btn.setStyleSheet(u"background-color: rgba(175, 227, 255, 0);\n"
"border-color: rgba(255, 255, 255, 0);")

        self.side_v_layout.addWidget(self.show_help_btn)

        self.setting_btn = QPushButton(self.centralwidget)
        self.setting_btn.setObjectName(u"setting_btn")
        sizePolicy.setHeightForWidth(self.setting_btn.sizePolicy().hasHeightForWidth())
        self.setting_btn.setSizePolicy(sizePolicy)
        self.setting_btn.setMinimumSize(QSize(56, 24))
        self.setting_btn.setFont(font1)
        self.setting_btn.setStyleSheet(u"background-color: rgba(175, 227, 255, 0);\n"
"border-color: rgba(255, 255, 255, 0);\n"
"")

        self.side_v_layout.addWidget(self.setting_btn)

        self.side_v_layout.setStretch(0, 1)
        self.side_v_layout.setStretch(1, 1)

        self.gridLayout.addLayout(self.side_v_layout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tab_root = QTabWidget(self.centralwidget)
        self.tab_root.setObjectName(u"tab_root")
        self.tab_root.setTabBarAutoHide(False)
        self.storage_tab = QWidget()
        self.storage_tab.setObjectName(u"storage_tab")
        self.verticalLayout = QVBoxLayout(self.storage_tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalFrame_3 = QFrame(self.storage_tab)
        self.horizontalFrame_3.setObjectName(u"horizontalFrame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.horizontalFrame_3.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_3.setSizePolicy(sizePolicy1)
        self.horizontalFrame_3.setMinimumSize(QSize(0, 65))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalFrame_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.ref_add_self_btn = QPushButton(self.horizontalFrame_3)
        self.ref_add_self_btn.setObjectName(u"ref_add_self_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ref_add_self_btn.sizePolicy().hasHeightForWidth())
        self.ref_add_self_btn.setSizePolicy(sizePolicy2)
        self.ref_add_self_btn.setMinimumSize(QSize(200, 0))
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(False)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.ref_add_self_btn.setFont(font2)

        self.horizontalLayout_5.addWidget(self.ref_add_self_btn)

        self.fav_ch_btn = QPushButton(self.horizontalFrame_3)
        self.fav_ch_btn.setObjectName(u"fav_ch_btn")
        sizePolicy2.setHeightForWidth(self.fav_ch_btn.sizePolicy().hasHeightForWidth())
        self.fav_ch_btn.setSizePolicy(sizePolicy2)
        self.fav_ch_btn.setMinimumSize(QSize(200, 0))
        self.fav_ch_btn.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.fav_ch_btn)

        self.open_search_manage_modal_btn = QPushButton(self.horizontalFrame_3)
        self.open_search_manage_modal_btn.setObjectName(u"open_search_manage_modal_btn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.open_search_manage_modal_btn.sizePolicy().hasHeightForWidth())
        self.open_search_manage_modal_btn.setSizePolicy(sizePolicy3)

        self.horizontalLayout_5.addWidget(self.open_search_manage_modal_btn)


        self.verticalLayout.addWidget(self.horizontalFrame_3)

        self.gridWidget_2 = QWidget(self.storage_tab)
        self.gridWidget_2.setObjectName(u"gridWidget_2")
        self.gridLayout_4 = QGridLayout(self.gridWidget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.other_scrollarea = QScrollArea(self.gridWidget_2)
        self.other_scrollarea.setObjectName(u"other_scrollarea")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.other_scrollarea.sizePolicy().hasHeightForWidth())
        self.other_scrollarea.setSizePolicy(sizePolicy4)
        self.other_scrollarea.setMinimumSize(QSize(190, 295))
        self.other_scrollarea.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.other_scrollarea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.other_scrollarea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_19 = QWidget()
        self.scrollAreaWidgetContents_19.setObjectName(u"scrollAreaWidgetContents_19")
        self.scrollAreaWidgetContents_19.setGeometry(QRect(0, 0, 231, 440))
        self.verticalLayout_29 = QVBoxLayout(self.scrollAreaWidgetContents_19)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_17 = QLabel(self.scrollAreaWidgetContents_19)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_22.addWidget(self.label_17)

        self.horizontalSpacer_17 = QSpacerItem(150, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_17)

        self.show_search_box_btn_3 = QPushButton(self.scrollAreaWidgetContents_19)
        self.show_search_box_btn_3.setObjectName(u"show_search_box_btn_3")
        sizePolicy2.setHeightForWidth(self.show_search_box_btn_3.sizePolicy().hasHeightForWidth())
        self.show_search_box_btn_3.setSizePolicy(sizePolicy2)
        self.show_search_box_btn_3.setMinimumSize(QSize(5, 24))

        self.horizontalLayout_22.addWidget(self.show_search_box_btn_3)

        self.other_sort_btn = QPushButton(self.scrollAreaWidgetContents_19)
        self.other_sort_btn.setObjectName(u"other_sort_btn")
        sizePolicy4.setHeightForWidth(self.other_sort_btn.sizePolicy().hasHeightForWidth())
        self.other_sort_btn.setSizePolicy(sizePolicy4)
        self.other_sort_btn.setMinimumSize(QSize(13, 0))

        self.horizontalLayout_22.addWidget(self.other_sort_btn)


        self.verticalLayout_29.addLayout(self.horizontalLayout_22)

        self.search_frame_3 = QFrame(self.scrollAreaWidgetContents_19)
        self.search_frame_3.setObjectName(u"search_frame_3")
        self.horizontalLayout_4 = QHBoxLayout(self.search_frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.ref_search_box_3 = QLineEdit(self.search_frame_3)
        self.ref_search_box_3.setObjectName(u"ref_search_box_3")
        sizePolicy.setHeightForWidth(self.ref_search_box_3.sizePolicy().hasHeightForWidth())
        self.ref_search_box_3.setSizePolicy(sizePolicy)
        self.ref_search_box_3.setMinimumSize(QSize(160, 0))

        self.horizontalLayout_4.addWidget(self.ref_search_box_3)

        self.ref_search_btn_3 = QPushButton(self.search_frame_3)
        self.ref_search_btn_3.setObjectName(u"ref_search_btn_3")
        sizePolicy2.setHeightForWidth(self.ref_search_btn_3.sizePolicy().hasHeightForWidth())
        self.ref_search_btn_3.setSizePolicy(sizePolicy2)
        self.ref_search_btn_3.setMinimumSize(QSize(5, 24))

        self.horizontalLayout_4.addWidget(self.ref_search_btn_3)


        self.verticalLayout_29.addWidget(self.search_frame_3)

        self.groupBox_16 = QGroupBox(self.scrollAreaWidgetContents_19)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.gridLayout_18 = QGridLayout(self.groupBox_16)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.textBrowser_118 = QTextBrowser(self.groupBox_16)
        self.textBrowser_118.setObjectName(u"textBrowser_118")
        self.textBrowser_118.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.textBrowser_118.sizePolicy().hasHeightForWidth())
        self.textBrowser_118.setSizePolicy(sizePolicy4)
        self.textBrowser_118.setMinimumSize(QSize(155, 90))

        self.gridLayout_18.addWidget(self.textBrowser_118, 0, 0, 1, 1)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.pushButton_31 = QPushButton(self.groupBox_16)
        self.pushButton_31.setObjectName(u"pushButton_31")
        sizePolicy4.setHeightForWidth(self.pushButton_31.sizePolicy().hasHeightForWidth())
        self.pushButton_31.setSizePolicy(sizePolicy4)
        self.pushButton_31.setMinimumSize(QSize(30, 40))

        self.verticalLayout_23.addWidget(self.pushButton_31)

        self.pushButton_32 = QPushButton(self.groupBox_16)
        self.pushButton_32.setObjectName(u"pushButton_32")
        sizePolicy4.setHeightForWidth(self.pushButton_32.sizePolicy().hasHeightForWidth())
        self.pushButton_32.setSizePolicy(sizePolicy4)
        self.pushButton_32.setMinimumSize(QSize(30, 20))

        self.verticalLayout_23.addWidget(self.pushButton_32)


        self.gridLayout_18.addLayout(self.verticalLayout_23, 0, 1, 1, 1)


        self.verticalLayout_29.addWidget(self.groupBox_16)

        self.groupBox_17 = QGroupBox(self.scrollAreaWidgetContents_19)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.gridLayout_19 = QGridLayout(self.groupBox_17)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.textBrowser_119 = QTextBrowser(self.groupBox_17)
        self.textBrowser_119.setObjectName(u"textBrowser_119")
        self.textBrowser_119.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.textBrowser_119.sizePolicy().hasHeightForWidth())
        self.textBrowser_119.setSizePolicy(sizePolicy4)
        self.textBrowser_119.setMinimumSize(QSize(155, 90))

        self.gridLayout_19.addWidget(self.textBrowser_119, 0, 0, 1, 1)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.pushButton_33 = QPushButton(self.groupBox_17)
        self.pushButton_33.setObjectName(u"pushButton_33")
        sizePolicy4.setHeightForWidth(self.pushButton_33.sizePolicy().hasHeightForWidth())
        self.pushButton_33.setSizePolicy(sizePolicy4)
        self.pushButton_33.setMinimumSize(QSize(30, 40))

        self.verticalLayout_24.addWidget(self.pushButton_33)

        self.pushButton_34 = QPushButton(self.groupBox_17)
        self.pushButton_34.setObjectName(u"pushButton_34")
        sizePolicy4.setHeightForWidth(self.pushButton_34.sizePolicy().hasHeightForWidth())
        self.pushButton_34.setSizePolicy(sizePolicy4)
        self.pushButton_34.setMinimumSize(QSize(30, 20))

        self.verticalLayout_24.addWidget(self.pushButton_34)


        self.gridLayout_19.addLayout(self.verticalLayout_24, 0, 1, 1, 1)


        self.verticalLayout_29.addWidget(self.groupBox_17)

        self.groupBox_18 = QGroupBox(self.scrollAreaWidgetContents_19)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.gridLayout_20 = QGridLayout(self.groupBox_18)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.textBrowser_120 = QTextBrowser(self.groupBox_18)
        self.textBrowser_120.setObjectName(u"textBrowser_120")
        self.textBrowser_120.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.textBrowser_120.sizePolicy().hasHeightForWidth())
        self.textBrowser_120.setSizePolicy(sizePolicy4)
        self.textBrowser_120.setMinimumSize(QSize(155, 90))

        self.gridLayout_20.addWidget(self.textBrowser_120, 0, 0, 1, 1)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.pushButton_35 = QPushButton(self.groupBox_18)
        self.pushButton_35.setObjectName(u"pushButton_35")
        sizePolicy4.setHeightForWidth(self.pushButton_35.sizePolicy().hasHeightForWidth())
        self.pushButton_35.setSizePolicy(sizePolicy4)
        self.pushButton_35.setMinimumSize(QSize(30, 40))

        self.verticalLayout_25.addWidget(self.pushButton_35)

        self.pushButton_36 = QPushButton(self.groupBox_18)
        self.pushButton_36.setObjectName(u"pushButton_36")
        sizePolicy4.setHeightForWidth(self.pushButton_36.sizePolicy().hasHeightForWidth())
        self.pushButton_36.setSizePolicy(sizePolicy4)
        self.pushButton_36.setMinimumSize(QSize(30, 20))

        self.verticalLayout_25.addWidget(self.pushButton_36)


        self.gridLayout_20.addLayout(self.verticalLayout_25, 0, 1, 1, 1)


        self.verticalLayout_29.addWidget(self.groupBox_18)

        self.other_scrollarea.setWidget(self.scrollAreaWidgetContents_19)

        self.gridLayout_4.addWidget(self.other_scrollarea, 2, 1, 1, 1)

        self.meat_scrollarea = QScrollArea(self.gridWidget_2)
        self.meat_scrollarea.setObjectName(u"meat_scrollarea")
        sizePolicy4.setHeightForWidth(self.meat_scrollarea.sizePolicy().hasHeightForWidth())
        self.meat_scrollarea.setSizePolicy(sizePolicy4)
        self.meat_scrollarea.setMinimumSize(QSize(190, 295))
        self.meat_scrollarea.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.meat_scrollarea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.meat_scrollarea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_18 = QWidget()
        self.scrollAreaWidgetContents_18.setObjectName(u"scrollAreaWidgetContents_18")
        self.scrollAreaWidgetContents_18.setGeometry(QRect(0, 0, 249, 458))
        self.verticalLayout_28 = QVBoxLayout(self.scrollAreaWidgetContents_18)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_16 = QLabel(self.scrollAreaWidgetContents_18)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_21.addWidget(self.label_16)

        self.horizontalSpacer_16 = QSpacerItem(150, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_16)

        self.show_search_box_btn_1 = QPushButton(self.scrollAreaWidgetContents_18)
        self.show_search_box_btn_1.setObjectName(u"show_search_box_btn_1")
        sizePolicy2.setHeightForWidth(self.show_search_box_btn_1.sizePolicy().hasHeightForWidth())
        self.show_search_box_btn_1.setSizePolicy(sizePolicy2)
        self.show_search_box_btn_1.setMinimumSize(QSize(5, 24))

        self.horizontalLayout_21.addWidget(self.show_search_box_btn_1)

        self.meat_sort_btn = QPushButton(self.scrollAreaWidgetContents_18)
        self.meat_sort_btn.setObjectName(u"meat_sort_btn")
        sizePolicy4.setHeightForWidth(self.meat_sort_btn.sizePolicy().hasHeightForWidth())
        self.meat_sort_btn.setSizePolicy(sizePolicy4)
        self.meat_sort_btn.setMinimumSize(QSize(13, 0))

        self.horizontalLayout_21.addWidget(self.meat_sort_btn)


        self.verticalLayout_28.addLayout(self.horizontalLayout_21)

        self.search_frame_1 = QFrame(self.scrollAreaWidgetContents_18)
        self.search_frame_1.setObjectName(u"search_frame_1")
        self.horizontalLayout = QHBoxLayout(self.search_frame_1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ref_search_box_1 = QLineEdit(self.search_frame_1)
        self.ref_search_box_1.setObjectName(u"ref_search_box_1")
        sizePolicy.setHeightForWidth(self.ref_search_box_1.sizePolicy().hasHeightForWidth())
        self.ref_search_box_1.setSizePolicy(sizePolicy)
        self.ref_search_box_1.setMinimumSize(QSize(160, 0))

        self.horizontalLayout.addWidget(self.ref_search_box_1)

        self.ref_search_btn_1 = QPushButton(self.search_frame_1)
        self.ref_search_btn_1.setObjectName(u"ref_search_btn_1")
        sizePolicy2.setHeightForWidth(self.ref_search_btn_1.sizePolicy().hasHeightForWidth())
        self.ref_search_btn_1.setSizePolicy(sizePolicy2)
        self.ref_search_btn_1.setMinimumSize(QSize(5, 24))

        self.horizontalLayout.addWidget(self.ref_search_btn_1)


        self.verticalLayout_28.addWidget(self.search_frame_1)

        self.verticalWidget = QWidget(self.scrollAreaWidgetContents_18)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalLayout_5 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_1 = QGroupBox(self.verticalWidget)
        self.groupBox_1.setObjectName(u"groupBox_1")
        self.gridLayout_2 = QGridLayout(self.groupBox_1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.textBrowser_1 = QTextBrowser(self.groupBox_1)
        self.textBrowser_1.setObjectName(u"textBrowser_1")
        self.textBrowser_1.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.textBrowser_1.sizePolicy().hasHeightForWidth())
        self.textBrowser_1.setSizePolicy(sizePolicy4)
        self.textBrowser_1.setMinimumSize(QSize(155, 90))

        self.gridLayout_2.addWidget(self.textBrowser_1, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton = QPushButton(self.groupBox_1)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy4.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy4)
        self.pushButton.setMinimumSize(QSize(30, 40))

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.groupBox_1)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy4.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy4)
        self.pushButton_2.setMinimumSize(QSize(30, 20))

        self.verticalLayout_2.addWidget(self.pushButton_2)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 1, 1, 1)


        self.verticalLayout_5.addWidget(self.groupBox_1)

        self.groupBox_5 = QGroupBox(self.verticalWidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_7 = QGridLayout(self.groupBox_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.textBrowser_2 = QTextBrowser(self.groupBox_5)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.textBrowser_2.sizePolicy().hasHeightForWidth())
        self.textBrowser_2.setSizePolicy(sizePolicy4)
        self.textBrowser_2.setMinimumSize(QSize(155, 90))

        self.gridLayout_7.addWidget(self.textBrowser_2, 0, 0, 1, 1)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.pushButton_9 = QPushButton(self.groupBox_5)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy4.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy4)
        self.pushButton_9.setMinimumSize(QSize(30, 40))

        self.verticalLayout_12.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.groupBox_5)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy4.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy4)
        self.pushButton_10.setMinimumSize(QSize(30, 20))

        self.verticalLayout_12.addWidget(self.pushButton_10)


        self.gridLayout_7.addLayout(self.verticalLayout_12, 0, 1, 1, 1)


        self.verticalLayout_5.addWidget(self.groupBox_5)

        self.groupBox_2 = QGroupBox(self.verticalWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.textBrowser_3 = QTextBrowser(self.groupBox_2)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.textBrowser_3.sizePolicy().hasHeightForWidth())
        self.textBrowser_3.setSizePolicy(sizePolicy4)
        self.textBrowser_3.setMinimumSize(QSize(155, 90))

        self.gridLayout_3.addWidget(self.textBrowser_3, 0, 0, 1, 1)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.pushButton_3 = QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy4.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy4)
        self.pushButton_3.setMinimumSize(QSize(30, 40))

        self.verticalLayout_9.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.groupBox_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy4.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy4)
        self.pushButton_4.setMinimumSize(QSize(30, 20))

        self.verticalLayout_9.addWidget(self.pushButton_4)


        self.gridLayout_3.addLayout(self.verticalLayout_9, 0, 1, 1, 1)


        self.verticalLayout_5.addWidget(self.groupBox_2)


        self.verticalLayout_28.addWidget(self.verticalWidget)

        self.meat_scrollarea.setWidget(self.scrollAreaWidgetContents_18)

        self.gridLayout_4.addWidget(self.meat_scrollarea, 0, 0, 1, 1)

        self.fishes_scrollarea = QScrollArea(self.gridWidget_2)
        self.fishes_scrollarea.setObjectName(u"fishes_scrollarea")
        sizePolicy4.setHeightForWidth(self.fishes_scrollarea.sizePolicy().hasHeightForWidth())
        self.fishes_scrollarea.setSizePolicy(sizePolicy4)
        self.fishes_scrollarea.setMinimumSize(QSize(190, 295))
        self.fishes_scrollarea.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.fishes_scrollarea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.fishes_scrollarea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_20 = QWidget()
        self.scrollAreaWidgetContents_20.setObjectName(u"scrollAreaWidgetContents_20")
        self.scrollAreaWidgetContents_20.setGeometry(QRect(0, 0, 245, 672))
        self.verticalLayout_30 = QVBoxLayout(self.scrollAreaWidgetContents_20)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_18 = QLabel(self.scrollAreaWidgetContents_20)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_23.addWidget(self.label_18)

        self.horizontalSpacer_18 = QSpacerItem(150, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_18)

        self.show_search_box_btn_4 = QPushButton(self.scrollAreaWidgetContents_20)
        self.show_search_box_btn_4.setObjectName(u"show_search_box_btn_4")
        sizePolicy2.setHeightForWidth(self.show_search_box_btn_4.sizePolicy().hasHeightForWidth())
        self.show_search_box_btn_4.setSizePolicy(sizePolicy2)
        self.show_search_box_btn_4.setMinimumSize(QSize(5, 24))

        self.horizontalLayout_23.addWidget(self.show_search_box_btn_4)

        self.sea_food_sort_btn = QPushButton(self.scrollAreaWidgetContents_20)
        self.sea_food_sort_btn.setObjectName(u"sea_food_sort_btn")
        sizePolicy4.setHeightForWidth(self.sea_food_sort_btn.sizePolicy().hasHeightForWidth())
        self.sea_food_sort_btn.setSizePolicy(sizePolicy4)
        self.sea_food_sort_btn.setMinimumSize(QSize(13, 0))

        self.horizontalLayout_23.addWidget(self.sea_food_sort_btn)


        self.verticalLayout_30.addLayout(self.horizontalLayout_23)

        self.search_frame_4 = QFrame(self.scrollAreaWidgetContents_20)
        self.search_frame_4.setObjectName(u"search_frame_4")
        self.horizontalLayout_6 = QHBoxLayout(self.search_frame_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.ref_search_box_4 = QLineEdit(self.search_frame_4)
        self.ref_search_box_4.setObjectName(u"ref_search_box_4")
        sizePolicy.setHeightForWidth(self.ref_search_box_4.sizePolicy().hasHeightForWidth())
        self.ref_search_box_4.setSizePolicy(sizePolicy)
        self.ref_search_box_4.setMinimumSize(QSize(160, 0))

        self.horizontalLayout_6.addWidget(self.ref_search_box_4)

        self.ref_search_btn_4 = QPushButton(self.search_frame_4)
        self.ref_search_btn_4.setObjectName(u"ref_search_btn_4")
        sizePolicy2.setHeightForWidth(self.ref_search_btn_4.sizePolicy().hasHeightForWidth())
        self.ref_search_btn_4.setSizePolicy(sizePolicy2)
        self.ref_search_btn_4.setMinimumSize(QSize(5, 24))

        self.horizontalLayout_6.addWidget(self.ref_search_btn_4)


        self.verticalLayout_30.addWidget(self.search_frame_4)

        self.groupBox_12 = QGroupBox(self.scrollAreaWidgetContents_20)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.gridLayout_14 = QGridLayout(self.groupBox_12)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.textBrowser_114 = QTextBrowser(self.groupBox_12)
        self.textBrowser_114.setObjectName(u"textBrowser_114")
        self.textBrowser_114.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.textBrowser_114.sizePolicy().hasHeightForWidth())
        self.textBrowser_114.setSizePolicy(sizePolicy4)
        self.textBrowser_114.setMinimumSize(QSize(155, 90))

        self.gridLayout_14.addWidget(self.textBrowser_114, 0, 0, 1, 1)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.pushButton_23 = QPushButton(self.groupBox_12)
        self.pushButton_23.setObjectName(u"pushButton_23")
        sizePolicy4.setHeightForWidth(self.pushButton_23.sizePolicy().hasHeightForWidth())
        self.pushButton_23.setSizePolicy(sizePolicy4)
        self.pushButton_23.setMinimumSize(QSize(30, 40))

        self.verticalLayout_19.addWidget(self.pushButton_23)

        self.pushButton_24 = QPushButton(self.groupBox_12)
        self.pushButton_24.setObjectName(u"pushButton_24")
        sizePolicy4.setHeightForWidth(self.pushButton_24.sizePolicy().hasHeightForWidth())
        self.pushButton_24.setSizePolicy(sizePolicy4)
        self.pushButton_24.setMinimumSize(QSize(30, 20))

        self.verticalLayout_19.addWidget(self.pushButton_24)


        self.gridLayout_14.addLayout(self.verticalLayout_19, 0, 1, 1, 1)


        self.verticalLayout_30.addWidget(self.groupBox_12)

        self.groupBox_11 = QGroupBox(self.scrollAreaWidgetContents_20)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.gridLayout_13 = QGridLayout(self.groupBox_11)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.textBrowser_113 = QTextBrowser(self.groupBox_11)
        self.textBrowser_113.setObjectName(u"textBrowser_113")
        self.textBrowser_113.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.textBrowser_113.sizePolicy().hasHeightForWidth())
        self.textBrowser_113.setSizePolicy(sizePolicy4)
        self.textBrowser_113.setMinimumSize(QSize(155, 90))

        self.gridLayout_13.addWidget(self.textBrowser_113, 0, 0, 1, 1)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.pushButton_21 = QPushButton(self.groupBox_11)
        self.pushButton_21.setObjectName(u"pushButton_21")
        sizePolicy4.setHeightForWidth(self.pushButton_21.sizePolicy().hasHeightForWidth())
        self.pushButton_21.setSizePolicy(sizePolicy4)
        self.pushButton_21.setMinimumSize(QSize(30, 40))

        self.verticalLayout_18.addWidget(self.pushButton_21)

        self.pushButton_22 = QPushButton(self.groupBox_11)
        self.pushButton_22.setObjectName(u"pushButton_22")
        sizePolicy4.setHeightForWidth(self.pushButton_22.sizePolicy().hasHeightForWidth())
        self.pushButton_22.setSizePolicy(sizePolicy4)
        self.pushButton_22.setMinimumSize(QSize(30, 20))

        self.verticalLayout_18.addWidget(self.pushButton_22)


        self.gridLayout_13.addLayout(self.verticalLayout_18, 0, 1, 1, 1)


        self.verticalLayout_30.addWidget(self.groupBox_11)

        self.groupBox_14 = QGroupBox(self.scrollAreaWidgetContents_20)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.gridLayout_16 = QGridLayout(self.groupBox_14)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.textBrowser_116 = QTextBrowser(self.groupBox_14)
        self.textBrowser_116.setObjectName(u"textBrowser_116")
        self.textBrowser_116.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.textBrowser_116.sizePolicy().hasHeightForWidth())
        self.textBrowser_116.setSizePolicy(sizePolicy4)
        self.textBrowser_116.setMinimumSize(QSize(155, 90))

        self.gridLayout_16.addWidget(self.textBrowser_116, 0, 0, 1, 1)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.pushButton_27 = QPushButton(self.groupBox_14)
        self.pushButton_27.setObjectName(u"pushButton_27")
        sizePolicy4.setHeightForWidth(self.pushButton_27.sizePolicy().hasHeightForWidth())
        self.pushButton_27.setSizePolicy(sizePolicy4)
        self.pushButton_27.setMinimumSize(QSize(30, 40))

        self.verticalLayout_21.addWidget(self.pushButton_27)

        self.pushButton_28 = QPushButton(self.groupBox_14)
        self.pushButton_28.setObjectName(u"pushButton_28")
        sizePolicy4.setHeightForWidth(self.pushButton_28.sizePolicy().hasHeightForWidth())
        self.pushButton_28.setSizePolicy(sizePolicy4)
        self.pushButton_28.setMinimumSize(QSize(30, 20))

        self.verticalLayout_21.addWidget(self.pushButton_28)


        self.gridLayout_16.addLayout(self.verticalLayout_21, 0, 1, 1, 1)


        self.verticalLayout_30.addWidget(self.groupBox_14)

        self.groupBox_15 = QGroupBox(self.scrollAreaWidgetContents_20)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.gridLayout_17 = QGridLayout(self.groupBox_15)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.textBrowser_117 = QTextBrowser(self.groupBox_15)
        self.textBrowser_117.setObjectName(u"textBrowser_117")
        self.textBrowser_117.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.textBrowser_117.sizePolicy().hasHeightForWidth())
        self.textBrowser_117.setSizePolicy(sizePolicy4)
        self.textBrowser_117.setMinimumSize(QSize(155, 90))

        self.gridLayout_17.addWidget(self.textBrowser_117, 0, 0, 1, 1)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.pushButton_29 = QPushButton(self.groupBox_15)
        self.pushButton_29.setObjectName(u"pushButton_29")
        sizePolicy4.setHeightForWidth(self.pushButton_29.sizePolicy().hasHeightForWidth())
        self.pushButton_29.setSizePolicy(sizePolicy4)
        self.pushButton_29.setMinimumSize(QSize(30, 40))

        self.verticalLayout_22.addWidget(self.pushButton_29)

        self.pushButton_30 = QPushButton(self.groupBox_15)
        self.pushButton_30.setObjectName(u"pushButton_30")
        sizePolicy4.setHeightForWidth(self.pushButton_30.sizePolicy().hasHeightForWidth())
        self.pushButton_30.setSizePolicy(sizePolicy4)
        self.pushButton_30.setMinimumSize(QSize(30, 20))

        self.verticalLayout_22.addWidget(self.pushButton_30)


        self.gridLayout_17.addLayout(self.verticalLayout_22, 0, 1, 1, 1)


        self.verticalLayout_30.addWidget(self.groupBox_15)

        self.groupBox_13 = QGroupBox(self.scrollAreaWidgetContents_20)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.gridLayout_15 = QGridLayout(self.groupBox_13)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.textBrowser_115 = QTextBrowser(self.groupBox_13)
        self.textBrowser_115.setObjectName(u"textBrowser_115")
        self.textBrowser_115.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.textBrowser_115.sizePolicy().hasHeightForWidth())
        self.textBrowser_115.setSizePolicy(sizePolicy4)
        self.textBrowser_115.setMinimumSize(QSize(155, 90))

        self.gridLayout_15.addWidget(self.textBrowser_115, 0, 0, 1, 1)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.pushButton_25 = QPushButton(self.groupBox_13)
        self.pushButton_25.setObjectName(u"pushButton_25")
        sizePolicy4.setHeightForWidth(self.pushButton_25.sizePolicy().hasHeightForWidth())
        self.pushButton_25.setSizePolicy(sizePolicy4)
        self.pushButton_25.setMinimumSize(QSize(30, 40))

        self.verticalLayout_20.addWidget(self.pushButton_25)

        self.pushButton_26 = QPushButton(self.groupBox_13)
        self.pushButton_26.setObjectName(u"pushButton_26")
        sizePolicy4.setHeightForWidth(self.pushButton_26.sizePolicy().hasHeightForWidth())
        self.pushButton_26.setSizePolicy(sizePolicy4)
        self.pushButton_26.setMinimumSize(QSize(30, 20))

        self.verticalLayout_20.addWidget(self.pushButton_26)


        self.gridLayout_15.addLayout(self.verticalLayout_20, 0, 1, 1, 1)


        self.verticalLayout_30.addWidget(self.groupBox_13)

        self.fishes_scrollarea.setWidget(self.scrollAreaWidgetContents_20)

        self.gridLayout_4.addWidget(self.fishes_scrollarea, 2, 0, 1, 1)

        self.vegetable_scrollarea = QScrollArea(self.gridWidget_2)
        self.vegetable_scrollarea.setObjectName(u"vegetable_scrollarea")
        sizePolicy4.setHeightForWidth(self.vegetable_scrollarea.sizePolicy().hasHeightForWidth())
        self.vegetable_scrollarea.setSizePolicy(sizePolicy4)
        self.vegetable_scrollarea.setMinimumSize(QSize(190, 295))
        self.vegetable_scrollarea.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.vegetable_scrollarea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.vegetable_scrollarea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_17 = QWidget()
        self.scrollAreaWidgetContents_17.setObjectName(u"scrollAreaWidgetContents_17")
        self.scrollAreaWidgetContents_17.setGeometry(QRect(0, 0, 231, 672))
        self.verticalLayout_27 = QVBoxLayout(self.scrollAreaWidgetContents_17)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_15 = QLabel(self.scrollAreaWidgetContents_17)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_20.addWidget(self.label_15)

        self.horizontalSpacer_15 = QSpacerItem(107, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_15)

        self.show_search_box_btn_2 = QPushButton(self.scrollAreaWidgetContents_17)
        self.show_search_box_btn_2.setObjectName(u"show_search_box_btn_2")
        sizePolicy2.setHeightForWidth(self.show_search_box_btn_2.sizePolicy().hasHeightForWidth())
        self.show_search_box_btn_2.setSizePolicy(sizePolicy2)
        self.show_search_box_btn_2.setMinimumSize(QSize(5, 24))

        self.horizontalLayout_20.addWidget(self.show_search_box_btn_2)

        self.fruit_vegetable_sort_btn = QPushButton(self.scrollAreaWidgetContents_17)
        self.fruit_vegetable_sort_btn.setObjectName(u"fruit_vegetable_sort_btn")
        sizePolicy4.setHeightForWidth(self.fruit_vegetable_sort_btn.sizePolicy().hasHeightForWidth())
        self.fruit_vegetable_sort_btn.setSizePolicy(sizePolicy4)
        self.fruit_vegetable_sort_btn.setMinimumSize(QSize(13, 0))

        self.horizontalLayout_20.addWidget(self.fruit_vegetable_sort_btn)


        self.verticalLayout_27.addLayout(self.horizontalLayout_20)

        self.search_frame_2 = QFrame(self.scrollAreaWidgetContents_17)
        self.search_frame_2.setObjectName(u"search_frame_2")
        self.horizontalLayout_3 = QHBoxLayout(self.search_frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.ref_search_box_2 = QLineEdit(self.search_frame_2)
        self.ref_search_box_2.setObjectName(u"ref_search_box_2")
        sizePolicy.setHeightForWidth(self.ref_search_box_2.sizePolicy().hasHeightForWidth())
        self.ref_search_box_2.setSizePolicy(sizePolicy)
        self.ref_search_box_2.setMinimumSize(QSize(160, 0))

        self.horizontalLayout_3.addWidget(self.ref_search_box_2)

        self.ref_search_btn_2 = QPushButton(self.search_frame_2)
        self.ref_search_btn_2.setObjectName(u"ref_search_btn_2")
        sizePolicy2.setHeightForWidth(self.ref_search_btn_2.sizePolicy().hasHeightForWidth())
        self.ref_search_btn_2.setSizePolicy(sizePolicy2)
        self.ref_search_btn_2.setMinimumSize(QSize(5, 24))

        self.horizontalLayout_3.addWidget(self.ref_search_btn_2)


        self.verticalLayout_27.addWidget(self.search_frame_2)

        self.groupBox_6 = QGroupBox(self.scrollAreaWidgetContents_17)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_8 = QGridLayout(self.groupBox_6)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.textBrowser_108 = QTextBrowser(self.groupBox_6)
        self.textBrowser_108.setObjectName(u"textBrowser_108")
        self.textBrowser_108.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.textBrowser_108.sizePolicy().hasHeightForWidth())
        self.textBrowser_108.setSizePolicy(sizePolicy4)
        self.textBrowser_108.setMinimumSize(QSize(155, 90))

        self.gridLayout_8.addWidget(self.textBrowser_108, 0, 0, 1, 1)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.pushButton_11 = QPushButton(self.groupBox_6)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy4.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy4)
        self.pushButton_11.setMinimumSize(QSize(30, 40))

        self.verticalLayout_13.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.groupBox_6)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy4.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy4)
        self.pushButton_12.setMinimumSize(QSize(30, 20))

        self.verticalLayout_13.addWidget(self.pushButton_12)


        self.gridLayout_8.addLayout(self.verticalLayout_13, 0, 1, 1, 1)


        self.verticalLayout_27.addWidget(self.groupBox_6)

        self.groupBox_10 = QGroupBox(self.scrollAreaWidgetContents_17)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.gridLayout_12 = QGridLayout(self.groupBox_10)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.textBrowser_112 = QTextBrowser(self.groupBox_10)
        self.textBrowser_112.setObjectName(u"textBrowser_112")
        self.textBrowser_112.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.textBrowser_112.sizePolicy().hasHeightForWidth())
        self.textBrowser_112.setSizePolicy(sizePolicy4)
        self.textBrowser_112.setMinimumSize(QSize(155, 90))

        self.gridLayout_12.addWidget(self.textBrowser_112, 0, 0, 1, 1)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.pushButton_19 = QPushButton(self.groupBox_10)
        self.pushButton_19.setObjectName(u"pushButton_19")
        sizePolicy4.setHeightForWidth(self.pushButton_19.sizePolicy().hasHeightForWidth())
        self.pushButton_19.setSizePolicy(sizePolicy4)
        self.pushButton_19.setMinimumSize(QSize(30, 40))

        self.verticalLayout_17.addWidget(self.pushButton_19)

        self.pushButton_20 = QPushButton(self.groupBox_10)
        self.pushButton_20.setObjectName(u"pushButton_20")
        sizePolicy4.setHeightForWidth(self.pushButton_20.sizePolicy().hasHeightForWidth())
        self.pushButton_20.setSizePolicy(sizePolicy4)
        self.pushButton_20.setMinimumSize(QSize(30, 20))

        self.verticalLayout_17.addWidget(self.pushButton_20)


        self.gridLayout_12.addLayout(self.verticalLayout_17, 0, 1, 1, 1)


        self.verticalLayout_27.addWidget(self.groupBox_10)

        self.groupBox_7 = QGroupBox(self.scrollAreaWidgetContents_17)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.gridLayout_9 = QGridLayout(self.groupBox_7)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.textBrowser_109 = QTextBrowser(self.groupBox_7)
        self.textBrowser_109.setObjectName(u"textBrowser_109")
        self.textBrowser_109.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.textBrowser_109.sizePolicy().hasHeightForWidth())
        self.textBrowser_109.setSizePolicy(sizePolicy4)
        self.textBrowser_109.setMinimumSize(QSize(155, 90))

        self.gridLayout_9.addWidget(self.textBrowser_109, 0, 0, 1, 1)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.pushButton_13 = QPushButton(self.groupBox_7)
        self.pushButton_13.setObjectName(u"pushButton_13")
        sizePolicy4.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy4)
        self.pushButton_13.setMinimumSize(QSize(30, 40))

        self.verticalLayout_14.addWidget(self.pushButton_13)

        self.pushButton_14 = QPushButton(self.groupBox_7)
        self.pushButton_14.setObjectName(u"pushButton_14")
        sizePolicy4.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy4)
        self.pushButton_14.setMinimumSize(QSize(30, 20))

        self.verticalLayout_14.addWidget(self.pushButton_14)


        self.gridLayout_9.addLayout(self.verticalLayout_14, 0, 1, 1, 1)


        self.verticalLayout_27.addWidget(self.groupBox_7)

        self.groupBox_9 = QGroupBox(self.scrollAreaWidgetContents_17)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.gridLayout_11 = QGridLayout(self.groupBox_9)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.textBrowser_111 = QTextBrowser(self.groupBox_9)
        self.textBrowser_111.setObjectName(u"textBrowser_111")
        self.textBrowser_111.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.textBrowser_111.sizePolicy().hasHeightForWidth())
        self.textBrowser_111.setSizePolicy(sizePolicy4)
        self.textBrowser_111.setMinimumSize(QSize(155, 90))

        self.gridLayout_11.addWidget(self.textBrowser_111, 0, 0, 1, 1)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.pushButton_17 = QPushButton(self.groupBox_9)
        self.pushButton_17.setObjectName(u"pushButton_17")
        sizePolicy4.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy4)
        self.pushButton_17.setMinimumSize(QSize(30, 40))

        self.verticalLayout_16.addWidget(self.pushButton_17)

        self.pushButton_18 = QPushButton(self.groupBox_9)
        self.pushButton_18.setObjectName(u"pushButton_18")
        sizePolicy4.setHeightForWidth(self.pushButton_18.sizePolicy().hasHeightForWidth())
        self.pushButton_18.setSizePolicy(sizePolicy4)
        self.pushButton_18.setMinimumSize(QSize(30, 20))

        self.verticalLayout_16.addWidget(self.pushButton_18)


        self.gridLayout_11.addLayout(self.verticalLayout_16, 0, 1, 1, 1)


        self.verticalLayout_27.addWidget(self.groupBox_9)

        self.groupBox_8 = QGroupBox(self.scrollAreaWidgetContents_17)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.gridLayout_10 = QGridLayout(self.groupBox_8)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.textBrowser_110 = QTextBrowser(self.groupBox_8)
        self.textBrowser_110.setObjectName(u"textBrowser_110")
        self.textBrowser_110.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.textBrowser_110.sizePolicy().hasHeightForWidth())
        self.textBrowser_110.setSizePolicy(sizePolicy4)
        self.textBrowser_110.setMinimumSize(QSize(155, 90))

        self.gridLayout_10.addWidget(self.textBrowser_110, 0, 0, 1, 1)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.pushButton_15 = QPushButton(self.groupBox_8)
        self.pushButton_15.setObjectName(u"pushButton_15")
        sizePolicy4.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy4)
        self.pushButton_15.setMinimumSize(QSize(30, 40))

        self.verticalLayout_15.addWidget(self.pushButton_15)

        self.pushButton_16 = QPushButton(self.groupBox_8)
        self.pushButton_16.setObjectName(u"pushButton_16")
        sizePolicy4.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy4)
        self.pushButton_16.setMinimumSize(QSize(30, 20))

        self.verticalLayout_15.addWidget(self.pushButton_16)


        self.gridLayout_10.addLayout(self.verticalLayout_15, 0, 1, 1, 1)


        self.verticalLayout_27.addWidget(self.groupBox_8)

        self.vegetable_scrollarea.setWidget(self.scrollAreaWidgetContents_17)

        self.gridLayout_4.addWidget(self.vegetable_scrollarea, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.gridWidget_2)

        self.tab_root.addTab(self.storage_tab, "")
        self.recipe_tab = QWidget()
        self.recipe_tab.setObjectName(u"recipe_tab")
        self.lineEdit_2 = QLineEdit(self.recipe_tab)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(170, 120, 113, 22))
        self.tab_root.addTab(self.recipe_tab, "")
        self.help_tab = QWidget()
        self.help_tab.setObjectName(u"help_tab")
        self.lineEdit_3 = QLineEdit(self.help_tab)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(130, 110, 113, 22))
        self.tab_root.addTab(self.help_tab, "")
        self.setting_tab = QWidget()
        self.setting_tab.setObjectName(u"setting_tab")
        self.setting_tab.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.verticalLayout_4 = QVBoxLayout(self.setting_tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.font_size_label = QLabel(self.setting_tab)
        self.font_size_label.setObjectName(u"font_size_label")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.font_size_label)

        self.font_size_cbx = QComboBox(self.setting_tab)
        self.font_size_cbx.setObjectName(u"font_size_cbx")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.font_size_cbx)

        self.lauage_label = QLabel(self.setting_tab)
        self.lauage_label.setObjectName(u"lauage_label")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lauage_label)

        self.lauage_cbx = QComboBox(self.setting_tab)
        self.lauage_cbx.setObjectName(u"lauage_cbx")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lauage_cbx)

        self.theme_label = QLabel(self.setting_tab)
        self.theme_label.setObjectName(u"theme_label")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.theme_label)

        self.theme_cbx = QComboBox(self.setting_tab)
        self.theme_cbx.setObjectName(u"theme_cbx")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.theme_cbx)


        self.verticalLayout_4.addLayout(self.formLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.data_backup_btn = QPushButton(self.setting_tab)
        self.data_backup_btn.setObjectName(u"data_backup_btn")

        self.verticalLayout_3.addWidget(self.data_backup_btn)

        self.data_import_btn = QPushButton(self.setting_tab)
        self.data_import_btn.setObjectName(u"data_import_btn")

        self.verticalLayout_3.addWidget(self.data_import_btn)

        self.data_reset_btn = QPushButton(self.setting_tab)
        self.data_reset_btn.setObjectName(u"data_reset_btn")

        self.verticalLayout_3.addWidget(self.data_reset_btn)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.tab_root.addTab(self.setting_tab, "")

        self.horizontalLayout_2.addWidget(self.tab_root)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 13)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tab_root.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.storage_status_btn.setText(QCoreApplication.translate("MainWindow", u"\uc7ac\n"
"\ub8cc\n"
"\ud604\n"
"\ud669", None))
        self.recipe_btn.setText(QCoreApplication.translate("MainWindow", u"\ub808\n"
"\uc2dc\n"
"\ud53c", None))
        self.show_help_btn.setText(QCoreApplication.translate("MainWindow", u"\u2754", None))
        self.setting_btn.setText(QCoreApplication.translate("MainWindow", u"\u2699\ufe0f", None))
        self.ref_add_self_btn.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.fav_ch_btn.setText(QCoreApplication.translate("MainWindow", u"\uc990\uaca8\ucc3e\ub294 \uc7ac\ub8cc", None))
        self.open_search_manage_modal_btn.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udd0d\ufe0e", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\uae30\ud0c0", None))
        self.show_search_box_btn_3.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udd0d\ufe0e", None))
        self.other_sort_btn.setText(QCoreApplication.translate("MainWindow", u"\u21c5", None))
        self.ref_search_btn_3.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udd0d\ufe0e", None))
        self.groupBox_16.setTitle("")
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"\u2661", None))
        self.pushButton_32.setText(QCoreApplication.translate("MainWindow", u"\u205d", None))
        self.groupBox_17.setTitle("")
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"\u2661", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"\u205d", None))
        self.groupBox_18.setTitle("")
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"\u2661", None))
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"\u205d", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\uc721\ub958", None))
        self.show_search_box_btn_1.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udd0d\ufe0e", None))
        self.meat_sort_btn.setText(QCoreApplication.translate("MainWindow", u"\u21c5", None))
        self.ref_search_btn_1.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udd0d\ufe0e", None))
        self.groupBox_1.setTitle("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u2661", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u205d", None))
        self.groupBox_5.setTitle("")
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u2661", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u205d", None))
        self.groupBox_2.setTitle("")
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u2661", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u205d", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\uc5b4\ub958", None))
        self.show_search_box_btn_4.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udd0d\ufe0e", None))
        self.sea_food_sort_btn.setText(QCoreApplication.translate("MainWindow", u"\u21c5", None))
        self.ref_search_btn_4.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udd0d\ufe0e", None))
        self.groupBox_12.setTitle("")
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"\u2661", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"\u205d", None))
        self.groupBox_11.setTitle("")
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"\u2661", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"\u205d", None))
        self.groupBox_14.setTitle("")
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"\u2661", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"\u205d", None))
        self.groupBox_15.setTitle("")
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"\u2661", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"\u205d", None))
        self.groupBox_13.setTitle("")
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"\u2661", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"\u205d", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\uacfc\uc77c & \ucc44\uc18c", None))
        self.show_search_box_btn_2.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udd0d\ufe0e", None))
        self.fruit_vegetable_sort_btn.setText(QCoreApplication.translate("MainWindow", u"\u21c5", None))
        self.ref_search_btn_2.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udd0d\ufe0e", None))
        self.groupBox_6.setTitle("")
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"\u2661", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"\u205d", None))
        self.groupBox_10.setTitle("")
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"\u2661", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"\u205d", None))
        self.groupBox_7.setTitle("")
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"\u2661", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"\u205d", None))
        self.groupBox_9.setTitle("")
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"\u2661", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"\u205d", None))
        self.groupBox_8.setTitle("")
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"\u2661", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"\u205d", None))
        self.tab_root.setTabText(self.tab_root.indexOf(self.storage_tab), QCoreApplication.translate("MainWindow", u"\uc7ac\ub8cc", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"\u3134\u3141\u3147\u3134\u3141", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u3141\u3147\u3134\u3141\u3147", None))
        self.tab_root.setTabText(self.tab_root.indexOf(self.recipe_tab), QCoreApplication.translate("MainWindow", u"\ub808\uc2dc\ud53c", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"\u314a\u314a\u314b\u314a\u314c", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u3141\u3147\u3134\u3141\u3147", None))
        self.tab_root.setTabText(self.tab_root.indexOf(self.help_tab), QCoreApplication.translate("MainWindow", u"\ub3c4\uc6c0\ub9d0", None))
        self.font_size_label.setText(QCoreApplication.translate("MainWindow", u"\uae00\uc790 \ud06c\uae30", None))
        self.lauage_label.setText(QCoreApplication.translate("MainWindow", u"\uc5b8\uc5b4", None))
        self.theme_label.setText(QCoreApplication.translate("MainWindow", u"\ud14c\ub9c8", None))
        self.data_backup_btn.setText(QCoreApplication.translate("MainWindow", u"\ubc31\uc5c5\ud558\uae30", None))
        self.data_import_btn.setText(QCoreApplication.translate("MainWindow", u"\uac00\uc838\uc624\uae30", None))
        self.data_reset_btn.setText(QCoreApplication.translate("MainWindow", u"\ucd08\uae30\ud654", None))
        self.tab_root.setTabText(self.tab_root.indexOf(self.setting_tab), QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
    # retranslateUi

