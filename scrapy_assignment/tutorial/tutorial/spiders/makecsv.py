import pandas as pd

df = pd.read_json("quotes.json")
df.to_csv("dataquotes.csv", index=False)