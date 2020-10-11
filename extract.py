"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """

    """ A list for keeping all the `NearEarthObject`s created from each CSV row """
    neo_list = []

    with open(neo_csv_path, 'r') as neo_file_obj:
        reader = csv.DictReader(neo_file_obj)

        """ Reading each row in the CSV file, creating `NearEarthObject` and adding to the list """
        for entry in reader:
            neo_list.append(NearEarthObject(**entry))

    return neo_list


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """

    """ A list for keeping all the `CloseApproach`s created from each JSON `data` entry """
    cad_list = []

    with open(cad_json_path, 'r') as cad_file_obj:
        json_reader = json.loads(cad_file_obj.read())

        cad_fields = json_reader['fields']
        for entry in json_reader['data']:
            cad = {}
            for index, value in enumerate(cad_fields):
                cad[value] = entry[index]
            cad_list.append(CloseApproach(**cad))

    return cad_list
