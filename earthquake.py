from earthquakes import earthquakes
import re
import logging
import sys

logger = logging.getLogger()


def get_quake(city: str, magnitude_min, period: str):
    try:
        earthquakes.connect()   # Establish connectivity to USGS to avoid cached results
        report = earthquakes.get_report(period, 'all')  # Ger earthquake report
    except:
        logger.warning('Unexpected error: ' + str(sys.exc_info()[0]))
        raise

    for i in report['earthquakes']: # Iterate earthquake report
        if re.search(city, i['location_description']):  # Search for matching location (city)
            logger.info(city + ' earthquake ' + str(i['magnitude']))
            if i['magnitude'] >= float(magnitude_min):  # Look for earthquake magnitude >= magnitude_min
                return True
    return False
