
from Objects.Country import Country

def show_countries_list(countries : list[Country]) -> None:
    '''
        Función que muestra la lista de países en pantalla.

        Parámetros:
        -----------

            countries : list[Country]
                Lista de países a mostrar.

        Retorna:
        --------
            None

        Ejemplo de uso::

            show_countries_list(countries)

        Lista de paises
            1.- Argentina
            2.- Bolivia
            3.- Brasil
            4.- Chile
            ...
    '''
    for index, country in enumerate(countries):
        print(f'''\t    {index + 1}.- {country.name()}''')
