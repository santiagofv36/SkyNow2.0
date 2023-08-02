
from Objects.Country import Country

from Objects.State import State

from Objects.Measurement import Measurement

from Menus.util import show_countries_list

from Utils.Chart import bar_chart

def mode(data : list[int | float]) -> int | float:
    '''
        Funcion para calcular la moda de una lista de datos

        Parametros:
        -----------
            data : list[int | float]
                Lista de datos a analizar
        Retorna:
        --------

            int | float

        Ejemplo de uso::

            mode([1, 2, 3, 4, 5, 6, 7, 8, 9, 7])

            >>> 7

    '''
    # Se crea un diccionario vacion para almacenar las frecuencias
    element_freq = {}

    # Se cuenta la cantidad de ocurrencias de cada elemento en la lista

    for element in data:
        if element in element_freq:
            element_freq[element] += 1
        else:
            element_freq[element] = 1

    # Se obtiene el maximo de la frecuencia en el diccionario

    max_freq = max(element_freq.values())

    # Se encuentra la(s) moda(s) mediante la coleccion de los elementos con la mayor frecuencia y se retorna

    return [element for element, freq in element_freq.items() if freq == max_freq]

def analyze_area_population(list : list[Country]) -> None:
    '''
        Funcion para analizar la superficie y el area de los paises de una lista

        Parametros:
        -----------
            list : list[Country]
                Lista de paises a analizar

        Retorna:
        --------
            None

        Ejemplo de uso::

            analyze_area_population(countries)
    '''
    max_population = max(list, key=lambda country: country.population())
    min_population = min(list, key=lambda country : country.population())
    max_area = max(list, key=lambda country: country.area())
    min_area = min(list, key=lambda country: country.area())
    avg_population = sum(country.population() for country in list)/len(list)
    avg_area = sum(country.area() for country in list)/len(list)
    
    print('')
    print(f'\t    Pais con mayor Poblacion   : {max_population.name()} con {max_population.population()} habitantes')
    print(f'\t    Pais con menor poblacion   : {min_population.name()} con {min_population.population()} habitantes')
    print(f'\t    Pais con mayor superficie  : {max_area.name()} con {max_area.area()} Km^2')
    print(f'\t    Pais con menor superficie  : {min_area.name()} con {min_area.area()} Km^2')
    print(f'\t    Promedio de las poblaciones: {avg_population:.2f} habitantes')
    print(f'\t    Promedio de Superficie     : {avg_area:.2f} Km^2')
    input('\t    Presione enter para continuar')

def analyze_area_population_states(list : list[State], country) -> None:
    '''
        Funcion para analizar la superficie y el area de los estados de un pais

        Parametros:
        -----------
            list : list[State]
                Lista de estados a analizar
            country : Country
                Pais al que pertenecen los estados

        Retorna:
        --------

            None

        Ejemplo de uso::

            country =Country('str', 'str',1000,1000,'str', 'str') 
            states [State('Str', 'Str',1,1), State('str', 'str',1,1)]
            analyze_area_population_states(states, country)
    '''
    max_population = max(list, key=lambda state : state.population())
    min_population = min(list, key=lambda state : state.population())
    max_area = max(list, key=lambda state: state.area())
    min_area = min(list, key=lambda state: state.area())
    avg_population = sum(state.population() for state in list)/len(list)
    avg_area = sum(state.area() for state in list)/len(list)
    print('')
    print(f'\t    Pais seleccionado: {country.name()}')
    print(f'\t    Estado con mayor Poblacion   : {max_population.name()} con {max_population.population()} habitantes')
    print(f'\t    Estado con menor poblacion   : {min_population.name()} con {min_population.population()} habitantes')
    print(f'\t    Estado con mayor superficie  : {max_area.name()} con {max_area.area()} Km^2')
    print(f'\t    Estado con menor superficie  : {min_area.name()} con {min_area.area()} Km^2')
    print(f'\t    Promedio de las poblaciones  : {avg_population:.2f} habitantes')
    print(f'\t    Promedio de Superficie       : {avg_area:.2f} Km^2')
    input('\t    Presione enter para continuar')

