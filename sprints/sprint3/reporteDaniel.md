# Reporte Sprint 3 # 

## Investigacion y analisis de tecnicas de preprocesamiento: Tecnicas de Analisis de Componentes

### Para el tercer sprint la actividad designada, es la investigacion y analisis de tecnicas de preprocesamiento, especificamente tecnicas referentes a Analisis de componentes, donde las mas conocidas son ICA (Analisis independiente de Componentes) y PCA (Analisis principal de Componentes)


Anteriormente enliste en manera de ejemplo, dos de los metodos de analisis de componentes, mas utilizados, pero a continuacion se enlistaran puntualmente todos los metodos que se utilizaran en este proyecto, y despues se desarrollara exensivamente en que consiste cada uno:


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

Ahora que ya se mencionaron las tecnicas reelevantes en cuanto al Analisis de componentes, a continuacion explicaremos en que consiste cada uno: 


## ICA (Independent Component Analysis) ##

El analisis de componentes independientes es una tecnica estadistica orientada a descomponer una senal multivariada en componentes subyacentes estadisticamente independientes.


ICA se basa en un modelo generativo de mezcla lineal:
$$x = A \cdot s$$


donde: 
* x: es el vector de observaciones (senales mezcladas)
* A: es la matriz de mezcla desconocida
* s: es el vector de componentes independientes que desafiamos estimar

El objetivo de ICA es encontrar una matriz de separacion W tal que:
$$s = W \cdot x$$

### Procedimiento ### 

El procesamiento es escenencial para facilitar el calculo y asegurar que los supuestos de independencia sean validos

1. Centrado

El centrado consiste en eliminar la media de la variable xi, garantizando que el vector resultante xcentrada tenga media cero: 

$$xcentrada = x - E[x]$$


2. Blanqueamiento

El blanqueamiento transforma las variables de los datos para que las variables sean no correlacionadas y con varianza unitaria. <br>
Utilizando la matriz de covarianza C de xcentrada

$$C = E[xcentrada \cdot xCentrada^T]$$

se realiza la decomposicion espectral 

$$C = E \cdot D \cdot E^T $$

donde: 
* E: Matriz de autovectores 
* D: Matriz diagonal de autovalores
* $E^T$: Matriz transpuesta de Autovectores

El blanqueamiento se calcula de la siguiente manera: 

$$xblanqueada = D^\frac{-1}{2} \cdot ET \cdot xcentrada$$

### Maximizacion de la independencia estadistica ### 

El nucleo de ICA es maximizar la independencia estadistica de las senales estimadas. Para ello se utilizan medidas de gaussanidad basadas en la Ley Central del Limite, que establece una combinacion de variables independientes tiende a seguir una distribucion mas gaussiana.

1. Medidas de No Gaussianidad

**Curtosis**: La curtosis evalua la dispersion de los datos alrededor de la distribucion normal. Se define como: 
$$curtosis(y) = E[y4] - 3(E[y2])2 $$

Para senales independientes, se busca maximizar esta medida
**Negentropia**: Basada en la entropia diferencial H(y), la negentropia mide las desivaciones de la gaussanidad.
$$ J(y) = H(ygaussiano) - H(y)$$

Donde H(y) = $ \int p(y)log(p(y))\, dx$ siendo p(y) la funcion de densidad de probabilidad




## PCA (Principal Component Analysis) ## 

El analisis de componentes principales es una tecnica simple no parametrica para informacion reelevante de datasets que contienen ruido. Con un ezfuerzo minimo PCA nos da un metodo para reducir un conjunto de datos complejo a una dimension menor para simplificar las caracteristicas clave de este conjunto de datos.

En resumen, PCA es un metodo utilizado para reconstruir un conjunto de datos con una menor dimensionalidad, y su formula principal puede ser expresada de la siguiente manera: 

$$PX = Y $$ 

donde:
* P: Matriz que transforma X a y
* X: Conjunto original de datos
* Y: Conjunto de datos reducido

De algebra lineal sabemos que, dadas dos matrices A de axb y B de bxc:

$$
A =
\begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1b} \\
a_{21} & a_{22} & \cdots & a_{2b} \\
\vdots & \vdots & \ddots & \vdots \\
a_{a1} & a_{a2} & \cdots & a_{ab}
\end{bmatrix}
\quad
B =
\begin{bmatrix}
b_{11} & b_{12} & \cdots & b_{1c} \\
b_{21} & b_{22} & \cdots & b_{2c} \\
\vdots & \vdots & \ddots & \vdots \\
b_{b1} & b_{b2} & \cdots & b_{bc}
\end{bmatrix}
$$

El producto \( C = AB \) es:

