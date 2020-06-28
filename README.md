# Tarea 3. Modelos Probabilisticos de Señales y Sistemas
# Grupo 2
# Estudiante: Rubén Venegas Zúñiga - Carné: B78278
# Profesor: Fabián Abarca Calderón


## Parte 1: 

Con los datos de **xy.csv** se obtiene la **función de densidad marginal de X**, y se genera 
la siguiente gráfica de esta función:

![alt text](fX.png)

Basado en la gráfica anterior se determina que los datos se pueden ajustar a un modelo 
probabilístico de densidad Gaussiana. 

Los siguientes son los parámetros obtenidos para el ajuste del modelo de *f<sub>X</sub>(x)*:

**&mu;<sub>x</sub>:  9.904843666257179**

**&sigma;<sub>x</sub>:  3.2994430045118897**

Obteniéndose entonces la siguiente función para el modelo (Gaussiana):

![alt text](eq1.svg)

Con los datos de **xy.csv** se obtiene la **función de densidad marginal de Y**, y se genera la 
siguiente gráfica de esta función:

![alt text](fY.png)

Basado en la gráfica anterior se determina que los datos se pueden ajustar a un modelo 
probabilístico de densidad Gaussiana. 

Los siguientes son los parámetros obtenidos para el ajuste del modelo para *f<sub>Y</sub>(y)*:

**&mu;<sub>y</sub>:  15.079460968463788**

**&sigma;<sub>y</sub>: 6.026937738126949**

Obteniéndose entonces la siguiente función para el modelo (Gaussiana):

![alt text](eq2.svg)

## Parte 2:
Si se asume independencia de X y Y entonces:

![alt text](eq3.svg)

Sustituyendo por los modelos para las funciones de densidad marginales de X y Y encontrados en la Parte 1 se tiene:

![alt text](eq4.svg)

## Parte 3:
Se obtuvieron los siguientes resultados:

La **correlación** se obtuvo a partir de la ecuación: *R<sub>XY</sub> = E[XY]*, de donde se obtuvo el 
siguiente resultado: 

**Correlación:  149.54281000000012**

Del valor obtenido se comprueba que no hay correlación entre las variables *X* y *Y*, pues si
se toman los valores de la media para ambas funciones del modelo encontrado para cada funcion
de densidad marginal, que serían *&mu;<sub>x</sub>* y *&mu;<sub>y</sub>*, se comprueba que
*E[XY] = E[X]E[Y] = &mu;<sub>x</sub>&mu;<sub>y</sub> = (15.070)(9.905) = 149.268*, valor que es
muy cercano al obtenido por la correlación por lo cual se comprueba que no hay correlación entre
las variables.

La **covarianza** se obtuvo a partir de la ecuación: *C<sub>XY</sub> = E[(X-X&#772;)(Y-Y&#772;)]*,  para lo cual se utilizaron los 
valores de la media (*&mu;<sub>x</sub>* y *&mu;<sub>y</sub>*)  obtenidos de los **modelos de la Parte 1**, de donde se obtuvo el 
siguiente resultado: 

**Covarianza:  0.06669156297337238**

Del valor de covarianza obtenido se puede decir que este es muy cercano a cero, lo cual evidencia que 
hay una independencia o no estan relacionadas las variables *X* y *Y*.

El **coeficiente** de Pearson se obtuvo a partir de la ecuación: *&rho;<sub>XY</sub> = E[((X-X&#772;)/&sigma;<sub>x</sub>)(Y-Y&#772;)/&sigma;<sub>y</sub>))​]*, para lo cual se utilizaron los valores de media (*&mu;<sub>x</sub>* y *&mu;<sub>y</sub>*) y desviación estandar (*&sigma;<sub>x</sub>* y *&sigma;<sub>y</sub>*) obtenidos de los **modelos de la Parte 1**, de donde se obtuvo el siguiente resultado: 


**Coef. Pearson:  0.003353772196327786**

En este resultado también se puede comprobar la independencia entre las variables *X* y *Y*, pues un coeficiente de
Pearson cercano a cero evidencia esto.

## Parte 4:
Las gráficas obtenidas para los modelos que ajustan los datos de las funciones de densidad 
para marginal de X y Y son las siguientes, respectivamente:

![alt text](modelo_fX.png)

![alt text](modelo_fY.png)

La **función de densidad conjunta (3D)** obtenida a partir del modelo de la Parte 2 es:

![alt text](3d.png)