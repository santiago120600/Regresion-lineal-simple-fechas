import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt

def regresion(x,y,rango_regresion,valor=None):
    x= crearFechas(x)
    xMenosPromedio = obtenerLista(x)
    yMenosPromedio = obtenerLista(y)
    xMenosXCuadrado = obtenerCuadrado(x)
    promedio_x = sum(x) / len(x)
    promedio_y = sum(y) / len(y)
    sumaCuadradosX = sum(xMenosXCuadrado)
    multiplicacionXyY = list(np.multiply(xMenosPromedio,yMenosPromedio)) 
    sumaResultadoMultiplicacion = sum(multiplicacionXyY)
    w1 = sumaResultadoMultiplicacion / sumaCuadradosX 
    w0 = -1*w1*promedio_x + promedio_y
    if valor:
        valor = convertirFecha(valor)
        print(obtenerValorRegresion(valor,w0,w1))
    else:
        obtenerLineaRegresion(x,y,rango_regresion,w0,w1)
    
def obtenerLineaRegresion(x,y,rango_regresion,w0,w1):
    linea_regresion = []
    regresion_x = []
    for valor_x in range(1,rango_regresion):
        valor_y = w0 + w1*valor_x
        regresion_x.append(valor_x)
        linea_regresion.append(valor_y)
    graficar(x,y,regresion_x,linea_regresion)

def obtenerValorRegresion(valor,w0,w1):
    y = w0 + w1*valor
    return y

def graficar(x,y,regresion_x,regresion_y):
    plt.plot(x, y, label="Data")
    plt.plot(regresion_x, regresion_y, label="Linear Regression")
    plt.legend()
    plt.show()

def obtenerLista(lista):
    iMenosPromedio = []
    promedio = sum(lista) / len(lista)
    for i in lista:
        resta = i - promedio
        iMenosPromedio.append(resta)
    return iMenosPromedio     

def obtenerCuadrado(lista):
    iMenosICuadrado = []
    promedio = sum(lista) / len(lista)
    for i in lista:
        resultado = (i - promedio)**2
        iMenosICuadrado.append(resultado)
    return iMenosICuadrado

def crearFechas(lista_fechas):
    lista_fechas = pd.to_datetime(lista_fechas,format="%D-%M-%Y")
    lista_fechas=lista_fechas.map(dt.datetime.toordinal)
    return lista_fechas

def convertirFecha(fecha):
    x = pd.DataFrame({"Date": [fecha]})  
    x['Date'] = pd.to_datetime(x['Date'])
    x['Date']=x['Date'].map(dt.datetime.toordinal)
    fecha = x['Date'][0]
    return fecha

if __name__ == "__main__":
    df = pd.read_excel('data.xlsx')
    y_column =  df['y']
    x_column = df['x']
    regresion(x_column,y_column,'',"2021/07/05")
    regresion(x_column,y_column,10000000)



