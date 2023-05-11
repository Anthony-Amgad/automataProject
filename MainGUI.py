from PyQt5 import QtWidgets, uic, QtGui
import sys

from NFA2DFA import N2D
from PdaGui import PDAUi

class MUi(QtWidgets.QMainWindow):
    def openDirectedWindow(self):
        self.ui = N2D()

    def openCfgToPdaWindow(self):
        self.ui = PDAUi()
        
    def __init__(self):
        super(MUi,self).__init__()
        uic.loadUi('res/ui/MainWindow.ui',self)

        self.setFixedSize(800, 230)

        self.setWindowIcon(QtGui.QIcon('res/img.png'))

        self.nfaToDfaPushButton.clicked.connect(self.openDirectedWindow)
        self.cfgToPdaPushButton.clicked.connect(self.openCfgToPdaWindow)

        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MUi()
    app.exec_()