import numpy as np
import matplotlib as plt
from sklearn.decomposition import FastICA
from scipy.signal import butter, filtfilt


#Actual ICA Computation 
def applyICA(signals):
    ica = FastICA(n_components=signals.shape[0])
    
    #Recover independent Signals 
    
    S_ica = ica.fit_transform(signals)
    
    return S_ica.T


#Low Pass filter, once the signals have been transformed to the ICA domain it's a good idea to apply filters to remove the noise 

def low_pass_filter(signal,cutoff=0.1, fs=1.0,order =5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    
    b,a = butter(order,normal_cutoff,btype='low',analog=False)
    return filtfilt(b,a,signal)