$$
C =
\begin{bmatrix}
a_{11}b_{11} + a_{12}b_{21} + \cdots + a_{1b}b_{b1} & a_{11}b_{12} + a_{12}b_{22} + \cdots + a_{1b}b_{b2} & \cdots & a_{11}b_{1c} + a_{12}b_{2c} + \cdots + a_{1b}b_{bc} \\
a_{21}b_{11} + a_{22}b_{21} + \cdots + a_{2b}b_{b1} & a_{21}b_{12} + a_{22}b_{22} + \cdots + a_{2b}b_{b2} & \cdots & a_{21}b_{1c} + a_{22}b_{2c} + \cdots + a_{2b}b_{bc} \\
\vdots & \vdots & \ddots & \vdots \\
a_{a1}b_{11} + a_{a2}b_{21} + \cdots + a_{ab}b_{b1} & a_{a1}b_{12} + a_{a2}b_{22} + \cdots + a_{ab}b_{b2} & \cdots & a_{a1}b_{1c} + a_{a2}b_{2c} + \cdots + a_{ab}b_{bc}
\end{bmatrix}.
$$


Por lo que, cada columna de Y en PCA tiene la siguiente forma: 

$$ y_{i} = \begin{bmatrix}
p_{1} \cdot x_{i}\\
p_{2} \cdot x_{i}\\
\vdots\\
p_{m} \cdot (x_{i})
\end{bmatrix}
\quad
$$ 

Cada columna de Y en esta transformacion seran los componentes principales de X.

## Objetivo ## 
Como se menciono anteriormente el objetivo de PCA es reducirle la dimensionalidad de los datos, y como vimos esto se logra a partir de una transformacion lineal, pero debemos saber que la transformacion lineal es la que mejor expresa los datos (i.e. la que menos perdida de informacion tiene), para esto debemos tomar en cuenta diversos aspectos:


1. ### Ruido y Rotacion ### 

El ruido medido en cualquier conjunto de datos debe de ser bajo, de lo contrario cualquier analisis que se utilize no podra obtener ninguna informacion. No existe una escala absoluta para ruido, pero todo el ruido es cuantificado con respecto a la escala de la senal. Una medida comun es la razon de senal-a-ruido SNR (Signal-to-noise Ratio), o una razon de varianzas $\sigma^2$, 

$$SNR= \frac{\sigma^2_{senal}}{\sigma^2_{ruido}}$$

Un SNR alto (>>1) indica una altra precision de medida, mientras que un SNR muy bajo indica un conjunto de datos muy ruidoso. 

2. ### Redundancia ### 

Al preguntarse si es buena idea utilizar PCA o cualquier algoritmo de reduccion de dimensionalidad en este sentido, debemos analizar los datos y comprobar si existe una correlacion entre variables, ya que si existe podemos afirmar que puede que alguna de las dimensiones no contenga informacion importante ya que puede ser estimada con otra variable. 




## NMF (Non-negative Matrix Factorization)

Es una tecnica utilizada para descomponer una matriz V en el producto de dos matrices mas pequenas W y H, cumpliendo las siguientes condiciones: 
1. No Negatividad: Todos los elementos de las matrices V,W,H son no negativos (>=0). 
2. Aproximacion: La matriz V se aproxima como el producto punto de W y H 
$$V≈W⋅H$$ 

Donde: 
* V: matriz de dimension mxn (original, no negativa)
* W: matriz de dimension mxr (matriz base)
* H: matriz de dimension rxn (matriz de pesos)
* r: es un valor mucho menor que m y n, lo que permite la reduccion de dimensiones 

Dado este planteamiento, NMF busca encontrar W y H que minimicen la diferencia o error entre V y $W \cdot H$. Esto se logra tipicamente resolviendo un problema de optimizacion como: 

$$min_{W,H} \| V - WH \|_F^2$$

Sujeto a W,H >= 0, donde $\| \cdot \|_F$ es la norma de Frobenius.

NMF es una tecnica similar a PCA para reduccir la dimensionalidad, solo que NMF tiene las restricciones que el conjunto de datos debe de ser enteramente positivo.




## SPC (Sparse Component Analysis) ##

Al igual que muchos de los metodos anteriores SPC es una tecnica de reduccion de dimensionalidad, que busca encontrar representaciones parciales (esparsas) de los datos en un espacio transformado. Es una extension o variante de **ICA** y se utiliza principalmente cuando las fuentes subyacentes que generan los datos originales son escasas o tienen variables poco significativas. 

### Concepto Clave de SPC ### 
En un contexto esparso, significa que: 
* La mayoria de los coeficientes son cero o cercanos a cero
* Solo unas pocas componentes tienen valores significativos o dominantes 

El objetivo del SPC es encontrar una representacion donde cada componente tenga la menor cantidad posible de variables no nulas, mientras se retiene la mayor cantidad de informacion util. 

