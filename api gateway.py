import pandas as pd
import json

# Load JSON file
with open("oracle-cards-20241106100156.json") as file:
    data = json.load(file)  # Load JSON data into a dictionary

# Convert JSON data to a DataFrame
df = pd.json_normalize(data)

# Count the unique parameters in the file
unique_parameters = df.columns.tolist()
print(f"Total unique parameters: {len(unique_parameters)}")
print("Parameter names:", unique_parameters)


#get