
from Objects.Country import Country
from Objects.State import State
from Menus.util import show_countries_list
import re

def validate_date_pattern(date : str) -> bool:
    '''
        Funcion para validar el patron de un string para una fecha

        Parametros:
        -----------
        date : str
            String a validar

        Retorno:
        --------
        bool
            True si el string cumple con el patron, False en caso contrario

        Ejemplo de uso::

            validate_date_pattern('2021/05/20')
            >>> True
    '''
    pattern = re.compile(r'^\d{4}/\d{2}/\d{2}$')
    if pattern.match(date):
        year, month, day = date.split('/')
        try:
            return validate_date(year, month, day)
        except ValueError:
            return False
    return False

def validate_date(year : str, month : str, day : str) -> bool:
    '''
        Funcion para validar una fecha

        Parametros:
        -----------
        year : str
            Año de la fecha
        month : str
            Mes de la fecha
        day : str
            Dia de la fecha

        Retorno:
        --------
        bool
            True si la fecha es valida, False en caso contrario

        Ejemplo de uso::

            validate_date('2021', '05', '20')
            >>> True

            validate_date('2021', '05', '32')
            >>> False
    '''
    
    year = int(year)
    month = int(month)
    day = int(day)
    '''
        Si el año es negativo, el mes es negativo o mayor a 12, o el dia es negativo o mayor a 31, la fecha no es valida
    '''
    if year < 0 or month < 0 or month > 12 or day < 0 or day > 31:
        return False
    '''
        Si el mes es de 30 dias y el dia es mayor a 30, la fecha no es valida
    '''
    if month in {4, 6, 9, 11} and day > 30:
        return False
    '''
        Si el mes es febrero y el dia es mayor a 29, la fecha no es valida
    '''
    if month == 2:
        if day > 29:
            return False
        '''
            Si el año no es bisiesto y el dia es 29, la fecha no es valida
        '''
        if day == 29 and year % 4 != 0:
            return False
    return True

def search_by_date(country: Country) -> None:
    '''
        Funcion para buscar mediciones por fecha

        Parametros:
        -----------
        country : Country
            Objeto Country del cual se buscaran las mediciones

        Retorno:
        --------
        None
            Imprime por pantalla los resultados del filtrado

        Ejemplo de uso::

            search_by_date(country)
            >>>
                'Temperatura'   'Humedad'  'Velocidad del viento'        'Fecha'
                        20.0        50.0                    10.0     2021/05/20
                        22.5        45.0                    15.0     2021/05/20
    '''

    # Se pide la fecha al usuario y se valida
    date = input('\t    Ingrese la fecha (YYYY/MM/DD): ')
    '''
        Si la fecha no cumple el patron, se muestra un mensaje de error
    '''
    if not validate_date_pattern(date):
        print('\n\t    Fecha invalida\n')
        return
    '''
        Se guardan las mediciones en una variable auxiliar para no perderlas
    '''
    measurements = country.measurements()
    '''
        Se filtran las mediciones por la fecha dada por el usuario
    '''
    measurements_copy = [ measurement for measurement in country.measurements() if measurement.date() == date]
    
    '''
        Si no se encontraron resultados, se muestra un mensaje indicandolo
    '''

    if not measurements_copy:
        print('\n\t    No se encontraron resultados\n')
        return
    '''
        Se asigna al objeto country las mediciones filtradas y se imprimen
    '''
    country.set_measurements(measurements_copy)
    country.print_measurements()

    '''
        Se restauran las mediciones originales
    '''
    country.set_measurements(measurements)
    input('\n\t    Presione enter para continuar')

def search_by_climate_variables(country : Country, variable : str) -> None:
    '''
        Funcion para buscar mediciones por variables climaticas

        Parametros:
        -----------

        country : Country
            Objeto Country del cual se buscaran las mediciones
        variable : str
            Variable climatica por la cual se filtraran las mediciones 
            Posibles valores: temperature, humidity, wind_speed
        
        Retorno:
        --------

        None
            Imprime por pantalla los resultados del filtrado

        Ejemplo de uso::

            search_by_climate_variables(country, 'temperature')
            >>>
                'Temperatura'   'Humedad'  'Velocidad del viento'        'Fecha'
                        20.0        50.0                    10.0     2021/05/20
                        20.0        60.0                    15.0     2021/05/21
    '''
    
    # Se crea una variable para guardar el nombre de la variable climatica en español
    variable_es = 'Temperatura' if variable == 'temperature' else 'Humedad' if variable == 'humidity' else 'Velocidad del Viento'
    try:
        '''
            Se pide el valor de la variable climatica y se valida
        '''
        value = float(input(f'\t    Ingrese el valor de la {variable_es}: '))
        '''
            Se guardan las mediciones en una variable auxiliar para no perderlas
        '''
        measurements = country.measurements()
        '''
            Se filtran las mediciones por la variable climatica y el valor dado por el usuario
        '''
        measurements_copy = [ measurement for measurement in country.measurements() if measurement.get(variable) == value]
        if not measurements_copy:
            print('\n\t    No se encontraron resultados\n')
            return
        country.set_measurements(measurements_copy)
        print(f'\t    Pais: {country.name()} \n\t    Variable: {variable_es} Valor: {value}')
        country.print_measurements()
        country.set_measurements(measurements)
        input('\n\t    Presione enter para continuar')
    except ValueError:
        '''
            Si el valor no es un numero, se muestra un mensaje de error
        '''
        print('\n\t    Valor invalido\n')
        return