### Caracteristicas Principales ### 

1. #### Esparcidad ####
    En lugar de buscar componentes independientes, asume que los datos son esparso-representados, es decir, pueden describirse con pocas variables no nulas en comparacion con el numero total de variables.

2. #### Separacion de Fuentes #### 
    El SPC es util para separar fuentes cuando las senales de origen tienen caracteristicas esparsas (por ejemplo, un encefalograma donde solo algunas areas del cerebro estan activas en un momento Dado)

3. #### Interpretabilidad #### 
    Debido a la esparsidad, los resultados de SPC tienden a ser mas interpretables que tecnicas como ICA e PCA 


SPC utiliza tecnicas de optimizacion para resolver el siguiente problema: 

1. Dado un conjunto de datos $X$ (mezclas de senales observadas), se busca una matriz de transformacion $W$ que descomponga los datos en sus componentes originales $S$ segun: 

$$ X = W \cdot S$$

Donde: 
* $S$ es un conjunto  de senales o componentes escasas
* $W$ es la matriz de mezcla

2. La solucion a este problema impone restricciones de esparsidad en $S$, es decir, busca minimizar el numero de valores distintos de cero en $S$, mientras maximiza la cantidad de la reconstruccion. 

SPC es una herramienta poderosa para trabajar con datos esparsos y compernder patrones significativos en senales o conjuntos de datos complejos.


## CCA (Canonical Correlation Analysis) ##

Es una tecnica estadistica que mide la relacion entre dos conjuntos de variables, donde su objetivo principal es encontrar combinaciones lineales de las variables en cada conjunto que esten maximalemnte correlacionadas entre si 

### Conceptos Clave ### 

En CCA, trabajamos con dos conjuntos de variables: 

* $X$ (con dimensiones $n$ x $p$): Representa $p$ variables independientes
* $Y$ (con dimensiones $n$ x $q$): Representa $q$ variables independientes 

El objetivo es encontrar vectores $a$ y $b$ que definan combinaciones lineales 

$$u = X \cdot a $$ 
$$ v=Y \cdot b$$

donde: 
* $v$ y $u$ son las combinaciones lineales de $X$ y $Y$
* La correlacion entre $u$ y $v$ es maxima

En terminos matematicos, este se traduce en maximizar: 

$$p = corr(u,v) = \frac{Cov(u,v)}{\sqrt{Var(u) \cdot Var(v)}}$$

### Caracteristicas Principales ### 

1. #### Relacion entre dos conjuntos de variables #### 
* CCA encuentra las dirrecciones en $X$ y $Y$ donde las variables tienen la mayor correlacion possible. 
2. #### Combinaciones Lineales #### 
* CCA no analiza cada variable individualmente, sino que traba con combinaciones lineales de las variables 
3. #### Multidimensionalidad #### 
* Genera varios pares de componentes canonicas ($u_i$,$v_i$), donde cada par es ortogonal a los demas y explica una parte diferente de la correlacion 
4. #### Simetria #### 
* No asume causalidad; trata ambos conjuntos de datos por igual. 

CCA es una tecnica versatil y poderosa para poder analizar las relaciones entre dos conjuntos de datos, especialmente cuando los datos estan altamente correlacionados o tienen estructura comun subyacente. 


## FA (Factor Analysis)

Es una tecnica estadistica disenada para descubrir patrones latentes en conjuntos de datos. Su objetivo principal es al igual que muchas de las tecnicas anteriores, reducir la dimensionalidad de los datos al identificar **Factores Latentes** que explican las correlaciones entre las variables observadas. 
Es particularmente util en situaciones donde se manejan muchas variables que parecen estar relacionadas y se quiere simplificar su estructura, agrupandolas en factores subyacentes. 


### Conceptos clave de FA ### 
El analisis factorial asume que las variables observadas ($x_1,x_2,...,x_p$) estan influenciadas por: 
1. Factores latentes ($f_1,f_2,...,f_k$), que son variables no observadas. 
2. Errores unicos ($e_1,e_2,...,e_p$) que son especificos de cada variable y no compartidos entre ellas. 

La relacion se expresa como: 
$$ x = Λf + \epsilon $$

donde: 

* $x$:Vector de variables observadas ($p$-dimensional)
* $Λ$: Matriz de cargas factoriales ($p$ x $k$), que muestra cuanto contribuye cada factor latente a cada variable observada. 
* $f$: Vector de factores latentes ($k$-dimensional, con $k<p$)
* $\epsilon$:Vector de errores unicos ($p$-dimensional)

El objetivo es estimar $Λ$, los factores $f$, y los errores $\epsilon$.

### Tipos de Analisis Factorial ### 

1. #### Exploratorio (Exploratory Factor Analysis, EFA) #### 

