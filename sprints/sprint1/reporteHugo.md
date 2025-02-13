# Estructuración del módulo de preprocesamiento
A partir de las investigaciones hechas. Gran parte de los autores menciona que la etapa de procesamiento tiene una enorme contribución para que los resultados finales del modelo sean satisfactorios. Existen muchas técnicas para el filtrado de las señales EEG, por lo que se vuelve necesario hacer pruebas pertinentes para los distintos tipos de filtrado encontrados en el estado del arte.

En esta sección se desarrolla la arquitectura general propuesta para poder llevaracabo distintas pruebas con distintos métodos de preprocesamiento. Para ello, se propone el siguiente diagrama de Actividades, proveniente del caso de uso “Usuario filtra las Señales”.
![Diagrama de actividades (1)](https://github.com/user-attachments/assets/ec1a0209-ad87-4e69-9e92-9f156896985a)

Como se puede observar, el proceso del procesamiento constará de distintas etapas, en donde se busca obtener una mejora significativa en la calidad de la señal. Los 3 primeros pasos, constan de darle el mismo formato a todas las señales entrantes al modelo. Para ello, se normaliza la señal, posteriormente, en función de la taza de muestras que se elija, se genera un conjunto de bloques muestrales, los cuales, a su vez, formaran las ventanas con las que el modelo se entrenará o hará predicciones. 

Posterior a esto, se comienza con la etapa de filtrado, en donde el usuario tendrá la opción de elegir “recursivamente” la cantidad de filtros a usar. De cada una de las combinaciones usadas, se obtiene una métrica de rendimiento en función de cual limpia es la señal. A partir de esto, se puede elegir aplicar otros filtros u obtener la señal filtrada y los filtros elegidos para obtener dicha señal.



