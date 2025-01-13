
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

# List of attack types
attack_types = ["Bot", "DDoS", "DoS GoldenEye", "DoS Hulk", "DoS Slowhttptest", "DoS slowloris", "FTP-Patator",
                "PortScan", "SSH-Patator"]
benign_type = "BENIGN"

# Initialize an empty list to store results as dictionaries
results = []

# Loop through each attack type
for attack_type in attack_types:
    # Read the feature importance file
    importance_file = f"{attack_type}_importance.csv"
    importance_data = pd.read_csv(importance_file)
    
    # Select the first 4 features
    selected_features = importance_data['Feature'][:3].tolist()
    
    # Read the data file
    data_file = f"{attack_type}_vs_{benign_type}.csv"
    data = pd.read_csv(data_file)
    
    # Select the selected features and the target column
    selected_data = data[selected_features + ['Label']]
    
    # Split the data into features (X) and target (y)
    X = selected_data[selected_features]
    y = selected_data['Label']
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)
    
    # Train Naive Bayes
    nb_model = GaussianNB()
    nb_model.fit(X_train, y_train)
    
    # Train Quadratic Discriminant Analysis
    qda_model = QuadraticDiscriminantAnalysis()
    qda_model.fit(X_train, y_train)
    
    # Train Multi-Layer Perceptron
    mlp_model = MLPClassifier(random_state=42, max_iter=1000, learning_rate_init=0.001)
    mlp_model.fit(X_train, y_train)
    
    # Predictions
    nb_preds = nb_model.predict(X_test)
    qda_preds = qda_model.predict(X_test)
    mlp_preds = mlp_model.predict(X_test)
    
    # Calculate accuracies
    nb_accuracy = accuracy_score(y_test, nb_preds)
    qda_accuracy = accuracy_score(y_test, qda_preds)
    mlp_accuracy = accuracy_score(y_test, mlp_preds)
    
    # Store the results as a dictionary
    result_dict = {
        'Attack Type': attack_type,
        'Naive Bayes Accuracy': nb_accuracy,
        'QDA Accuracy': qda_accuracy,
        'MLP Accuracy': mlp_accuracy
    }
    
    # Append the dictionary to the results list
    results.append(result_dict)

# Create a Pandas DataFrame from the results list 
results_df = pd.DataFrame(results)

# Display the DataFrame
print(results_df)









