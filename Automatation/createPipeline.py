import itertools
from azureml.core import Workspace, Dataset, Experiment
from azureml.core import PythonScriptStep
from azureml.core.runconfig import RunConfiguration






def create_pipeline_steps(ws,preprocessing_order):
    
    

    #Get dataset, assuming the dataset is uploaded to our workspace 

    datastore = ws.get_default_datastore()

    dataset = Dataset.file.from_files(path=(datastore, 'datasetName.fileExtension'))


    #Define compute target (cluster or an instance)

    compute_target = ws.compute_targets['compute_target_name']



    #Define the run configuration (Optional, if we need to specify the environment)
    run_config = RunConfiguration()
    # run_config.environment = my_custom_environment

 
    #List that stores the Preprocessing Steps
    steps = [] 

    #Input data 

    previous_output = "data/input.npy"

    #Map the preproccessing methods 

    methods_map= {
        "notch_filter": "../Preprocessing/signalConditioning.py",
        "bandpass_filter" :"../Preprocessing/signalConditioning.py"
    }


    for method in preprocessing_order: 
        step = PythonScriptStep(
            name = f"{method.capitalize()} Step", 
            script_name = methods_map[method],
            arguments = ["--method",method,"--input",previous_output,"--output",f"outputs/{method}_output.npy"],
            # arguments=["--input", previous_output, "--output", f"outputs/{method}_output.npy"], Example for when a preprocessing step is in it's own file
            compute_target = "your_compute_target",
            runconfig = RunConfiguration(), 
            source_directory = "Pipeline"
        )
        
        #We add the current step to the list 
        
        steps.append(step)
        
        previous_output = f"outputs/{method}_output.npy"
    
    return steps



