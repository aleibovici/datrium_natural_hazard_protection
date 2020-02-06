import pyowm
import logging
import sys
import settings


logger = logging.getLogger()


def get_wind(city: str, country: str):

    try:
        observation = __get_weather(city, country)
        w = observation.get_weather().get_wind()['speed']
        logger.info('Wind speed ' + str(w) + ' KM/h')
        return float(w)
    except:
        logger.error('Unexpected error: ' + str(sys.exc_info()[0]))
        raise


def get_temperature(city: str, country: str):

    try:
        observation = __get_weather(city, country)
        w = observation.get_weather().get_temperature('celsius')['temp']
        logger.info('Temperature ' + str(w) + ' ºC')
        return float(w)
    except:
        logger.error('Unexpected error: ' + str(sys.exc_info()[0]))
        raise


def __get_weather(city: str, country: str):

    owm = pyowm.OWM(settings.CONFIG_DICT['pyowm_api_key'])

    key = city + ", " + country

    try:
        observation = owm.weather_at_place(key)
        return observation
    except:
        logger.warning('Unexpected error: ' + str(sys.exc_info()[0]))
        pass
