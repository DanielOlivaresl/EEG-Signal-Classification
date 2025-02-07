#File for the very basic preprocessing steps, needed to apply the more complex preprocessing 


import numpy as np
import scipy.signal as signal
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