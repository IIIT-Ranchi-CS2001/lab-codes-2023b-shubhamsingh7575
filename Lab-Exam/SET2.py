import pandas as pd

# Load the dataset (replace 'your_dataset.csv' with the actual filename)
dataset_path = 'AQI_Data.csv'
data = pd.read_csv(dataset_path)

# (a) Rename columns
data.rename(columns={
    "AQI": "Air Quality Index",
    "PM2.5": "Particular Matter 2.5",
    "PM10": "Particular Matter 10",
    "City": "Location"
}, inplace=True)

# (b) Replace "Unknown" with "Not Available" in the "Location" column
data['Location'] = data['Location'].replace("Unknown", "Not Available")


output_path = 'result.csv'
data.to_csv(output_path, index=False)


print(data)
