# Investigación y Recopilación de conjunto de datos de P300 # 
El primer conjunto de datos es el llamado “BCI Competition III, dataset II”. Este conjunto de datos no cuenta con una descripción precisa de los participantes con los que se generó el conjunto. Únicamente en el trabajo se menciona que son 2 participantes. Por otro lado, se realizaron un total de 5 sesiones para cada sujeto, cada sesión se constituyó de varias ejecuciones. Para cada época de ejecución se le mostró al participante una matriz de caracteres de 12 filas por 12 columnas en blanco durante 2.5s. Posteriormente, cada fila y columna de la matriz se intensificó aleatoriamente durante 100ms. 

Después de la intensificación de una fila o columna, la matriz estuvo en blanco durante 75ms. Las intensificaciones se aleatorizaron por bloques de 12. Esto se repitió un total de 15 veces para cada época de carácter (es decir, cada fila/columna específica fue intensificada 15 veces, resultando en un total de 180 intensificaciones para cada época de carácter). Cada época de carácter fue seguida por un período de 2.5 segundos, durante el cual la matriz estuvo en blanco.

También es importante señalar que se generó la captura de datos mediante un casco de EEG de 64, en donde se utilizó nomenclatura la propuesta por, la cual está basado en el sistema internacional 10-20 y propone  8 letras para catalogar a los 64 nodos.



Despues de una investigacion inicial se encontraron mas datasets de P300 referentes a diversas actividades, se busca obtener un formato que sea compatible con el formato del dataset de la etapa de clasificacion, debido a que en el funcionamiento de los modelos, se busca que tengan el mismo, o un formato extremadamente similar. 


## Datasets ## 

### 1. GIB-UVA ERP-BCI Dataset ### 

Este dataset contiene senales de 73 sujetos (42 sanos y 31 con alguna discapacidad) las senales contienen 8 canales y una frecuencia de muestreo de 128Hz. 

El dataset contiene las siguientes variables 

 - Caracteristicas [n_stimulti x n_samples x n_channels] -> EEG Epochs [0,1000]. La senal ya esta preprocessada (FIR Bandpass, orden de filtro 1000 [0.5-45] Hz, CAR, Normalizacion de linea base [-200,0]ms. Orden de los canales ['FZ', 'CZ', 'PZ', 'P3', 'P4', 'PO7', 'PO8', 'OZ'])

 https://ieee-dataport.org/documents/gib-uva-erp-bci-dataset

 https://github.com/esantamariavazquez/EEG-Inception


 ### 2. Event Related Potentials (P300, EEG) - BCI Dataset ### 

Este dataset contiene senales de 16 adultos jovenes saludables (22-30). Los participantes nunca habian participado en algun experimento relacionado. Las senales fueron oobtenidas utilizando 16 canales con una frecuencia de muestreo de 256 Hz. Los electrodos fueron posicionados conforme al sistema 10-20 

https://ieee-dataport.org/documents/event-related-potentials-p300-eeg-bci-dataset

### 3. Kaggle P300 Dataset ### 

Dataset de 8 sujetos saludables con una frecuencia de muestreo de 250 Hz con un flitro notch de 50Hz y un filtro pasobandas de 0.1-30Hz

https://www.kaggle.com/datasets/rramele/p300samplingdataset

### 4. EEG Dataset for RVSP and P300 Speller Brain-Computer Interfaces ### 


https://www.nature.com/articles/s41597-022-01509-w#code-availability

https://github.com/Kyungho-Won/EEG-dataset-for-RSVP-P300-speller

### 5. Building Brain Invaders: EEG data of an experimental validation ### 

Dataset de 25 sujetos donde los potenciales son evocados por estimulacion visual. Las senales fueron obtenidas con 16 canales 


https://zenodo.org/records/2649069