* No se hace suposicion previa sobre cuantos factores existen o como estan estructurados
* Se usa para explorar las relaciones latentes en los datos

2. #### Confirmatorio (Confirmatory Factor Analysis) ####

* Se parte de una hipotesis especficia sobre la cantidad de factores y como se relacionan con las variables observadas. 
* Se utiliza para validar un modelo teorico.


### Suposiciones en FA ### 

1. **Linealidad**: Las variables observadas son combinaciones lineales de los factores
2. **Normalidad**: Las variables siguen una distribucion normal multivariada. 
3. **Independencia**: Los errores ($\epsilon$) son independientes entre si. 

### Limitaciones del Analisis Factorial ### 

1. Requiere un tamano de muestra grande para obtener resultados confiables. 
2. La interpretacion de los factores puede ser subjetiva. 
3. No captura relaciones no lineales entre las variables. 

El analisis factorial es una herramienta poderosa para reducir la dimensionalidad y descubrir patrones latentes en los datos, especialmente cuando se trabaja con muchas variables correlacionadas. 



## BSS (Blind Source Separation) ## 

Es una tecnica fundamental en el procesamiento de senales, que se centra en separar las senales fuente originales a partir de mezclas observadas sin tener informacion previa acerca de las fuentes ni el proceso de mezcla. Se utiliza ampliamente en aplicaciones donde multiples senales (como sonidos, imagenes, o datos biometricos) estan combinadas y se busca recuperar cada fuente de manera independiente. 

### Definicion de BSS ### 

Dado un conjunto de senales mezcladas $ X = [x_1, x_2, ..., x_n]$, el objetivo de BSS es encontrar un conjunto de senales fuente $S= [s_1,s_2, ... , s_m]$, y una matriz de mezcla $A$ tal que: 

$$ X = A \cdot S $$

Donde: 

* $X$: Senales observadas (mezclas)
* $S$: Senales fuente originales 
* $A$: Matriz de mezcla desconocida

El desfio de BSS radica en recuperar $S$ unicamente a partir de $X$, sin conocer a $A$. 

### Caracteristicas de BSS ### 

1. **Separacion Ciega**: La palabra "ciega" impica que no se tiene conocimiento previo de las caracteristicas de las senales fuente ni del proceso de mezcla. 
2. **Independencia**: En la mayoria de los casos, BSS asume que las senales fuente son estadisticamente independientes entre si. 
3. **No supervisado**: Se basa en tecnicas no supervisadas, yas que no se dispone de etiquetas o informacion directa sobre las senales originales.

### Desafios y limitaciones ### 
1. Ambiguedad en escala y orden: La magnitud y el orden de las senales fuente no se puede determinar directamente. 
2. Requerimientos de Independencia: BSS asume que las senales fuente son independientes, lo cual puede no ser siempre cierto. 
3. Ruido y mezclas no lineales: La presencias de ruido o mezclas no lineales complica significativamente el problema. 

BSS es una herramienta poderosa que encuentra aplicaciones en una gran variedad de problemas reales, donde la separación de señales es clave para el análisis y la interpretación de datos complejos.



## TD (Tensor Decompositon) ## 

Es una tecnica matematica que generaliza conceptos de descomposicion de matrices a estructuras multidimensionales llamadas tensores. Un tensor es una generalizacion de un vector (tensor de orden 1) o una matriz (tensor de orden 2) a dimensiones superiores (de orden 3 o mas). Esta tecnica es especialmente util cuando se trabajan con datos complejos que tienen multiples dimensiones, como senales multidimensionales o imagenes multicanal, que pueden ser representadas como tensores. 

### Definicion de Tensor Decomposition (TD) ### 
La descomposicion de un tensor tiene como objetivo factorizar este tensor en un conjunto de componentes mas simples, que pueden ser matrices o tensores de menor orden, facilitando la interpretacion o el procesamiento de datos. Formalmente, si tienes un tensor $𝑋$ de orden $N$ (es decir tiene $N$ dimensiones), la descomposicion de tensores busca expresar este tensor como la suma de productos de matrices de menor orden o tensored de menor orden, de manera similar a como la descomposicion de valores singulares (SVD) funciona para matrices. 

### Notacion ### 
Se supone que se tiene un tensor tridimensional $X$, con dimensiones $I$ x $J$ x $K$. La descomposicion mas comun, llamada descomposicion $CANDECOMP/PARAFAC(CP)$, trata de aproximar $X$ como la suma de productos de tres matrices $A$, $B$ y $C$, tal que: 

$$ X \approx \sum_{r=1}^{R} a_r \circ b_r \circ c_r$$

