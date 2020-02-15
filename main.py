#!/usr/bin/env python

import os
from logging.config import dictConfig
import settings
import configparser
import time
import logging
import earthquake
import da
import weather
import mailer

''' Initiate global variables '''

settings.init()

'''Events and errors are formated using the configuration below and placed at main.log'''

logging_config = dict(
    version=1,
    formatters={
        'info': {
            'class': 'logging.Formatter',
            'format': '%(asctime)s %(name)-15s %(levelname)-8s %(message)s'
        }
    },
    handlers={
        'console': {'class': 'logging.StreamHandler',
                    'formatter': 'info',
                    'level': logging.INFO},
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'main.log',
            'mode': 'a',
            'formatter': 'info',
            'level': logging.INFO
        }
    },
    root={
        'handlers': ['file'],
        'level': logging.INFO,
    },
)

logging.config.dictConfig(logging_config)
logger = logging.getLogger()


''' Function to establish connection to production DVX defined in prod_dvx_fqdn '''


def connect_dvx(prod_dvx_fqdn: str,
                prod_dvx_username: str,
                prod_dvx_password: str):
    return da.connect(
        prod_dvx_fqdn,
        prod_dvx_username,
        prod_dvx_password)


''' Function to load and parse application parameters file and log '''


def load_config(configFilePath: str, log: bool):
    logger.info(' ')
    logger.info('Loading configuration')

    config = configparser.ConfigParser()
    config.read(configFilePath)
    settings.CONFIG_DICT = dict(config.items('DEFAULT'))  # read config file

    if is_docker():   # test for docker conatiner and reload settings from os.environ
        for key in settings.CONFIG_DICT:
            if key in os.environ:
                settings.CONFIG_DICT[key] = os.environ[key]

    for key in settings.CONFIG_DICT:
        if (not key == 'prod_dvx_password') and (not key == 'pyowm_api_key') and (not key == 'smtp_password'):   # Do not log passwords and API key
            if log:
                logger.info('> ' + key + ' : ' + settings.CONFIG_DICT[key])             # Log settings

    vms = []
    vms = vms_to_protect(settings.CONFIG_DICT['vms_to_protect_filename'])
    for i in vms:
        if ('EOF') in i:    # exit at end of vms
            break
        else:
            if not log:
                logger.info('Protected VM : ' + i)

    return settings.CONFIG_DICT


''' Function to detect if running inside a docker container'''


def is_docker():
    path = '/proc/self/cgroup'
    return (
        os.path.exists('/.dockerenv') or
        os.path.isfile(path) and any('docker' in line for line in open(path))
    )


''' Function to trigger snapshot and replication within DVX. '''


def protect(reason: str, replicate: str):
    vms = []
    vms = vms_to_protect(settings.CONFIG_DICT['vms_to_protect_filename'])   # Read vms list to protect from vms_to_protect_filename

    for i in vms:   # Loop vms from vms_to_protect_filename
        if ('EOF') in i:    # exit at end of vms
            return
        snapshot_response = da.take_vm_snapshot(
            settings.DVX, [i], settings.CONFIG_DICT['snapshot_retention'], reason)
        if snapshot_response.state != 'SUCCESS':    # Test for sucesfull snapshot response
            print("ALERT! Snapshot Error")
            exit
        if replicate == 'true':   # Snapshot replication if repl_replicate = True
            da.replicate_vm_snapshot(
                settings.DVX, snapshot_response.keyValues._values[2].val.stringVal, settings.CONFIG_DICT['repl_location'], settings.CONFIG_DICT['snapshot_retention'])


''' Function to read virtual nachine list to protect from a list defined in vms_to_protect_filename '''


def vms_to_protect(filename: str):

    vms = []

    with open(filename, 'r') as filehandle:  # open file and read the content in a list
        for line in filehandle:
            currentPlace = line[:-1]    # remove linebreak which is the last character of the string
            vms.append(currentPlace)    # add item to the list

    return vms


''' Main loop function to check for natural hazard events and trigger protection functions '''


