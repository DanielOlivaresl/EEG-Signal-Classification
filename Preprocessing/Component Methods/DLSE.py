#Dictonary Learning , Sparse Encoding
from sklearn.decomposition import DictionaryLearning



def applyDictionaryLearningtoEEGSignal(X, n_components = 50):
    """_summary_

    Args:
        X (ndarray (timesteps,channels)):Set of EEG multichannel signals

    """
    
    
    
    dictLearning = DictionaryLearning(n_components=n_components,transform_algorithm='omp',alpha=1)
    
    #Adjust the dictionary to the data 
    
    dictionary = dictLearning.fit(X)
    
    return dictionary


def calculateSparseRepresentations(dictionary,X):
    
    
    A = dictionary.transform(X)
    
    return A
