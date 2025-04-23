# Reporte Sprint 5 # 

### Para este sprint la actividad designada, es la creacion e implementacion de los metodos para componentes ###

En el sprint pasado, se hizo un analisis de que metodos eran los mas viables, para posteriormente ser implementados, en este sprint seran implementados, destacando de un punto de vista mas tecnico los aspectos de implementacion de cada uno de los metodos. 

Los metodos que se realizaran son los siguientes: 


- ICA (Independent Component Analysis) 
- PCA (Principal Component Analysis)
- NMF (Non-Negative Matrix Factorization)
- TD (Tensor Decomposition)
- Dictionary Learning & Sparse Encoding
- IVA (Independent Vector Analysis) 
- DeepICA (Deep Learning based ICA)
- Autoencoders


### ICA (Independent Component Analysis) ### 

Como se menciono en reportes anteriores, ICA se basa en un modelo generativo de mezcla lineal:

$$x = A \cdot s$$


donde: 
* x: es el vector de observaciones (senales mezcladas)
* A: es la matriz de mezcla desconocida
* s: es el vector de componentes independientes que desafiamos estimar

El objetivo de ICA es encontrar una matriz de separacion W tal que:
$$s = W \cdot x$$


Tambien en los reportes anteriores, se menciono que cuando se aplica ICA se necesitan cumplir ciertas condiciones, las cuales solamente se mencionaran, si se requiere profundizar la informacion correspondiente se puede encontrar en __, por lo que ahora solo se mencionaran:

1. Centrado 
2. Blanqueamiento

El objetivo central de ICA es maximizar la independencia estadistica mediante la **Curtosis** o la **Negentropia** 


En la implementacion real de ICA, funciona mediante un algoritmo llamado FastICA, este algoritmo se basa en la maximizacion de la no gaussanidad, mediante un proceso iterativo. Se apoya en la suposicion de que las senales independientes son no gaussianas (por el teorema central del limite).

#### Pasos de FastICA #### 

1. **Centrado de los datos**:

Primero los datos se centran restando la media 

$$ X = X - media(X) $$ 

Esto asegura que los datos tengan media cero en cada dimension.

**2. Blanqueo (Whitening)** 

El objetivo de este paso es transformar los datos para que sean decorrelacionados y tengan varianza unitaria. Se logra con **Analisis de Componentes Principales (PCA)**:
    
1. Se calcula la **matriz de covarianza** de los datos centrados:

$$ \sum= \frac{1}{N}XX^T $$

2. Se obtiene la descomposicion en valores propios de $ \sum $ 

$$ \sum = EDE^T $$

* $E$ contiene los **autovectores** (vectores principales)
* $D$ es una matriz diagonal con los **autovalores** (varianza en cada direccion)

3. Se calcula la **Matriz de blanqueo**: 

$$ X_{whitened} = D^\frac{-1}{2}E^TX $$ 

Esto hace que las nuevas variables tengan varianzas iguales y sean decorrelacionadas

**3. Iteracion para encontrar componentes independientes**

Aqui esta lo principal de FastICA, se busca maximizar la no-gaussanidad de cada componente iterativamente usando una funcion de contraste $ g(y) $. Las funciones comunes son: 

* G1: $g(y)=tanh(y)$ -> Rapida y estable
* G2: $g(y)=y^3$ -> Mas sensible a valores extremos

**Regla de Actualizacion de FastICA**

Se inicializa un vector aleatorio $w$ y se itera con:

1. Actualizar $w$ con la funcion de contraste: 

