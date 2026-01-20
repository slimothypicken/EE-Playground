import pandas as pd
import matplotlib.pyplot as plt

#Load CSV

df = pd.read_csv("sensor_data.csv")

#requires a CSV column called value

values = df["value"]

# Compute stats 
mean_val = values.mean() 
std_val = values.std() 
min_val = values.min() 
max_val = values.max() 
print("Mean:", mean_val) 
print("Std Dev:", std_val) 
print("Min:", min_val) 
print("Max:", max_val) 

# Plot 
plt.figure(figsize=(10, 4)) 
plt.plot(values) 
plt.title("Sensor Readings") 
plt.xlabel("Sample") 
plt.ylabel("Value") 
plt.grid(True) 
plt.show()