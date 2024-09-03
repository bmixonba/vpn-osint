
import networkx as nx
import matplotlib.pyplot as plt

# Example: Create a network graph to visualize software phylogenetics
def visualize_phylogenetics(versions, similarities):
    G = nx.Graph()

    # Add nodes for each version
    for version in versions:
        G.add_node(version)

    # Add edges based on similarities
    for i in range(len(versions)):
        for j in range(i + 1, len(versions)):
            similarity = similarities[i][j]
            if similarity > 0.5:  # Adjust threshold as needed
                G.add_edge(versions[i], versions[j], weight=similarity)

    # Layout and plot the graph
    pos = nx.spring_layout(G)  # You can use different layout algorithms
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title('Software Phylogenetics')
    plt.show()

# Example usage
versions = ['v1', 'v2', 'v3', 'v4']
similarities = [
    [1.0, 0.8, 0.4, 0.6],
    [0.8, 1.0, 0.7, 0.5],
    [0.4, 0.7, 1.0, 0.3],
    [0.6, 0.5, 0.3, 1.0]
]

visualize_phylogenetics(versions, similarities)
