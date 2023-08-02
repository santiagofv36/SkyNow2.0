

'''
    Modulo para generar graficas
'''

import matplotlib.pyplot as plt


def bar_chart(x : list, y : list, title : str, x_label : str, y_label : str) -> None:
    '''
        Genera una grafica de barras

        Parámetros:
        -----------

            x : list
                Lista de valores para el eje x
            y : list
                Lista de valores para el eje y
            title : str
                Titulo de la grafica
            x_label : str
                Etiqueta del eje x
            y_label : str
                Etiqueta del eje y

        Retorna:
        --------

            None

        Ejemplo de uso::

            bar_chart([1,2,3,4], ['v1','v2','v3'], 'Titulo', 'Valor en x', 'Valor en y')

    '''
    
    plt.bar(x, y)
    plt.title(title)
    plt.xticks(rotation=90)
    plt.xticks(fontsize=8)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()