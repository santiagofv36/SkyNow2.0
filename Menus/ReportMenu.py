
from Objects.Country import Country

from Menus.util import show_countries_list

def report_menu(countries):
    '''
        Menú de reportes.
        -----------------

            Muestra un menú con las opciones de reportes disponibles.
            Mostrar información del país.
            Mostrar estados del país.
            Mostrar datos meteorológicos del país.

        Parámetros:
        -----------

            countries : list[Country]
                Lista de países a mostrar.

        Retorna:
        --------

            None

        Ejemplo de uso::

            report_menu(countries)
    '''
    
    op ='-1'
    while op != '0':
        print('')
        print('\t    Elige un pais para ver sus reportes\n')
        show_countries_list(countries)
        print('''\t    0.- Regresar''')
        op = input('\t    Ingrese una opcion: ')
        try:
            if op == '0':
                break
            country = countries[int(op) - 1]
            op2 = '-1'
            print('\n\n\t    Reportes')
            while op2 != '0':
                print()
                print(f'''\t    Pais Seleccionado: {country.name()}\n''')
                print('\t    1.- Mostrar información del Pais')
                print('\t    2.- Mostrar Estados del Pais')
                print('\t    3.- Mostrar Datos Meteorológicos del Pais')
                print('\t    0.- Regresar')
                op2 = input('\t    Ingrese una opcion: ')
                print()
                if op2 == '1':
                    Country.print([country])
                elif op2 == '2':
                    print(f'\n\t    Estados del Pais {country.name()}\n')
                    country.print_states()
                elif op2 == '3':
                    print(f'\n\t    Datos Meteorológicos del Pais {country.name()}\n')
                    country.print_measurements()
                elif op2 == '0':
                    break
                elif not op2.isnumeric():
                    print('\n\t    Opcion invalida (La opción ingresada no es un numero) \n')
                    continue
                elif op2 not in ['1','2','3','0']:
                    print('\n\t    Opcion invalida (La opción ingresada no se encuentra en el rango 0-3)')
                    continue

        except ValueError:
            print('\n\t    Opcion invalida (La opción ingresada no es un numero)')
            continue
        except IndexError:
            print('\n\t    Opcion invalida (No se encuentra en el rango 0-10)')
            continue


