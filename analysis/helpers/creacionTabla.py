import pandas as pd
from bs4 import BeautifulSoup

def crearTabla(dataFrame,nombreTabla):
    
    #crear un HTML desde un Datframe de python
    archivoHTML=dataFrame.to_html()
    
    #Establecemos la ruta donde vamos a guardar la tabla
    rutaArchivo=f"tables/{nombreTabla}.html"
    
    #Generamos una estructura HTML
    encabezadoHTML=''' 
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="UTF-8">
                <title>tablas</title>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
            </head>
        </html>
    '''
    
    #Adaptar los estilos de la tabla
    arbol=BeautifulSoup(archivoHTML,'html.parser')
    
    for tr in arbol.find_all('tr'):
        tr.attrs.pop('style',None)
    
    archivoHTML=str(arbol)
    
    archivoHTML=archivoHTML.replace('<table border="1" class="dataframe">','<table class="table table-striped">')
    
    with open(rutaArchivo,"w",endcoding="utf-8") as archivo:
        archivo.write(f"{encabezadoHTML}\n{archivoHTML}\n</body>\n</html>")