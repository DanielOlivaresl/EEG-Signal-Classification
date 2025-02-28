from azureml.train.hyperdrive import HyperDriveConfig, choice
from azureml.train.hyperdrive.sampling import RandomParameterSampling, GridParameterSampling
from azureml.train.hyperdrive import PrimaryMetricGoal
from azureml.core import Workspace, Dataset, Experiment
from azureml.core.runconfig import RunConfiguration
from azureml.core import ScriptRunConfig
from azureml.pipeline.core import Pipeline, PipelineParameter
from createPipeline import create_pipeline_steps  # Assuming you have a custom function here
from azureml.core import ComputeTarget
from azureml.core import Dataset,Environment

import itertools
from azureml.core import Experiment
from azureml.pipeline.core import Pipeline
from createPipeline import create_pipeline_steps
import itertools

# Get Workspace
ws = Workspace.from_config()

# List of preprocessing methods
# preprocessing_methods = ['notch_filter', 'bandpass_filter', 'mean_referencing', 'scale_signal', 'normalize']
preprocessing_methods = ['notch_filter']

# Generate all combinations of preprocessing methods
preprocessing_combinations = []

for i in range(len(preprocessing_methods)):
    preprocessing_combinations.extend(list(itertools.permutations(preprocessing_methods, i + 1)))

# Submit each pipeline run asynchronously
experiment = Experiment(workspace=ws, name="preprocessing_experiment")
compute_target = ws.compute_targets["eegComputeCluster"]

env = Environment.get(ws, "eegEnv")
run_config = RunConfiguration()
run_config.environment = env
for combination in preprocessing_combinations:
    order_list = list(combination)
    
    # Create pipeline steps dynamically
    steps = create_pipeline_steps(ws, order_list,run_config)
    
    # Create pipeline object
    pipeline = Pipeline(workspace=ws, steps=steps)
    
    
    run = experiment.submit(pipeline)
    print(f"Submitted pipeline for order: {order_list} (Run ID: {run.id})")



