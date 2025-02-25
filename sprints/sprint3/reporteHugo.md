# Investigación y Análisis de métodos de preprocesamiento

## Filtro Notch

El filtro Notch es uno de los más relevantes en cuanto a señales EEG debido a que es el que quita uno de los ruidos más relevantes, debido a que el instrumento de medición para este tipo de senales es un encefalograma, el cual mide la actividad cerebral como voltaje existe una alta interferecnia de la red eléctrica, este filtro busca quitar esa interferencia en una frecuencia de 50/60hz, como se menciona en [87] “El filtro Notch se utiliza para eliminar el ruido de la red eléctrica en señales EEG, lo que resulta en datos más limpios y fáciles de interpretar al enfocarse en la interferencia de 50/60 Hz.”

El filtro notch funciona al rechazar un determinado intervalo de frecuencias en este caso rechaza el rango 50-60Hz, y puede ser expresada de la siguiente manera: 

$$
H(z) = \frac{1 - 2\cos(\omega_0)z^{-1} + z^{-2}}{1 + \alpha z^{-1} + z^{-2}}
$$

donde:	
$ω_0$: Frecuencia a eliminar en radianes.
$α$: Ancho de banda de la frecuencia a eliminar.


## Filtro Paso Bandas 

El filtro paso bandas es muy relevante en las senales EEG, dado que este tipo de senales se distribuyen en diferentes bandas de frecuencia dependiendo de ciertos estados cognitivos, dado esto el filtro se aplica para aislar una banda de interés como se menciona en [88] "Los filtros paso banda se utilizan para aislar frecuencias específicas de las señales EEG que corresponden a diferentes bandas relacionadas con estados cognitivos específicos. Esto permite un análisis más detallado de los procesos cerebrales asociados con dichas frecuencias."


El filtro paso bandas combina características de un filtro paso alto y paso bajo, donde se rechazan las frecuencias mayores y menores que ciertos intervalos, y matemáticamente puede ser expresada como: 

$$
H(z)=(1-2 cos⁡(ω_0 ) z^(-1)+z^(-2))/(1+αz^(-1)+z^(-2) )
$$

donde:	
$ω_0$: Frecuencia a eliminar en radianes.
$α$: Ancho de banda de la frecuencia a eliminar.

## Filtro Paso Bandas 
El filtro paso bandas es muy relevante en las senales EEG, dado que este tipo de senales se distribuyen en diferentes bandas de frecuencia dependiendo de ciertos estados cognitivos, dado esto el filtro se aplica para aislar una banda de interés como se menciona en [88] "Los filtros paso banda se utilizan para aislar frecuencias específicas de las señales EEG que corresponden a diferentes bandas relacionadas con estados cognitivos específicos. Esto permite un análisis más detallado de los procesos cerebrales asociados con dichas frecuencias."
El filtro paso bandas combina características de un filtro paso alto y paso bajo, donde se rechazan las frecuencias mayores y menores que ciertos intervalos, y matemáticamente puede ser expresada como: 

$$
H(s)=(ω_c/Q s)/(s^2+ω_c/Q s+ω_c^2 )
$$

donde:	
$s=jω$: Variable compleja en el dominio de Laplace.
$ω_c=2πfc$: Frecuencia angular central.
$Q$: Factor de calidad. 

