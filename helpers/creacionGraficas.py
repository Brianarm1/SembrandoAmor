import matplotlib.pyplot as plt


def generarGrafica(dataFrame):
    #Agrupar datos del dataFrame segun el analisis que quiera graficar
    #Estadisticas de siembras por ciudad y su promedio al año
    siembrasPromedioPorCiudad=dataFrame.groupby("Vereda")["Hectareas"].mean()
    print(siembrasPromedioPorCiudad)

    #0. Generando lista de colores
    colores=["#FD8E00","#FE2828","#00E2FD"]

    #1. Generar una figura
    plt.figure(figsize=(10,10))


    #2. Genero la grafica que deseo
    plt.bar(siembrasPromedioPorCiudad.index, siembrasPromedioPorCiudad.values, color=colores)

    #3. Muestro la grafica
    #plt.show()

    #4. Agrego titulo a la grafica
    plt.title("Las veredas con las mayores hectareas")

    #5 etiqueta o nombre del eje x
    plt.xlabel("Veredas")

    #6 Etiqueta o nombre del eje y
    plt.ylabel("Hectareas")

    #7. Activar el grid
    plt.grid(True)

    #8 Rotar los labels
    plt.xticks(rotation=45)

    #9. Guardando la grafica
    plt.savefig("./graphs/veredasConMasHectareas.png")