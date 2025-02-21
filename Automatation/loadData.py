from azureml.core import Workspace, Dataset

# Connect to the Azure ML workspace
ws = Workspace.from_config()

# Get the datastore
datastore = ws.datastores["workspaceblobstore"]  # Ensure this is your correct datastore name

# Define the dataset path (modify based on your folder structure)
dataset_path = [(datastore, "trainingData/rawSignalData/")]

# Create a FileDataset
dataset = Dataset.File.from_files(path=dataset_path)

# Register the dataset in AzureML
dataset = dataset.register(workspace=ws,
                           name="EEG_Raw_Signal_Dataset",
                           description="Raw EEG signal data stored in Blob",
                           create_new_version=True)

print("Dataset registered successfully in AzureML!")
