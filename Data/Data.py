'''
    Modulo para obtener datos de una API

    Contiene las funciones para obtener los datos de los estados y las mediciones desde una API.

    Funciones:
    ----------

        get_states(url: str = 'https://raw.githubusercontent.com/Andresarl16/API-Retos/main/location-states-api.json') -> list[dict] | None:

            Obtiene los estados o provincias desde una API en formato JSON.

            Parámetros:
            ----------
                url (str, opcional): URL de la API que proporciona los estados. Por defecto, se utiliza una URL predefinida.

            Retorna:
            --------
                list[dict] | None: Una lista de diccionarios que representan los estados, o None si ocurre un error al obtener los datos.

            Ejemplo de uso::

                estados = get_states()
                if estados:
                    for estado in estados:
                        print(estado['state_name'])

        get_measurements(url: str = 'https://raw.githubusercontent.com/Andresarl16/API-Retos/main/locations-api.json') -> list[dict] | None:

            Obtiene las mediciones meteorológicas desde una API en formato JSON.

            Parámetros:

                url (str, opcional): URL de la API que proporciona las mediciones. Por defecto, se utiliza una URL predefinida.

            Retorna:
            --------

                list[dict] | None: Una lista de diccionarios que representan las mediciones, o None si ocurre un error al obtener los datos.

            Ejemplo de uso::

                mediciones = get_measurements()
                if mediciones:
                    for medicion in mediciones:
                        print(medicion['location_name'])


        get_countries(url: str='https://raw.githubusercontent.com/Andresarl16/API-Retos/main/locations-data-api.json') -> list[Country] | None:

            Obtiene los países desde una API en formato JSON.

            Parámetros:

                url (str, opcional): URL de la API que proporciona los países. Por defecto, se utiliza una URL predefinida.

            Retorna:
            --------

                list[Country] | None: Una lista de objetos Country, o None si ocurre un error al obtener los datos.

            Ejemplo de uso::

                paises = get_countries()
                if paises:
                    for pais in paises:
                        print(pais.name())

'''
import requests

from Objects.Country import Country
from Objects.State import State
from Objects.Measurement import Measurement



