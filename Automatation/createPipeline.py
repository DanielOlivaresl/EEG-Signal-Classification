from azureml.pipeline.steps import PythonScriptStep
from azureml.pipeline.core import PipelineData
from azureml.core import Dataset,Environment

def create_pipeline_steps(ws, preprocessing_order):
    env = Environment.get(ws, "AzureML-ACPT-pytorch-1.13-py38-cuda11.7-gpu")
    dataset = Dataset.get_by_name(ws, "EEG_Raw_Signal_Dataset")
    input_data = dataset.as_named_input("raw_data")  

    # Create intermediate output for aggregated data
    aggregated_data = PipelineData("aggregated_data", datastore=ws.get_default_datastore())

    # Step 1: Data Aggregation Step
    data_aggregation_step = PythonScriptStep(
        name="Data Aggregation",
        script_name="aggregate_data.py",  # This script will merge multiple files into one list/array
        arguments=["--input", input_data, "--output", aggregated_data],
        inputs=[input_data],
        outputs=[aggregated_data],
        compute_target="eegCompute",
        runconfig=None,
        source_directory="./Automatation"
    )

    # Update input for preprocessing steps
    previous_output = aggregated_data
    steps = [data_aggregation_step]

    # Preprocessing steps
    methods_map = {
        "notch_filter": "../Preprocessing/signalConditioning.py",
        "bandpass_filter": "../Preprocessing/signalConditioning.py",
        "mean_referencing": "../Preprocessing/signalConditioning.py",
        "scale_signal": "../Preprocessing/signalConditioning.py",
        "normalize": "../Preprocessing/signalConditioning.py"
    }

    for method in preprocessing_order:
        
        output_data = PipelineData(f"{method}_output", datastore=ws.get_default_datastore())

        step = PythonScriptStep(
            name=f"{method.capitalize()} Step",
            script_name=methods_map[method],
            arguments=["--method", method, "--input", previous_output, "--output", output_data],
            inputs=[previous_output],
            outputs=[output_data],
            compute_target="eegCompute",
            runconfig=None,
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
        compute_target="eegCompute",
        source_directory="./Automatation",
        runconfig=None,
        allow_reuse=True
    )

    steps.append(train_step)

    return steps