def analyze_languages(list : list[Country]) -> None:
    '''
        Funcion para analizar los idiomas de los paises de una lista

        Parametros:
        -----------
            list : list[Country]
                Lista de paises a analizar

        Retorna:
        --------
            None

        Ejemplo de uso::

            analyze_languages(countries)
    '''

    '''
        Se hace uso de un set comprehension
        Se define un set (Conjunto) en donde se almacena los principales idiomas hablados en los paises (idioma que no se repita)
    '''
    languages_set = { country.language() for country in list } 
    '''
    Se define un diccionario con cada uno de los idiomas principales con una lista vacia de los paises que lo hablan
    '''
    languages_dict = { language : [] for language in languages_set } 
    for country in list: # Itero sobre los paises
        for lan in languages_set: # itero sobre los idiomas
            if country.language() == lan: # si el nombre del pais es igual al idioma en el set
                # agrego el nombre del pais en la clave del idioma del dicconario
                languages_dict[lan].append(country.name())
    
    print('')
    for key,value in languages_dict.items():
        print(f'\t    Idioma: {key}')
        for country in value:
            print(f'\t    {country}')
        print('')
    input('\t    Presione enter para continuar')

def analyze_measurements(list : list[Measurement], country: Country) -> None:
    '''
        Funcion para analizar las mediciones de los paises de una lista

        Parametros:
        -----------
            list : list[Measurement]
                Lista de mediciones a analizar
            country : Country
                Pais al que pertenecen las mediciones
        
        Retorna:
        --------
            None

        Ejemplo de uso::

            analyze_measurements(measurements, country)
    '''
    
    temperatures = [measurement.temperature() for measurement in list]
    humidities = [measurement.humidity() for measurement in list]
    wind_speeds = [measurement.wind_speed() for measurement in list]
    print(f'\t    Pais: {country.name()}')
    print('\t    ------------------------MODA-----------------------')
    print(f'\t    Moda Temperatura:             {mode(temperatures)[0]}°C')
    print(f'\t    Moda Humedad:                 {mode(humidities)[0]*100.:2f}%')
    print(f'\t    Moda Velocidad del Viento:    {mode(wind_speeds)[0]} Km/h')
    print('\t    ---------------------------------------------------')
    print('\t    ----------------------Promedio---------------------')
    print(f'\t    Promedio Temperatura:         {(sum(temperatures)/len(temperatures)):2f}°C')
    print(f'\t    Promedio Humedad:             {(sum(humidities)/len(humidities))*100.:2f}%')
    print(f'\t    Promedio Velocidad del Viento {(sum(wind_speeds)/len(wind_speeds)):2f} Km/h')
    print('\t    ---------------------------------------------------')
    print('\t    -----------------------Máximo----------------------')
    print(f'\t    Máximo Temperatura            {max(temperatures)}°C')
    print(f'\t    Máximo Humedad                {max(humidities)*100.:2f}%')
    print(f'\t    Máximo Velocidad del Viento   {max(wind_speeds)} Km/h')
    print('\t    ---------------------------------------------------')
    print('\t    -----------------------Mínimo----------------------')
    print(f'\t    Mínimo Temperatura            {min(temperatures)}°C')
    print(f'\t    Mínimo Humedad                {min(humidities)*100.:2f}%')
    print(f'\t    Mínimo Velocidad del Viento   {min(wind_speeds)} Km/h')
    print('\t    ---------------------------------------------------')
    input('\t    Presione enter para continuar')

def graph_menu(country) -> None:
    '''
        Funcion para mostrar el menu de graficas

        Parametros:
        -----------
            country : Country
                Pais a graficar

        Retorna:
        --------
            None

        Ejemplo de uso::

            graph_menu(country)
    '''
    
    op=-1
    while op != '0':
        print('\n\t   Elige una opcion para graficar:\n')
        print('\t   1.- Superficie de los estados')
        print('\t   2.- Poblacion de los estados')
        print('\t   0.- Regresar')
        op = input('\t   Ingrese una opcion: ')
        if op == '0':
            break
        elif op == '1':
            plot_states_area(country.states(), country)
        elif op == '2':
            plot_states_population(country.states(), country)
        elif not op.isnumeric():
            print('\n\t   Opcion no valida (La opción ingresada no es un numero punto flotante) \n')
            continue
        elif op not in ['0','1','2']:
            print('\n\t   Opcion no valida (No se encuentra dentro del rango 0-2) \n')
            continue

