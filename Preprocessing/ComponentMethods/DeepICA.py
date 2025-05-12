import tensorflow as tf
from tensorflow import keras 
from tensorflow.keras import layers 
import numpy as  np
import matplotlib.pyplot as plt 
from scipy.stats import entropy 





import h5py


def loadSignals():
    
    hf = h5py.File("../../Datasets/data.hdf5", 'r')
    features = np.array(hf.get("features"))
    erp_labels = np.array(hf.get("erp_labels"))
    codes = np.array(hf.get("codes"))
    trials = np.array(hf.get("trials"))
    sequences = np.array(hf.get("sequences"))
    matrix_indexes = np.array(hf.get("matrix_indexes"))
    run_indexes = np.array(hf.get("run_indexes"))
    subjects = np.array(hf.get("subjects"))
    database_ids = np.array(hf.get("database_ids"))
    target = np.array(hf.get("target"))
    matrix_dims = np.array(hf.get("matrix_dims"))
    hf.close()
    
    return features


def splitData(data,train_split=0.7):
        
    train_size = int(data.shape[0]* train_split)    
    
    X_train, X_test = data[:train_size], data[train_size]
    
    return X_train,X_test




def modelDefinition(input_dim =8):
    
    
    #Learns an ICA Representation
    encoder = keras.Sequential([
        layers.Dense(16,activation= "relu"), 
        layers.Dense(input_dim,activation= "linear")    
    ])
    
    
    #Decoder Reconstructs the signal
    
    decoder = keras.Sequential([
        layers.Dense(16,activation="relu"), 
        layers.Dense(input_dim,activation="linear")
    ])
    
    
    #Model definition 
    
    inputs = keras.Input(shape= (input_dim,))
    encoded = encoder(inputs)
    decoded = decoder(encoded)
    
    deep_ICA = keras.Model(inputs,decoded)
    
#Loss function


def negentropy_loss(y_true, y_pred):
    """Loss based on the independence of components"""
    
    entropy_term = tf.reduce_mean(tf.tanh(y_pred)**2) #Negentropy penalization 
    mse_loss = tf.reduce_mean(tf.square(y_true- y_pred)) #Error de reconstruccion 
    return mse_loss - 0.1 * entropy_term
    
    
    
#Model Training 

def train(model,X_train, X_test):
    
    model.compile(optimizers=keras.optimizers.Adam(learning_rate=0.001),loss=negentropy_loss)
    model.fit(X_train,X_train,epochs = 50, batch_size = 64,validation_data=(X_test,X_test))
    


def extractIndependentSignals(encoder,data):
    X_transformed = encoder.predict(data)
    
    
#PLotting of the signals

def plotSignals(num_channels,X_transformed):
    
    plt.figure(figsize=(12, 6))
    for i in range(num_channels):
        plt.subplot(num_channels, 1, i+1)
        plt.plot(X_transformed[:, i])
        plt.title(f"Componente Independiente {i+1}")
    plt.tight_layout()
    plt.show()

    