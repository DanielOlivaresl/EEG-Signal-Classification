# Reporte Sprint 2 # 

### Para este sprint la actividad designada, es el analisis y seleccion de metodos de analisis de componentes que se investigaron en el sprint anterior, estos metodos fueron:  ###

- ICA (Independent Component Analysis) 
- PCA (Principal Component Analysis)
- NMF (Non-Negative Matrix Factorization)
- SPC (Sparse Component Analysis)
- CCA (Canonical Correlation Analysis)
- FA (Factor Analysis)
- BSS (Blind Source Separation)
- TD (Tensor Decomposition)
- Dictionary Learning & Sparse Encoding
- Variational Bayesian Inference and Probabilistic ICA 
- IVA (Independent Vector Analysis) 
- DeepICA (Deep Learning based ICA)
- Autoencoders

A continuacion se hara un analisis mas detallado de cada metodo tomando en cuenta el potencial papel que podria jugar con relacion a las senales EEG: 

### ICA ### 

ICA en este contexto puede ser muy util debido a que si se aplica correctamente puede efectivamente separar las senales EEG "puras" de alguna manera de el ruido externo al patron real. 

Una limitacion que debemos de considerar de ICA y que se vera al hacer pruebas es que ICA asume independencia lineal de las fuentes, esto puede no ser el caso en las senales EEG, por lo que tambien se probaran metodos mas complejos, pero que tienen un principio similar. 

### PCA ### 

PCA puede ser util y no solamente para limpiar las senales, sino tambien para reducir la dimensionalidad de estas, lo cual puede hacer que tecnicas mas complejas sean menos costosas computacionalmente sin perder gran informacion, algo a considerar al aplicar PCA enfocandonos en el problema que estamos intentando resolver, es el hecho de que PCA se basa en la varianza de las senales, y en este contexto la actividad cerebral no siempre tiene la mayor varianza, lo cual puede llevar a perdidad de informacion importante si no esta representada adecuadamente. 

### NMF ### 

Similarmente a como funciona ICA, NMF puede separar la senal del ruido, util para quitar completamente artefactos que no son deseados, como se explico anteriormente una restriccion impuesta al intentar utilizar NMF es que los datos deben de ser no negativos, por lo cual se podria decir que esta restriccion puede ser convertida en una ventaja, NMF es una buena opcion ya que no asume nada sobre la estructura de los datos como en PCA, lo que permite una mejor adaptabilidad a una variedad de Senales con carateristicas y patrones diferentes. 


### SPC ### 

SPC puede ser una buena tecnica por su capacidad para descomponer las senales en un numero reducido de componentes que capturan los patrones mas importantes. Esto puede ser muy util para las senales EEGm que pueden ser muy ruidosas y contener muchos artefactos. Al suponer que solo al suponer que solo algunos componentes son importantes, SPC Puede identificar y separar estos componentes reelevantes.

SPC es eficaz en separar el ruido de los componentes cerebrales significativos. Dado que los artefactos y el ruido tienden a ser densos y distribuidos en muchas frequencias y dimensiones, la escazes en la representacion permite que los artefactos se asignen a componentes pequenos o nulos, mientras que las senales cerebrales de interes se mantienen en componentes mas grandes. 

SPC es una muy buena tecnica para manejar el ruido, ya que asume que la mayoria de los componentes de la senal son irrelevantes (escasos). Esto puede llevar a una mejor separacion entre las senales de interes y los artefactos que otros metodos, como PCA, podrian no detectar bien. 

Una desventaja de SPC es que tiende a tener problemas con senales no lineales o artefactos complejos que no pueden ser representados con combinaciones lineales de componentes. Otra desventaja es que si las senales cerebrales tienen una representacion densa en el espacio de componentes, SPC podria no ser tan efectivo. Esta tecnica asume que las senales relevantes pueden representarse de manera escasa, lo que podria no ser cierto en todos los casos, especialmente cuando las senales cerebrales son complejas y densas en informacion. 

### CCA ###

Puede ser una muy buena opcion, dado que es eficaz para identificar y extraer componentes que estan altamente correlacionados entre dos conjuntos de datos. En el caso de las senales EEG, esto puede ser util para correlacionar las senales EEG con otras fuentes de informacion (como la actividad de referencia o patrones esperados de actividad cerebral), lo que permite aislar la senal de interes de los artefactos.

