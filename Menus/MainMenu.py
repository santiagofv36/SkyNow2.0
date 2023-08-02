from Data.Data import get_countries
from Menus.ReportMenu import report_menu
from Menus.AnalyzeMenu import analyze_menu
from Menus.FilteringMenu import filter_menu
from Menus.SearchMenu import search_menu


def main_menu():
    """
        Función que representa el menú principal de la aplicación.

        Muestra las opciones disponibles para el usuario y llama a los diferentes menús según la opción elegida.

        Retorna:
        --------
            None

        Ejemplo de uso::
            >>> main_menu()
            Menu Principal
                1.- Reportes
                2.- Analisis de Datos
                3.- Filtrado de Datos
                4.- Búsqueda y consulta de Datos
                0.- Salir
    """
    op = '-1'
    countries = get_countries()
    if countries is None:
        return
    while op != '0':
        print('''
                Menu Principal
            1.- Reportes
            2.- Analisis de Datos
            3.- Filtrado de Datos
            4.- Búsqueda y consulta de Datos
            0.- Salir
        ''')
        op = input('\t    Ingrese una opcion: ')
        if op == '1':
            report_menu(countries)
        elif op == '2':
            analyze_menu(countries)
        elif op == '3':
            filter_menu(countries)
        elif op == '4':
            search_menu(countries)
        elif op =='0':
            return
        elif not op.isnumeric():
            print('\n\t    Opción no válida (La opción ingresada no es un numero punto flotante) \n')
            continue
        elif op not in ['1','2','3','4','0']:
            print('\n\t    Opción no válida (La opción ingresada no se encuentra en el rango 0-4) \n')
            continue

