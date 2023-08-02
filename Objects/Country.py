'''
    Modulo que contiene la clase Country
'''

from Objects.Measurement import Measurement
from Objects.State import State


class Country:
    """
    Clase para representar un país.

    Atributos:
    ----------
        ○ __name (str): Nombre del país.
        
        ○ __capital (str): Capital del país.
        
        ○ __population (int): Población del país.
        
        ○ __area (int): Área del país en kilómetros cuadrados.
        
        ○ __currency (str): Moneda local del país.
        
        ○ __language (str): Idioma principal del país.
        
        ○ __states (list[State]): Lista de estados o provincias del país.
        
        ○ __measurements (list[Measurement]): Lista de mediciones meteorológicas del país.

    Métodos:
    --------
        ○ __init__(self, name: str, capital: str, population: int, area: int, currency: str, language: str) -> None:
            Constructor de la clase Country.

        ○ name(self) -> str:
            Retorna el nombre del país.

        ○ capital(self) -> str:
            Retorna la capital del país.

        ○ population(self) -> int:
            Retorna la población del país.

        ○ currency(self) -> str:
            Retorna la moneda local del país.

        ○ language(self) -> str:
            Retorna el idioma principal del país.

        ○ area(self) -> int:
            Retorna el área del país en kilómetros cuadrados.

        ○ states(self) -> list[State]:
            Retorna la lista de estados o provincias del país.

        ○ measurements(self) -> list[Measurement]:
            Retorna la lista de mediciones meteorológicas del país.

        ○ setName(self, name: str) -> None:
            Establece un nuevo nombre para el país.

        ○ setCapital(self, capital: str) -> None:
            Establece una nueva capital para el país.

        ○ setPopulation(self, population: int) -> None:
            Establece una nueva población para el país.

        ○ setCurrency(self, currency: str) -> None:
            Establece una nueva moneda local para el país.

        ○ setLanguage(self, language: str) -> None:
            Establece un nuevo idioma principal para el país.

        ○ setArea(self, area: int) -> None:
            Establece una nueva área para el país.

        ○ add_state(self, state: State) -> None:
            Agrega un estado o provincia a la lista de estados del país.

        ○ add_measurement(self, measurement: Measurement) -> None:
            Agrega una medición meteorológica a la lista de mediciones del país.

        ○ set_measurements(self, measurements: list[Measurement]) -> None:
            Establece una nueva lista de mediciones meteorológicas para el país.

        ○ print(list_of_countries) -> str:
            Método estático para imprimir una lista de países en formato tabular.

        ○ print_states(self) -> str:
            Imprime la lista de estados o provincias del país en formato tabular.

        ○ print_measurements(self) -> str:
            Imprime la lista de mediciones meteorológicas del país en formato tabular.
    """

    def __init__(self,name : str, capital : str , population, area : int, currency : str, language : str) -> None:
        """
            Constructor de la clase Country.

            Parámetros:
            -----------
            ○ name (str): Nombre del país.
            ○ capital (str): Nombre de la capital.
            ○ population (int): Población del país.
            ○ area (int): Área del país en kilómetros cuadrados.
            ○ currency (str): Moneda utilizada en el país.
            ○ language (str): Idioma principal hablado en el país.

            Retorna:
            --------
            None

            Ejemplo:
            >>> pais = Country('Estados Unidos', 'Washington, D.C.', 328200000, 9833520, 'USD', 'Inglés')
        """
        self.__name : str = name 
        self.__capital : str = capital
        self.__population : int = population
        self.__area : str = area
        self.__currency : str = currency
        self.__language : str = language
        self.__states : list[State] = []
        self.__measurements : list[Measurement] = []

    '''
        Getters
    '''
    def name(self) -> str:
        """
    Método para obtener el nombre del país.

    Retorna:
    --------
    str: El nombre del país.
    """
        return self.__name
    
    def capital(self) -> str:
        """
    Método para obtener el nombre de la capital.

    Retorna:
    --------
    str: El nombre de la capital.
    """
        return self.__capital
    
    def population(self) -> int:
        """
    Método para obtener la población del país.

    Retorna:
    --------
    int: La población del país.
    """
        return self.__population
    
    def currency(self) -> str:
        """
    Método para obtener la moneda utilizada en el país.

    Retorna:
    --------
    str: La moneda utilizada en el país.
    """
        return self.__currency
    
    def language(self) -> str:
        """
    Método para obtener el idioma principal hablado en el país.

    Retorna:
    --------
    str: El idioma principal hablado en el país.
    """
        return self.__language
    
    def area(self) -> int:
        """
    Método para obtener el área del país en kilómetros cuadrados.

    Retorna:
    --------
    int: El área del país.
    """
        return self.__area
    
    def states(self) -> list[State]:
        """
    Método para obtener una lista de objetos State que representan los estados o provincias del país.

    Retorna:
    --------
    list[State]: Una lista de objetos State que representan los estados o provincias del país.
    """
        return self.__states
    
    def measurements(self) -> list[Measurement]:
        """
    Método para obtener una lista de objetos Measurement que representan las mediciones del clima del país.

    Retorna:
    --------
    list[Measurement]: Una lista de objetos Measurement que representan las mediciones del clima del país.
    """
        return self.__measurements

    '''
        Setters
    '''
    def setName(self, name : str) -> None:
        """
            Método para establecer el nombre del país.

            Parámetros:
            -----------
            name (str): El nuevo nombre del país.

            Retorna:
            --------
            None
        """
        self.__name = name

    def setCapital(self, capital : str) -> None:
        """
            Método para establecer el nombre de la capital.

            Parámetros:
            -----------
            capital (str): El nuevo nombre de la capital.

            Retorna:
            --------
            None
        """
        self.__capital = capital

    def setPopulation(self, population : str) -> None:
        """
            Método para establecer la población del país.

            Parámetros:
            -----------
            population (int): La nueva población del país.

            Retorna:
            --------
            None
        """
        self.__population = population

    def setCurrency(self, currency : str) -> None:
        """
            Método para establecer la moneda utilizada en el país.

            Parámetros:
            -----------
            currency (str): La nueva moneda utilizada en el país.

            Retorna:
            --------
            None
        """
        self.__currency = currency

    def setLanguage(self, language : str) -> None:
        """
            Método para establecer el idioma principal hablado en el país.

            Parámetros:
            -----------
            language (str): El nuevo idioma principal hablado en el país.

            Retorna:
            --------
            None
        """
        self.__language = language

    def setArea(self, area : int) -> None:
        """
            Método para establecer el área del país en kilómetros cuadrados.

            Parámetros:
            -----------
            area (int): La nueva área del país.

            Retorna:
            --------
            None
        """
        self.__area = area

    '''
        Metodos
    '''
    def add_state(self, state : State) -> None:
        """
            Método para agregar un objeto State a la lista de estados o provincias del país.

            Parámetros:
            -----------

            state (State): El objeto State a agregar.

            Retorna:
            --------
            None

            Ejemplo::

                >>> pais = Country('Estados Unidos', 'Washington, D.C.', 328200000, 9833520, 'USD', 'Inglés')
                >>> estado = State('California', 'Sacramento', 39510000, 423970, pais)
                >>> pais.add_state(estado)

        """
        self.__states.append(state)

    def add_measurement(self, measurement : Measurement) -> None:
        """
            Método para agregar un objeto Measurement a la lista de mediciones del clima del país.

            Parámetros:
            -----------

            measurement (Measurement): El objeto Measurement a agregar.

            Retorna:
            --------
            None

            Ejemplo::

                >>> pais = Country('Estados Unidos', 'Washington, D.C.', 328200000, 9833520, 'USD', 'Inglés')
                >>> medicion = Measurement('2021-10-01', 20, 10, 15, 5, 0, pais)
                >>> pais.add_measurement(medicion)

        """
        self.__measurements.append(measurement)

    def set_measurements(self, measurements : list[Measurement]) -> None:
        """
            Método para establecer la lista de mediciones del clima del país.

            Parámetros:
            -----------

            measurements (list[Measurement]): La nueva lista de mediciones del clima del país.

            Retorna:
            --------
            None

            Ejemplo::

                >>> pais = Country('Estados Unidos', 'Washington, D.C.', 328200000, 9833520, 'USD', 'Inglés')
                >>> medicion1 = Measurement('2021-10-01', 20, 10, 15, 5, 0, pais)
                >>> medicion2 = Measurement('2021-10-02', 20, 10, 15, 5, 0, pais)

                >>> pais.set_measurements([medicion1, medicion2])

        """
        self.__measurements = measurements

    @staticmethod
    def print(list_of_countries) -> str:
        """
            Método para imprimir una lista de objetos Country.

            Parámetros:
            -----------

            list_of_countries (list[Country]): La lista de objetos Country a imprimir.

            Retorna:
            --------

            str: Una cadena con la lista de objetos Country formateada.

            Ejemplo::

                >>> pais1 = Country('Estados Unidos', 'Washington, D.C.', 328200000, 9833520, 'USD', 'Inglés')
                >>> pais2 = Country('México', 'Ciudad de México', 126200000, 1964375, 'MXN', 'Español')

                >>> Country.print([pais1, pais2])

                Nombre           Capital          Poblacion        Area             Moneda Local     Idioma
                Estados Unidos   Washington, D.C. 328200000        9833520          USD              Inglés
                México           Ciudad de México 126200000        1964375          MXN              Español

        """
        # Get the list of attributes from the first country object
        header = ['Nombre', 'Capital', 'Poblacion', 'Area', 'Moneda Local', 'Idioma Principal']

        # Se crea una lista con los datos a imprimir
        list_to_print = [header]
        list_to_print.extend([country.name(), country.capital(), country.population(),
                            country.area(), country.currency(), country.language()] for country in list_of_countries)

        # Calculamos el ancho de cada columna
        longest_cols = [max(len(str(row[i])) for row in list_to_print) + 3 for i in range(len(list(list_to_print[0])))]

        # Creamos el formato de cada fila
        row_format = "".join(["{:>" + str(longest_col) + "}" for longest_col in longest_cols])

        # Se imprime el encabezado
        print(row_format.format(*header))

        # Se imprime el separador del encabezado con los datos
        print("".join(["-" * col_width for col_width in longest_cols]))

        # Se imprime cada columna
        for row in list_to_print[1:]:
            print(row_format.format(*row))
    
    def print_states(self,) -> str:
        # Se crea el encabezado
        header = ['Nombre', 'Capital', 'Poblacion', 'Area',]

        # Se crea una lista con los datos a imprimir
        list_to_print = [header]
        list_to_print.extend([state.name(), state.capital(), state.population(), state.area()] for state in self.__states)

        # Calculamos el ancho de cada columna
        longest_cols = [max(len(str(row[i])) for row in list_to_print) + 3 for i in range(len(list(list_to_print[0])))]

        # Creamos el formato de cada fila
        row_format = "".join(["{:>" + str(longest_col) + "}" for longest_col in longest_cols])

        # Se imprime el encabezado
        print(row_format.format(*header))

        # Se imprime el separador del encabezado con los datos
        print("".join(["-" * col_width for col_width in longest_cols]))

        # Se imprime cada columna
        for row in list_to_print[1:]:
            print(row_format.format(*row))
    
    '''
        Metodo para imprimir las mediciones de un pais
    '''

    def print_measurements(self,) -> str:
        # Se crea el encabezado
        header = ['Temperatura (°C)','Humedad (%)', 'Velocidad del Viento (Km/h)', 'Fecha',]

        # Se crea una lista con los datos a imprimir
        list_to_print = [header]
        list_to_print.extend([measurement.temperature(), measurement.humidity(), measurement.wind_speed(), measurement.date()] for measurement in self.__measurements)

        # Calculamos el ancho de cada columna
        longest_cols = [max(len(str(row[i])) for row in list_to_print) + 3 for i in range(len(list(list_to_print[0])))]

        # Creamos el formato de cada fila
        row_format = "".join(["{:>" + str(longest_col) + "}" for longest_col in longest_cols])

        # Se imprime el encabezado
        print(row_format.format(*header))

        # Se imprime el separador del encabezado con los datos
        print("".join(["-" * col_width for col_width in longest_cols]))

        # Se imprime cada columna
        for row in list_to_print[1:]:
            print(row_format.format(*row))
    



'''






'''