def main():

    CONFIG_DICT = load_config('main.config', True)    # Load application parameters
    settings.DVX = connect_dvx(settings.CONFIG_DICT['prod_dvx_fqdn'], settings.CONFIG_DICT['prod_dvx_username'], settings.CONFIG_DICT['prod_dvx_password'])  # Connect to DVX

    # Test initial connectivity
    try:
        da.test_connection(settings.DVX)
    except:
        mailer.send_mail(settings.CONFIG_DICT['smtp_server'], settings.CONFIG_DICT['smtp_port'], settings.CONFIG_DICT['smtp_sender_email'],
                         settings.CONFIG_DICT['smtp_receiver_email'], settings.CONFIG_DICT['smtp_password'], "Connection to DVX Failed")
        raise

    while True:

        CONFIG_DICT = load_config('main.config', False)    # Load application parameters
        logger.info('Checking for natural hazards in ' + CONFIG_DICT['prod_location_city'] + ", " + CONFIG_DICT['prod_location_country'])

        ''' Check for Nautral Hazards '''

        # Function to check for winds

        if weather.get_wind(CONFIG_DICT['prod_location_city'], CONFIG_DICT['prod_location_country']) > float(CONFIG_DICT['wind_speed_max']):
            logger.info('>> High Winds Detected: ' + CONFIG_DICT['prod_location'])
            mailer.send_mail(settings.CONFIG_DICT['smtp_server'], settings.CONFIG_DICT['smtp_port'], settings.CONFIG_DICT['smtp_sender_email'],
                             settings.CONFIG_DICT['smtp_receiver_email'], settings.CONFIG_DICT['smtp_password'], "High Winds Detected")
            protect("HighWinds", CONFIG_DICT['repl_replicate'])

        # Function to check for temperature

        elif weather.get_temperature(CONFIG_DICT['prod_location_city'], CONFIG_DICT['prod_location_country']) > float(CONFIG_DICT['temperature_max']):
            logger.info('>> High Temperatures Detected: ' + CONFIG_DICT['prod_location_city'] + ', ' + CONFIG_DICT['prod_location_country'])
            mailer.send_mail(settings.CONFIG_DICT['smtp_server'], settings.CONFIG_DICT['smtp_port'], settings.CONFIG_DICT['smtp_sender_email'],
                             settings.CONFIG_DICT['smtp_receiver_email'], settings.CONFIG_DICT['smtp_password'], "High Temperatures Detected")
            protect("HighTemperature", CONFIG_DICT['repl_replicate'])

        # Function to check for earthquakes

        elif earthquake.get_quake(CONFIG_DICT['prod_location_city'], CONFIG_DICT['quake_magnitude_min'], CONFIG_DICT['quake_period']):
            logger.info('>>> Earthquake Detected in ' + CONFIG_DICT['prod_location_city'] + ', ' + CONFIG_DICT['prod_location_country'])
            mailer.send_mail(settings.CONFIG_DICT['smtp_server'], settings.CONFIG_DICT['smtp_port'], settings.CONFIG_DICT['smtp_sender_email'],
                             settings.CONFIG_DICT['smtp_receiver_email'], settings.CONFIG_DICT['smtp_password'], "Earthquake Detected")
            protect("Earthquake", CONFIG_DICT['repl_replicate'])
        else:
            logger.info('No natural hazards')

        logger.info('> Waiting ' + str(int(CONFIG_DICT['frequency_check'])/60).split('.')[0] + ' minutes before checking')

        time.sleep(int(CONFIG_DICT['frequency_check']))  # Sleep for defined frequency_check

        # Test connectivity
        try:
            da.test_connection(settings.DVX)
        except:
            mailer.send_mail(settings.CONFIG_DICT['smtp_server'], settings.CONFIG_DICT['smtp_port'], settings.CONFIG_DICT['smtp_sender_email'],
                             settings.CONFIG_DICT['smtp_receiver_email'], settings.CONFIG_DICT['smtp_password'], "Connection to DVX Failed")
            raise


main()
