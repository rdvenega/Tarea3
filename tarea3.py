# Tarea 3 Modelos Probabilisticos de Señales y Sistemas
# Grupo 2
# Estudiante: Rubén Venegas Zúñiga - Carné: B78278
# Profesor: Fabián Abarca Calderón

import csv, operator #Operador que permite usar archivos .csv
import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from mpl_toolkits.mplot3d import Axes3D

def gaussiana(x,mu,sigma):
    return 1/(np.sqrt(2*np.pi*sigma**2))*np.exp(-(x-mu)**2/(2*sigma**2))

def correlacion(x_i,y_i,matriz):
    corr = 0
    for n in range(len(matriz)):
        y_k = y_i
        for k in range(len(matriz[0])):
            corr = corr + float(matriz[n][k])*x_i*y_k
            y_k=y_k+1
        x_i=x_i+1
    return corr

def covarianza(x_i,y_i,media_x,media_y, matriz):
    corr = 0
    for n in range(len(matriz)):
        y_k = y_i
        for k in range(len(matriz[0])):
            corr = corr + float(matriz[n][k])*(x_i - media_x)*(y_k-media_y)
            y_k=y_k+1
        x_i=x_i+1
    return corr

def coef_Pearson(x_i,y_i,media_x,media_y, sigma_x, sigma_y, matriz):
    corr = 0
    for n in range(len(matriz)):
        y_k = y_i
        for k in range(len(matriz[0])):
            corr = corr + float(matriz[n][k])*((x_i - media_x)/sigma_x)*((y_k-media_y)/sigma_y)
            y_k=y_k+1
        x_i=x_i+1
    return corr

###### Obtencion de datos csv ##############
datos =[]
with open('xy.csv') as csvarchivo: #Se abre el archivo lote.csv
    entrada = csv.reader(csvarchivo) #Se guarda en entrada los datos de csv
    for inp in entrada: #Se recorre cada linea de entrada
        datos.append(inp)

########### PARTE 1 ########################
print("\n########### PARTE 1 ########################")
datos_f = []
for n in range(1,len(datos)):
    datos_f.append(datos[n][1:])

matriz = np.array(datos_f, dtype='f')

#################### fX ###############################
fx = np.sum(matriz, axis =1)
x = np.linspace(5,15,11)

param1,_ = curve_fit(gaussiana, x, fx)

print("\nfX: ", fx)
print('\nParametros modelo (Gaussiana) probabilistico para fX:')
print('mu: ', param1[0])
print('sigma: ', param1[1])
print("modelo_fX = 0.121*exp(-(x-9.905)^2/(21.767))")
plt.plot(x,fx)
plt.grid(True)
plt.title('Funcion de densidad marginal de $f_x(x)$')
plt.ylabel('$f_X(x)$')
plt.xlabel('$x$')
plt.savefig('fX.png')
plt.clf()

#################### fY ################################

fy = np.sum(matriz, axis =0)
y = np.linspace(5,25,21)

param2,_ = curve_fit(gaussiana, y, fy)

print("\nfY: ", fy)
print('\nParametros modelo (Gaussiana) probabilistico para fY:')
print('mu: ', param2[0])
print('sigma: ', param2[1])
print("modelo_fY = 0.066*exp(-(y-15.079)^2/(72.647))")

plt.plot(y, fy)
plt.grid(True)
plt.title('Funcion de densidad marginal de $f_y(y)$')
plt.ylabel('$f_Y(x)$')
plt.xlabel('$y$')
plt.savefig('fY.png')
plt.clf()

############  PARTE 2  ############################
print("\n############  PARTE 2  ############################")

print("\nf_XY = modelo_fX * modelo_fY. Sustituyendo:")
print("f_XY = 0.008*exp(-(x-9.905)^2/(21.767))*exp(-(y-15.079)^2/(72.647))")

############  PARTE 3  ############################
print("\n############  PARTE 3  ############################")
print("\nCorrelacion: ", correlacion(5,5,datos_f))
print("Covarianza: ", covarianza(5,5,param1[0], param2[0],datos_f))
print("Coef. Pearson: ", coef_Pearson(5,5,param1[0], param2[0],param1[1], param2[1],datos_f))
print('\n')


############# PARTE 4 ##############################
print("\n############# PARTE 4 ##############################")

####### Ajuste fX ##########

x = np.linspace(5,15, 100)    
ajuste_fx = []
for n in range(len(x)):
    ajuste_fx.append(gaussiana(x[n], param1[0], param1[1]))

plt.plot(x, ajuste_fx, color = 'magenta')
plt.grid(True)
plt.title('Modelo de distribucion Gaussiana para funcion de densidad marginal $f_x(x)$')
plt.ylabel('$f_X(x)$')
plt.xlabel('$x$')
plt.savefig('modelo_fX.png')
plt.clf()

####### Ajuste fY ##########
y = np.linspace(5,25, 100)
ajuste_fy = []
for n in range(len(y)):
    ajuste_fy.append(gaussiana(y[n], param2[0], param2[1]))

plt.plot(y, ajuste_fy, color = 'green')
plt.grid(True)
plt.title('Modelo de distribucion Gaussiana para funcion de densidad marginal $f_y(y)$')
plt.ylabel('$f_Y(y)$')
plt.xlabel('$y$')
plt.savefig('modelo_fY.png')
plt.clf()

###### Distribucion Conjunta 3D ####################
x = np.linspace(5,15, 100)
y = np.linspace(5,25, 100)

X, Y = np.meshgrid(x, y)
Z = gaussiana(X,param1[0],param1[1])*gaussiana(Y,param2[0],param2[1])
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 200, cmap='viridis')
ax.set_title('Función de densidad conjunta')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('$f_{x,y}(x,y)$')
plt.savefig('3d.png')
