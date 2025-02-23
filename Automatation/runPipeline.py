from azureml.train.hyperdrive import HyperDriveConfig, choice
from azureml.train.hyperdrive.sampling import RandomParameterSampling, GridParameterSampling
from azureml.train.hyperdrive import PrimaryMetricGoal
from azureml.core import Workspace, Dataset, Experiment
from azureml.core.runconfig import RunConfiguration
from azureml.core import ScriptRunConfig
from azureml.pipeline.core import Pipeline, PipelineParameter
from createPipeline import create_pipeline_steps  # Assuming you have a custom function here
from azureml.core import ComputeTarget

import itertools

# Get Workspace
ws = Workspace.from_config()


# List of preprocessing methods
preprocessing_methods = ['notch_filter', 'bandpass_filter', 'mean_referencing', 'scale_signal', 'normalize']

# Generate all combinations of preprocessing methods
preprocessing_combinations = []
preprocessing_combinations.extend(list(itertools.permutations(preprocessing_methods, len(preprocessing_methods))))

for i in range(len(preprocessing_methods)):
    preprocessing_combinations.extend(list(itertools.permutations(preprocessing_methods, i + 1)))

# Convert tuples to string format for AzureML
preprocessing_combinations_str = ["-".join(comb) for comb in preprocessing_combinations]

# Define hyperparameter search space
search_space = {
    "preprocessing_order": choice(*preprocessing_combinations_str)
}


preprocessing_order_param = PipelineParameter(name="preprocessing_order", default_value="notch_filter-bandpass_filter")

default_order_list = preprocessing_order_param.default_value.split("-")


# Create preprocessing steps dynamically

steps = create_pipeline_steps(ws,default_order_list)

#Create pipeline object 

pipeline = Pipeline(workspace=ws,steps=steps)

run_config = RunConfiguration()
run_config.environment = ws.environments["AzureML-ACPT-pytorch-1.13-py38-cuda11.7-gpu"]

# Use ScriptRunConfig to configure the pipeline's run configuration
script_run_config = ScriptRunConfig(source_directory='./Automatation', script='train.py', run_config=run_config,compute_target=ComputeTarget(workspace=ws, name="eegCompute"))





# Define the hyperdrive config
hyperdrive_config = HyperDriveConfig(
    run_config=script_run_config,
    hyperparameter_sampling=RandomParameterSampling(search_space),
    primary_metric_name="accuracy",
    primary_metric_goal=PrimaryMetricGoal.MAXIMIZE,
    max_total_runs=3
)

# Create and submit the experiment
experiment = Experiment(workspace=ws, name="preprocessing_experiment")
run = experiment.submit(hyperdrive_config)
