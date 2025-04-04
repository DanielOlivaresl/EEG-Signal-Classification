import numpy as np 
from sklearn.decomposition import PCA 


def applyPCAtoEEGSignal(X, n_components = 10):
    """_summary_

    Args:
        X (ndarray (timesteps,channels)): EEG Multichannel signal

    """
    
    
    
    
    X_centered = X - np.mean(X,axis=0)
    
    #We now apply PCA 
    
    pca = PCA(n_components=n_components)
    
    
    X_Pca = pca.fit_transform(X_centered)
    
    return X_Pca
    
    
    
    
    