Donde: 
* $a_r \epsilon \mathbb{R}^I, b_r \epsilon \mathbb{R}^J,c_r \epsilon \mathbb{R}^K$ son vectores
* El simbolo $\circ$ representa el producto Hadamard (producto elemento a elemento)
* $R$ es el numero de componentes latentes que se utilizan en la aproximacion  

### Ventajas de la descomposicion de Tensores ### 

* Reduccion de dimensionalidad: Permite representar datos de alta dimension de manera mas compacta, manteniendo las caracteristicas mas reelevantes. 
* Mejor interpretacion: Puede ayudar a descomponer datos compejos en componentes significativas, facilitando su interpretacion. 
* Mejora en la eficiencia computacional: Al reducir el tamano de los datos y los parametros, las tecnicas de descomposicion de tensores pueden acelerar el procesamiento, especialmente en aplicaciones de aprendizaje automatico.


### Desafios y Limitaciones ### 

* Seleccion de componentes: Determinar cuantos componentes latentes o factores utilizar en la descomposicion es un desafio y depende del contexto del problema.
* Estabilidad numerica: La descomposicion de tensores puede ser inestable en algunos casos, especialmente si los datos son ruidosos o tienen caracteristicas complejas.
* Requiere gran capacidad computacional: Aunque la descomposicion de tensores reduce la dimensionalidad, aun puede requerir una considerable cantidad de recursos computacionales, especialmente para tensores de gran tamano. 


La descomposicion de tensores es una herramienta poderosa para el analisis de datos multidimensionales, permitiendo simplificar y extraer patrones de datos complejos. Su aplicacion en el procesamiento de senales EEG es valiosa para eliminar ruido y mejorar la calidad de las senales. 

## Dictionary Learning and Sparse Encoding ## 

Son tecnicas fundamentales en el campo de procesamiento de senales. Estan relacionadas y se utilizan para representar datos de manera eficiente, descomponiendolos en componentes mas simples y significativos. 

### Dictionary Learning ### 

Se refiere a un proceso en el que se aprende un conjunto de "atomos" o "bases" (llamado diccionario) que puede representar datos de manera mas eficiente que una representacion estandar. En lugar de usar una base fija (como en algebra lineal o las funciones de onda en tranformadas), el diccionario se aprende a partir de los dato, lo que permite una representacion mas adaptativa y ajustada a las caracteristicas especificas de los datos. 
* Diccionario: Un conjunto de vectores (o funciones) base que se utilizan para representar las senales de entrada. 
* El objetivo del aprendizaje de diccionario es encontrar ese conjunto de vectores base, que minimicen la diferencia entre los datos originales y su reconstruccion a partir de una combinacion lineal de estos vectores base. 

### Sparse Encoding ### 

La codificacion dispersa es el proceso mediante el cual un dato se representa como una combinacion lineal de unos pocos vectores del diccionario aprendido. En otras palabras, en lugar de usar todos los vectores del diccionario, solo se usan unos pocos que mejor representen los datos. Este proceso se llama "disperso" porque la mayoria de los coeficientes de la combinacion lineal son cero o cercanos a cero.
* En este contexto, el temino "disperso" se refiere a la propiedad de que la representacion de los datos es escasa, es decir, que la mayoria de los coeficientes de la combinacion lineal son cero o muy pequenos. Esto da como resultado uina representacion eficiente, donde se utiliza solo una pequena parate del diccionario para representar los datos.

### Relacion entre Dictionary Learning y Sparse Encoding ### 

Mientras que el aprendizaje de diccionario se centra en aprender un conjunto de bases que describan bien a los datos, la codificacion dispersa se ocupa de encontrar la representacion mas eficiente de los datos utilizando una combinacion lineal de solo unos pocos de estos vectores base. La combinacion de estas tecnicas proporciona una representacion muy eficiente de los datos en terminos de almacenamiento y computacion.

### Ventajas ### 
* Reduccion de dimensionalidad: Permite representar los datos de manera mas compacta. 
* Mejora en la interpretacion: Al aprender un diccionario que se ajust a los datos, se pueden identificar componentes subyacentes mas relevantes.
* Robustez frente al ruido: La codificacion dispersa es robusta frente al ruido, ya que solo utiliza unos pocos vectores base, lo que ayuda a ignorar el ruido no reelevante.

### Desafios ### 
* Computacionalmente intensivo: El proceso de aprendizaje puede ser intensivo en terminos computacionales especialmente para grandes conjuntos de datos. 
* Seleccion de la cantidad de dispersion: Determinar cuantos coeficientes deben ser diferentes de cero es un desafio, ya que influye en la calidad de la representacion. 

Son tecnicas poderosas para representar los datos de manera eficiente. Al aprender diccionarios adaptativos y codificar senales de manera dispersa se pueden obtener representaciones mas compactas y robustas, lo que facilita el analisis y mejora la calidad de la senal.


