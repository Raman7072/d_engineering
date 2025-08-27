import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Main topic
G.add_node("Python for Data Engineering")

# Subtopics and details
topics = {
    "Why Python is Popular": [
        "Beginner-Friendly",
        "Google's Support",
        "Glue Language"
    ],
    "Built-in Toolbox": [
        "collections",
        "array",
        "re",
        "json, csv, xml"
    ],
    "Third-Party Libraries": [
        "Tabular Data → pola.rs",
        "Text Data → NLTK, spaCy",
        "Scientific Computing → numpy, scipy"
    ],
    "Why This Matters": [
        "Extracting Data",
        "Cleaning Data",
        "Transforming Data",
        "Loading to DBs"
    ],
    "Practice Tasks": [
        "Word Count (Counter)",
        "JSON Handling",
        "Email Validation (re)",
        "CSV with pola.rs",
        "Text Analysis (spaCy)"
    ]
}

# Add nodes and edges
for topic, details in topics.items():
    G.add_node(topic)
    G.add_edge("Python for Data Engineering", topic)
    for detail in details:
        G.add_node(detail)
        G.add_edge(topic, detail)

# Draw the mindmap-style diagram
plt.figure(figsize=(14, 10))
pos = nx.spring_layout(G, k=0.6, seed=42)

nx.draw(
    G, pos, with_labels=True, 
    node_size=2800, node_color="lightblue", 
    font_size=9, font_weight="bold", 
    edge_color="gray", arrows=True
)

plt.title("Python for Data Engineering - Mindmap", fontsize=14, fontweight="bold")
plt.show()
