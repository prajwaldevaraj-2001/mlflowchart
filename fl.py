from graphviz import Digraph

# Create a Digraph object
dot = Digraph(format="png")

# Define nodes
nodes = [
    ("Data Collection", "Use Teachable Machine\nCollect 6,000+ images\nCategorize into 3 classes"),
    ("Data Extraction & Structuring", "Extract 'Project1_2.zip'\nVerify directory structure\nOrganize images by class"),
    ("Data Splitting", "Train (80%)\nValidation (10%)\nTest (10%)"),
    ("Data Preprocessing & Augmentation", "Normalize pixel values\nApply augmentation\n(Rotate, zoom, flip, etc.)"),
    ("CNN Model Architecture", "Conv2D, MaxPooling\nBatchNorm, Dropout\nFlatten & Dense layers\nSoftmax activation"),
    ("Model Training & Evaluation", "Train for 50 epochs\nEarlyStopping & ModelCheckpoint\nEvaluate test accuracy"),
    ("Results Visualization", "Plot accuracy & loss\nCheck convergence"),
    ("Confusion Matrix", "Compute true/false pos & neg\nPlot as heatmap"),
    ("Classification Report", "Compute precision, recall, F1-score\nSummarize performance"),
]

# Add nodes to the graph
for i, (title, text) in enumerate(nodes):
    dot.node(str(i), f"{title}\n{text}", shape="box", style="filled", fillcolor="lightblue", fontname="Arial")

# Add arrows between steps
for i in range(len(nodes) - 1):
    dot.edge(str(i), str(i + 1))

# Render and display the flowchart
dot.render("model_flowchart", view=True)
