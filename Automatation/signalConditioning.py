#File for the very basic preprocessing steps, needed to apply the more complex preprocessing 


import argparse
import numpy as np
import scipy.signal as signal
import os


from sklearn.preprocessing import StandardScaler

#1.  
def bandPassFilter(
    eeg_data: np.ndarray,
    fs: float,
    lowcut:float =0.5,
    highcut:float=50 ,
    order:int=4
)-> np.ndarray:
    """
    BandPass filter to remove irrelevant frequency components, applies a bandpass filter to an eeg signal
    
    Parameters: 
    
        eeg_data (ndarray: EEG data (n_channels, n_timesteps))
        fs (float): Sampling Frequency in Hz
        lowcut (float,optional): Low cutoff frequency in Hz
        highcut (float,optional): High cutoff frequency in Hz.
        order (int, optional): Filter order.
    
    
    
    """

    nyquist = fs* 0.5
    low = lowcut/nyquist
    high = highcut/nyquist
    
    #Butterworth pass filter
    
    b,a = signal.butter(order,[low,high],btype= 'band')
    
    #Apply the filter 
    
    filtered_data = signal.filtfilt(b,a,eeg_data,axis=-1)
    
    return filtered_data


#2.
def notchFilter(eeg_data, fs, freq=50, quality_factor=30):
    """
    notch filter to remove noise from electricity
    
    Parameters: 
    
        eeg_data (ndarray: EEG data (n_channels, n_timesteps))
        fs (float): Sampling Frequency in Hz
        freq  (float,optional): Frequency to be removed
        quality_factor(float,optional): Quality factor of the notch filter
            
    
    
    """
    nyquist = 0.5 * fs
    freq = freq / nyquist  # Normalize frequency

    # Design Notch Filter
    b, a = signal.iirnotch(w0=freq,Q=quality_factor,fs=fs)
    
    # Apply the filter
    notch_filtered_data = signal.filtfilt(b, a, eeg_data, axis=-1)
    return notch_filtered_data

#3. Mean referencing to help remove the common noise in between the signals
def mean_referencing(data):
    """
    Mean referencing to help remove the common noise from the data
    
    Parameters: 
    
        data (ndarray: EEG data (n_channels, n_timesteps))
    
    
    """
    #We calculate the mean signsl
    mean_signal = np.mean(data,axis=0) #Compute mean across channels (every timepoint)
    
    #We will now substract the mean from each channel 
    rereferencedData = data  -mean_signal
    
    return rereferencedData


# 4.
def scale_signal(data, scale_factor = 50/ 1e6):
    """
    scale signal, so that the model can learn better without any scaling issues
    
    Parameters: 
    ;
        data (ndarray: EEG data (n_channels, n_timesteps))
        scale_factor (float: Scaling factor, the amount of times the signal scale will decrease)
    
    
    """

    return data*scale_factor

#5.
def normalize(data):
    """
    Normalization so that the models can learn the pattern more efficiently
    
    Parameters: 
    
        data (ndarray: EEG data (n_channels, n_timesteps))
    
    
    """

    scaler = StandardScaler()    
    data_reshaped = data.reshape(data.shape[0],-1) #Flatten
    data_normalized = scaler.fit_transform(data_reshaped)
    data_normalized = data_normalized.reshape(data.shape)


    return data_normalized 


    
def restructureSignals(signalArray):
    """Function that takes in the cleaned signals

    Args:
        signalArray (List of ndarray): All the signals to be restructured
    """
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--method",type=str,required=True,choices = ["notch_filter", "bandpass_filter", "mean_referencing","scale_signal","normalize"])
    parser.add_argument("--input",type=str,required=True)
    parser.add_argument("--output",type=str,required=True)
    
    args = parser.parse_args()
    
    
    #We obtain the input data from the pipeline 
    
    
    input_path = args.input
    print(f"Recieved input is: {input_path}")
    
    
    for file_name in os.listdir(input_path):
        if file_name.endswith(".npy"):
            file_path = os.path.join(input_path,file_name)
            
            data = (np.load(file_path))

    
    
            #Call the appropriate method based on the argument 
    
    
            if args.method == "notch_filter":
                output = notchFilter(data,fs=250)
                
            elif args.method == "bandpass_filter":
                output = bandPassFilter(data)
                
            elif args.method ==  "mean_referencing":
                output = mean_referencing(data)
                
            elif args.method == "scale_signal":
                output = scale_signal(data)
                
            elif args.method == "normalize":
                output = normalize(data)
            
            output_file = os.path.join(args.output,file_name)
            os.makedirs(args.output, exist_ok = True)
            np.save(output_file,data)
            
            # print(output_file)
            
            
        else:
            # print(f"NOT A .NPY FILE: \n\n\n\n")
            file_path = os.path.join(input_path,file_name)
            for i in os.listdir(file_path):
                
                data = (np.load(os.path.join(file_path,i),allow_pickle=True))
            
                print(data.shape)
