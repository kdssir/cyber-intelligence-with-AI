# cyber-intelligence-with-AI
Cyber Threat detection using ML algorithms. The "Threat Detection in Cyber Security Using Machine Learning Classifier" POC aims to develop a threat intelligence system using machine learning Classifier. The project consists of several steps, each of which contributes to the overall goal of enhancing cyber security. Here's an overview of each step:

### Step 1: Data Preprocessing (preprocess.py)

- This step involves data preprocessing to prepare the dataset for machine learning.
- The dataset used is the CIC-IDS2017 dataset, which should be stored in the "CSVs" folder located in the same directory as the program.
- You can access the dataset files [here](https://www.unb.ca/cic/datasets/ids-2017.html).

### Step 2: Attack Data Filtering (attack_division.py)

- In this step, the program uses the "attack_data.csv" file to create attack-specific files.
- These attack files are then saved in the "./attack_data/" directory for further analysis.
- The dataset contains a total of 12 attack types, and this step separates them for individual examination.

### Step 3: Feature Selection and Machine Learning (feature_selection.py)

- This step focuses on feature selection for the attack files created in Step 2.
- The program identifies the four features with the highest weight for each file.
- These selected features are used as input for machine learning algorithms.

### Step 4: Machine Learning Algorithm Evaluation (ML_train.py)

- The final step applies seven machine learning algorithms to each attack file multiple times for robust evaluation.
- Results of these operations are displayed on the screen and saved in the file "./attacks/results_1.csv".
- Additionally, box and whisker graphics representing the results are generated.
- Both the graphics and results are saved in the "./attacks/result_graph_1/" folder.
- 
## Dataset Source

You can access the CIC-IDS2017 dataset [here](https://www.unb.ca/cic/datasets/ids-2017.html).


