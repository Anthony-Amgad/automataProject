from PyQt5 import QtWidgets, uic, QtWebEngineWidgets, QtCore, QtGui
import sys
import os.path

from NFAgraph import NFAGraphPlot
from DFAgraph import DFAGraphPlot


class N2D(QtWidgets.QMainWindow):

    Nodes = []
    Edges = []
    AdjLi = {}
    count = 0

    def reGraph(self):
        self.AdjLi = NFAGraphPlot.plotDir(self.Nodes,self.Edges)
        self.graphBrowser.load(QtCore.QUrl.fromLocalFile(os.path.abspath("res/NFAgraph.html")))

    def DFAdraw(self, nodes, edges):
        self.AdjLi = DFAGraphPlot.plotDir(nodes, edges)
        self.treeBrowser.load(QtCore.QUrl.fromLocalFile(os.path.abspath("res/DFAgraph.html")))
    
    def addNode(self, bool):
        self.count+=1
        self.Nodes.append({"name":self.count, "goal":bool})
        self.fromEdAddCom.addItem(str(self.count))
        self.toEdAddCom.addItem(str(self.count))
        self.delNodeCom.addItem(str(self.count))
        self.reGraph()
        """try:
            if next((x for x in self.Nodes if x["name"] == self.nodeNameTxt.text()), None)  != None:
                msg = QtWidgets.QMessageBox()
                msg.setWindowIcon(QtGui.QIcon('res/error.png'))
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText('Please Enter Unique Node Name')
                msg.setWindowTitle("Error")
                msg.exec_()
            elif self.nodeNameTxt.text() == "" or self.nodeNameTxt.text()[0].isdigit():
                msg = QtWidgets.QMessageBox()
                msg.setWindowIcon(QtGui.QIcon('res/error.png'))
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText('Please Make sure the Node Name is entered with a character at the start')
                msg.setWindowTitle("Error")
                msg.exec_()
            else:
                nH = self.nodeHuerTxt.text()
                if nH == "":
                    nH = 0.0
                else:
                    nH = float(nH)
                if nH < 0:
                    raise Exception("No Negative Numbers")
                nG = self.checkBox.isChecked()
                nN = self.nodeNameTxt.text().strip()
                self.Nodes.append({"name":nN, "heur":nH, "goal":nG})
                self.fromEdAddCom.addItem(nN)
                self.toEdAddCom.addItem(nN)
                self.delNodeCom.addItem(nN)
                self.nodeNameTxt.setText("")
                self.nodeHuerTxt.setDisabled(False)
                self.nodeHuerTxt.setText("")
                self.checkBox.setCheckState(False)
                if not nG:
                    self.startNodeCom.addItem(nN)
                self.reGraph()
                if len(self.Nodes) >= 2:
                    ngg = list(filter(lambda node: node['goal'], self.Nodes))
                    if (len(ngg) != len(self.Nodes)) and (len(ngg) >= 1):
                        self.searchBtn.setDisabled(False)

        except:
            msg = QtWidgets.QMessageBox()
            msg.setWindowIcon(QtGui.QIcon('res/error.png'))
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Please check that Node Heuristic is valid')
            msg.setWindowTitle("Error")
            msg.exec_()"""

    
    def addEdge(self):
        try:
            if (self.fromEdAddCom.currentIndex() == -1) or (self.toEdAddCom.currentIndex() == -1):
                msg = QtWidgets.QMessageBox()
                msg.setWindowIcon(QtGui.QIcon('res/error.png'))
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText('Please Make sure both a from and to Node are selected')
                msg.setWindowTitle("Error")
                msg.exec_()
            else:
                eC = self.edPathCTxt.text()
                if eC == "":
                    eC = "ε"
                self.Edges.append({"from":int(self.fromEdAddCom.currentText()),"to":int(self.toEdAddCom.currentText()),"cost":eC})
                self.delEdCom.addItem(self.fromEdAddCom.currentText() + " > " + self.toEdAddCom.currentText() + " : " + str(eC))
                self.fromEdAddCom.setCurrentIndex(-1)
                self.toEdAddCom.setCurrentIndex(-1)
                self.edPathCTxt.setText("")
                self.reGraph()

        except:
            msg = QtWidgets.QMessageBox()
            msg.setWindowIcon(QtGui.QIcon('res/error.png'))
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Please check that Edge Path Cost is valid')
            msg.setWindowTitle("Error")
            msg.exec_()

    def delNode(self):
        if self.delNodeCom.currentIndex() != -1:
            nL = list(filter(lambda node: node['name'] != int(self.delNodeCom.currentText()), self.Nodes))
            nE = list(filter(lambda edge: edge['from'] != int(self.delNodeCom.currentText()), self.Edges))
            nE = list(filter(lambda edge: edge['to'] != int(self.delNodeCom.currentText()), nE))
            self.Edges = nE
            self.Nodes = nL
            fC = [self.fromEdAddCom.itemText(i) for i in range(self.fromEdAddCom.count())]
            for i in range(0,len(fC)):
                if fC[i] == self.delNodeCom.currentText():
                    self.fromEdAddCom.removeItem(i)
            tC = [self.toEdAddCom.itemText(i) for i in range(self.toEdAddCom.count())]
            for i in range(0,len(tC)):
                if tC[i] == self.delNodeCom.currentText():
                    self.toEdAddCom.removeItem(i)
            #sC = [self.startNodeCom.itemText(i) for i in range(self.startNodeCom.count())]
            #for i in range(0,len(sC)):
                #if sC[i] == self.delNodeCom.currentText():
                    #self.startNodeCom.removeItem(i)
            self.delNodeCom.removeItem(self.delNodeCom.currentIndex())
            self.reGraph()
            if len(self.Nodes) < 2:    
                self.searchBtn.setDisabled(True)
            else:
                ngg = list(filter(lambda node: node['goal'], self.Nodes))
                if (len(ngg) == len(self.Nodes)) or (len(ngg) < 1):
                    self.searchBtn.setDisabled(True)
            dEc = [self.delEdCom.itemText(i) for i in range(self.delEdCom.count())]
            nl = []
            for i in range(0,len(dEc)):
                Ef, Et = dEc[i].split('>')
                Ef.strip()
                Ef.strip()
                Et, Ec = Et.split(':')
                Et.strip()
                Ec = Ec[1:]
                if next((edge for edge in self.Edges if ((edge['from'] == int(Ef)) or (edge['to'] == int(Et)))), None)  == None:
                    nl.append(i)
            for kk in range(len(nl)-1,-1,-1):
                self.delEdCom.removeItem(nl[kk])            
            self.delNodeCom.setCurrentIndex(-1)   

    def delEdge(self):
        if self.delEdCom.currentIndex() != -1:
            Ef, Et = self.delEdCom.currentText().split('>')
            Ef.strip()
            Et, Ec = Et.split(':')
            Et.strip()
            Ec = Ec[1:]
            #Ef = Ef[:-1]
            #Et = Et[1:-1]
            self.Edges.remove({"from":int(Ef),"to":int(Et),"cost":Ec})
            self.delEdCom.removeItem(self.delEdCom.currentIndex())
            self.reGraph()
            self.delEdCom.setCurrentIndex(-1)
            
    def checkBoxClick(self):
        if self.checkBox.isChecked():
            self.Nodes[0] = {"name":0, "goal":True}
        else:
            self.Nodes[0] = {"name":0, "goal":False}
        self.reGraph()

    def getClosure(self, node):
        nodes = {node}
        nodes2disc = [node]
        #print(self.AdjLi[node])
        for curn in nodes2disc:
            for n in self.AdjLi[curn]:
                try:
                    if (not {n}.issubset(nodes)) and (self.Edges.index({'from':curn, 'to':n, 'cost':"ε"}) != None):
                        nodes.add(n)
                        nodes2disc.append(n)
                except:
                    pass
        print(nodes)
        return nodes

    def onClickConv(self):
        DFAnodes = []
        finalNodes = []
        DFAedges = []

        for n in self.Nodes:
            clos = self.getClosure(n["name"])
            try:
                if DFAnodes.index(clos) != None:
                    pass
            except:
                DFAnodes.append(clos)

        for no in DFAnodes:
            for n in no:
                nE = list(filter(lambda edge: (edge['from'] == n) and (edge['cost'] != "ε"), self.Edges))
                for edge in nE:
                     for nod in DFAnodes:
                         if {edge["to"]}.issubset(nod):
                             DFAedges.append({"from":no, "to":nod, "cost":edge["cost"]})

        for no in DFAnodes:
            goal = False
            for n in no:
                gN = list(filter(lambda nod: (nod['name'] == n) and (nod['goal'] == True), self.Nodes))
                if len(gN) > 0:
                    goal = True
            finalNodes.append({"name":no ,"goal":goal})

        #print(DFAnodes)
        self.DFAdraw( finalNodes, DFAedges)                   

    
    def __init__(self):
        super(N2D,self).__init__()
        uic.loadUi('res/GraphingWindow.ui',self)

        self.Nodes = [{"name":0, "goal":False}]
        self.Edges = []
        self.AdjLi = {}
        self.count = 0

        self.setWindowIcon(QtGui.QIcon('res/img.png'))
        self.setWindowTitle("Directed Graph")


        self.setFixedSize(1112, 858)
        
        self.graphBrowser = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.graphBrowser.setGeometry(QtCore.QRect(0, 220, 551, 601))
        self.graphBrowser.setObjectName("graphBrowser")
        self.reGraph()

        self.treeBrowser = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.treeBrowser.setGeometry(QtCore.QRect(560, 220, 551, 601))
        self.treeBrowser.setObjectName("treeBrowser")
        #self.reTree(False)

         

        self.fromEdAddCom.lineEdit().setPlaceholderText("From")
        self.toEdAddCom.lineEdit().setPlaceholderText("To")
        self.delEdCom.lineEdit().setPlaceholderText("Pick an Edge to Delete")
        self.delNodeCom.lineEdit().setPlaceholderText("Pick a Node to Delete")
        
        self.fromEdAddCom.addItem("0")
        self.toEdAddCom.addItem("0")

        self.adAccNodeBtn.clicked.connect(lambda: self.addNode(True))
        self.adTransNodeBtn.clicked.connect(lambda: self.addNode(False))
        self.adEdgeBtn.clicked.connect(self.addEdge)
        self.delNodeBtn.clicked.connect(self.delNode)
        self.delEdgeBtn.clicked.connect(self.delEdge)
        self.searchBtn.clicked.connect(self.onClickConv)
        self.checkBox.clicked.connect(self.checkBoxClick)


        self.show()

        ##This is for finding functions using auto complete as they cannot be found with the item loaded in the .ui
        #self.x = QtWidgets.QCheckBox(self.centralwidget)
        #self.x.clicked.connect


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = N2D()
    app.exec_()