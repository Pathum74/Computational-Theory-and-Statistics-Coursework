import matplotlib.pyplot as plt
import csv

num_points = []
mean_pi = []
mode_pi = []

with open('pi_estimates.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        num_points.append(int(row[0]))
        mean_pi.append(float(row[1]))
        mode_pi.append(float(row[2]))

true_pi = 3.14159

plt.figure(figsize=(10, 5))
plt.plot(num_points, mean_pi, marker='o', label='Mean π', color='blue')
plt.plot(num_points, mode_pi, marker='o', label='Mode π', color='green')
plt.axhline(y=true_pi, color='red', linestyle='--', label='True π')
plt.xscale('log')
plt.xlabel('Number of Points (log scale)')
plt.ylabel('π Estimate')
plt.title('Convergence of π Estimates')
plt.legend()
plt.grid(True)
plt.show()