## Variational Bayesian Inference and Probabilistic ICA ## 

Son enfoques avanzados en estadistica y aprendizaje automatico que se utilizan para modelar datos compejos y para abordar problemas de separacion de senales y aprendizaje no supervisado. 

### Variational Bayesian Inference (VBI) ###
La inferencia bayesiana variacional es una tecnica que se utiliza para aproximar las distribuciones posteriores en modelos bayesianos complejos. En lugar de calcular directamente la distribucion posterior (lo cual puede ser muy dificil en modelos de alta dimension), se utiliza en un enfoque de aproximacion 

#### Functionamiento de VBI #### 
1. Modelo probabilistico: En la inferencia bayesiana, se modelan los datos observados como una funcion de parametros latentes y observables. La distribucion posterior de estos parametros dados los datos (es decir, la probabilidad de los parametros despues de observar los datos) es generalmente dificil de calcular directamente. 
2. Aproximacion Variacional: En lugar de calcular directamente esta distribucion posterior, VBI introduce una distribucion aproximada $q(\theta)$ sobre los parametros $\theta$. Esta distribucion $q(\theta)$ es mas facil de manejar y calcular. Se ajusta de manera que minimice la divergencia Kullback-Leibler(KL) entre la distribucion posterior exacta y la aproximacion $q(\theta)$. 
3. Optimizacion: La optimizacion se realiza buscando la mejor aproximacion para $q(\theta)$ mediante un algoritmo de optimizacion que maximice la evidencia de los datos observados. 

### Probabilistic Independent Compononet Analysis (Probabilistic ICA) ### 

El analisis de componentes independientes Probabilistico (ICA Probabilistico) es una extension del ICA clasico, que busca separar senales mezcladas en componentes independientes. Mientras que el ICA tradicional asume que las senales son lineales e independientes, la version probabilistica introduce un marco estadistico que permite manejar la incertidumbre y los errores en los datos.

#### Funcionamiento de Probabilistic ICA #### 

1. Modelos de Mezcla Probabilistica: ICA clasico busca separar las senales de una mezcla lineal. En el caso probabilistico, se modelan senales observadas como una mezcla de fuentes independientes y no gaussianasm utilizando un modelo probabilistico. 
2. Estimacion Bayesiana: A traves de la inferencia bayesiana, se estiman las fuentes independientes. Esto se hace utilizando la distribucion posterior de las fuentes dado los datos observados. En lugar de asumir que las fuentes son completamente independientes, el ICA probabilistico incorpora la idea de que pueden existir dependencias latentes o ruido en el proceso de mezcla.
3. Aproximacion Variacional: La inferencia bayesiana variacional se utiliza en ICA probabilistico para estimar las distribuciones de las fuentes de manera mas eficiente. Se trata de aproximar la distribucion posterior de las fuentes independientes mediante un proceso de optimizacion.

### Relacion entre VBI e ICA Probabilistico ### 

Ambas utilizan inferencia bayesiana para manejar incertidumbres y esimar distribuciones posteriores. En el caso de Probabilistic ICA, VBI se utiliza para obtener una aproximacion eficiente de la distribucion posterior de las fuentes independientes. Esto permite manejar modelos mas complejos, como los que involucran ruido o incertidumbre.

### Ventajas de Probabilistic ICA y VBI ### 

* Manejo de la incertidumbre: Ambos metodos permiten incorporar la incertidumbre en los modelos, lo que es fundamental cuando los datos contienen ruido o cuando las senales subyacentes son ruidosas. 
* Estimacion robusta: La aproximacion bayesiana y variacional es robusta frente a datos incompletos, lo que permite un modelado mas flexible y preciso. 
* Aplicacion de senales reales: En aplicaciones de senales como EEG o separacion de fuentes de audio, estos metodos son utiles debido a su capacidad para manejar fuentes no gaussianas y mezclas de senales. 

### Desafios ### 

* Complejidad Computacional: La inferencia bayesiana variacional puede ser intensiva en terminos computacionales, especialmente en modelos grandes o con muchos parametros. 
* Seleccion del modelo adecuado: Elegir la distribucion apropiada y las tecnicas de optimizacion para ajustar el modelo es un desafio clave, ya que depende de las caracteristicas especificas de los datos


Variational Bayesian Inference es una poderosa herramienta para aproximar distribuciones posteriores en modelos bayesianos complejos, y Probabilistic ICA extiende el Análisis de Componentes Independientes clásico al marco probabilístico, permitiendo manejar incertidumbres y características de datos más complejas. Juntas, estas técnicas ofrecen soluciones robustas para el procesamiento y análisis de señales complejas en una variedad de aplicaciones.

## IVA (Independent Vector Analysis) ## 

