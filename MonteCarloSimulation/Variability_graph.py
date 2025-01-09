import csv
import matplotlib.pyplot as plt

estimates = []
num_points = []

with open('pi_estimates.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        num_points.append(int(row[0]))
        estimates.append(eval(row[3]))

variability = [max(group) - min(group) for group in estimates]

plt.figure(figsize=(10, 5))
plt.plot(num_points, variability, marker='o', label='Variability Range', color='purple')
plt.xscale('log')
plt.xlabel('Number of Points (log scale)')
plt.ylabel('Range of Estimates')
plt.title('Variability in π Estimates')
plt.legend()
plt.grid(True)
plt.show()
