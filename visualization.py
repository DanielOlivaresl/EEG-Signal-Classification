#File for visualization functions 

import numpy as np
import matplotlib.pyplot as plt

from IPython.display import clear_output
import time
from matplotlib.animation import FuncAnimation

    
def plotEEG(
    eegData: np.ndarray,
    plotSize: tuple
    
    ):
    """Function that plots EEG Data using matplotlib

    Args:
        eegData (np.ndarray): EEG ndarray of shape (channels,timesteps)
        plotSize (tuple): size of the plot
    """ 
    
    
    if len(eegData.shape) ==1:
        fig,axs = plt.subplots(1,1,figsize=plotSize)
        axs.plot(eegData)
        plt.show()
    
    if len(eegData.shape) !=2:
        return
    
    #We will iterate the channels of the signal passed and plot them accordingly
    fig,axs = plt.subplots(eegData.shape[0]//2,2,figsize=plotSize,layout="constrained")
    

    print(axs.shape)
    for i in range(axs.shape[0]):
        for j in range(axs.shape[1]):
            
            axs[i][j].plot(eegData[i*axs.shape[1] + j])
        
        
            axs[i][j].set_title(f"EEG Channel {i*axs.shape[1] + j}")
        # axs[i].set_xlabel("time")

    plt.show()    
    
    
    
import numpy as np
import matplotlib.pyplot as plt
import time
from IPython.display import clear_output



def dynamicEEGPlot(eegData: np.ndarray,  plotSize: tuple, displayLength: int = 1000):
    
    # Case 1: Single-channel EEG data
    if len(eegData.shape) == 1:
        for i in range(len(eegData) - displayLength):
            clear_output(wait=True)  # Clear previous output

            plt.figure(figsize=plotSize)
            plt.plot(eegData[i:displayLength + i], label=f"Time step {i}")
            plt.legend()
            plt.title("Single-Channel EEG")
            plt.xlabel("Time")
            plt.ylabel("Amplitude")
            plt.show()
            time.sleep(0.004)  # Pause for 4ms (250 Hz refresh rate)

        return
    
    if len(eegData.shape) != 2:
        raise ValueError("Input EEG data should be either 1D (single channel) or 2D (multi-channel).")
    
    num_channels = eegData.shape[0]
        
    for time_step in range(0,eegData.shape[1] - displayLength,10):  # Iterate over time steps

        clear_output(wait=True)  # Clear previous output
        fig,axs = plt.subplots(eegData.shape[0]//2,2,figsize=plotSize,layout="constrained")
        axs = axs.flatten()
    
        

        

        for i, ax in enumerate(axs):
            ax.cla()
            ax.plot(eegData[i, time_step:time_step + displayLength])
            ax.set_title(f"EEG Channel {i}")
            ax.set_xlabel("Time")
            ax.set_ylabel("Amplitude")    
            
        plt.show()
        # plt.pause(0.004)
        