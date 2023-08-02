
'''
    Clase para almacenar los diferentes estados
'''

class State:

    '''
        Clase para almacenar los diferentes estados

        Atributos:
        ----------
            ○ __name : str
                Nombre del estado
            ○ __capital : str
                Capital del estado
            ○ __population : int
                Poblacion del estado
            ○ __area : int
                Area del estado

        Métodos:
        --------
            ○ __init__(self, name : str, capital : str, population : int, area : int) -> None
                Constructor de la clase
            ○ name(self) -> str
                Getter del nombre del estado
            ○ capital(self) -> str
                Getter de la capital del estado
            ○ population(self) -> int
                Getter de la poblacion del estado
            ○ area(self) -> int
                Getter del area del estado
            ○ setName(self, name : str) -> None
                Setter del nombre del estado
            ○ setCapital(self, capital : str) -> None
                Setter de la capital del estado
            ○ setPopulation(self, population : int) -> None
                Setter de la poblacion del estado
            ○ setArea(self, area : int) -> None
                Setter del area del estado
            ○ print(list_of_states) -> None
                Método estático para imprimir una lista de estados

        Ejemplo de uso::

            state = State('Nuevo Leon', 'Monterrey', 5000000, 100000)
    '''

    def __init__(self, name : str, capital : str, population : int, area : int) -> None:
        self.__name : str = name
        self.__capital : str = capital
        self.__population : int = population
        self.__area : int = area
    
    '''
        Getters
    '''

    def name(self) -> str:
        return self.__name
    
    def capital(self) -> str:
        return self.__capital
    
    def population(self)-> int:
        return self.__population
    
    def area(self)-> int:
        return self.__area
    
    '''
        Setters
    '''

    def setName(self, name : str) -> None:
        self.__name = name

    def setCapital(self, capital : str) -> None:
        self.__capital = capital

    def setPopulation(self, population) -> None:
        self.__population = population

    def setArea(self, area) -> None:
        self.__area = area

    '''
        Metodos
    '''
    @staticmethod
    def print(list_of_states) -> None:
        # Get the list of attributes from the first country object
        header = ['Nombre', 'Capital', 'Poblacion', 'Area']

        # Se crea una lista con los datos a imprimir
        list_to_print = [header]
        list_to_print.extend([state.name(), state.capital(), state.population(), state.area()] for state in list_of_states)

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
    def get(self,key: str) -> str | float | int:
        if key == 'name':
            return self.__name
        elif key == 'capital':
            return self.__capital
        elif key == 'population':
            return self.__population
        elif key == 'area':
            return self.__area
        else:
            return None
