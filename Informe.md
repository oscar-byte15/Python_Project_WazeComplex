# **Informe** 
## **Introducción**
Las aplicaciones de mapas nos brindan, no solo direcciones detalladas hacia un destino determinado, pero también, información adicional sobre las características de las rutas, tales como el tiempo que nos tomará viajar por ellas y  el nivel de tráfico. Asimismo, nos muestran alternativas a la ruta principal, para que el usuario pueda elegir la que le sea más conveniente. 

Muchas de las funcionalidades principales que estas aplicaciones tienen pueden ser simuladas con diferentes estructuras de datos y algoritmos de búsqueda de grafos. Por esta razón, en el presente proyecto, se elaborará una mapa de calles similar a "Waze", donde podremos hallar diferentes rutas entre 2 puntos, tomando en cuenta factores de tiempo y tráfico. Además, se pondrá enfásis al diseño de algoritmos para hallar los factores y las rutas más optimas. 

## **Objetivos**
- Consolidar los conocimientos adquiridos en el curso de Complejidad Algorítmica en un proyecto integrador.
- Poner en práctica la capacidad de resolución de problemas y organización de tiempo para el proyecto.
- Encontrar una ruta óptima entre 2 puntos determinados.

## **Elaboración del programa**

### **Registro de calles**
Nosotros registramos el nombre de cada calle y el nombre de las calles con las que cada una se interseca. En código, a cada calle le asignamos un identificador numérico y lo guardamos en un diccionario al que llamamos streetsDictionary, donde las keys son los nombres de las calles y los values son los identificadores.

### **Vértices del grafo**
En el programa, cada calle del grafo está identificado por un número. La Avenida Los Olivos, por ejemplo, se representa con el número 62. Asimismo, la Avenida Canta Callao está representada por el número 30. De esta forma, los vértices del grafo representan una intersección entre 2 calles. En la imagen, por ejemplo, se puede observar el vértice (62, 30).

![alt text](imgs/interseccion.png)

### **Aristas del grafo**
En el grafo, una arista representa la unión de 2 intersecciones de calles. En el siguiente ejemplo, el vértice (Avenida Alisos – Las Lilas) está unido con (Las Lilas – Los Laureles) por medio de una arista.

<img src="imgs/aristas.png" width="300"/>

Además, a cada arista, se le agrega un valor aleatorio, generado por Perlin Noise. Este valor, posteriormente, nos ayudará a asignarle un peso a cada arista del grafo. En código, se ve así: 

<img src="imgs/graphRandValues.png" width="500"/>

### **Algoritmo de búsqueda**
Para hallar los caminos más cortos de 1 punto hacia otro, utilicé Dijkstra. Este algoritmo encuentra todos los caminos desde un vértice hasta todos los demás. Por esta razón, decidí tomar todos los vecinos de mi nodo de inicio e implementar el algoritmo de búsqueda por cada nodo vecino hacia el mismo destino. De esta forma, tendría podría obtener diversos caminos. Además el valor de retorno serían 2 arreglos: 1 de los diferentes caminos posibles y, el otro, de costos.

## **Conclusiones**
- Las funcionalidades de las aplicaciones de mapas nos permiten analizar diversas formas sobre cómo podemos implementar un algoritmo de la manera más eficaz.
- El presente proyecto me ha permitido evaluar la manera cómo podría representar de datos y la manera cómo registrarlos para poder trabajar con ellos lo más fácil posible en el código.
- Los algoritmos de búsqueda y los grafos nos permiten similar caminos desde un punto determinado hacia otros. En este proyecto, se evaluó cuál el mejor algoritmo para nuestro código, pero que también nos devuelva los resultados esperados.
