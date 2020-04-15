import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('covid_19_data.csv')

all_states = df.state

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
print(all_states)
