# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI3.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1322, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(100, 10, 1071, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.verticalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(50, 0, 50, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_open = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_open.sizePolicy().hasHeightForWidth())
        self.pushButton_open.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_open.setFont(font)
        self.pushButton_open.setCheckable(False)
        self.pushButton_open.setChecked(False)
        self.pushButton_open.setAutoDefault(False)
        self.pushButton_open.setDefault(False)
        self.pushButton_open.setFlat(False)
        self.pushButton_open.setObjectName("pushButton_open")
        self.horizontalLayout.addWidget(self.pushButton_open)
        self.pushButton_DCT = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_DCT.sizePolicy().hasHeightForWidth())
        self.pushButton_DCT.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_DCT.setFont(font)
        self.pushButton_DCT.setCheckable(True)
        self.pushButton_DCT.setObjectName("pushButton_DCT")
        self.horizontalLayout.addWidget(self.pushButton_DCT)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.spinBox_Q_2 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_Q_2.setFont(font)
        self.spinBox_Q_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.spinBox_Q_2.setProperty("value", 3)
        self.spinBox_Q_2.setObjectName("spinBox_Q_2")
        self.horizontalLayout_2.addWidget(self.spinBox_Q_2)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_Q = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Q.setSpacing(6)
        self.horizontalLayout_Q.setObjectName("horizontalLayout_Q")
        self.label_Q = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.label_Q.setFont(font)
        self.label_Q.setObjectName("label_Q")
        self.horizontalLayout_Q.addWidget(self.label_Q)
        self.spinBox_Q = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_Q.setFont(font)
        self.spinBox_Q.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.spinBox_Q.setProperty("value", 50)
        self.spinBox_Q.setObjectName("spinBox_Q")
        self.horizontalLayout_Q.addWidget(self.spinBox_Q)
        self.horizontalLayout.addLayout(self.horizontalLayout_Q)
        self.pushButton_confirm = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_confirm.setFont(font)
        self.pushButton_confirm.setObjectName("pushButton_confirm")
        self.horizontalLayout.addWidget(self.pushButton_confirm)
        self.pushButton_transmit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_transmit.setFont(font)
        self.pushButton_transmit.setObjectName("pushButton_transmit")
        self.horizontalLayout.addWidget(self.pushButton_transmit)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(920, 640, 251, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_pos = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_pos.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_pos.setObjectName("verticalLayout_pos")
        self.label_click_pos = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_click_pos.setFont(font)
        self.label_click_pos.setObjectName("label_click_pos")
        self.verticalLayout_pos.addWidget(self.label_click_pos)
        self.label_norm_pos = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_norm_pos.setFont(font)
        self.label_norm_pos.setObjectName("label_norm_pos")
        self.verticalLayout_pos.addWidget(self.label_norm_pos)
        self.label_real_pos = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_real_pos.setFont(font)
        self.label_real_pos.setObjectName("label_real_pos")
        self.verticalLayout_pos.addWidget(self.label_real_pos)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(100, 60, 1071, 42))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_title = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_title.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_title.setObjectName("horizontalLayout_title")
        self.label_original = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_original.setFont(font)
        self.label_original.setObjectName("label_original")
        self.horizontalLayout_title.addWidget(self.label_original)
        self.label_output = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_output.setFont(font)
        self.label_output.setObjectName("label_output")
        self.horizontalLayout_title.addWidget(self.label_output)
        self.layoutWidget2 = QtWidgets.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(100, 640, 811, 141))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_sidegraph = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_sidegraph.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_sidegraph.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout_sidegraph.setSpacing(35)
        self.horizontalLayout_sidegraph.setObjectName("horizontalLayout_sidegraph")
        self.label_text_original = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_text_original.setFont(font)
        self.label_text_original.setScaledContents(False)
        self.label_text_original.setObjectName("label_text_original")
        self.horizontalLayout_sidegraph.addWidget(self.label_text_original)
        self.label_side_original = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_side_original.sizePolicy().hasHeightForWidth())
        self.label_side_original.setSizePolicy(sizePolicy)
        self.label_side_original.setFrameShape(QtWidgets.QFrame.Box)
        self.label_side_original.setText("")
        self.label_side_original.setObjectName("label_side_original")
        self.horizontalLayout_sidegraph.addWidget(self.label_side_original)
        self.label_text_DCT = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_text_DCT.setFont(font)
        self.label_text_DCT.setObjectName("label_text_DCT")
        self.horizontalLayout_sidegraph.addWidget(self.label_text_DCT)
        self.label_side_DCT = QtWidgets.QLabel(self.layoutWidget2)
        self.label_side_DCT.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_side_DCT.sizePolicy().hasHeightForWidth())
        self.label_side_DCT.setSizePolicy(sizePolicy)
        self.label_side_DCT.setFrameShape(QtWidgets.QFrame.Box)
        self.label_side_DCT.setText("")
        self.label_side_DCT.setObjectName("label_side_DCT")
        self.horizontalLayout_sidegraph.addWidget(self.label_side_DCT)
        self.label_text_zigzag = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_text_zigzag.setFont(font)
        self.label_text_zigzag.setObjectName("label_text_zigzag")
        self.horizontalLayout_sidegraph.addWidget(self.label_text_zigzag)
        self.label_side_zigzag = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_side_zigzag.sizePolicy().hasHeightForWidth())
        self.label_side_zigzag.setSizePolicy(sizePolicy)
        self.label_side_zigzag.setFrameShape(QtWidgets.QFrame.Box)
        self.label_side_zigzag.setText("")
        self.label_side_zigzag.setObjectName("label_side_zigzag")
        self.horizontalLayout_sidegraph.addWidget(self.label_side_zigzag)
        self.horizontalLayout_sidegraph.setStretch(0, 1)
        self.horizontalLayout_sidegraph.setStretch(1, 2)
        self.horizontalLayout_sidegraph.setStretch(2, 1)
        self.horizontalLayout_sidegraph.setStretch(3, 2)
        self.horizontalLayout_sidegraph.setStretch(4, 1)
        self.horizontalLayout_sidegraph.setStretch(5, 2)
        self.graphicsView_graphicL = QtWidgets.QGraphicsView(Form)
        self.graphicsView_graphicL.setGeometry(QtCore.QRect(100, 110, 515, 515))
        self.graphicsView_graphicL.setObjectName("graphicsView_graphicL")
        self.graphicsView_graphicR = QtWidgets.QGraphicsView(Form)
        self.graphicsView_graphicR.setGeometry(QtCore.QRect(655, 110, 515, 515))
        self.graphicsView_graphicR.setObjectName("graphicsView_graphicR")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_open.setText(_translate("Form", "Open"))
        self.pushButton_DCT.setText(_translate("Form", "DCT"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\">COM</p></body></html>"))
        self.label_Q.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">&rho;</span></p></body></html>"))
        self.pushButton_confirm.setText(_translate("Form", "Show"))
        self.pushButton_transmit.setText(_translate("Form", "Transmit"))
        self.label_click_pos.setText(_translate("Form", "Clicked position = (x,y)"))
        self.label_norm_pos.setText(_translate("Form", "Norm position = (x, y)"))
        self.label_real_pos.setText(_translate("Form", "Real position = (x, y)"))
        self.label_original.setText(_translate("Form", "<html><head/><body><p align=\"center\">Original</p></body></html>"))
        self.label_output.setText(_translate("Form", "<html><head/><body><p align=\"center\">Output</p></body></html>"))
        self.label_text_original.setText(_translate("Form", "<html><head/><body><p align=\"center\">Original</p></body></html>"))
        self.label_text_DCT.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">DCT</span></p></body></html>"))
        self.label_text_zigzag.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Output</span></p></body></html>"))
