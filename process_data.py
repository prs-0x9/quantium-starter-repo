import pandas as pd
import os

# Define the correct path to the data folder
data_folder = os.path.join(os.getcwd(), "data")

# Define the path to the data
files = [
    os.path.join(data_folder, "daily_sales_data_0.csv"),
    os.path.join(data_folder, "daily_sales_data_1.csv"),
    os.path.join(data_folder, "daily_sales_data_2.csv")
]

# Initialize an empty list to store the dataframes
dfs = []

# Loop through the files
for file in files:
    if os.path.exists(file):  

        # Load the data
        df = pd.read_csv(file)

        # Filter the data for pink morsels
        df = df[df["product"].str.strip().str.lower() == "pink morsel"]

        # Create the 'sales' column by multiplying 'quantity' and 'price'
        df["sales"] = df["quantity"] * df["price"].replace({'\$': '', ',': ''}, regex=True).astype(float)

        # Keep the relevant columns
        df = df[["sales", "date", "region"]]

        # Append the dataframe to the list
        dfs.append(df)

    else:
        print(f"File {file} not found")

# Combine and save if there is data
if dfs:
    final_df = pd.concat(dfs, ignore_index=True)
    final_df.to_csv("formatted_sales.csv", index=False)
    print("Formatted data saved to formatted_sales.csv")
else:
    print("No valid data found.")
