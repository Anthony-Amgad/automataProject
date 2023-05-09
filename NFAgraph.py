
from pyvis.network import Network

class NFAGraphPlot:

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

        for n in Nodes:
            if n["goal"]:
                G.add_node(n["name"], "q"+str(n["name"]), shape="ellipse", color = "yellow")
            else:
                G.add_node(n["name"], "q"+str(n["name"]), shape="ellipse")

        G.add_edge("start", 0)

        for e in Edges:
            G.add_edge(e["from"], e["to"], label = e["cost"])
        #G.toggle_physics(status=True)
        G.save_graph("res/NFAgraph.html")
        return G.get_adj_list()

    def plotDir(Nodes,Edges):
        return NFAGraphPlot.plot(Nodes, Edges, True)

    def plotUnDir(Nodes,Edges):
        return NFAGraphPlot.plot(Nodes, Edges, False)
        