Otra ventaja muy grande de este metodo, es si se tiene un conjunto de senales de referencia (como los artefactos causados por parpadeo ocular o el movimiento muscular), CCA puede ayudar a eliminar el ruido que corresponde a estos artefactos. 

La principal desventaja de este metodo, es que necesita ese conjunto de datos de referencia, el cual no siempre se tiene, ademas de esto CCA solo es capaz de encontrar dependencias lineales entre los conjuntos de datos y es enteramente dependiente de la calidad del conjunto de referencia y la escala de este mismo.


### FA ### 

Al igual que PCA una de las principales ventajas de este metodo es que puede servir para reducir la complejidad computacional adjuntada al manejar estos datos complejos, ademas de esto, FA es capaz de identificar factores latentes, i.e. componentes subyacentes en las senales que pueden representar la actividad cerebral asi como el ruido, lo cual facilita la separacion de estos componentes de la senal. 

A parte de esto, FA permite modelar correlaciones entre senales EEG de una manera mas estructurada. Esto puede ser util para comprender mejor como las diferentes regiones del cerebro interactuan entre si, lo que puede ayudar a separar las senales reelevantes de los artefactos, especialmente cuando estan correlacionados entre varios electrodos. 

Una de las desventajas de este metodo, es que requiere suposiciones sobre la estructura de los factores, por ejemplo, se asume que las senales son combinaciones lineales de los factores latentes, si esto no se cumple limita la efectividad de FA. 

### TD ### 

TD puede ser una buena opcion debido a que puede modelar relaciones complejas entre las dimensiones espaciales(electrodos), temporales y frequenciales. Esto permite una representacion mas rica de las senales. Ademas de eso, esta tecnica sirve para reducir la dimensionalidad siendo util para reducir el costo computacional, manteniendo la informacion escencial. TD tiene ventajas en comparacion con metodos que hacen tareas similares, es una muy buena opcion en encontrar interacciones complejas entre las diferentes fuentes de la senal

Una de las desventajas de este metodo es si las senales con las cuales se efectua son demasiado ruidosas o llenas de artefactos, si es el caso puede que no sea capaz de separar los componentes, ademas de esto este metodo es muy propenso al sobreajuste (overfitting), especialmente cuando los conjuntos de datos no son tan grandes 

### Sparse Encoding & Dictionary Learning ### 

Puede ser una buena opcion, debido a que al reprentar las senales de manera esparsa, el aprendizaje de diccionario permite reducir la dimensionalidad de los datos, lo que hace que el procesamiento sea mas eficiente. Esto facilita el entrenamiento de modelos de clasificacion mas rapidos y con menos sobreajuste, debido a que solo se utilizan los coeficientes mas reelevantes.
Esta tecnica puede identificar patrones o caracteristicas significativas de las senales, incluso cuando los datos estan ruidosos o contaminados. El uso de un diccionario aprendido ayuda a captar las relaciones mas importantes que otros metodos no pueden. 
La codificacion esparsa ayuda a distinguir las senales utiles (actividad cerebral) de los ruidos o artefactos al asignar pesos mas bajos a las caracteristicas irrelevantes. 

Una de las desventajas de este metodo es que el proceso de aprendizaje del diccionario puede ser propenso al sobreajuste, esto es comun cuando la cantidad de datos de entrenamiento no es tan grande. A parte de esto el rendimiento de este metodo depende mucho del preprocesamiento de los datos.

### Variational Bayesian Inference and Probabilistic ICA ### 

Una de las principales ventajas es su capacidad para manejar senales con ruido. Dado que estas tecnicas se basan en enfoques probabilisticos, pueden modelar la incertidumbre inherente a este tipo de datos, lo que permite separar senales de manera mas robusta. Aparte de esto, ofrece mayor flexibilidad para separar fuentes de senales que pueden estar correlacionadas o que tienen distribuciones no estandar. Esto puede ser util en el contexto de EEG, donde las senales cerebrales pueden no ser completamente independientes.
VBI permite aproximar distribuciones complejas, lo que es util en situaciones donde las fuentes cerebrales no son completamente independientes o cuando los datos estan distribuidos de manera no estandar. Lo cual puede mejorar la precision de fuentes cerebrales en Senales EEG. Por ultimo, La combinacion de VBI y Probabilistic ICA puede ser mas efectiva en la modelizacion de senales EEG no lineales, ya que la inferencia bayesiana permite manejar relaciones no lineales entre las fuentes y las mezclas de senales. 

