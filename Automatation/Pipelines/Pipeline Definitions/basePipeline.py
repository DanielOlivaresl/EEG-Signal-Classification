from azure.ai.ml import MLClient, Input, Output
from azure.ai.ml.dsl import pipeline


import sys
import os

#Line for detecting the "Pipeline Steps module"
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))



#Import needed pipeline components 
from PipelineSteps.loadData import test_component
from PipelineSteps.loadData import authenticate





def buildPipeline(cluster_name):




    # Build the pipeline
    @pipeline(default_compute=cluster_name)
    def pipeline_with_python_function_components(input_data: Input):
        """A simple pipeline with the test component"""
        try:
        
            test_node = test_component(input_data=input_data)
        #  print(f"Test component executed successfully, output data: {test_node.outputs.output_data.path}")
            return {"test_output": test_node.outputs.output_data}
        
        
        
        except Exception as e:
            print(f"Error in pipeline: {e}")
            raise

    return pipeline_with_python_function_components




if __name__ == "__main__": 

    print("Running main")
    # Authenticate
    credential = authenticate()

    # Initialize the ML Client using the credential
    ml_client = MLClient.from_config(credential=credential)

    # Set the cluster name
    cluster_name = "eegComputeCluster"



    # Print out the cluster details for debugging
    try:
        cluster_info = ml_client.compute.get(cluster_name)
        print(f"Cluster details: {cluster_info}")
    except Exception as e:
        print(f"Failed to retrieve cluster information: {e}")
        raise

    # Get environment details
    try:
        env = ml_client.environments.get(name="eegEnv", version="57")
        print(f"Environment Name: {env.name}, Version: {env.version}")
    except Exception as e:
        print(f"Failed to retrieve environment details: {e}")
        raise



    # Fetch the data asset
    try:
        data_asset = ml_client.data.get("Event-Related-Potentials-P300", version="1")
        print(f"Data asset retrieved: {data_asset.id}")
    except Exception as e:
        print(f"Failed to retrieve data asset: {e}")
        raise

    # Submit the pipeline job
    try:
        
        pipelineFunc = buildPipeline(cluster_name)
        
        pipeline_job = pipelineFunc(
            input_data=Input(type="uri_folder", path=data_asset.id)
        )


        pipeline_job = ml_client.jobs.create_or_update(
            pipeline_job,experiment_name="test sdk 3 experiment"
        )


        print("Pipeline submitted")
    except Exception as e:
        print(f"Error in pipeline job submission: {e}")
        raise
