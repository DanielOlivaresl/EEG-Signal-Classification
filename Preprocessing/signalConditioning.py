#File for the very basic preprocessing steps, needed to apply the more complex preprocessing 


import numpy as np
import scipy.signal as signal
from sklearn.preprocessing import StandardScaler

#1. BandPass filter to remove irrelevant frequency components 
def bandPassFilter(data,fs,lowcut=0.5,highcut=50,order=4):
    nyquist = fs* 0.5
    low = lowcut/nyquist
    high = highcut/nyquist
    
    #Butterworth pass filter
    
    b,a = signal.butter(order,[low,high],btype= 'band')
    
    #Apply the filter 
    
    filtered_data = signal.filtfilt(b,a,data,axis=0)
    
    return filtered_data


#2.
def notchFilter(data, fs, freq=50, quality_factor=30):
    nyquist = 0.5 * fs
    freq = freq / nyquist  # Normalize frequency

    # Design Notch Filter
    b, a = signal.iirnotch(freq, quality_factor)
    
    # Apply the filter
    notch_filtered_data = signal.filtfilt(b, a, data, axis=-1)
    
    return notch_filtered_data

#3. Mean referencing to help remove the common noise in between the signals
def mean_referencing(data):
    
    #We calculate the mean signsl
    mean_signal = np.mean(data,axis=0) #Compute mean across channels (every timepoint)
    
    #We will now substract the mean from each channel 
    rereferencedData = data  -mean_signal
    
    return rereferencedData


#4.
def scale_signal(data, scale_factor = 50/ 1e6):
    data *= scale_factor
    return data

#5.
def normalize(data):
    scaler = StandardScaler()    
    data_reshaped = data.reshape(-1,data.shape[-1]) #Flatten
    data_normalized = scaler.fit_transform(data_reshaped)
    data_normalized = data_normalized.reshape(data.shape)
