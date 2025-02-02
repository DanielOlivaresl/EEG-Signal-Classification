# Component Methods # 

This folder corresponds to the component methods for preprocessing signals, Here we will link to each of the methods corresponding documentation, where we will have each of the methods corresponding definition from a mathematical standpoint, the code corresponding to the implementation and the analysis made of why se chose each of the methods. 

Starting with: 

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
