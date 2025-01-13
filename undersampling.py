import pandas as pd
from imblearn.under_sampling import RandomUnderSampler

# List of attack types and BENIGN
attack_types = ["Bot", "DDoS", "DoS GoldenEye", "DoS Hulk", "DoS Slowhttptest", "DoS slowloris", "FTP-Patator",
                "Heartbleed", "Infiltration", "PortScan", "SSH-Patator", "Web Attack  Brute Force",
                "Web Attack  Sql Injection", "Web Attack  XSS"]
benign_type = "BENIGN"
# Loop through each attack type
for attack_type in attack_types:
    # Load the combined data file
    input_filename = f"{attack_type}_vs_{benign_type}.csv"
    combined_data = pd.read_csv(input_filename)
    
    # Separate features (X) and labels (y)
    X = combined_data.drop(columns=[" Label"])
    y = combined_data[" Label"]
    
    # Skip undersampling if the class count is too low
    if len(set(y)) <= 1:
        print(f"Skipping {attack_type}, not enough classes")
        continue
    
    # Perform undersampling using RandomUnderSampler
    sampler = RandomUnderSampler(sampling_strategy=0.5, random_state=42)
    X_resampled, y_resampled = sampler.fit_resample(X, y)
    
    # Create a DataFrame with resampled data
    resampled_data = pd.DataFrame(X_resampled, columns=X.columns)
    resampled_data["Label"] = y_resampled
    
    # Save the resampled data back to the original file
    resampled_data.to_csv(input_filename, index=False)
    print(f"Resampled and replaced {input_filename}")



import matplotlib.pyplot as plt
import pandas as pd
# Loop through each attack type
for attack_type in attack_types:
    # Load the combined data file
    input_filename = f"{attack_type}_vs_{benign_type}.csv"
    combined_data = pd.read_csv(input_filename)
    
    # Count the number of instances for each class
    class_counts = combined_data[" Label"].value_counts()
    
    # Plot the class distribution
    plt.figure(figsize=(8, 6))
    class_counts.plot(kind="bar", color=["green", "red"])
    plt.title(f"Class Distribution for {attack_type}")
    plt.xlabel("Class")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.legend(["BENIGN", attack_type])
    plt.tight_layout()
    plt.show()



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
    num_benign = (data['Label'] == 'BENIGN').sum()
    num_attack = (data['Label'] != 'BENIGN').sum()
    
    # Print information
    print(f"File: {file_name}")
    print(f"Number of Benign instances: {num_benign}")
    print(f"Number of Attack instances: {num_attack}")
    print("Shape of the dataset:", data.shape)
    print("-----------------------------")






