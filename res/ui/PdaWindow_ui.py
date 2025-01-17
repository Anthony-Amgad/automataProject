# Form implementation generated from reading ui file 'f:\Ain Shams\Spring 2023\Automata\Project\automataProject\res\ui\PdaWindow.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 1039)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("f:\\Ain Shams\\Spring 2023\\Automata\\Project\\automataProject\\res\\ui\\logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainWidget = QtWidgets.QWidget(self.centralwidget)
        self.mainWidget.setGeometry(QtCore.QRect(0, 0, 1101, 1011))
        self.mainWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.mainWidget.setObjectName("mainWidget")
        self.insertStartSymbolLabel = QtWidgets.QLabel(self.mainWidget)
        self.insertStartSymbolLabel.setGeometry(QtCore.QRect(40, 10, 341, 41))
        self.insertStartSymbolLabel.setStyleSheet("color: rgb(6, 96, 159);\n"
"font: 75 16pt \"Georgia\";")
        self.insertStartSymbolLabel.setObjectName("insertStartSymbolLabel")
        self.inputStartSymbolTextEdit = QtWidgets.QTextEdit(self.mainWidget)
        self.inputStartSymbolTextEdit.setGeometry(QtCore.QRect(40, 50, 440, 50))
        self.inputStartSymbolTextEdit.setStyleSheet("border-color: rgb(4, 72, 117);\n"
"font: 10pt \"DejaVu Sans Mono\";\n"
"background-color: rgb(212, 232, 247);")
        self.inputStartSymbolTextEdit.setTabChangesFocus(True)
        self.inputStartSymbolTextEdit.setCursorWidth(1)
        self.inputStartSymbolTextEdit.setPlaceholderText("ex: S")
        self.inputStartSymbolTextEdit.setObjectName("inputStartSymbolTextEdit")
        self.showPDAPushButton = QtWidgets.QPushButton(self.mainWidget)
        self.showPDAPushButton.setGeometry(QtCore.QRect(460, 230, 161, 61))
        self.showPDAPushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.showPDAPushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Cambria\";\n"
"background-color:rgb(7, 119, 197);\n"
"border-radius:30px;\n"
"")
        self.showPDAPushButton.setObjectName("showPDAPushButton")
        self.pdaGroup = QtWidgets.QWidget(self.mainWidget)
        self.pdaGroup.setGeometry(QtCore.QRect(300, 310, 781, 691))
        self.pdaGroup.setObjectName("pdaGroup")
        self.pdaWebEngineView = QtWebEngineWidgets.QWebEngineView(self.pdaGroup)
        self.pdaWebEngineView.setGeometry(QtCore.QRect(10, 50, 761, 620))
        self.pdaWebEngineView.setObjectName("pdaWebEngineView")
        self.pdaLabel = QtWidgets.QLabel(self.pdaGroup)
        self.pdaLabel.setGeometry(QtCore.QRect(290, 20, 271, 31))
        self.pdaLabel.setStyleSheet("color: rgb(6, 96, 159);\n"
"font: 75 16pt \"Georgia\";")
        self.pdaLabel.setObjectName("pdaLabel")
        self.insertAlphabetLabel = QtWidgets.QLabel(self.mainWidget)
        self.insertAlphabetLabel.setGeometry(QtCore.QRect(40, 110, 411, 41))
        self.insertAlphabetLabel.setStyleSheet("color: rgb(6, 96, 159);\n"
"font: 75 16pt \"Georgia\";")
        self.insertAlphabetLabel.setObjectName("insertAlphabetLabel")
        self.inputAlphabetTextEdit = QtWidgets.QTextEdit(self.mainWidget)
        self.inputAlphabetTextEdit.setGeometry(QtCore.QRect(40, 150, 440, 50))
        self.inputAlphabetTextEdit.setAutoFillBackground(False)
        self.inputAlphabetTextEdit.setStyleSheet("border-color: rgb(4, 72, 117);\n"
"font: 10pt \"DejaVu Sans Mono\";\n"
"background-color: rgb(212, 232, 247);")
        self.inputAlphabetTextEdit.setTabChangesFocus(True)
        self.inputAlphabetTextEdit.setPlaceholderText("ex: a,*,+,(,)")
        self.inputAlphabetTextEdit.setObjectName("inputAlphabetTextEdit")
        self.line = QtWidgets.QFrame(self.mainWidget)
        self.line.setGeometry(QtCore.QRect(30, 300, 1021, 20))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.insertRulesLabel = QtWidgets.QLabel(self.mainWidget)
        self.insertRulesLabel.setGeometry(QtCore.QRect(590, 10, 341, 41))
        self.insertRulesLabel.setStyleSheet("color: rgb(6, 96, 159);\n"
"font: 75 16pt \"Georgia\";")
        self.insertRulesLabel.setObjectName("insertRulesLabel")
        self.inputRulesTextEdit = QtWidgets.QTextEdit(self.mainWidget)
        self.inputRulesTextEdit.setGeometry(QtCore.QRect(590, 50, 440, 153))
        self.inputRulesTextEdit.setStyleSheet("border-color: rgb(4, 72, 117);\n"
"font: 10pt \"DejaVu Sans Mono\";\n"
"background-color: rgb(212, 232, 247);")
        self.inputRulesTextEdit.setTabChangesFocus(True)
        self.inputRulesTextEdit.setObjectName("inputRulesTextEdit")
        self.transitionsTitleLabel = QtWidgets.QLabel(self.mainWidget)
        self.transitionsTitleLabel.setGeometry(QtCore.QRect(40, 320, 341, 41))
        self.transitionsTitleLabel.setStyleSheet("color: rgb(6, 96, 159);\n"
"font: 75 16pt \"Georgia\";")
        self.transitionsTitleLabel.setObjectName("transitionsTitleLabel")
        self.scrollArea = QtWidgets.QScrollArea(self.mainWidget)
        self.scrollArea.setGeometry(QtCore.QRect(40, 360, 251, 641))
        self.scrollArea.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 249, 639))
        self.scrollAreaWidgetContents.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.transitionsTextLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.transitionsTextLabel.setGeometry(QtCore.QRect(0, 0, 251, 641))
        self.transitionsTextLabel.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 12pt \"Times New Roman\";\n"
