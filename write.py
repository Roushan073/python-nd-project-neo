"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json


# /Users/roushan-kumar/Downloads/Udacity/python-nd-project-1/data/write-test.csv
def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = ('datetime_utc', 'distance_au', 'velocity_km_s', 'designation', 'name', 'diameter_km', 'potentially_hazardous')
    # TODO: Write the results to a CSV file, following the specification in the instructions.
    print("Writing data to: {}".format(filename))
    with open(filename, mode='w') as neo_file:
        neo_writer = csv.writer(neo_file, delimiter=',')
        neo_writer.writerow(fieldnames)
        for row in results:
            ser_approach = row.serialize()
            ser_neo = ser_approach['neo']
            neo_writer.writerow([ser_approach['datetime_utc'], ser_approach['distance_au'], ser_approach['velocity_km_s'],
                                 ser_neo['designation'], ser_neo['name'], ser_neo['diameter_km'],
                                 ser_neo['potentially_hazardous']])
    print("Written data to: {}".format(filename))


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    # TODO: Write the results to a JSON file, following the specification in the instructions.
    print("Writing data to: {}".format(filename))
    with open(filename, mode='w') as neo_file:
        approach_list = []
        for row in results:
            approach_list.append(row.serialize())
        json_object = json.dumps(approach_list, indent=4)
        neo_file.write(json_object)
    print("Written data to: {}".format(filename))


'''
output_type = type(data[0]).__name__
# Write NearEarthObject Object
if output_type == "NearEarthObject":
    output_filename = f'{PROJECT_ROOT}/data/neo_output.csv'
    print("Writing data to: {}".format(output_filename))
    header = ["Neo Id", "Neo Name", "Orbits", "Orbit Date"]
    with open(output_filename, mode='w') as neo_file:
        neo_writer = csv.writer(neo_file, delimiter=',')
        neo_writer.writerow(header)
        for row in data:
            neo_writer.writerow([str(row.id), str(row.name), str(len(row.orbits)), str(", ".join(map(lambda o: o.close_approach_date, row.orbits)))])
    print("Written data to: {}".format(output_filename))
'''