# Investigación y Análisis de métodos de preprocesamiento

## Filtro Notch

El filtro Notch es uno de los más relevantes en cuanto a señales EEG debido a que es el que quita uno de los ruidos más relevantes, debido a que el instrumento de medición para este tipo de senales es un encefalograma, el cual mide la actividad cerebral como voltaje existe una alta interferecnia de la red eléctrica, este filtro busca quitar esa interferencia en una frecuencia de 50/60hz, como se menciona en [87] “El filtro Notch se utiliza para eliminar el ruido de la red eléctrica en señales EEG, lo que resulta en datos más limpios y fáciles de interpretar al enfocarse en la interferencia de 50/60 Hz.”

El filtro notch funciona al rechazar un determinado intervalo de frecuencias en este caso rechaza el rango 50-60Hz, y puede ser expresada de la siguiente manera: 

$$
H(z) = \frac{1 - 2\cos(\omega_0)z^{-1} + z^{-2}}{1 + \alpha z^{-1} + z^{-2}}
$$


