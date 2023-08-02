

'''
    Clase para almacenar las diferentes mediciones
'''

class Measurement:

    """
    Clase para representar una medición meteorológica.

    Atributos:
    ---------
        ○ __temperature (float): Temperatura registrada en la medición.
        ○ __humidity (float): Humedad registrada en la medición.
        ○ __wind_speed (int): Velocidad del viento registrada en la medición.
        ○ __date (str): Fecha de la medición en formato de cadena.

    Métodos:
    --------
        ○ __init__(self, temperature: float, humidity: float, wind_speed: int, date: str) -> None:
            Constructor de la clase Measurement.

        ○ temperature(self) -> float:
            Retorna el valor de la temperatura.

        ○ humidity(self) -> float:
            Retorna el valor de la humedad.

        ○ wind_speed(self) -> int:
            Retorna el valor de la velocidad del viento.

        ○ date(self) -> str:
            Retorna la fecha de la medición.

        ○ setTemperature(self, temperature: float) -> None:
            Establece un nuevo valor para la temperatura.

        ○ setHumidity(self, humidity: float) -> None:
            Establece un nuevo valor para la humedad.

        ○ setWind_speed(self, wind_speed: int) -> None:
            Establece un nuevo valor para la velocidad del viento.

        ○ setDate(self, date: str) -> None:
            Establece una nueva fecha para la medición.

        ○ get(self, key: str) -> float | int | str:
            Retorna el valor de un atributo según su nombre.

            ○ Parámetros:
                key (str): Nombre del atributo ('temperature', 'humidity', 'wind_speed' o 'date').

            ○ Retorna:
                El valor del atributo si existe, de lo contrario, retorna None.
    """

    def __init__(self, temperature : float, humidity: float, wind_speed : int, date : str) -> None:
        self.__temperature : float = temperature
        self.__humidity : float = humidity
        self.__wind_speed : int = wind_speed
        self.__date : str = date

    '''
        Getters
    '''

    def temperature(self) -> float:
        return self.__temperature
    
    def humidity(self) -> float:
        return self.__humidity
    
    def wind_speed(self) -> int:
        return self.__wind_speed
    
    def date(self) -> str:
        return self.__date
    
    '''
        Setters
    '''

    def setTemperature(self, temperature : float) -> None:
        self.__temperature = temperature

    def setHumidity(self, humidity : float) -> None:
        self.__humidity = humidity

    def setWind_speed(self, wind_speed : int) -> None:
        self.__wind_speed = wind_speed

    def setDate(self, date : str) -> None:
        self.__date = date

    '''
        Metodos
    '''
    '''
        Metodo para obtener el valor de un atributo segun su nombre
    '''
    def get(self,key : str) -> float | int | str:
        if key == 'temperature':
            return self.__temperature
        elif key == 'humidity':
            return self.__humidity
        elif key == 'wind_speed':
            return self.__wind_speed
        elif key == 'date':
            return self.__date
        else:
            return None