def binary_search_state(states : list[State], state_name : str) -> int:
    '''
        Funcion para buscar un estado en una lista de estados

        Parametros:
        -----------

        states : list[State]
            Lista de objetos State
        state_name : str
            Nombre del estado a buscar

        Retorno:
        --------

        int
            Indice del estado en la lista de estados, -1 si no se encontro

        Ejemplo de uso::

            binary_search_state(states, 'Buenos Aires')
            >>>
                0

            binary_search_state(states, 'Buenos Aire')
            >>>
                -1
    '''
    '''
        Se inicializan las variables para el algoritmo de busqueda binaria
    '''
    left = 0
    right = len(states) - 1
    middle = (left + right) // 2
    '''
        Se busca el estado en la lista de estados
    '''
    while left <= right:
        if states[middle].name().lower() == state_name.lower():
            return middle
        elif states[middle].name().lower() < state_name.lower():
            left = middle + 1
        else:
            right = middle - 1
        middle = (left + right) // 2

    return -1

def search_by_state(states : list[State]) -> None:
    """
    Función para buscar información de un estado o provincia en una lista de estados.

    Parametros:
    -----------
        states (list[State]): Lista de objetos State que representa los estados o provincias disponibles.

    Retorno:
    --------
        None: Imprime por pantalla los resultados de la búsqueda y muestra un mensaje de error si el estado no es encontrado.

    Ejemplo de uso::

        search_by_state(states)
        >>>
                  Nombre     Capital   Población    Superficie
            Buenos Aires    La Plata    15625084        307571  
    """
    state_name = input('\t    Ingrese el nombre del estado: ')
    '''
        Se busca el estado en la lista de estados
    '''
    state_index = binary_search_state(states, state_name)
    '''
        Si no se encontro el estado, se muestra un mensaje de error
    '''
    if state_index == -1:
        print('\n\t    Estado no encontrado\n')
        return
    
    state = states[state_index]

    State.print([state])
    input('\n\t    Presione enter para continuar')

def search_menu(countries: list[Country]) -> None:
    '''
        Menu para buscar datos

        Parametros:
        -----------

        countries : list[Country]
            Lista de objetos Country

        Retorno:
        --------
        None
            Imprime por pantalla las opciones del menu

        Ejemplo de uso::

            >>> search_menu(countries)
            Busqueda y consulta de Datos

                1.- Busqueda por fecha
                2.- Busqueda por variables climaticas
                3.- Busqueda de información de un estado
                0.- Regresar
    '''
    
    op = '-1'
    while op != '0':
        print('\t    Busqueda y consulta de Datos\n')
        print('\t    1.- Busqueda por fecha')
        print('\t    2.- Busqueda por variables climaticas')
        print('\t    3.- Busqueda de información de un estado')
        print('\t    0.- Regresar')
        op = input('\t    Ingrese una opcion: ')
        if op == '0':
            return
        elif not op.isnumeric():
            print('\n\t    Opcion invalida (La opción ingresada no es un numero punto flotante) \n')
            continue
        elif op not in {'1', '2', '3'}:
            print('\n\t    Opcion invalida (La opción ingresada no se encuentra dentro del rango (0-3)) \n')
            continue
        op2 = '-1'
        while op2 != '0':
            show_countries_list(countries)
            print('''\t    0.- Regresar''')
            op2 = input('''\t    Ingrese una opcion: ''')
            try:
                if op2 == '0':
                    break
                country = countries[int(op2) - 1]
                print('\t    Pais Seleccionado: ', country.name())
                if op == '1':
                    search_by_date(country)
                elif op == '2':
                    op2 = '-1'
                    while op2 != '0':
                        print('\t    1.- Temperatura')
                        print('\t    2.- Humedad')
                        print('\t    3.- Velocidad Del Viento')
                        print('\t    0.- Regresar')
                        op2 = input('\t    Ingrese una opcion: ')
                        if op2 == '0':
                            break
                        elif op2 in {'1', '2', '3'}:
                            search_by_climate_variables(country, 'temperature' if op2 == '1' else 'humidity' if op2 == '2' else 'wind_speed')
                        elif not op2.isnumeric():
                            print('\n\t    Opcion invalida (La opción ingresada no es un numero punto flotante) \n')
                            continue
                        elif op2 not in {'0','1', '2', '3'}:
                            print('\n\t    Opcion invalida (La opción ingresada no se encuentra dentro del rango (0-3)) \n')
                            continue
                elif op == '3':
                    search_by_state(country.states())
            except ValueError:
                print('\n\t    Opcion invalida (La opción ingresada no es un numero punto flotante) \n')
                continue
            except IndexError:
                print('\n\t    Opcion invalida (La opción no se encuentra dentro del rango (0-10) ) \n')
                continue