$$ w^+ = E \left\{ Xg(w^TX)\right\}- E\left\{g'(w^TX)\right\}w $$ 

Donde: 

* $g(y)$ es la funcion de no-linealidad
* $g'(y)$ es su derivada

2. Normalizar $w$ para mantener varianza unitaria: 

$$ w = \frac{w}{||w||} $$ 


3. Ortogonalizacion (si hay multiples componentes)

    Para evitar que los vectores $w$ converjan al mismo resultado, se ortogonalizan utilizando Gram-schmidt.

4. Repetir hasta convergencia: 
    
    La iteracion se detiene cuando $w$ no cambia significativamente.


**4. Recuperacion de senales**

Una vez encontrados los vectores de mezcla $W$, podemos recuperar las senales independientes: 

$$ S = WX_{whitened}    $$

Donde $S$ son las senales esperadas.

Una vez que se hizo este proceso antes de reconstruir S a partir de ${W}$ primero se debe de filtrar la senal en el dominio de ICA para quitar las partes estadisticamente ruidosas de la senal y retornar una senal libre de artefactos. 


### PCA (Principal Component Analysis)

Ya se menciono anteriormente la funcionalidad y las generalidades de PCA, por lo cual se pasaran directamente a la forma en la que PCA funciona. 

**1. Centrado de los datos**

El primer paso en PCA es centrar los datos al restarle la media a cada variable: 
$$ X = X- media(X) $$ 
L
Este paso asegura que cada dimension tenga una media de cero, lo que es necesario para calcular la covarianza. 

**2. Matriz de Covarianza** 

La matriz de covarianza describe la relacion entre las variables: 

$$ \sum  = {\frac{1}{N}XX^T} $$ 

Donde: 

- $X$ son los datos centrados
- $N$ es el numero de muestras
- $\Sigma$ es la matriz de covarianza


**3. Descomposicion en valores propios** 

Para obtener las componentes principales, se realiza la descomposicion en valores propios de la matriz de covarianza: 

$$ \Sigma v = \lambda v $$ 

Donde: 
- $v$ son los autovectores (direccioens principales de los datos)
- $\lambda$ son los autovalores (cantidad de varianza explicada por cada componente)

Los autovectores definen la nueva base del espacio transformado, mientras que los autovalores indican la importancia de cada componente. 

**4. Seleccion de componentes principales** 

Se ordenan los autovalores en orden descendente y se eligen los primeros $k$ componentes principales, donde $k$ es el numero de dimensiones deseadas: 

$$ X_{PCA} = XV_k $$ 

Donde: 
- $V_k$ es la matriz con los $k$ autovectores seleccionados. 
- $X_{PCA}$ es la nueva representacion reducida de los datos. 


El numero de componentes puede seleccionarse con base en la varianza explicada: 

$$ \frac{\sum_{i=1}^k \lambda_i}{\sum_{j=1}^d \lambda_j} $$ 

Donde $d$ es el numero total de dimensiones y el umbral suele ser entre 90%-95%






## NMF (Non-Negative Matrix Factorization) ##

dado una matriz de datos, el objetivo de NMF es encontrar dos matrices $W$ y $H$ tales que: 


$$ X ≈ WH $$ 

donde: 

- $W$ es una matriz de bases de tamano $ N \times K$ que representa patrones en los datos
- $H$ es una matriz de **coeficientes** de tamano $ k \times M$ que indica la contribucion de cada base a cada variable(canal). 
- $k$ es el numero de componentes a extraer (hiperparametro)

*NMF solo permite valores positivos* 

### Pasos de NMF ###

1. **Preparacion de los datos** 

    - Se obtiene la matriz  $X$ con dimensiones $N \times M$ 
    - Se normalizan los v alores para que sean positiovs de ser necesario 
2. **Inicializacion de matrices**

    - $W$ y $H$ se inicializan aleatoriamente con valores positivos

3. **Optimizacion iterativa** 

    - Se minimiza el error entre $X$ y $WH$ usando una metrica como la divergencia de kullback-Leiber o el error cuadratico medio 
    - Se usa una regla de actualizacion de multiplicacion para garantizar que $W$ y $H$ permanezcan no negativos: 

    $$ H ← H \times \frac{W^TX}{W^TWH}$$ 
    $$ W ← W \times \frac{H^TX}{WHH^T}$$ 
    
    - Se itera hasta convergencia

4. **Interpretacion de los resultados** 

    - $W$ contiene patrones espaciales
    - $H$ muestra como varian esos patrones en el tiempo


## TD (Tensor-Decomposition) ## 

Un **tensor** de orden $N$ es una generalizacion de una matriz a $N$ dimensiones. Se representa como: 

$$ X \in \mathbb{R}^{I_1 \times I_2 \times \dots \times I_N} $$ 

donde cada $ I_n$ es el tamano de la dimension $n$. \
El objetivo de TD es descomponer el tensor $X$ en factores de menor dimension que caputren sus caracteristicas principales.

Los dos enfoques mas comunes son: 

1. **CPD (Canonical Polyadic Decomposition)** 

$$ X ≈ \sum_{r=1}^R a_r \circ b_r \circ c_r $$ 

donde $a_r,b_r,c_r$ son vectores que representan cada modo del tensor. 

2. **Tucker Decomposition** 

$$ X ≈ G \times_1 A \times_2 B \times_3 C $$ 

donde $G$ es un nucleo tensorial y $A,B,C$ son matrices de transformacion para cada dimension.

### Pasos de TD ### 

1. **Construccion del tensor** 

    Para senales EEG multicanal, el tensor se puede construir de diversas maneras. 

    - $(canales \times tiempo \times ensayos)$ -> Para analizar variaciones espaciales y temporales. 

    - $(canales \times frecuencia \times tiempo)$ -> Para analisis tiempo-frecuencia.

2. **Centrado y Normalizacion** 

Se normalizan los datos en cada dimension para mejorar la factorizacion del tensor. 

$$ X = \frac{X-\mu}{\sigma} $$ 

3. **Eleccion del metodo de decomposicion** 

- **CPD**(cuando se busca una decomposicion unica de los factores) 
- **Tucker**(cuando se quiere mayor flexibilidad y compresion de datos)

4. **Aplicacion de algoritmos de descomposicion** 
Algunos metodos para resolver la decomposicion incluyen: 

- Alternating least Squares (ALS)
- Gradient Descent
- Hierarchical Alternating Least Squares(HALS)

5. **Interpretacion de resultados** 

Los factores obtenidos $(A,B,C)$ representan patrones en cada modo del tensor. 
- **Modo 1(A)**: Relacionado con los canales (patrones espaciales)
- **Modo 2(B)**: Relacionado con el tiempo (dinamica temporal)
- **Modo 3(C)**: Relacionado con ensayos o frecuencias.



## Dictionary Learning y Sparse Encoding ## 

### Dictionary Learning ### 

El modelo general de Dictionary Learning se puede escribir como: 

$$ X = D \cdot A $$


- $X ∈ \mathbb{R}^{m \times n}$: La matriz de datos (donde $m$ es la cantidad de caracteristicas y $n$ es el numero de muestras). 

- $D ∈ \mathbb{R}^{m \times k}$: El **diccionario** $k$ columnas (vectores base).

El objetivo es aprender tanto $D$ como $A$ minimizando el error de reconstruccion sujeto a una restriccion de esparcidad sobre las columnas de $A$: 

$$ min_{D,A} || X - D \cdot A||_F^2 + \lambda ||A||_1 $$ 

Donde: 

- $||X-D \cdot A||_F$ es el error de reconstruccion 
- $\lambda$ es un parametro de regularizacion que controla la esparcidad. 
- $||A||_1$ es la norma $l_1$ de $A$, que impone la esparcidad en las representaciones.

### Pasos de Dictionary learning ### 

1. **Inicializacion** 

Se seleccionan aleatoriamente las primeras columnas de $X$ como diccionario inicial, o se puede usar un proceso como K-SVD (K-means para diccionarios)

2. **Aprendizaje de Diccionario (D)** 

El diccionario $D$ se aprende iterativamente, manteniendo las coordenadas $A$ fijas y actualizando $D$ para reducir el error de reconstruccion. 

3. **Calculo de las coordenadas esparsas(A)** 

Para un diccionario dado, $A$ se obtiene minimizando el error de reconstruccion bajo la restriccion de esparsidad. Se utilizan tecnicas como el **Lasso* o **OMP**(Orthogonal Matching Pursuit)

4. **Iteracion** 

Los pasos de optimizacion de $D$ y $A$ se repiten hasta la convergencia.


### Sparse Encoding ### 

Dado un diccionario $D$ previamente aprendido, el objetivo es encontrar la representacion esparsa $A$ que minimice el error de reconstruccion: 

$$ min_A || X-D \cdot A ||_F^2 + \lambda ||A||_1$$

Donde: 

- $X \in \mathbb{R}^{m \times n}$
- $D \in \mathbb{R}^{m \times k}$
- $A \in \mathbb{R}^{k \times n}$


### Pasos de Sparse Encoding ### 

1. **Obtencion del diccionario** 

Se obtiene un diccionario $D$ a partir de datos (Dictionary Learnign). Este diccionario contiene una base de vectores sobre la cual las senales pueden ser representadas. 

2. **Calculo de las coordenadas Esparsas (A)**

Para los datos $X$, se busca $A$ que minimice el error de reconstruccion bajo la restriccion de esparsidad, ulilizando tecnicas como **OMP** o **Lasso** 


## IVA (Independent Vector Analysis) ## 

El modelo de mezcla de IVA se representa de la siguiente manera: 

$$ X = A \cdot S $$ 

Donde: 

- $X$ es una matriz de senales mixtas, de tamano $N \times M$(donde $N$ es el numero de canales y $M$ es el numero de muestras)
- $A$ es una matriz de mezcla de tamano $N \times N$
- $S$ es la matriz de senales independientes de tamano $N \times M$ 

El objetivo de IVA es encontrar una **Matriz de separacion** $W$ tal que: 

$$ S = W \cdot X $$ 

Donde $W$ es la matriz de separacion que permite recuprerar las senales independientes. 

### Requerimientos y Condiciones para IVA ### 

1. **Centrado**: Las senales deben de ser centradas, es decir, con media cero.
2. **Blanqueo**(Whitening): Se requiere que las senales sean decorrelacionadas y tengan varianza unitaria.
3. **Independencia Estadistica**: IVA se basa en la suposicion de que las senales son estadisticamente independientes y deben estar decorrelacionadas.

### Pasos de IVA ### 

1. **Centrado de datos**: Primero, las senales mixtas deben centrarse. Esto implica restar la media de cada canal: 

$$ X = X - media(X) $$ 
Esto asegura que cada canal tenga una media de cero. 

2. **Blanqueo**: Las senales deben ser decorrelacionadas y tener varianza unitaria. Para esto, se realiza un proceso de blanqueo, que puede lograrse con PCA o mediante la descomposicion de valores propios. El paso de blanqueo transforma la senales para que sean linealmente independientes. 

    Se calcula la matriz de covarianza de las senales centradas: 

    $$ \sum = \frac{1}{MXX^T} $$ 

    Luego, se calcula la descomposicion en valores propios: 

    $$ \sum = EDE^T $$

    Con $E$ como los **autovectores** y $D$ como los **autovalores**. Se obtiene la matriz de blanqueo: 

    $$ X_{whitened} = D^{-\frac{1}{2}}E^TX $$ 


3. **Optimizacion Iterativa (Calculo de las senales Independientes)**: 

El objetivo es maximizar la independencia estadistica de las senales a traves de una funcion de contraste. El metodo de optimizacion mas comun es basado en el gradiente.

Se actualiza la matriz de separacion $W$ con la siguiente formula: 

$$W + = E\left\{ Xg(W^T X) \right\} - E\left\{ g'(W^T X) \right\} W
$$    
    
Donde $g(y)$ es la funcion de contraste y $g'(y)$ es su derivada. Algunas funciones de contraste comunes son: 

- $g_1(y) = tanh(y)$
- $g_2(y) = y^3$

Este paso busca maximizar la no-gaussianidad de las senales esperadas, utilizando un proceso iterativo

4. **Ortogonalizacion (si hay multiples componentes)** 

Si hay multiples senales a separar, los vectores $W$ deben ser otrogonalizados para evitar que converjan al mismo resultado. Esto se realiza usando el proceso de Gram-Schmidt. 

5. **Repetir hasta convergencia** 

El proceso se repite hasta que los cambios en $W$ sean minimos, lo que indica que se ha alcanzado la convergencia. 

6. **Recuperacion de senales independientes** 

Una vez que se ha obtenido la matriz de separacion $W$, las senales independientes se pueden recuperar: 

$$ S = W \cdot X_{Whitened} $$ 

Aqui, $S$ es la matriz de senales independientes, que son las senales que deseamos recuperar. 

## Deep ICA ## 

Deep ICA es una version de ICA donde se utiliza una red Neuronal en vez de ICA para generar separacion no lineal. 

### Pasos de Deep ICA ### 

1. Construccion de una red neuronal para separar las senales de las fuentes 
2. Entrenamiento de red utilizando una funcioon de independencia basada en la curtosis
3. Aplicacion de la red a los datos para obtener las senales separadas

## Autoencoders ## 

Son modelos que aprenden una representacion comprimida de los datos de entrada. 

### Pasos de Autoencoders ### 


1. Preprocesamiento de EEG: Antes de aplicar encoders la senal de eeg necesita estar lo mas limpia posible en frecuencia. 

2. Definicioni de Autoencoder: 

    El modelo se compone de: 

    1. **Encoder** 
            
        - Reduce la senal EEG a un espacio latente (menor dimension)
        - Puede ser una capa densa o convolucional
    
    2. **Decoder**
        - Reconstruye la senal original desde la representacion comprimida

$$X→Encoder→Z→Decoder→\hat{X}$$
 
Donde: 

- $X$ es la senal original
- $Z$ es la representacion comprimida (codigo latente)
- $\hat{X}$ es la reconstruccion de la senal 


El modelo se entrena minimizando la diferencia entre $X$ y $\hat{X}$ (MSE)


## Variational Autoencoders ## 

Los VAEs son una version avanzada de los autoencoders, en la que el espacio latente $Z$ se representa como una distribucion probabilistica, en lugar de un punto fijo 

### Ventajas en EEG ### 

- Permite modelar la variabilidad natural de las senales EEG 
- Puede generar nuevas senales a partir de la distribucion aprendida
- Ayuda a filtrar artefactos aprendiendo una representacion mas robusta

En un VAE, el encoder produce **media** ($\mu$) y **varianza** ($\sigma^2$) en lugar de una unica representacion $Z$: 

$$ Z = \mu + \sigma + \epsilon $$ 


Donde $\epsilon$ es una variable aleatoria normal

El **decoder** usa esta representacion $Z$ para reconstruir la senal. 



### Entrenamiento y Extraccion de Caracteristicas ### 


1. Entrenar el autoencoder con senales EEG sin etiquetar. 
2. Obtener la representacion comprimida $Z$. 
3. Usar $Z$ como entrada a otro modelo. 

Este proceso permite convertir EEG en un conjunto de caracteristicas mas manejable para otras tareas.

