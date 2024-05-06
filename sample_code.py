#Importanting required file names
import pandas as pd
import numpy as np
from rapidfuzz import process, fuzz

# Reading Master File and Lookup file
master_df = pd.read_csv("filePath\\MasterFileName.csv")
lookup_df = pd.read_csv("filePath\\LookupFileName.csv")

# Delete records with Null values from Master file
master_df = master_df.dropna(subset=['Clean Name'])

# Creating a tuple having Matching Value from the Master File, Matching percent, and Index of the matched record in the master file
# Matching cut-off is selected as 80%. If a record in lookup has a match of 80% or more, the tuple will be returned
lookup_df['join_key_tuple'] = lookup_df['Clean Name'].apply(lambda x: process.extractOne(x, master_df['Clean Name'], scorer=fuzz.QRatio, score_cutoff=80))

# Setting index=False to avoid writing row indices to CSV
lookup_df.to_csv(“Final_data.csv", index=False)  
