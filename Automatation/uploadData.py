from azureml.core import Workspace, Dataset
import os
import time


def uploadFiles(localPath,remotePath):


    ws = Workspace.from_config() 

    datastore = ws.get_default_datastore() 



    npy_files = [f for f in os.listdir(localPath) if f.endswith('.npy')]
    max_retries =5

    if npy_files:
        print(f"Uploading files from {localPath} to {remotePath}")

        # Retry logic for uploading files
        attempt = 0
        while attempt < max_retries:
            try:
                # Create a Dataset from the local directory
                dataset = Dataset.File.upload_directory(
                    src_dir=localPath, 
                    target=(datastore, remotePath)
                )
                print("Upload successful.")
                break
            except Exception as e:
                attempt += 1
                print(f"Attempt {attempt} failed with error: {e}")
                if attempt >= max_retries:
                    print("Max retries reached. Upload failed.")
                    raise
                else:
                    time.sleep(5)  # Wait before retrying
    else:
        print(f"No .npy files to upload")

        
        

signals_localPath = "..\Data"
signals_remotePath = "trainingData/rawSignalData"


uploadFiles(signals_localPath,signals_remotePath)
# uploadFiles(labels_localPath,labels_remotePath)

