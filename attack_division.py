# Importing the libraries
import pandas as pd
import numpy as np
import time
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.utils import resample
from sklearn import preprocessing
from warnings import simplefilter
from imblearn.under_sampling import RandomUnderSampler

# Suppress FutureWarning messages
simplefilter(action='ignore', category=FutureWarning)

# Record start time
start_time = time.time()

# Load the main dataset (./attack_data/attack_data.csv)
main_dataset = pd.read_csv("./attack_data/combined_data.csv")

# List of attack types and BENIGN
attack_types = ["Bot", "DDoS", "DoS GoldenEye", "DoS Hulk", "DoS Slowhttptest", "DoS slowloris", "FTP-Patator",
                "Heartbleed", "Infiltration", "PortScan", "SSH-Patator", "Web Attack  Brute Force",
                "Web Attack  Sql Injection", "Web Attack  XSS"]
benign_type = "BENIGN"

# Loop through each attack type
for attack_type in attack_types:
    # Create a DataFrame for the current attack type
    attack_data = main_dataset[main_dataset[" Label"] == attack_type]
    
    # Create a DataFrame for BENIGN data
    benign_data = main_dataset[main_dataset[" Label"] == benign_type]
    
    # Concatenate the attack and benign data
    combined_data = pd.concat([attack_data, benign_data], axis=0)
    
    # Shuffle the combined data
    combined_data = combined_data.sample(frac=1, random_state=42)
    
    # Save the combined data to a CSV file
    output_filename = f"./attack_data/{attack_type}_vs_{benign_type}.csv"
    combined_data.to_csv(output_filename, index=False)
    print(f"Saved {output_filename}")

# Calculate and print the execution time
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.2f} seconds")



import pandas as pd
import glob

# List of file names
file_names = [
    'Bot_vs_BENIGN.csv', 'DDoS_vs_BENIGN.csv', 'DoS GoldenEye_vs_BENIGN.csv',
    'DoS Hulk_vs_BENIGN.csv', 'DoS Slowhttptest_vs_BENIGN.csv',
    'DoS slowloris_vs_BENIGN.csv', 'FTP-Patator_vs_BENIGN.csv',
    'Heartbleed_vs_BENIGN.csv', 'Infiltration_vs_BENIGN.csv',
    'PortScan_vs_BENIGN.csv', 'SSH-Patator_vs_BENIGN.csv',
    'Web Attack  Brute Force_vs_BENIGN.csv',
    'Web Attack  Sql Injection_vs_BENIGN.csv', 'Web Attack  XSS_vs_BENIGN.csv'
]

# Loop through each file
for file_name in file_names:
    # Read the file using pandas
    data = pd.read_csv(file_name)
    
    # Count the number of benign and attack instances
    num_benign = (data[' Label'] == 'BENIGN').sum()
    num_attack = (data[' Label'] != 'BENIGN').sum()
    
    # Print information
    print(f"File: {file_name}")
    print(f"Number of Benign instances: {num_benign}")
    print(f"Number of Attack instances: {num_attack}")
    print("Shape of the dataset:", data.shape)
    print("-----------------------------")






