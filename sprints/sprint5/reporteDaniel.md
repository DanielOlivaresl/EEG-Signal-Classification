# Reporte Sprint 5 # 

### Para este sprint la actividad designada, es la creacion e implementacion de los metodos para componentes ###

En el sprint pasado, se hizo un analisis de que metodos eran los mas viables, para posteriormente ser implementados, en este sprint seran implementados, destacando de un punto de vista mas tecnico los aspectos de implementacion de cada uno de los metodos. 

Los metodos que se realizaran son los siguientes: 


- ICA (Independent Component Analysis) 
- PCA (Principal Component Analysis)
- NMF (Non-Negative Matrix Factorization)
- BSS (Blind Source Separation)
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



    
    import numpy as np
    
    def g(y):
        """Función de contraste (no-linealidad)"""
        return np.tanh(y)
    
    def g_derivative(y):
        """Derivada de la función de contraste"""
        return 1 - np.tanh(y) ** 2
    
    def fastICA(X, n_components, max_iter=200, tol=1e-6):
        """Implementación del algoritmo FastICA"""
        
        # 1. Centrar los datos
        X -= np.mean(X, axis=0)
    
        # 2. Blanqueo usando PCA
        cov = np.cov(X, rowvar=False)
        eigvals, eigvecs = np.linalg.eigh(cov)
        D = np.diag(1.0 / np.sqrt(eigvals))
        X_white = X @ eigvecs @ D @ eigvecs.T
        
        # 3. Inicializar matriz de pesos W aleatoriamente
        n_samples, n_features = X.shape
        W = np.random.rand(n_components, n_features)
    
        for _ in range(max_iter):
            W_old = W.copy()
    
            # 4. Aplicar función de contraste y actualizar pesos
            WX = X_white @ W.T
            W_new = (X_white.T @ g(WX)) / n_samples - np.mean(g_derivative(WX), axis=0) * W
            
            # 5. Ortogonalizar con Gram-Schmidt
            W_new = np.linalg.qr(W_new.T)[0].T  # QR decomposition
    
            # 6. Verificar convergencia
            if np.max(np.abs(np.abs(np.diag(W_new @ W_old.T)) - 1)) < tol:
                break
    
            W = W_new
    
        # 7. Calcular señales separadas
        S = X_white @ W.T
        return S, W
    
    # Prueba con datos mixtos
    np.random.seed(42)
    n_samples = 2000
    time = np.linspace(0, 8, n_samples)
    s1 = np.sin(2 * time)  # Señal senoidal
    s2 = np.sign(np.sin(3 * time))  # Señal cuadrada
    S_true = np.c_[s1, s2] + 0.1 * np.random.normal(size=(n_samples, 2))
    
    # Mezclamos señales
    A = np.array([[1, 0.5], [0.5, 1]])  # Matriz de mezcla
    X_mixed = S_true @ A.T  # Señales mezcladas
    
    # Aplicamos FastICA
    S_recovered, W_estimated = fastICA(X_mixed, n_components=2)
    
    # Graficamos resultados
    import matplotlib.pyplot as plt
    plt.figure(figsize=(8, 4))
    plt.plot(time, S_recovered[:, 0], label="Señal 1 Recuperada")
    plt.plot(time, S_recovered[:, 1], label="Señal 2 Recuperada")
    plt.legend()
    plt.title("Señales separadas con FastICA")
    plt.show()
    


 


