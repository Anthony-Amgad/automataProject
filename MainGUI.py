from PyQt5 import QtWidgets, uic, QtGui
import sys

from NFA2DFA import N2D

class MUi(QtWidgets.QMainWindow):
    def openDirectedWindow(self):
        self.ui = N2D()

    def openUnDirectedWindow(self):
        self.ui = N2D()
        
    def __init__(self):
        super(MUi,self).__init__()
        uic.loadUi('res/ui/MainWindow.ui',self)

        self.setFixedSize(804, 156)

        self.setWindowIcon(QtGui.QIcon('res/img.png'))

        self.dirPushBut.clicked.connect(self.openDirectedWindow)
        self.undirPushBut.clicked.connect(self.openUnDirectedWindow)

        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MUi()
    app.exec_()