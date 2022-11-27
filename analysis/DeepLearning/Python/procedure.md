# Performing Deep Learning on the Bike Sharing Dataset

## Defining Steps for the Project:
- Load the dataset from csv file onto a pandas dataframe
- Data Preprocessing
    - Clean the dataset
        - Remove Missing Values
    - Encode Data as per their type
        - Convert Datetime Variables to Categorical Variables
        - Convert Binary Categorical Variables to [0,1]
        - Convert Categorical Variables to Dummy Variables (One Hot Encoding)
        - Convert Numerical Variables to Standardized Variables
            - Can also be done within the Sequential model as well.
            - But, it is better to do it in the model, as it stores the respective ranges of the variables.
    - Split the dataset into Training, Validation, and Test Sets
- Data Preparation
    - Convert the dataset into tf.data.Dataset object
- Model Building
    - Define the model
    - Compile the model
    - Train the model
    - Evaluate the model
        - Record the rmse, mae, and mape values
    - Predict using the model