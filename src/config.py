import os
from pconf import Pconf
import json

Pconf.env(separator='__')
Pconf.env()


def load_config_file(filename):
    '''
    Load all the configuration variables from config.json file
    '''


# Load the default config.json file
config_file = os.path.join(os.path.dirname(__file__), '../config.json')
if not os.path.isfile(config_file):
    print('Warning: Could not find configuration file \'{file}\''.format(
        file=config_file))
else:
    try:
        # Check that the file is correct json format
        with open(config_file, 'r') as f:
            json.load(f)
    except json.JSONDecodeError:
        raise ValueError(
            '\'{file}\' is not a valid json file. Please check the format'
            .format(file=config_file))
    except FileNotFoundError:
        raise FileNotFoundError(
            '\'{file}\' not found. Please check the path'
            .format(file=config_file))
    print('Loading config file \'{filename}\''.format(filename=config_file))
    Pconf.file(config_file, encoding='json')

# Get all the config values parsed from the sources
config = Pconf.get()
