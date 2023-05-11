from PyQt5 import QtWidgets, uic, QtGui, QtWebEngineWidgets, QtCore
import sys
import os.path
from PDA import PDA

class PDAUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(PDAUi,self).__init__()
        uic.loadUi('res/ui/PdaWindow.ui',self)
        #self.setFixedSize(1080, 968)
        self.showPDAPushButton.clicked.connect(self.onClickConvert)
        self.show()

    def onClickConvert(self):
        startSymbol = str(self.inputStartSymbolTextEdit.toPlainText()).strip()
        terminals = str(self.inputAlphabetTextEdit.toPlainText()).strip().replace(' ', '').split(',')
        rules = str(self.inputRulesTextEdit.toPlainText()).strip()
        
        pda = PDA(startSymbol, terminals, rules)
        states , transitions = pda.states, pda.transitions
        states , transitions = pda.getStatesTransitions()
        
        pda.drawGraph()
        self.pdaWebEngineView.load(QtCore.QUrl.fromLocalFile(os.path.abspath("res/graphs/PDAgraph.html")))

        transitionsText = ''
        statesText = [state.name for state in states]

        for trans in transitions:
            transitionsText += (trans.toString()+'\n')
        
        self.transitionsTextLabel.setText(transitionsText)
        
        print(f'PDA States: \n{statesText}')
        print(f'\nPDA Transitions: \n{transitionsText}')
                
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PDAUi()
    app.exec_()