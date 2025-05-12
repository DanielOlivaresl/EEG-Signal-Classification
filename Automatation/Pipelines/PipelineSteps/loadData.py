from azure.ai.ml import MLClient, Input, Output
from mldesigner import command_component
import os
from azure.identity import DefaultAzureCredential, ManagedIdentityCredential

from Preprocessing.ComponentMethods.testFile import testFunction


# Function to authenticate using DefaultAzureCredential, fallback to ManagedIdentityCredential
def authenticate():
    try:
        credential = DefaultAzureCredential()
        # Check if DefaultAzureCredential works by calling a simple token request
        credential.get_token("https://management.azure.com/.default")
        print("Authenticated using DefaultAzureCredential")
        return credential
    except Exception as ex:
        print(f"DefaultAzureCredential failed with error: {ex}")
        print("Falling back to ManagedIdentityCredential")
        return ManagedIdentityCredential()



credential = authenticate()

    # Initialize the ML Client using the credential
ml_client = MLClient.from_config(credential=credential)


try:
    env = ml_client.environments.get(name="eegEnv", version="57")
    print(f"Environment Name: {env.name}, Version: {env.version}")
except Exception as e:
    print(f"Failed to retrieve environment details: {e}")
    raise



@command_component(
        name="load_data",
        display_name="Data loading component",
        description="Component for loading the dataset of EEG P300 Signals",
        environment=env,
    )
def test_component(
    input_data: Input(type="uri_folder"),
    output_data: Output(type="uri_folder")
):
    
    try:
        print(f"Input data path: {input_data}")
        print(f"Output data path: {output_data}")
        
        
        print("Testing the user made library: ")
        testFunction("Testing the library in azureml")

    
        
    except Exception as e:
        print(f"Error in test_component: {e}")
        raise