import os
from dotenv import load_dotenv
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

from azure.ai.ml.entities import Environment, BuildContext




# Load the environment variables from the .env file
load_dotenv()

# Get the Azure subscription and resource group from the environment variables
subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
resource_group = os.getenv("AZURE_RESOURCE_GROUP")
workspace_name = os.getenv("AZURE_WORKSPACE_NAME")

credential = DefaultAzureCredential()

# Initialize the MLClient using Azure CLI credentials
client = MLClient(
    credential=credential,  # Use default authentication from Azure CLI
    subscription_id=subscription_id,
    resource_group_name=resource_group,
    workspace_name=workspace_name
)

# Test the connection by listing workspaces
workspaces = client.workspaces.list()
for workspace in workspaces:
    print(workspace.name)




# Create the environment object
conda_env = Environment(
    name="eegEnv",
    build=BuildContext(path="."),

    # conda_file = "conda_dependencies.yaml",
    description = "Environment for training EEG Classification model",
    
    )



client.environments.create_or_update(conda_env)