Es una extension avanzada de ICA. Mientras que ICA se utiliza para separar fuentes independientes a partir de una sola observacion mixta (mezcla de senales), el IVA esta disenado para separar fuentes independientes presentes en multiples observaciones o conjuntos de datos simultaneamente. 

### Fundamentos de IVA ### 

El IVA trabaja bajo el supuesto de que las fuentes dentro de cada conjunto de datos son independientes entre si, pero puede haber dependencias entre las fuentes de diferentes conjuntos de datos. Este enfoque tiene una ventaja significativa en escenarios donde las relaciones entre conjuntos de datos contienen informacion relevante que puede ser explotada para mejorar la separacion

Por ejemplo: 
* En el caso del procesamiento de senales EEG en diferentes canales, las senales de cada canal pueden contener informacion correlacionada que el IVA puede aprovechar
* En el caso multicanal (mezclas grabadas por multiples microfonos), el IVA puede extraer fuentes independientes explotando la redundancia espacial entre las grabaciones. 

### Formulacion Matematica ### 

1. #### Modelo de Mezcla #### 
    El IVA asume que los datos observados $\mathbf{x}_k = \mathbf{A}_k \mathbf{S}_k$ , $k = 1,2,...,K, $

    donde $K$ es el numero de conjuntos de datos. 

2. #### Objetivo: #### 

    El objetivo es encontrar las matrices de separacion $ \mathbf{W}_k$ que producen estimaciones de las fuentes independientes $\hat{\mathbf{S}}_k$: 

    $$ \mathbf{\hat{S}_k} = \mathbf{{W}_k}\mathbf{{X}_k} $$

3. #### Dependencias entre conjnutos: #### 

    Para mejorar la separacion, se modelan las dependencias entre $\mathbf{S_1},\mathbf{S_2},...,\mathbf{S_k}$ usando distribuciones adecuadas.

### Ventajas de IVA ### 

* Modela relaciones inter-conjuntos: Esto permite obtener una separacion mas precisa en aplicaciones donde existen dependencias entre diferentes conjuntos de datos.

* Mayor robustez: Es menos sensible al ruido y a problemas de permutacion en comparacion con ICA. 


### Limitaciones ### 

 * Mayor complejidad computacional: Dado que trabaja con multiples conjuntos de datos y modela dependencias, requiere mayor capacidad computacional que el ICA.

 * Configuracion mas compleja: Elegir modelos adecuados para las dependencias entre conjuntos puede ser un desafio.

 El IVA es una herramienta poderosa en escenarios donde las relaciones entre datos multivariados son escenciales para resolver problemas complejos como las limpieza de senales o la separacion de fuentes.

 ## DeepICA (Deep Learning-based Independent Component Analysis) ## 

 Es una extension de ICA que incorpora tecnicas de aprendizaje profundo para abordad limitaciones de ICA tradicional. Especificamente, DeepICA se utiliza para descomponer datos observados en componentes subyacentes que son independientes entre si, mientras aprovecha la capacidad de los modelos de aprendizaje profundo para capturar relaciones no lineales, estructuras complejas y manejar datos de alta dimensionalidad. 

 ### Fundamentos de DeepICA ### 

 ICA tradicional asume que: 

* Los datos observados son una combinacion lineal de fuentes independientes. 
* La independencia entre las fuentes puede inferirse usando propriedades estadisticas como la no-Gaussanidad. 

Sin embargo, esta tecnica tiene limitaciones en escenarios mas complejos: 
1. No puede capturar mezclas no lineales. 
2. Es sensible a ruido y depende de supuestos estrictos. 
3. Tiene problemas para escalar con datos de alta dimensionalidad o no estructurados.

DeepICA aborda estas limitaciones al integrar modelos de aprendizaje profundo dentro del marco de ICA. 

### Componentes principales de DeepICA 

1. Modelos no lineales: DeepICA utiliza redes neuronales profundas para modelar relaciones no lineales entre las observaciones y las fuentes latentes, superando la limitacion de las mezclas lineales en el ICA tradicional.

2. Funciones de costo: Para garantizar la independencia de las fuentes extraidas, DeepICA optimiza una funcion de costo basada en criterios como: 
    * Minimizacion de la dependencia estadistica entre las fuentes mediante medidas como informacion mutua o correlacion cruzada. 
    * Maximizacion de la entropia de las fuentes para fomentar la no-Gaussanidad. 
3. Capacidad para manejar datos complejos: 

* DeepICA es util para datos de alta dimensionalidad, como imagenes, series de tiempo, senales EEG o MEG. 
* Puede incorporar transformaciones mas ricas gracias a las arquitecturas profundas. 

4. Metodos de entrenamiento
    * DeepICA se entrena tipicamente utilizando algoritmos de optimizacion estocastica como Adam.
    * A menudo incluye regularizacion para prevenir sobreajuste y garantizar la estabilidad del modelo.

