import numpy as np
import matplotlib.pyplot as plt

# Example simulation data (replace with your actual variables)
num_simulations = 1000000
children = np.random.choice(["B", "G"], size=(num_simulations, 2))
at_least_one_girl = np.any(children == "G", axis=1)
both_girls = np.all(children == "G", axis=1)

# Count outcomes
labels = ['At least one girl', 'Both girls']
values = [np.sum(at_least_one_girl), np.sum(both_girls & at_least_one_girl)]

# Bar chart
plt.figure(figsize=(6, 4))
plt.bar(labels, values, color=['skyblue', 'lightcoral'])
plt.title("Gender Distribution in Simulations")
plt.ylabel("Number of Families")
plt.show()
