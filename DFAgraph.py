
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
        name = ""
        for n in Nodes:
            if n["goal"]:
                G.add_node(str(n["name"]), "q"+str(n["name"]), shape="ellipse", color = "yellow")
            else:
                G.add_node(str(n["name"]), "q"+str(n["name"]), shape="ellipse")
            if first:
                name = str(n["name"]) 
            first = False           
        
        G.add_edge("start", name)

        for e in Edges:
            G.add_edge(str(e["from"]), str(e["to"]), label = e["cost"])
        #G.toggle_physics(status=True)
        G.save_graph("res/DFAgraph.html")
        return G.get_adj_list()

    def plotDir(Nodes,Edges):
        return DFAGraphPlot.plot(Nodes, Edges, True)

    def plotUnDir(Nodes,Edges):
        return DFAGraphPlot.plot(Nodes, Edges, False)
        