def get_states(url: str = 'https://raw.githubusercontent.com/Andresarl16/API-Retos/main/location-states-api.json') -> list[dict] | None:
    """
    Obtiene los estados o provincias desde una API en formato JSON.

    Parámetros:
    ----------
        url (str, opcional): URL de la API que proporciona los estados. Por defecto, se utiliza una URL predefinida.

    Retorna:
    --------
        list[dict] | None: Una lista de diccionarios que representan los estados, o None si ocurre un error al obtener los datos.

    Ejemplo de uso::

        estados = get_states()
        if estados:
            for estado in estados:
                print(estado['state_name'])
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        print("No se pudo cargar los datos de los estados, Url Inválida")
    except Exception as e:
        print("Error de conexion al intentar cargar los datos de los estados, por favor conectese a internet") # si no se pudo cargar los datos se regresa None
        return None

def get_measurements(url: str = 'https://raw.githubusercontent.com/Andresarl16/API-Retos/main/locations-api.json') -> list[dict] | None:
    """
    Obtiene las mediciones meteorológicas desde una API en formato JSON.

    Parámetros:
        url (str, opcional): URL de la API que proporciona las mediciones. Por defecto, se utiliza una URL predefinida.

    Retorna:
        list[dict] | None: Una lista de diccionarios que representan las mediciones, o None si ocurre un error al obtener los datos.

    Ejemplo de uso:
        mediciones = get_measurements()
        if mediciones:
            for medicion in mediciones:
                print(medicion['temperature'], medicion['humidity'])
    """
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        print("No se pudo cargar los datos de las mediciones, Url Inválida")
    except Exception as e:
        print("Error de conexion al intentar cargar los datos meteorologicos, por favor conectese a internet") # si no se pudo cargar los datos se regresa None
        return None


def add_states_to_countries(countries: list[Country], states: list[dict]) -> None:
    """
    Asocia los estados con sus respectivos países.

    Parámetros:
    ----------
        countries (list[Country]): Una lista de objetos de la clase Country, que representan los países.
        states (list[dict]): Una lista de diccionarios que representan los estados.

    Retorna:
    --------
        None

    Ejemplo de uso::

        paises = get_countries()
        estados = get_states()
        if paises and estados:
            add_states_to_countries(paises, estados)
            for pais in paises:
                print(pais.name(), pais.capital())
                for estado in pais.states():
                    print('-', estado.name())
    """
    # Se procede a agregar los estados a cada pais, para esto se recorre la lista de estados y paises al mismo tiempo
    for _states, _country in zip(states,countries):
            key, stateList = _states.items() # regresa una tupla con dos elementos el primero es el key y el segundo es el value
            # key sera de la siguiente manera ('location_name', 'Pais')
            # stateList sera de la siguiente manera ('location_states', [{ state_name: 'estado' ,...} ,...] )
            if _country.name() == key[1]: # se compara el nombre del pais con el nombre del pais en la tupla
                for state in stateList[1]: # se recorre la lista de estados
                    # se agrega el estado a la lista de estados del pais
                    _country.states().append(
                        State(
                            state.get('state_name'),
                            state.get('state_capital'),
                            state.get('population'),
                            state.get('area'),
                        )
                    )
    return None
  
  
def add_measurements_to_countries(countries: list[Country], measurements: list[dict]) -> None:
    
    '''
        Asocia las mediciones con sus respectivos países.

        Recorre la lista de mediciones y la lista de paises al mismo tiempo, para luego comparar el nombre del pais con el nombre del pais en la tupla

        convierte la lista de mediciones en una lista de objetos Measurement y la agrega a la lista de mediciones del pais

        Parámetros:
        ----------
            countries (list[Country]): Una lista de objetos de la clase Country, que representan los países.
            measurements (list[dict]): Una lista de diccionarios que representan las mediciones.

        Retorna:
        --------
            None

        Ejemplo de uso::

            paises = get_countries()
            mediciones = get_measurements()
            if paises and mediciones:
                add_measurements_to_countries(paises, mediciones)
                for pais in paises:
                    print(pais.name(), pais.capital())
                    for medicion in pais.measurements():
                        print('-', medicion.temperature())
    '''

    # Se procede a agregar las mediciones a cada pais, para esto se recorre la lista de mediciones y paises al mismo tiempo
    for _measurements, _country in zip(measurements,countries):
        key, measurementList = _measurements.items() # regresa una tupla con dos elementos el primero es el key y el segundo es el value
        # key sera de la siguiente manera ('location_name', 'Pais')
        # measurementList sera de la siguiente manera ('location_measurements', [{ temperature: 'temperatura' ,...} ,...] )
        if _country.name() == key[1]: # se compara el nombre del pais con el nombre del pais en la tupla
            for measurement in measurementList[1]: # se recorre la lista de mediciones
                # se agrega la medicion a la lista de mediciones del pais
                _country.measurements().append(
                    Measurement(
                        measurement.get('temperature'),
                        measurement.get('humidity'),
                        measurement.get('wind_speed'),
                        measurement.get('date')
                    )
                )
    return None

def get_countries(url: str='https://raw.githubusercontent.com/Andresarl16/API-Retos/main/locations-data-api.json') -> list[Country] | None:
    """
    Obtiene los países desde una API en formato JSON y los asocia con sus respectivos estados y mediciones.

    Parámetros:
    ----------
        url (str, opcional): URL de la API que proporciona los países. Por defecto, se utiliza una URL predefinida.

    Retorna:
    --------
        list[Country] | None: Una lista de objetos de la clase Country, que representan los países con sus estados y mediciones asociadas, o None si ocurre un error al obtener los datos.

    Ejemplo de uso::

        paises = get_countries()
        if paises:
            for pais in paises:
                print(pais.name(), pais.capital())
                for estado in pais.states():
                    print('-', estado.name())
                for medicion in pais.measurements():
                    print('-', medicion.temperature(), medicion.humidity())
    """
    states = get_states()
    measurements = get_measurements()
    if states is None or measurements is None: # si no se pudo obtener los estados o las mediciones se retorna None
        return None
    try:
        response = requests.get(url)
        if response.status_code == 200:
            countries = [
                Country(
                    country.get('location_name'),
                    country.get('location_capital'),
                    country.get('population'),
                    country.get('area'),
                    country.get('currency'),
                    country.get('main_language')
                )
                for country in response.json()
            ]
            # Ya se tienen los paises almacenados en una lista de objetos de paises
            add_states_to_countries(countries, states)
            add_measurements_to_countries(countries, measurements)
            return countries # se regresa la lista de paises con sus estados y mediciones
        print("No se pudo cargar los datos de los paises , Url Inválida")
    except Exception as e:
        return None


