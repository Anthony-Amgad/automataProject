from PyQt5 import QtWidgets, uic, QtGui, QtWebEngineWidgets, QtCore
import sys
import os.path
from PDA import PDA

class PDAUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(PDAUi,self).__init__()
        uic.loadUi('res/ui/PdaWindow.ui',self)
        self.setFixedSize(1000, 968)
        self.showPDAPushButton.clicked.connect(self.onClickShowPDA)
        self.show()

    def onClickShowPDA(self):
        startSymbol = str(self.inputStartSymbolTextEdit.toPlainText()).strip()
        terminals = str(self.inputAlphabetTextEdit.toPlainText()).strip().replace(' ', '').split(',')
        rules = str(self.inputRulesTextEdit.toPlainText()).strip()
        
        pda = PDA(startSymbol, terminals, rules)
        states , transitions = pda.states, pda.transitions
        states , transitions = pda.getStatesTransitions()
        pda.drawGraph()
        self.pdaWebEngineView.load(QtCore.QUrl.fromLocalFile(os.path.abspath("res/graphs/PDAgraph.html")))

        
        for state in states:
            print(state)
        for trans in transitions:
            print(trans)
                
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PDAUi()
    app.exec_()