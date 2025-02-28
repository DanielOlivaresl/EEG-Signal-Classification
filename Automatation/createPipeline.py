from azureml.pipeline.steps import PythonScriptStep
from azureml.pipeline.core import PipelineData
from azureml.core import Dataset,Environment

def create_pipeline_steps(ws, preprocessing_order,run_config):
    dataset = Dataset.get_by_name(ws, "EEG_Raw_Signal_Dataset")
    input_data = dataset.as_named_input("raw_data").as_mount()  
    
    
    
    
    previous_output = input_data
    steps = []

    # Preprocessing steps
    methods_map = {
        "notch_filter": "signalConditioning.py",
        "bandpass_filter": "signalConditioning.py",
        "mean_referencing": "signalConditioning.py",
        "scale_signal": "signalConditioning.py",
        "normalize": "signalConditioning.py"
    }

    for method in preprocessing_order:
        
        output_data = PipelineData(f"{method}_output", datastore=ws.get_default_datastore())

        step = PythonScriptStep(
            name=f"{method.capitalize()} Step",
            script_name=methods_map[method],
            arguments=["--method", method, "--input", previous_output, "--output", output_data],
            inputs=[previous_output],
            outputs=[output_data],
            compute_target="eegComputeCluster",
            runconfig=run_config,
            source_directory="./Automatation"
            
        )

        steps.append(step)
        previous_output = output_data

    # Training step
    train_step = PythonScriptStep(
        name="Model Training",
        script_name="train.py",
        arguments=["--input", previous_output],
        inputs=[previous_output],
        compute_target="eegComputeCluster",
        source_directory="./Automatation",
        runconfig=run_config,
        allow_reuse=True
    )

    steps.append(train_step)

    return steps
