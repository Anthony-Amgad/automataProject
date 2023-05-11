# Form implementation generated from reading ui file 'f:\Ain Shams\Spring 2023\Automata\Project\automataProject\res\ui\GraphingWindow.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1112, 858)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("font: 10pt \"DejaVu Sans Mono\";\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(550, 0, 16, 171))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.edPathCTxt = QtWidgets.QLineEdit(self.centralwidget)
        self.edPathCTxt.setGeometry(QtCore.QRect(580, 10, 521, 31))
        self.edPathCTxt.setStyleSheet("border-color: rgb(4, 72, 117);\n"
"font: 10pt \"DejaVu Sans Mono\";\n"
"background-color: rgb(212, 232, 247);")
        self.edPathCTxt.setInputMask("")
        self.edPathCTxt.setMaxLength(1)
        self.edPathCTxt.setObjectName("edPathCTxt")
        self.fromEdAddCom = QtWidgets.QComboBox(self.centralwidget)
        self.fromEdAddCom.setGeometry(QtCore.QRect(580, 51, 161, 31))
        self.fromEdAddCom.setStyleSheet("background-color: rgb(212, 232, 247);")
        self.fromEdAddCom.setEditable(True)
        self.fromEdAddCom.setObjectName("fromEdAddCom")
        self.toEdAddCom = QtWidgets.QComboBox(self.centralwidget)
        self.toEdAddCom.setGeometry(QtCore.QRect(760, 50, 181, 31))
        self.toEdAddCom.setStyleSheet("background-color: rgb(212, 232, 247);")
        self.toEdAddCom.setEditable(True)
        self.toEdAddCom.setObjectName("toEdAddCom")
        self.adEdgeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.adEdgeBtn.setGeometry(QtCore.QRect(950, 50, 141, 31))
        self.adEdgeBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Cambria\";\n"
"background-color:rgb(7, 119, 197);\n"
"border-radius:20px;\n"
"")
        self.adEdgeBtn.setObjectName("adEdgeBtn")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 110, 1111, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.delNodeCom = QtWidgets.QComboBox(self.centralwidget)
        self.delNodeCom.setGeometry(QtCore.QRect(20, 130, 371, 31))
        self.delNodeCom.setStyleSheet("background-color: rgb(212, 232, 247);")
        self.delNodeCom.setEditable(True)
        self.delNodeCom.setObjectName("delNodeCom")
        self.delNodeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.delNodeBtn.setGeometry(QtCore.QRect(400, 130, 141, 28))
        self.delNodeBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Cambria\";\n"
"background-color:rgb(7, 119, 197);\n"
"border-radius:20px;\n"
"")
        self.delNodeBtn.setObjectName("delNodeBtn")
        self.delEdCom = QtWidgets.QComboBox(self.centralwidget)
        self.delEdCom.setGeometry(QtCore.QRect(580, 130, 371, 31))
        self.delEdCom.setStyleSheet("background-color: rgb(212, 232, 247);")
        self.delEdCom.setEditable(True)
        self.delEdCom.setObjectName("delEdCom")
        self.delEdgeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.delEdgeBtn.setGeometry(QtCore.QRect(960, 130, 141, 31))
        self.delEdgeBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Cambria\";\n"
"background-color:rgb(7, 119, 197);\n"
"border-radius:20px;\n"
"")
        self.delEdgeBtn.setObjectName("delEdgeBtn")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 170, 1111, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.searchBtn = QtWidgets.QPushButton(self.centralwidget)
        self.searchBtn.setGeometry(QtCore.QRect(490, 190, 141, 51))
        self.searchBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Cambria\";\n"
"background-color:rgb(7, 119, 197);\n"
"border-radius:20px;\n"
"")
        self.searchBtn.setObjectName("searchBtn")
        self.adAccNodeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.adAccNodeBtn.setGeometry(QtCore.QRect(310, 60, 201, 31))
        self.adAccNodeBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Cambria\";\n"
"background-color:rgb(7, 119, 197);\n"
"border-radius:20px;\n"
"")
        self.adAccNodeBtn.setObjectName("adAccNodeBtn")
        self.adTransNodeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.adTransNodeBtn.setGeometry(QtCore.QRect(40, 60, 201, 31))
        self.adTransNodeBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Cambria\";\n"
"background-color:rgb(7, 119, 197);\n"
"border-radius:20px;\n"
"")
        self.adTransNodeBtn.setObjectName("adTransNodeBtn")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(70, 10, 461, 20))
        self.checkBox.setObjectName("checkBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NFA to DFA"))
        self.edPathCTxt.setPlaceholderText(_translate("MainWindow", "Transition Token (leave empty for ε)"))
        self.fromEdAddCom.setProperty("placeholderText", _translate("MainWindow", "From Node"))
        self.toEdAddCom.setProperty("placeholderText", _translate("MainWindow", "To Node"))
        self.adEdgeBtn.setText(_translate("MainWindow", "Add Transition"))
        self.delNodeCom.setProperty("placeholderText", _translate("MainWindow", "Pick a Node to Delete"))
        self.delNodeBtn.setText(_translate("MainWindow", "Delete Node"))
        self.delEdCom.setProperty("placeholderText", _translate("MainWindow", "Pick an Edge to Delete"))
        self.delEdgeBtn.setText(_translate("MainWindow", "Delete Edge"))
        self.searchBtn.setText(_translate("MainWindow", "Convert"))
        self.adAccNodeBtn.setText(_translate("MainWindow", "Add Accepted State"))
        self.adTransNodeBtn.setText(_translate("MainWindow", "Add Transitional State"))
        self.checkBox.setText(_translate("MainWindow", "Make q0 (starting state) an accepted state"))
