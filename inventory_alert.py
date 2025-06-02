import pandas as pd

def check_inventory(file_path):
    df = pd.read_csv(file_path)  # Reads CSV

    for index, row in df.iterrows():
        item = row['Item']
        quantity = row['Quantity']
        threshold = row['Threshold']

        if quantity < threshold:
            print(f"⚠️  Low stock alert: '{item}' (Quantity: {quantity}, Threshold: {threshold})")

if __name__ == "__main__":
    check_inventory("sample_inventory.csv")

