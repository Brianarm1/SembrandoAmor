import pandas as pd
from helpers.creacionTabla import crearTabla
from helpers.creacionGraficas import generarGrafica


def analizarArboles():
    #2. Sin importar la fuente (sql, xls, JSON, csv...)
    #crear una tabla tabulada que se llama DATAFRAME

    tabla=pd.read_csv('./data/Siembras.csv')

    #print(tabla)
    crearTabla(tabla,"siembras")

    #3. Aplico filtros para limpiar o seleccionar datos

    #print(tabla.head(20)) #primeros N registros
    #print(tabla.tail())

    #filtroPanes=tabla.query(" (Producto=='Pan') and (Origen=='India') ")

    #filtroPrecios=tabla.query(" (PrecioporUnidad<50)")

    #crearTabla(filtroPrecios,"filtroPrecios")


    filtroArbolesSembradosEnMedellin=tabla.query("(Ciudad=='Medellín') and (Arboles>200)")
    crearTabla(filtroArbolesSembradosEnMedellin,"ArbolesSembradosEnMedellin")


    filtroVeredaPasoReal=tabla.query("(Vereda=='Paso Real')")
    filtroVeredaTonuscoArriba=tabla.query("(Vereda=='Tonusco Arriba')")

    crearTabla(filtroVeredaPasoReal,"FiltroVeredaPasoReal")
    crearTabla(filtroVeredaTonuscoArriba,"FiltroVeredaTonuscoArriba")


    filtroElBagre=tabla.query("(Vereda=='El Bagre') and (Arboles>60)")
    crearTabla(filtroElBagre,"FiltroElBagre")


    filtroLasCruces=tabla.query("(Vereda=='Las Cruces')")
    crearTabla(filtroLasCruces,"FiltroLasCruces")


    filtroMinaVieja=tabla.query("(Vereda=='Mina Vieja')")
    crearTabla(filtroMinaVieja,"FiltroMinaVieja")



    #Graficas de los dataFrame

    filtroSimebra=tabla.query(" (Arboles>50000) ")
    generarGrafica(filtroSimebra)


    filtroVereda=tabla.query("(Arboles>45000) ")
    generarGrafica(filtroVereda)

    filtroVeredaConMayoresHectareas=tabla.query("(Hectareas>80) ")
    generarGrafica(filtroVeredaConMayoresHectareas)


    