En ICA se expresa de la siguiente manera: 

$$ X = A \cdot S $$ 

Donde $A$ es la matriz de mezcla. En DeepICA, este modelo se expande con una red neuronal que aprende relaciones no lineales: 

$$ X = f_{deep}(S;\theta) $$ 

Aqui $f_{deep}$ representa una red neuronal com parametros $\theta$, disenada para modelar una transformacion mas compleja entre $S$ y $X$.

### Ventajas de DeepICA ### 
1. Flexibilidad no lineal: Modela mezclas mas complejas que el ICA tradicional 
2. Escalabilidad: Maneja grandes cantidades de datos gracias a las arquitecturas profundas. 
3. Generalizacion: Aprovecha el aprendizaje profundo para trabajar con datos ruidosos y no estructurados.

### Limitaciones ### 
1. Complejidad computacional: Entrenar DeepICA requiere mas recursos computacionales que el ICA tradicional. 
2. Necesidad de datos: El aprendizaje profundo generalmente requiere conjnutos de datos mas grandes para entrenar de manera efectiva.
3. Interpretabilidad: Las redes neuronales profuncdas pueden ser dificiles de interpretar, lo que puede complicar la comprension de las fuentes extraidas. 


### Relacion con ICA no lineal y aprendizaje generativo ### 

DeepICA se consiedera una extension del ICA no lineal, utilizando redes neuronales profundas para modelar las transformaciones. Ademas, se conecta estrechamente con modelos generativos, como redes autoencoder y modelos de mezclas gaussianas, para modelar y separar las fuentes. 

DeepICA es una poderosa herramienta que combina lo mejor del ICA tradicional con la flexibilidad y el poder del aprendizaje profundo, permitiendo aplicaciones en una amplia gama de dominios complejos.


## AutoEncoders ## 

Son un tipo de red neuronal especial disenada para aprender una representacion comprimida (o codificada) de los datos de entrada. Esto se logra mediante un proceso de compresion y descompresion que intenta reconstruir los datos originales lo mas fielmente posible. Los autoencoders son utiles para tareas como reduccion de dimensionalidad, eliminacion de ruido y deteccion de anomalias.

### Estructura de los autoencoders ### 

Un autoencoder consta de dos componentes principales: 

1. Codificador (Encoder): 
    * Transforma los datos de entrada de alta dimensionalidad ($\mathbf{X}$) en una representacion comprimida ($\mathbf{Z}$) llamada codigo latente. 

    * El codificador suele estar compuesto por capas densas, convolucionales o recurrentes, dependiendo del tipo de datos.

    * Funcion general: 
    $$ Z = f_{encoder}(X:\theta) $$ 

    Donde $\theta$ son los parametros del codificador. 

2. Decodificador(Decoder): 
    * Reconstruye los datos originales ($\mathbf{\hat{X}}$) a partir del codigo latente ($Z$). 
    * Su objetivo es minimizar la perdida entre los datos originales y los reconstruidos.
    * Funcion general: 
    $$\mathbf{\hat{X}} = f_{decoder}(Z;\phi) $$

    Donde $\phi$ son los parametros del decodificador.

3. Perdida de Reconstruccion 
    * Evalua que tan cerca los datos reconstruidos $\mathbf{\hat{X}}$ de los originales $X$. 
    
        Ejemplo:

        $$ \mathcal{L} = ||X -\hat{X}||^2 $$
    
    Otras metricas como la entropia cruzada tambien se pueden usar, dependiendo de los datos.

### Ventajas de los AutoEncoders ### 

1. Flexibilidad: 
    * Se pueden ajustar para datos no lineales y de alta dimensionalidad. 
2. Capacidad generativa: 
    * Modelos como los VAEs pueden generar nuevos datos realistas. 
3. Especificos al Dominio: 
    * Aprenden caracteristicas significativas especificas del conjunto de datos, lo que puede mejorar el rendimiento de tareas personalizadas. 

### Limitaciones ### 

1. Dependencia de Datos de Entrenamiento: 
    * Los autoencoders tienden a aprender representaciones especificas del conjunto de entrenamiento, lo que puede limitar su capacidad para generalizar. 

2. Reconstruccion perfecta vs Generalizacion: 
    * Un modelo sobreajustado puede reconstruir perfectamente los datos de entrenamiento, pero no generalizar a datos nuevos.

3. Diseno y Entrenamiento Complejo: 
    * Requieren una arquitectura cuidadosamente disenada y un ajuste adecuado de hiperparametros. 

Los autoencoders son herramientas versatiles que combinan la reduccion de dimensionalidad, la extraccion de caracteristicas y el modelado generativo en un solo marco poderoso.