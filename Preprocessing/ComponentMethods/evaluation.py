#Function to evaluate preprocessing technique 
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense,LSTM, Dropout, Bidirectional,Input
from tensorflow.keras.optimizers import Adam
from sklearn.preprocessing import StandardScaler

from keras.models import Sequential
from keras.layers import Dense, Dropout, Embedding, SimpleRNN,BatchNormalization, TimeDistributed
from tensorflow.keras.datasets import reuters

from sklearn.metrics import confusion_matrix,classification_report
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score

from sklearn.utils.class_weight import compute_class_weight

from tensorflow.keras.callbacks import EarlyStopping



from sklearn.model_selection import train_test_split

def evaluateTechnique(X,y,model = None, batch_size = 128, epochs = 50, validation_split = 0.1):
    
    #If none was passed as a model argument, meaning no model was passed, we will define a default lstm model

    if model == None:
        
        model = Sequential()
        # Add LSTM layer
        model.add(LSTM(units=128, return_sequences=False,input_shape=X[0].shape))
        model.add(LSTM(units=64, return_sequences=True))
        model.add(LSTM(units=32, return_sequences=False))
        # Dense layers
        # model.add(Dense(units=128, activation='relu'))
        model.add(Dense(units=64, activation='relu'))
        model.add(Dense(units=32, activation='relu'))
        model.add(Dense(units=y.shape[1], activation='softmax'))

        # Compile the model
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

        # Model summary
        model.summary()

    history = model.fit(X,y,epochs=epochs,batch_size=batch_size,validation_split= validation_split)
    
    
    
    return history
    

    
    
    
    
    