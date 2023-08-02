
from Menus.util import show_countries_list
from Objects.Country import Country
from Objects.State import State
from Objects.Measurement import Measurement

def show_states(states: list[State],key: str) -> None:
    '''
        Función que muestra la lista de estados en pantalla.

        Parámetros:
        -----------
            states : list[State]
                Lista de estados a mostrar.
            key : str
                Clave para filtrar por area o poblacion
    
        Retorna:
        --------
            None

        Ejemplo de uso::

            show_states(states, 'area')
    '''
    
    try:
        min_value = float(input('\t    Ingrese el valor minimo: '))
        if key == 'area':
            max_value = float(input('\t    Ingrese el valor maximo: '))
            if min_value > max_value:
                print('\n\t    Valor minimo no puede ser mayor a valor maximo\n')
                return
            states = [ state for state in states if state.area() >= min_value and state.area() <= max_value]
        else:
            states = [ state for state in states if state.population() >= min_value]
        if not states:
            print('\n\t    No se encontraron resultados\n')
            return
        State.print(states)
        input('\n\t    Presione enter para continuar')
    except ValueError:
        print('\n\t    Valor invalido (El valor ingresado no es un numero punto flotante)\n')
        return

def filter_states_by_population(countries: list[Country]) -> None:
    '''
        Menu para filtrar por poblacion

        Parámetros:
        -----------
            countries : list[Country]
                Lista de países a mostrar.

        Retorna:
        --------
            None

        Ejemplo de uso::

            filter_states_by_population(countries)
    '''
    op = '-1'
    while op != '0':
        show_countries_list(countries)
        print('\t    0.- Regresar')
        op = input('\t    Ingrese una opcion: ')
        try:
            if op == '0':
                return
            country = countries[int(op) - 1]
            print('\t    Pais Seleccionado: ', country.name())
            print('\t    Filtrado de Estados por Poblacion\n')
            show_states(country.states(),'population')
        except ValueError:
            print('\n\t    Opcion invalida (La opción ingresada no es un numero punto flotante) \n')
            continue
        except IndexError:
            print('\n\t    Opcion invalida (No se encuentra en el rango 0-10) \n')
            continue

def filter_states_by_area(countries: list[Country]) -> None:
    '''
        Menu para filtrar por area

        Parámetros:
        -----------
            countries : list[Country]
                Lista de países a mostrar.

        Retorna:
        --------
            None

        Ejemplo de uso::

            filter_states_by_area(countries)

    '''
    op = '-1'
    while op != '0':
        show_countries_list(countries)
        print('\t    0.- Regresar')
        op = input('\t    Ingrese una opcion: ')
        try:
            if op == '0':
                return
            country = countries[int(op) - 1]
            print('\t    Pais Seleccionado: ', country.name())
            print('\t    Filtrado de Estados por Superficie\n')
            show_states(country.states(),'area')
        except ValueError:
            print('\n\t    Opcion invalida (La opción ingresada no es un numero punto flotante) \n')
            continue
        except IndexError:
            print('\n\t    Opcion invalida (No se encuentra en el rango 0-10) \n')
            continue

def filter_menu(countries: list[Country]) -> None:
    '''
        Menu para filtrar por area o poblacion

        Parámetros:
        -----------
            countries : list[Country]
                Lista de países a mostrar.

        Retorna:
        --------
            None

        Ejemplo de uso::

            filter_menu(countries)
    '''
    op = '-1'
    while op != '0':
        print('\t    Filtrado de Datos\n')
        print('\t    1.- Filtrado de estados por poblacion')
        print('\t    2.- Filtrado de estados por area')
        print('\t    0.- Regresar')
        op = input('\t    Ingrese una opcion: ')
        if op == '0':
            return
        elif op == '1':
            filter_states_by_population(countries)
        elif op == '2':
            filter_states_by_area(countries)
        elif not op.isnumeric():
            print('\n\t    Opcion invalida (La opción ingresada no es un número) \n')
        elif op not in ['1','2']:
            print('\n\t    Opcion invalida (No se encuentra en el rango 0-2) \n')