Una de las desventajas de este metodo es que la calidad de los datos sigue siendo un factor reelevante, si los datos contienen ruido muy fuerte, el modelo probabilistico puede tener dificultades para separar las fuentes. Una de las desventajas principales es que para aplicar este metodo se requiere de conocimiento previo de la distribucion de los datos, lo cual no siempre esta disponible. 

### IVA ###

IVA es muy bueno en donde las senales de diferentes canales estan correlacionadas, algo que es comun en senales EEG. Lo que permite la separacion adecuada de estas senales, manteniendo las dependencias entre ellas. Ademas de esto, IVA puede manejar situaciones en las que las senales cerebrales no son completamente independientes entre si, permitiendo una mayor flexibilidad en los modelos.

IVA es un algoritmo mas avanzado, por lo que requiere una mayor cantidad de datos para poder estimar correctamente las fuentes y sus relaciones. Ademas de esto otro problema es que requiere conocimiento de la estructura de los datos y sus dependencias mutuas que puede ser un gran desafio.


### DeepICA ### 

Uno de los principales beneficios de DeepICA sobre de ICA es que puede manejar separaciones no lineales. Las redes neuronales profundas son capaces de aprender representaciones mas complejas de las senales que las tecnicas lineales, lo que mejora la separacion de las fuentes, especialmente cuando contienen relaciones no lineales. Cuando se utilizan Redes Neuronales Profundas, DeepICA puede extraer caracteristicas a diferentes niveles de abstraccion, lo cual puede mejorar significativamente la precision. Una ventaja muy grande de DeepICA es que no requiere ninguna suposicion de los datos, ademas de que tiene una gran capacidad de retener caracteristicas reelevantes aunque haya presencia de ruido, finalmente DeepICA es una tecnica muy escalable teniendo buen rendimiento con grandes cantidades de datos.

Una de las desventajas principales de este metodo es la necesidad de datos de entrenamiento, lo que lo hace sensible a la calidad y cantidad de datos de entrenamiento, otra desventaja es la necesidad de preprocesamiento y la complejidad del modelo. 

### Autoencoders ### 

Los autoencoders son una buena opcion debido a que comprimen los datos facilitando su procesamiento, ademas de esto, no requieren etiquetas para el entrenamiento, esta tecnica tambien tiene la capacidad de capturar relaciones no lineales, aparte de reducir la dimensionalidad esta tecnica es utilizada para eliminar el ruido, mejorando la calidad de datos incluso cuando las senales estan contaminadas por artefactos.
Otra ventaja de esta tecnica es la escalabilidad ya que se pueden ajustar a diferentes configuraciones de datos EEG y su arquitectura puede personalizarse dependiendo de la tarea realizada, finalmente, Las representaciones latentes generadas pueden ser utilizadas para modelos supervisados. 

Este tecnica tiene un gran riesgo al sobre ajuste si el conjunto de datos no es suficientemente grande o representativo, ademas necesitan trabajar con datos limpios, si contienen mucho ruido o artefactos severos, el rendimiento puede ser reducido considerablemente.



## Tecnicas que se descartaran ## 

Las siguiente tecnicas se descartaran por que no son viables para nuestro proyecto y solo se desarrollaran las demas: 

### Variational Bayesian Inference and Probabilistic ICA ### 

Esta tecnica se descartara por el hecho de que requiere un conocimiento previo de la distribucion de datos, lo cual es impractico en nuestro caso, ademas de esto es una tecnica muy sensible al ruido, el cual no podemos asegurar que se quitara por completo.

### SPC (Sparse Component Analysis) ### 

Esta tecnica tiende a fallar con senales densas o no lineales, lo cual es comun en senales EEG, ademas de esto esta tecnica asume que las senales relevantes son escasas, lo cual puede no ser cierto en todos los casos, especialmente cuando se esta buscando modelar patrones complejos.

### CCA (Canonical Correlation Analysis) ### 

Esta tecnica no sera acceptada debido a que necesita datos de referencia de calidad, los cuales no siempre estan disponibles, ademas de esto, solo detecta dependencias lineales entre conjuntos de datos, limitando su eficiencia si las relaciones no son lineales, ademas de esto ya consideramos mas metodos que detectan relaciones lineales

### Factor Analysis ### 

Finalmente descartaremos esta tecnica debido a que asume una estructura lineal de los factores, lo cual podria no ser valido en senales EEG complejas y no lineales, aunque es util para reduccion de dimensionalidad, tecnicas como PCA y TD pueden cumplir con este proposito de una manera mas eficaz.





