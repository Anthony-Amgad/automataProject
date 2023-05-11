from pyvis.network import Network

class PDA:
    startSymbol = ''
    terminals = []
    rules = ''
    states = []
    transitions = []

    def __init__(self, startSymbol, terminals, rules):
        self.startSymbol = startSymbol
        self.terminals = terminals
        self.rules = rules
        #self.states, self.transitions = self.__getStatesTransitions()

    def getStatesTransitions(self):
        
        # initial state & transition
        self.states = [ State('q0', True, False),
                       State('q1', False, False),
                       State('q2', False, False),
                       State('q3', False, True) ]
        
        self.transitions = [ Transition("ε", 'q0', 'q1', "ε", "$"),
                            Transition("ε", 'q1', 'q2', "ε", self.startSymbol),
                            Transition("ε", 'q2', 'q3', "$", "ε") ]

        try:
            self.rules = self.rules.splitlines() 
            unit_rules = []
            for rule in self.rules:
                rule = rule.strip().replace(' ', '')
                [lhs, rhs] = rule.split('->')
                rhs = rhs.split('|')
                for term in rhs:
                    unit_rules.append((lhs, term))
            
            for rule in unit_rules:
                lhs, rhs = rule[0], rule[1]
                rhs = rhs[::-1] # Necessary for the terminals to pushed in correct order
                start = 'q2'
                for i, char in enumerate(rhs):  #####!!!!!!! rhs.reverse()
                    poped = lhs if i==0 else "ε" 
                    if i==len(rhs)-1:
                        trans = Transition("ε", start, 'q2', poped , rhs[i])
                    else:
                        end = 'q'+str(len(self.states))
                        state = State(end, False, False)
                        self.states.append(state)
                        trans = Transition("ε", start, end, poped , rhs[i])
                        start = end
                    
                    self.transitions.append(trans)
                
            for terminal in self.terminals:
                self.transitions.append(Transition(terminal, 'q2', 'q2', terminal, 'ε'))

        except:
            raise IllegalFormatException('rule')
    
        return self.states, self.transitions
    
    def drawGraph(self):
        G = Network(height='100%', width='100%', directed=True)

        G.set_options("""var options = {
                "physics":{
                "enabled": true
                },
                  "edges": {
                    "smooth": {
                        "enabled" : true
                    },
                    "color": {
                        "inherit" : false
                    }
                  },
                  "interaction": {
                    "hover": true,
                    "keyboard": {
                      "enabled": true
                    },
                    "multiselect": true,
                    "navigationButtons": true
                  }
                }
        """)
        
        for state in self.states:
            G.add_node(state.name, state.name)
        
        for trans in self.transitions:
            G.add_edge(trans.currState, trans.nextState, label=str(trans))

        G.save_graph("res/graphs/PDAgraph.html")

class State:
    name = ""
    isInitial = False
    isFinal = False

    def __init__(self, name, isInitial, isFinal):
        self.name = name
        self.isInitial = isInitial
        self.isFinal = isFinal
    
    def setFinal (self, isFinal):
        self.isFinal = isFinal
    
    def setInitial (self, isInitial):
        self.isInitial = isInitial
    
    def __str__(self):
        string = self.name 
        return string


class Transition:
    inputSymbol = ''
    currState = ''
    nextState = ''
    popSymbol = ''
    pushSymbol = ''
    
    def __init__(self, inputSymbol, currState, nextState, popSymbol, pushSymbol):
        self.inputSymbol = inputSymbol
        self.currState = currState
        self.nextState = nextState
        self.popSymbol = popSymbol
        self.pushSymbol = pushSymbol
    
    def __str__(self):
        string = self.inputSymbol + ", " + self.popSymbol + " → " + self.pushSymbol 
        return string


class IllegalFormatException(Exception):
    def __init__(self, rule):
        self.st1 = "Illegal format in this rule" + rule
    def __str__(self):
        string =  self.st1
        return string  
        
