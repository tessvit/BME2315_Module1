import pandas as pd
df = pd.read_csv("C:/Users/tmvit/OneDrive/Desktop/BME 2315/Module 0/BME2315_Module1/Metadata and Protein Data for Module 1.csv")

for header in df.columns:
    print(header)