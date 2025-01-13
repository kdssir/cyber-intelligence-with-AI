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


# CSV files names:
all_files = [
    "Tuesday-WorkingHours.pcap_ISCX",
    "Wednesday-workingHours.pcap_ISCX",
    "Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX",
    "Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX",
    "Friday-WorkingHours-Morning.pcap_ISCX",
    "Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX",
    "Friday-WorkingHours-Afternoon-DDos.pcap_ISCX"
]
'''
# Load the first CSV file
initial_df = pd.read_csv("Monday-WorkingHours.pcap_ISCX.csv")
initial_df.columns = initial_df.columns.str.strip()
main_labels = repr(list(initial_df.columns)) + "\n"
'''


import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler

# Initialize a list to store processed DataFrames
processed_dataframes = []

# Create a StandardScaler instance for normalization
std_scaler = StandardScaler()

# Function for normalization
def normalize_dataframe(df, columns_to_normalize):
    df[columns_to_normalize] = std_scaler.fit_transform(df[columns_to_normalize])
    return df

for file_path in all_files:
    # Read CSV file
    df = pd.read_csv(file_path + ".csv", encoding='iso-8859-2', engine='python')
    df = pd.DataFrame(df)
    
    # Drop rows with missing Flow Duration values
    df = df.drop(df[pd.isnull(df[" Flow Duration"])].index)
    
    # Replace infinite values with NaN
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    
    # Drop rows with NaN values
    df.dropna(inplace=True)
    
    # Normalize numeric columns
    numeric_columns = df.select_dtypes(include='number').columns
    df[numeric_columns] = df[numeric_columns].astype(np.float32)
    df = normalize_dataframe(df.copy(), numeric_columns)
    
    # Identify and handle categorical columns
    string_columns = [col for col in df.columns if df[col].dtype == "object"]
    try:
        string_columns.remove(' Label')
    except ValueError:
        pass
    
    # Convert categorical columns to numeric
    label_encoder_X = preprocessing.LabelEncoder()
    for col in string_columns:
        try:
            df[col] = label_encoder_X.fit_transform(df[col])
        except:
            df[col] = df[col].replace('Infinity', -1)
   
        # Append the processed and undersampled DataFrame to the list
    processed_dataframes.append(df)
    print("Preprocessing and undersampling of file", file_path, " is done")
# Concatenate the processed DataFrames
combined_dataframe = pd.concat(processed_dataframes, ignore_index=True)

# Save the concatenated DataFrame to a new CSV file
combined_dataframe.to_csv("./attack_data/combined_data.csv", index=False)
print("Concatenation and saving to CSV is done")