def plot_states_area(states : list[State], country : Country) -> None:
    '''
        Funcion para graficar la superficie de los estados de un pais

        Parametros:
        -----------

            states : list[State]
                Lista de estados a graficar
            country : Country
                Pais al que pertenecen los estados

        Retorna:
        --------
            None

        Ejemplo de uso::

            plot_states_area(states, country)
    '''
    states_names = [state.name() for state in states]
    states_area = [state.area() for state in states]
    bar_chart(states_names, states_area, f'Estados de {country.name()}', 'Superficie de los estados','Superficie (Km^2)', )

def plot_states_population(states : list[State], country : Country) -> None:
    '''
        Funcion para graficar la poblacion de los estados de un pais

        Parametros:
        -----------

            states : list[State]
                Lista de estados a graficar
            country : Country
                Pais al que pertenecen los estados

        Retorna:
        --------
            
            None

        Ejemplo de uso::

            plot_states_population(states, country)
    '''
    states_names = [state.name() for state in states]
    states_population = [state.population() for state in states]
    bar_chart(states_names, states_population, f'Estados de {country.name()}', 'Poblacion de los estados','Poblacion', )


def analyze_menu(countries : list[Country]) -> None:
    '''
        Funcion para mostrar el menu de analisis

        Parametros:
        -----------
            countries : list[Country]
                Lista de paises a analizar

        Retorna:
        --------
            None

        Ejemplo de uso::

            analyze_menu(countries)

    '''
    
    op = '-1'
    while op != '0':
        print('')
        print('\t    1.- Análisis de Superficie y Población de los paises')
        print('\t    2.- Análisis de Superficie y Población de los estados')
        print('\t    3.- Análisis de Idiomas')
        print('\t    4.- Análsis estadístico de los datos meteorológicos')
        print('\t    5.- Graficar datos')
        print('\t    0.- Regresar')
        op = input('\t    Ingrese una opcion: ')
        if op == '0':
            break
        elif op == '1':
            analyze_area_population(countries)
        elif op=='2':
            print('')
            op2= '-1'
            while op2 != '0':
                print('\t    Elige un pais para analizar la superficie y poblacion de sus estados:\n')
                show_countries_list(countries)
                print('''\t    0.- Regresar''')
                op2 = input('\t    Ingrese una opcion: ')
                try:
                    if op2 == '0':
                        break
                    country = countries[int(op2) - 1]
                    analyze_area_population_states(country.states(), country)
                except ValueError:
                    print('\n\t    Opcion invalida (La opción ingresada no es un numero punto flotante)\n')
                    continue
                except IndexError:
                    print('\n\t    Opcion invalida (No se encuentra dentro del rango 0-10)\n')
                    continue
        elif op=='3':
            analyze_languages(countries)
        elif op=='4':
            op3= '-1'
            while op3 != '0':
                print('\t    Elige un pais para analizar la superficie y poblacion de sus estados:\n')
                show_countries_list(countries)
                print('''\t    0.- Regresar''')
                op3 = input('\t    Ingrese una opcion: ')
                try:
                    if op3 == '0':
                        break
                    country = countries[int(op3) - 1]
                    analyze_measurements(country.measurements(), country)
                except ValueError:
                    print('\n\t    Opcion invalida (La opción ingresada no es un numero punto flotante)\n')
                    continue
                except IndexError:
                    print('\n\t    Opcion invalida (El número no se encuentra dentro del rango 0-10)\n')
                    continue
        elif op=='5':
            op4='-1'
            while op4 != '0':
                print('\t    Elige un pais para graficar sus datos:\n')
                show_countries_list(countries)
                print('''\t    0.- Regresar''')
                op4 = input('\t    Ingrese una opcion: ')
                try:
                    if op4 == '0':
                        break
                    country = countries[int(op4) - 1]
                    graph_menu(country)
                except ValueError:
                    print('\n\t    Opcion invalida (La opción ingresada no es un numero punto flotante)\n')
                    continue
                except IndexError:
                    print('\n\t    Opcion invalida (El número no se encuentra dentro del rango 0-10)\n')
                    continue
        elif not op.isnumeric():
            print('\n\t    Opcion no valida (La opción ingresada no es un numero punto flotante) \n')
            continue
        elif op not in ['0','1','2','3','4','5']:
            print('\n\t    Opcion no valida (El número no se encuentra dentro del rango 0-5) \n')
            continue
