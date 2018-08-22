# encoding: utf-8
"""
Configuration Module
"""

import json
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # This is your Project Root
CONFIG_PATH = os.path.join(ROOT_DIR, 'config.json')


def save_json_file(filepath, data):
    """ Saves JSON Data to File"""
    with open(filepath, 'w') as outfile:
        try:
            json.dump(data, outfile, indent=2)
        except ValueError:
            return False
        return True


def get_json_file(filepath):
    """ Get Data from cached file """
    if not os.path.exists(filepath):
        return None
    with open(filepath) as stream:
        try:
            return json.load(stream)
        except ValueError:
            return None


# noinspection PyMethodMayBeStatic
class Config(object):
    """
    Class to handle configuration file
    """

    def __init__(self):
        pass

    def get(self):
        """
        Retrieve config from file
        """
        return get_json_file(CONFIG_PATH)

    def save(self, config_object):
        """
        Save config to file
        """
        return save_json_file(CONFIG_PATH, config_object)
