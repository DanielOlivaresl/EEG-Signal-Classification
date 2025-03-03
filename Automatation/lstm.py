#File for LSTM Architectures
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense,LSTM, Dropout, Bidirectional,Input
from tensorflow.keras.optimizers import Adam

def createLSTM(input_shape, numClasses,LSTMlayers= 1,widthLSTMLayers = 128, denseLayers = 3, widthDenseLayers =256):
    model = Sequential()
    
    #LSTM
    if(LSTMlayers == 1):
        model.add(LSTM(units=widthLSTMLayers, return_sequences=False,input_shape=input_shape))
    else:
        model.add(LSTM(units=widthLSTMLayers, return_sequences=True,input_shape=input_shape))
        
    
    for i in range(1,LSTMlayers): 
        
        if(i == LSTMlayers-1): #Final Layer
            
            model.add(LSTM(units = widthLSTMLayers/(2**i)),return_sequences=False)
    
    # Dense Layers 
    
    for i in range(denseLayers):
        
        if(i == denseLayers-1):
            model.add(Dense(units = numClasses,activation= 'softmax'))
        else:
            model.add(Dense(units = widthDenseLayers/(2**i),activation= 'softmax'))
            
    
            

    # Compile the model
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    return model
    
    