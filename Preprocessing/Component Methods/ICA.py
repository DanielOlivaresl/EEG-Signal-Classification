import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import FastICA
from scipy.stats import kurtosis

# Actual ICA Computation
def applyICA(signals):
    """
    Apply FastICA to extract independent components.
    
    :param signals: 2D numpy array (channels x time)
    :return: ICA-transformed signals (independent components) and the ICA object
    """
    ica = FastICA(n_components=signals.shape[0], random_state=42,max_iter=200,tol=0.1)  # Added random_state for reproducibility
    
    # Recover independent signals
    S_ica = ica.fit_transform(signals.T).T  # Ensure correct shape
    
    return S_ica, ica  # Return both ICA signals and the ICA object

# Function to calculate features (variance, kurtosis)
def calculate_component_features(ica_result):
    """
    Calculate statistical features for each ICA component.
    Features: variance, kurtosis
    """
    features = np.array([
        (np.var(component), kurtosis(component)) for component in ica_result
    ])
    
    
    return features

# Function to automatically filter components based on features
def filter_artifacts(ica_result, features, variance_threshold=0.1, kurtosis_threshold=5.0):
    """
    Filter out ICA components that likely correspond to artifacts based on feature thresholds.
    
    :param variance_threshold: Components with variance higher than this value are removed
    :param kurtosis_threshold: Components with kurtosis higher than this value are removed
    """
    components_to_remove = [
        i for i, (variance, comp_kurtosis) in enumerate(features)
        if variance > variance_threshold or comp_kurtosis > kurtosis_threshold
    ]
    
    # Remove components by setting them to zero in a copy
    ica_cleaned = ica_result.copy()
    ica_cleaned[components_to_remove, :] = 0
    
    return ica_cleaned, components_to_remove

# Function to reconstruct signals after artifact removal
def reconstruct_signals(ica_result, ica_object):
    """
    Reconstruct the signals from the cleaned ICA components.
    
    :param ica_result: Cleaned ICA components
    :param ica_object: The trained ICA object
    :return: Reconstructed signals
    """
    return np.dot(ica_object.mixing_, ica_result)  # Correct reconstruction formula


# Main pipeline to apply ICA and filter out artifact components automatically
def ica_pipeline(signals, variance_threshold=0.1, kurtosis_threshold=5.0):
    """
    ICA pipeline to extract, filter, and reconstruct signals.
    
    :param signals: 2D numpy array (channels x time)
    :return: Cleaned signals and list of removed component indices
    """
    # Step 1: Apply ICA
    ica_signals, ica_object = applyICA(signals)
    
    # Step 2: Calculate features (variance, kurtosis) for each ICA component
    features = calculate_component_features(ica_signals)
    
    # Step 3: Automatically filter out artifact components
    ica_signals_cleaned, removed_components = filter_artifacts(
        ica_signals, features, variance_threshold, kurtosis_threshold
    )
    
    
    
    # Step 4: Reconstruct cleaned signals from remaining components
    cleaned_signals = reconstruct_signals(ica_signals_cleaned, ica_object)
    
    print(f"Removed components: {removed_components} / {ica_signals.shape[0]}")

    
    
    return cleaned_signals
