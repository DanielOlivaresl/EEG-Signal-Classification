from azureml.train.hyperdrive import GridParameterSampling, HyperDriveConfig, choice
from azureml.core import Pipeline
from azureml.train.hyperdrive import PrimaryMetricGoal
from azureml.core import Workspace, Dataset, Experiment
from azureml.core.runconfig import RunConfiguration
from createPipeline import create_pipeline_steps 

#We define a hyperparameter search space for method order

search_space = GridParameterSampling(
    {
        "preprocessing_order" : choice(
            ["notch_filter", "bandpass_filter"] #Will search all possible combinations
        )
    }
)


#Create the pipeline with a specific order (Which will be selected by HyperDrive)

preprocessing_order = ["notch_filter", "bandpass_filter"]

#get Workspace 

ws = Workspace.from_config() 



steps = create_pipeline_steps(preprocessing_order,ws)

#Create the pipeline 

pipeline = Pipeline(workspace = ws, steps = steps)

#Define the hyperdrive config 

hyperdrive_config = HyperDriveConfig(
    run_config=RunConfiguration(), 
    hyperparameter_sampling= search_space, 
    primary_metric_name= "accuracy", 
    primary_metric_goal=PrimaryMetricGoal.MAXIMIZE, 
    max_total_runs=10
)

#Create an experiment 
experiment = Experiment(workspace=ws, name= "preprocessing_ex")

#Submit the experiment 

