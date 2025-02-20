from azureml.core import Workspace, Datastore, Dataset
import os

# Connect to the Azure ML workspace
ws = Workspace.from_config()

# Get the datastore by name
datastore = ws.datastores["workspaceblobstore"]  # Replace with your datastore name

# Option 1: Download the dataset to local
datastore.download(target_path="./data", overwrite=True)  # Downloads all files to local './data' folder
print(f"Downloaded data to './data' folder.")

# Option 2: Mount the datastore (if you don't want to download)
mount_path = datastore.mount()
mount_path.start()
print(f"Datastore mounted at: {mount_path}")

# Now you can use the mounted path or downloaded data as your dataset
# Example: List all files in the mounted path
for root, dirs, files in os.walk(mount_path):
    for file in files:
        print(f"Found file: {file}")
