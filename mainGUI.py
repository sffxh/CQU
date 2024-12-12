
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1002, 544)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 6, 7, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 7, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 2)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 12, 0, 1, 1)
        self.time_gap = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.time_gap.setFont(font)
        self.time_gap.setObjectName("time_gap")
        self.gridLayout.addWidget(self.time_gap, 0, 7, 1, 1)
        self.ellipse_y = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.ellipse_y.setFont(font)
        self.ellipse_y.setObjectName("ellipse_y")
        self.gridLayout.addWidget(self.ellipse_y, 12, 9, 1, 1)
        self.DDA_end_x = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.DDA_end_x.setFont(font)
        self.DDA_end_x.setObjectName("DDA_end_x")
        self.gridLayout.addWidget(self.DDA_end_x, 9, 1, 1, 2)
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.gridLayout.addWidget(self.label_30, 13, 7, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 0, 5, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 13, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 9, 0, 1, 1)
        self.ellipse_short = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.ellipse_short.setFont(font)
        self.ellipse_short.setObjectName("ellipse_short")
        self.gridLayout.addWidget(self.ellipse_short, 14, 8, 1, 1)
        self.ellipse_long = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.ellipse_long.setFont(font)
        self.ellipse_long.setObjectName("ellipse_long")
        self.gridLayout.addWidget(self.ellipse_long, 13, 8, 1, 1)
        self.fixed_axis = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.fixed_axis.setFont(font)
        self.fixed_axis.setObjectName("fixed_axis")
        self.gridLayout.addWidget(self.fixed_axis, 0, 2, 1, 3)
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.gridLayout.addWidget(self.label_32, 11, 9, 1, 2)
        self.ellipse_x = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.ellipse_x.setFont(font)
        self.ellipse_x.setObjectName("ellipse_x")
        self.gridLayout.addWidget(self.ellipse_x, 12, 8, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.gridLayout.addWidget(self.label_31, 7, 9, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 8, 0, 1, 1)
        self.DDA_start_y = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.DDA_start_y.setFont(font)
        self.DDA_start_y.setObjectName("DDA_start_y")
        self.gridLayout.addWidget(self.DDA_start_y, 8, 3, 1, 1)
        self.B_start_x = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.B_start_x.setFont(font)
        self.B_start_x.setObjectName("B_start_x")
        self.gridLayout.addWidget(self.B_start_x, 12, 1, 1, 2)
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.gridLayout.addWidget(self.label_27, 11, 8, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 8, 7, 1, 1)

        self.circle_x = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.circle_x.setFont(font)
        self.circle_x.setObjectName("circle_x")
        self.gridLayout.addWidget(self.circle_x, 8, 8, 1, 1)

        self.Bcircle_x = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.Bcircle_x.setFont(font)
        self.Bcircle_x.setObjectName("Bcircle_x")
        self.gridLayout.addWidget(self.Bcircle_x, 17, 8, 1, 1)



        self.B_end_y = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.B_end_y.setFont(font)
        self.B_end_y.setObjectName("B_end_y")
        self.gridLayout.addWidget(self.B_end_y, 13, 3, 1, 1)
        self.B_go = QtWidgets.QPushButton(self.centralwidget)
        self.B_go.setObjectName("B_go")
        self.gridLayout.addWidget(self.B_go, 12, 4, 2, 2)

        self.M_go = QtWidgets.QPushButton(self.centralwidget)
        self.M_go.setObjectName("M_go")
        self.gridLayout.addWidget(self.M_go, 16, 4, 2, 2)

        self.tc_go = QtWidgets.QPushButton(self.centralwidget)
        self.tc_go.setObjectName("tc_go")
        self.gridLayout.addWidget(self.tc_go, 21, 4, 2, 2)

        self.DDA_start_x = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.DDA_start_x.setFont(font)
        self.DDA_start_x.setObjectName("DDA_start_x")
        self.gridLayout.addWidget(self.DDA_start_x, 8, 1, 1, 2)
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.gridLayout.addWidget(self.label_28, 9, 7, 1, 1)

        self.label_40 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.gridLayout.addWidget(self.label_40, 18, 7, 1, 1)


        self.DDA_end_y = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.DDA_end_y.setFont(font)
        self.DDA_end_y.setObjectName("DDA_end_y")
        self.gridLayout.addWidget(self.DDA_end_y, 9, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 6, 0, 1, 1)

        self.circle_go = QtWidgets.QPushButton(self.centralwidget)
        self.circle_go.setObjectName("circle_go")
        self.gridLayout.addWidget(self.circle_go, 8, 10, 2, 1)


        self.Bcircle_go = QtWidgets.QPushButton(self.centralwidget)
        self.Bcircle_go.setObjectName("Bcircle_go")
        self.gridLayout.addWidget(self.Bcircle_go, 17, 10, 2, 1)

        self.B_start_y = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.B_start_y.setFont(font)
        self.B_start_y.setObjectName("B_start_y")
        self.gridLayout.addWidget(self.B_start_y, 12, 3, 1, 1)

        self.circle_y = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.circle_y.setFont(font)
        self.circle_y.setObjectName("circle_y")
        self.gridLayout.addWidget(self.circle_y, 8, 9, 1, 1)

        self.Bcircle_y = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.Bcircle_y.setFont(font)
        self.Bcircle_y.setObjectName("Bcircle_y")
        self.gridLayout.addWidget(self.Bcircle_y, 17, 9, 1, 1)

        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 7, 8, 1, 1)
        self.circle_r = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.circle_r.setFont(font)
        self.circle_r.setObjectName("circle_r")
        self.gridLayout.addWidget(self.circle_r, 9, 8, 1, 1)

        self.Bcircle_r = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.Bcircle_r.setFont(font)
        self.Bcircle_r.setObjectName("Bcircle_r")
        self.gridLayout.addWidget(self.Bcircle_r, 18, 8, 1, 1)

        self.DDA_go = QtWidgets.QPushButton(self.centralwidget)

        self.DDA_go.setObjectName("DDA_go")
        self.gridLayout.addWidget(self.DDA_go, 8, 4, 2, 2)

        self.ellipse_go = QtWidgets.QPushButton(self.centralwidget)
        self.ellipse_go.setObjectName("ellipse_go")
        self.gridLayout.addWidget(self.ellipse_go, 12, 10, 2, 1)
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 14, 7, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 12, 7, 1, 1)

        self.label_39 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.gridLayout.addWidget(self.label_39, 17, 7, 1, 1)

        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 11, 3, 1, 1)
        self.B_end_x = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.B_end_x.setFont(font)
        self.B_end_x.setObjectName("B_end_x")
        self.gridLayout.addWidget(self.B_end_x, 13, 1, 1, 2)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 11, 1, 1, 2)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 10, 0, 1, 3)
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.gridLayout.addWidget(self.label_29, 10, 7, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 9, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 0, 10, 1, 1)

        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.gridLayout.addWidget(self.label_33, 17, 0, 1, 1)

        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.gridLayout.addWidget(self.label_34, 16, 0, 1, 1)

        self.label_35 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.gridLayout.addWidget(self.label_35, 14, 0,1,3)

        self.label_42 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.gridLayout.addWidget(self.label_42, 19, 0, 1, 3)

        self.label_36 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.gridLayout.addWidget(self.label_36, 15, 1, 1, 2)

        self.label_37 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.gridLayout.addWidget(self.label_37, 15, 3, 1, 2)

        self.label_38 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.gridLayout.addWidget(self.label_38, 15, 7, 1, 2)

        self.label_41 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.gridLayout.addWidget(self.label_41, 21, 0, 1, 2)

        self.M_start_x = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.M_start_x.setFont(font)
        self.M_start_x.setObjectName("M_start_x")
        self.gridLayout.addWidget(self.M_start_x, 16, 1, 1, 2)

        self.M_end_x = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.M_end_x.setFont(font)
        self.M_end_x.setObjectName("M_end_x")
        self.gridLayout.addWidget(self.M_end_x, 17, 1, 1, 2)

        self.M_end_y = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.M_end_y.setFont(font)
        self.M_end_y.setObjectName("M_end_y")
        self.gridLayout.addWidget(self.M_end_y, 17, 3, 1, 1)

        self.TC_end_y = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.TC_end_y.setFont(font)
        self.TC_end_y.setObjectName("TC_end_y")
        self.gridLayout.addWidget(self.TC_end_y, 21, 3, 1, 1)

        self.TC_end_x = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.TC_end_x.setFont(font)
        self.TC_end_x.setObjectName("TC_end_x")
        self.gridLayout.addWidget(self.TC_end_x, 21, 1, 1, 1)

        self.M_start_y = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.M_start_y.setFont(font)
        self.M_start_y.setObjectName("M_start_y")
        self.gridLayout.addWidget(self.M_start_y, 16, 3, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1002, 32))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Computer_Graphics_Experiment_Program"))
        self.label_22.setText(_translate("MainWindow", "中点圆算法"))
        self.label_8.setText(_translate("MainWindow", "纵坐标y"))
        self.label_7.setText(_translate("MainWindow", "横坐标x"))
        self.label_3.setText(_translate("MainWindow", "绘图配置"))
        self.label_11.setText(_translate("MainWindow", "起始点坐标"))
        self.time_gap.setText(_translate("MainWindow", "0.1"))
        self.ellipse_y.setText(_translate("MainWindow", "3"))
        self.DDA_end_x.setText(_translate("MainWindow", "10"))
        self.label_30.setText(_translate("MainWindow", "长半轴"))
        self.label_13.setText(_translate("MainWindow", "打点间隔（s）"))
        self.label_9.setText(_translate("MainWindow", "终止点坐标"))
        self.label_6.setText(_translate("MainWindow", "终止点坐标"))
        self.ellipse_short.setText(_translate("MainWindow", "43"))
        self.ellipse_long.setText(_translate("MainWindow", "21"))
        self.fixed_axis.setText(_translate("MainWindow", "固定坐标轴"))
        self.label_32.setText(_translate("MainWindow", "纵坐标y"))
        self.ellipse_x.setText(_translate("MainWindow", "2"))
        self.label_31.setText(_translate("MainWindow", "纵坐标y"))
        self.label_5.setText(_translate("MainWindow", "起始点坐标"))
        self.DDA_start_y.setText(_translate("MainWindow", "0"))
        self.B_start_x.setText(_translate("MainWindow", "16"))
        self.label_27.setText(_translate("MainWindow", "横坐标x"))
        self.label_23.setText(_translate("MainWindow", "圆心坐标"))
        self.circle_x.setText(_translate("MainWindow", "-12"))
        self.Bcircle_x.setText(_translate("MainWindow", "-1"))
        self.Bcircle_r.setText(_translate("MainWindow", "20"))
        self.B_end_y.setText(_translate("MainWindow", "-21"))
        self.B_go.setText(_translate("MainWindow", "绘制"))
        self.Bcircle_y.setText(_translate("MainWindow", "-2"))
        self.M_go.setText(_translate("MainWindow", "绘制"))

        self.DDA_start_x.setText(_translate("MainWindow", "1"))

        self.M_end_x.setText(_translate("MainWindow", "1314"))

        self.M_start_x.setText(_translate("MainWindow", "520"))

        self.M_end_y.setText(_translate("MainWindow", "211"))

        self.M_start_y.setText(_translate("MainWindow", "985"))

        self.label_28.setText(_translate("MainWindow", "半径"))
        self.DDA_end_y.setText(_translate("MainWindow", "20"))
        self.label.setText(_translate("MainWindow", "DDA算法"))
        self.circle_go.setText(_translate("MainWindow", "绘制"))
        self.B_start_y.setText(_translate("MainWindow", "15"))
        self.circle_y.setText(_translate("MainWindow", "4"))
        self.label_24.setText(_translate("MainWindow", "横坐标x"))
        self.circle_r.setText(_translate("MainWindow", "20"))
        self.DDA_go.setText(_translate("MainWindow", "绘制"))
        self.ellipse_go.setText(_translate("MainWindow", "绘制"))
        self.label_26.setText(_translate("MainWindow", "短半轴"))
        self.label_25.setText(_translate("MainWindow", "椭圆中点"))
        self.label_41.setText(_translate("MainWindow", "种子坐标"))

        self.label_42.setText(_translate("MainWindow", "种子填充"))

        self.B_end_x.setText(_translate("MainWindow", "-43"))
        self.label_10.setText(_translate("MainWindow", "横坐标x"))
        self.label_2.setText(_translate("MainWindow", "Bresenham算法"))
        self.label_29.setText(_translate("MainWindow", "中点椭圆算法"))
        self.label_4.setText(_translate("MainWindow", "软件工程04班 解瑞"))
        self.label_14.setText(_translate("MainWindow", "2332830516"))
        self.label_33.setText(_translate("MainWindow", "终止点坐标"))
        self.label_34.setText(_translate("MainWindow", "起始点坐标"))
        self.label_35.setText(_translate("MainWindow", "中点画线算法"))
        self.label_36.setText(_translate("MainWindow", "横坐标x"))
        self.label_37.setText(_translate("MainWindow", "纵坐标y"))
        self.label_38.setText(_translate("MainWindow", "Bresenham画圆"))
        self.label_39.setText(_translate("MainWindow", "圆心坐标"))
        self.label_40.setText(_translate("MainWindow", "半径"))
        self.Bcircle_go.setText(_translate("MainWindow", "绘制"))
        self.tc_go.setText(_translate("MainWindow", "绘制"))