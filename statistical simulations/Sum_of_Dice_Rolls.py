import numpy as np
import matplotlib.pyplot as plt

# Example simulation data (replace with your actual variables)
num_simulations = 1000000
dice_rolls = np.random.randint(1, 7, size=(num_simulations, 10))
sum_equals_30 = np.sum(dice_rolls, axis=1) == 30

# Histogram of dice roll sums
plt.figure(figsize=(8, 5))
plt.hist(np.sum(dice_rolls, axis=1), bins=range(10, 70), color='purple', edgecolor='black', alpha=0.7)
plt.title("Distribution of Sums from 10 Dice Rolls")
plt.xlabel("Sum of Dice Rolls")
plt.ylabel("Frequency")
plt.axvline(30, color='red', linestyle='--', label='Sum = 30')
plt.legend()
plt.show()
