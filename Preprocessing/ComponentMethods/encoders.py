import numpy as np
import mne
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model
from sklearn.preprocessing import StandardScaler


def autoencoder(data):
    window_size = data.shape[1]
    input_shape = (window_size,data.shape[2],1)
    
    latent_dim = 32
    
    #Encoder
    
    input_eeg = Input(shape=input_shape)
    x = keras.layers.Conv2D(16, (3,3),activation = 'relu',padding = 'same')(input_eeg)
    x = keras.layers.MaxPooling2D((2,2,),padding="same")(x)
    x = keras.layers.Conv2D(8,(3,3),activation = "relu",padding="same")(x)
    x = keras.layers.MaxPooling2D((2, 2), padding='same')(x)
    x = keras.layers.Flatten()(x)
    
    encoded = Dense(latent_dim,activation="relu")(x)
    
    
    #Decoder 
    
    x = Dense(64,activation= "relu")(encoded)
    x = keras.layers.Reshape((4,4,4))(x)
    x = keras.layers.Conv2DTranspose(8,(3,3),activation= "relu",padding="same")(x)
    x = keras.layers.Upsampling2D((2,2))(x)
    x = keras.layers.Conv2DTranspose(16,(3,3),activation= "relu",padding="same")(x)
    x = keras.layers.UpSampling2D((2,2))(x)
    decoded = keras.layers.Conv2D(1,(3,3),activation = "sigmoid",padding = "same")(x)
    
    
    #Autoencoder Model
    
    autoencoder = Model(input_eeg,decoded)
    autoencoder.compile(optimizer= "adam",loss= "mse")
    
    #Training
    
    autoencoder.fit(data,data,epochs = 50,batch_size = 32,validation_split = 0.2)