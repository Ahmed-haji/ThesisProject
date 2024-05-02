import matplotlib.pyplot as plt

# Recall levels
recall_levels = [0, 0.25, 0.5, 0.75, 1.0]

# Precision values
precision_values = [0, 0.5, 0.67, 0.75, 1.0]

# Plot interpolated precision-recall curve
plt.plot(recall_levels, precision_values, marker='o')

# Add labels and title
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Interpolated Precision-Recall Curve')

# Show the plot
plt.grid(True)
plt.show()

