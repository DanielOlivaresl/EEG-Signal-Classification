import tensorly as tl 
from tensorly.decomposition import parafac 


def applyTDtoEEGSignal(X, rank = 3):
    """_summary_

    Args:
        X (ndarray (timesteps,channels)): EEG Multichannel signal

    """
    
    
    
    #We first create a tensor of EEG (Channels,time_steps,datapoints)
    
    eegTensor = tl.tensor(X)
    
    factors = parafac(eegTensor,rank=rank)
    
    A,B,C = factors
    
    return A,B,C
    
    
