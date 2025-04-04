import numpy as np 
from sklearn.decomposition import NMF


def applyNMFtoEEGSignal(X, n_components = 10):
    """_summary_

    Args:
        X (ndarray (timesteps,channels)): EEG Multichannel signal

    """
    
    #We convert the signal to only positive values 
    
    X = np.abs(X)
    
    # We apply NMF 
    
    
    nmf = NMF(n_components=n_components,init='random',random_state=42)
    W = nmf.fit_transform(X)
    H = nmf.components_
    
    
    
    
    
    
    return W,H
    