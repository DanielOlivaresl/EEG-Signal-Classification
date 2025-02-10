import numpy as np
import matplotlib as plt
from sklearn.decomposition import FastICA
from scipy.signal import butter, filtfilt
from scipy.stats import kurtosis



#Actual ICA Computation 
def applyICA(signals):
    ica = FastICA(n_components=signals.shape[0])
    
    #Recover independent Signals 
    
    S_ica = ica.fit_transform(signals)
    
    return S_ica.T

# Function to calculate features (variance, kurtosis)
def calculate_component_features(ica_result, fs=1.0):
    """
    Calculate statistical features for each ICA component.
    Features: variance, kurtosis
    """
    features = []
    
    for i in range(ica_result.shape[0]):
        component = ica_result[i, :]
        
        # Calculate the variance of the component
        variance = np.var(component)
        
        # Calculate the kurtosis of the component
        comp_kurtosis = kurtosis(component)
        
        features.append((variance, comp_kurtosis))
        
    return np.array(features)

# Function to automatically filter components based on features
def filter_artifacts(ica_result, features, variance_threshold=0.1, kurtosis_threshold=5.0):
    """
    Filter out ICA components that likely correspond to artifacts based on feature thresholds.
    :param variance_threshold: Components with variance higher than this value are removed
    :param kurtosis_threshold: Components with kurtosis higher than this value are removed
    """
    components_to_remove = []
    
    for i, (variance, comp_kurtosis) in enumerate(features):
        if variance > variance_threshold or comp_kurtosis > kurtosis_threshold:
            components_to_remove.append(i)
    
    # Remove components by setting them to zero
    ica_result[components_to_remove, :] = 0
    return ica_result, components_to_remove

# Function to reconstruct signals after artifact removal
def reconstruct_signals(ica_result, ica_object):
    """
    Reconstruct the signals from the cleaned ICA components.
    """
    return np.dot(ica_result, ica_object.components_)

# Function to visualize components
def plot_components(ica_result):
    """
    Plot the ICA components for visual inspection.
    """
    num_components = ica_result.shape[0]
    plt.figure(figsize=(10, num_components * 2))
    for i in range(num_components):
        plt.subplot(num_components, 1, i + 1)
        plt.plot(ica_result[i, :])
        plt.title(f'Component {i + 1}')
    plt.tight_layout()
    plt.show()

# Main pipeline to apply ICA and filter out artifact components automatically
def ica_pipeline(signals, fs=1.0, n_components=None):
    # Step 1: Apply ICA
    ica_signals, ica_object = applyICA(signals, n_components=n_components)
    
    # Step 2: Calculate features (variance, kurtosis) for each ICA component
    features = calculate_component_features(ica_signals, fs)
    
    # Step 3: Automatically filter out artifact components
    ica_signals_cleaned, removed_components = filter_artifacts(ica_signals, features)
    
    # Step 4: Reconstruct cleaned signals from remaining components
    cleaned_signals = reconstruct_signals(ica_signals_cleaned, ica_object)
    
    # Optionally: Plot components for visual inspection (to validate automatic removal)
    plot_components(ica_signals_cleaned)
    
    return cleaned_signals, removed_components