"border-color: rgb(255, 255, 255);")
        self.transitionsTextLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.transitionsTextLabel.setWordWrap(True)
        self.transitionsTextLabel.setObjectName("transitionsTextLabel")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1100, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuShow = QtWidgets.QMenu(self.menuBar)
        self.menuShow.setObjectName("menuShow")
        self.menuDeveloped_by = QtWidgets.QMenu(self.menuBar)
        self.menuDeveloped_by.setObjectName("menuDeveloped_by")
        MainWindow.setMenuBar(self.menuBar)
        self.actionYoussef_Geroge_19P9880 = QtGui.QAction(MainWindow)
        self.actionYoussef_Geroge_19P9880.setObjectName("actionYoussef_Geroge_19P9880")
        self.actionMostafa_Nasrat_19P4619 = QtGui.QAction(MainWindow)
        self.actionMostafa_Nasrat_19P4619.setObjectName("actionMostafa_Nasrat_19P4619")
        self.actionAnthony_Amgad_19P9880 = QtGui.QAction(MainWindow)
        self.actionAnthony_Amgad_19P9880.setObjectName("actionAnthony_Amgad_19P9880")
        self.actionKerrolos_Wageeh_19P3468 = QtGui.QAction(MainWindow)
        self.actionKerrolos_Wageeh_19P3468.setObjectName("actionKerrolos_Wageeh_19P3468")
        self.showParsingTableAction = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("f:\\Ain Shams\\Spring 2023\\Automata\\Project\\automataProject\\res\\ui\\parsingtable.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.showParsingTableAction.setIcon(icon1)
        self.showParsingTableAction.setObjectName("showParsingTableAction")
        self.showDemoAction = QtGui.QAction(MainWindow)
        self.showDemoAction.setObjectName("showDemoAction")
        self.menuShow.addAction(self.showDemoAction)
        self.menuDeveloped_by.addAction(self.actionYoussef_Geroge_19P9880)
        self.menuDeveloped_by.addAction(self.actionMostafa_Nasrat_19P4619)
        self.menuDeveloped_by.addAction(self.actionAnthony_Amgad_19P9880)
        self.menuDeveloped_by.addAction(self.actionKerrolos_Wageeh_19P3468)
        self.menuBar.addAction(self.menuShow.menuAction())
        self.menuBar.addAction(self.menuDeveloped_by.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PDA"))
        self.insertStartSymbolLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Start symbol:</span></p></body></html>"))
        self.showPDAPushButton.setText(_translate("MainWindow", "Convert"))
        self.pdaLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">PDA Graph:</p></body></html>"))
        self.insertAlphabetLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Alphabet (terminals): </span><span style=\" font-size:9pt;\">&quot;separated by commas&quot;</span></p></body></html>"))
        self.insertRulesLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Production rules: </span><span style=\" font-size:9pt;\">&quot;each on a separate line&quot;</span></p></body></html>"))
        self.inputRulesTextEdit.setPlaceholderText(_translate("MainWindow", "ex: E -> E + T | T"))
        self.transitionsTitleLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">PDA Transitions:</span></p></body></html>"))
        self.transitionsTextLabel.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.menuShow.setTitle(_translate("MainWindow", "Show"))
        self.menuDeveloped_by.setTitle(_translate("MainWindow", "Developed by"))
        self.actionYoussef_Geroge_19P9880.setText(_translate("MainWindow", "Youssef George    19P9824"))
        self.actionMostafa_Nasrat_19P4619.setText(_translate("MainWindow", "Mostafa Nasrat    19P4619"))
        self.actionAnthony_Amgad_19P9880.setText(_translate("MainWindow", "Anthony Amgad  19P9880"))
        self.actionKerrolos_Wageeh_19P3468.setText(_translate("MainWindow", "Kerrolos Wageeh 19P3468"))
        self.showParsingTableAction.setText(_translate("MainWindow", "Parsing Table"))
        self.showParsingTableAction.setStatusTip(_translate("MainWindow", "Opens SLR(1) parsing table"))
        self.showParsingTableAction.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.showDemoAction.setText(_translate("MainWindow", "Demo"))
from PyQt6 import QtWebEngineWidgets
