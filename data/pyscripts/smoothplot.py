import pandas as pd
import matplotlib.pyplot as plt
import sys

MEMORY = 3600

# Path to Pandas dataframe pickle
path = sys.argv[1]

# Read pickle to dataframe
df = pd.read_pickle(path);

df.plot(x='datetime', y='p')
# Smooth
df['p'] = pd.rolling_mean(df['p'], 3600)

df.plot(x='datetime', y='p')
plt.show()

