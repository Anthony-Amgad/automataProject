
from pyvis.network import Network

class DFAGraphPlot:

    def plot(Nodes, Edges, bool):
        G = Network(height='100%', width='100%', directed=bool)

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
        
        
        G.add_node("start", "start", shape="ellipse", color = "white")

        first = True
        for n in Nodes:
            if n["goal"]:
                G.add_node(str(n["name"]), "q"+str(n["name"]), shape="ellipse", color = "yellow")
            else:
                G.add_node(str(n["name"]), "q"+str(n["name"]), shape="ellipse")
            if first:
                G.add_edge("start", str(n["name"])) 
            first = False           
        
        finalE = []
        for e in Edges:
            fE = list(filter(lambda edge: (edge['from'] == e['from']) and (edge['to'] == e['to']), finalE))
            if len(fE) > 0:
                 finalE[finalE.index(fE[0])]['cost'] = finalE[finalE.index(fE[0])]['cost'] + "," + e['cost']
            else:
                finalE.append(e.copy())

        for e in finalE:
            G.add_edge(str(e["from"]), str(e["to"]), label = e["cost"])

        G.save_graph("res/graphs/DFAgraph.html")
        return G.get_adj_list()

    def plotDir(Nodes,Edges):
        return DFAGraphPlot.plot(Nodes, Edges, True)

    def plotUnDir(Nodes,Edges):
        return DFAGraphPlot.plot(Nodes, Edges, False)
        


