import numpy as np 
import pyiva






def applyIVAtoEEGSignal(X, n_components = 10):
    """_summary_

    Args:
        X (ndarray (timesteps,channels)): EEG Multichannel signal

    """
    #We create a random mixing matrix 
    
    mixing_matrix = np.random.rand(X.shape[1],X.shape[1])
    
    #mixed signals 
    
    mixed_X = np.dot(X,mixing_matrix.T)
    
    
    X_centered = mixed_X - np.mean(mixed_X,axis=0)
    
    
    #Whitening 
    
    cov_matrix = np.cov(X_centered,rowvar=False)
    eigvals,eigvecs = np.linalg.eigh(cov_matrix)
    
    whitening_matrix = np.dot(eigvecs,np.diag(1.0/np.sqrt(eigvals)))
    
    X_whitened = np.dot(X_centered,whitening_matrix)
    
    iva = pyiva.IVA()
    
    S_separated = iva.fit(X_whitened)
    
    return S_separated
    
    
    