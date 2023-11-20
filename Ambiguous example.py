import json
import matplotlib.pyplot as plt

# Load data from the file
map_coordinates_path = "snli_roberta_0_6_data_map_coordinates.jsonl"

with open(map_coordinates_path, "r") as file:
    map_coordinates_data = [json.loads(line) for line in file]

# Extract variability values
variability_values = [entry["variability"] for entry in map_coordinates_data]

# Print the distribution
print("Variability Distribution:")
print(variability_values)

# Plot the distribution
plt.hist(variability_values, bins=30, color='blue', edgecolor='black', alpha=0.7)
plt.title('Variability Distribution')
plt.xlabel('Variability')
plt.ylabel('Frequency')
plt.show()
