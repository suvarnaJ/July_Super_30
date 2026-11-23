
import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# --------------------------------
# 1. CREATE ENTITIES (NODES)
# --------------------------------

# Suppliers
G.add_node("Lithium Mining Co", type="Supplier", tier="Tier-2")
G.add_node("Battery Materials Ltd", type="Supplier", tier="Tier-1")
G.add_node("ChipTech Electronics", type="Supplier", tier="Tier-1")

# Components
G.add_node("Lithium Battery", type="Component")
G.add_node("Microcontroller", type="Component")

# Products
G.add_node("Electric Vehicle", type="Product")

# Plants
G.add_node("Pune Plant", type="Plant")

# Countries
G.add_node("Australia", type="Country")
G.add_node("China", type="Country")
G.add_node("India", type="Country")

# Shipments
G.add_node("Shipment-101", type="Shipment")
G.add_node("Shipment-102", type="Shipment")


# --------------------------------
# 2. CREATE RELATIONSHIPS (EDGES)
# --------------------------------

# Supplier -> Component
G.add_edge(
    "Battery Materials Ltd",
    "Lithium Battery",
    relationship="SUPPLIES"
)

G.add_edge(
    "ChipTech Electronics",
    "Microcontroller",
    relationship="SUPPLIES"
)

# Tier-2 supplier -> Tier-1 supplier
G.add_edge(
    "Lithium Mining Co",
    "Battery Materials Ltd",
    relationship="SUPPLIES"
)

# Component -> Product
G.add_edge(
    "Lithium Battery",
    "Electric Vehicle",
    relationship="USED_IN"
)

G.add_edge(
    "Microcontroller",
    "Electric Vehicle",
    relationship="USED_IN"
)

# Product -> Plant
G.add_edge(
    "Electric Vehicle",
    "Pune Plant",
    relationship="MANUFACTURED_AT"
)

# Supplier -> Country
G.add_edge(
    "Lithium Mining Co",
    "Australia",
    relationship="LOCATED_IN"
)

G.add_edge(
    "Battery Materials Ltd",
    "China",
    relationship="LOCATED_IN"
)

G.add_edge(
    "ChipTech Electronics",
    "India",
    relationship="LOCATED_IN"
)

# Shipment -> Component
G.add_edge(
    "Shipment-101",
    "Lithium Battery",
    relationship="CONTAINS"
)

G.add_edge(
    "Shipment-102",
    "Microcontroller",
    relationship="CONTAINS"
)

# Shipment -> Plant
G.add_edge(
    "Shipment-101",
    "Pune Plant",
    relationship="DESTINED_FOR"
)

G.add_edge(
    "Shipment-102",
    "Pune Plant",
    relationship="DESTINED_FOR"
)


# --------------------------------
# 3. DISPLAY GRAPH INFORMATION
# --------------------------------

print("\n--- SUPPLY CHAIN NODES ---")

for node, attributes in G.nodes(data=True):
    print(node, attributes)

print("\n--- SUPPLY CHAIN RELATIONSHIPS ---")

for source, target, attributes in G.edges(data=True):
    print(
        source,
        "-->",
        attributes["relationship"],
        "-->",
        target
    )


# --------------------------------
# 4. VISUALIZE GRAPH
# --------------------------------

pos = nx.spring_layout(G, seed=42, k=1.5)

node_colors = []

color_map = {
    "Supplier": "orange",
    "Component": "lightblue",
    "Product": "lightgreen",
    "Plant": "red",
    "Country": "lightyellow",
    "Shipment": "violet"
}

for node in G.nodes():
    node_type = G.nodes[node]["type"]
    node_colors.append(color_map[node_type])

plt.figure(figsize=(18, 12))

nx.draw_networkx_nodes(
    G,
    pos,
    node_color=node_colors,
    node_size=2200
)

nx.draw_networkx_labels(
    G,
    pos,
    font_size=8,
    font_weight="bold"
)

nx.draw_networkx_edges(
    G,
    pos,
    arrows=True,
    arrowsize=20,
    edge_color="gray",
    connectionstyle="arc3,rad=0.05"
)

edge_labels = nx.get_edge_attributes(
    G, "relationship"
)

nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=edge_labels,
    font_size=7
)

plt.title(
    "Mini Supply Chain Risk Graph",
    fontsize=18
)

plt.axis("off")
plt.tight_layout()
plt.show()



# --------------------------------
# 5. SUPPLIER RISK ANALYSIS
# --------------------------------

def identify_affected_products(supplier):

    affected_components = []

    for node in G.successors(supplier):

        relationship = G[supplier][node]["relationship"]

        if relationship == "SUPPLIES":
            affected_components.append(node)

    affected_products = set()

    for component in affected_components:

        for product in G.successors(component):

            relationship = G[component][product]["relationship"]

            if relationship == "USED_IN":
                affected_products.add(product)

    return affected_components, affected_products


supplier = "Lithium Mining Co"

components, products = identify_affected_products(supplier)

print("\n--- SUPPLIER RISK REPORT ---")

print("At-risk supplier:", supplier)

print("Affected components:", components)

print("Affected products:", list(products))

for product in products:

    for plant in G.successors(product):

        if G[product][plant]["relationship"] == "MANUFACTURED_AT":

            print("Affected manufacturing plant:", plant)
