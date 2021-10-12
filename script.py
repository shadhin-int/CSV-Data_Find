# %%
import pandas as pd
from collections import Counter

# reading CSV file
data = pd.read_csv("Wheat.csv")

# converting column data to list
genome_varity = data['genome_varity'].tolist()
data_count = Counter(genome_varity)
# printing list data
print('Data Counting:', data_count)
