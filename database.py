"""A database encapsulating collections of near-Earth objects and their close approaches.

A `NEODatabase` holds an interconnected data set of NEOs and close approaches.
It provides methods to fetch an NEO by primary designation or by name, as well
as a method to query the set of close approaches that match a collection of
user-specified criteria.

Under normal circumstances, the main module creates one NEODatabase from the
data on NEOs and close approaches extracted by `extract.load_neos` and
`extract.load_approaches`.

You'll edit this file in Tasks 2 and 3.
"""

from functools import reduce

class NEODatabase:
    """A database of near-Earth objects and their close approaches.

    A `NEODatabase` contains a collection of NEOs and a collection of close
    approaches. It additionally maintains a few auxiliary data structures to
    help fetch NEOs by primary designation or by name and to help speed up
    querying for close approaches that match criteria.
    """
    def __init__(self, neos, approaches):
        """Create a new `NEODatabase`.

        As a precondition, this constructor assumes that the collections of NEOs
        and close approaches haven't yet been linked - that is, the
        `.approaches` attribute of each `NearEarthObject` resolves to an empty
        collection, and the `.neo` attribute of each `CloseApproach` is None.

        However, each `CloseApproach` has an attribute (`._designation`) that
        matches the `.designation` attribute of the corresponding NEO. This
        constructor modifies the supplied NEOs and close approaches to link them
        together - after it's done, the `.approaches` attribute of each NEO has
        a collection of that NEO's close approaches, and the `.neo` attribute of
        each close approach references the appropriate NEO.

        :param neos: A collection of `NearEarthObject`s.
        :param approaches: A collection of `CloseApproach`es.
        """
        self._neos = neos
        self._approaches = approaches

        # TODO: What additional auxiliary data structures will be useful?
        # As per data one designation is associated with only one NEO
        self._neos_by_designation = {} # str -> NearEarthObject

        # There can be multiple NEOs associated with same name
        self._neos_by_name = {} # str -> list[str]

        '''
        Iterating over all the NEOs and creating dictionary for storing -
        1. neo desgination -> list of neos
        2. neo name -> list of neo designation
        '''
        for _neo in self._neos:
            # Creating a dictionary storing neo desgination and list of neos
            self._neos_by_designation[_neo.designation] = _neo

            # Creating a dictionary storing neo name and list of neo designation
            if _neo.name in self._neos_by_name:
                self._neos_by_name[_neo.name].append(_neo.designation)
            else:
                self._neos_by_name[_neo.name] = [_neo.designation]

        # TODO: Link together the NEOs and their close approaches.
        '''
        Iterating over all the CloseApproach -
            1. Find neo by designation in `_neos_by_designation`
            2. Updating neos approaches in `_neos_by_designation`
            3. Associating neo with CloseApproach
        '''
        for index, cad in enumerate(self._approaches):
            if cad._designation in self._neos_by_designation:
                cur_neo = self._neos_by_designation[cad._designation]

                # Updating approach details in the NEO
                self._neos_by_designation[cad._designation].approaches.append(cad)

                # Updating NEO info in the CloseApproach
                self._approaches[index].neo = cur_neo

    def get_neo_by_designation(self, designation):
        """Find and return an NEO by its primary designation.

        If no match is found, return `None` instead.

        Each NEO in the data set has a unique primary designation, as a string.

        The matching is exact - check for spelling and capitalization if no
        match is found.

        :param designation: The primary designation of the NEO to search for.
        :return: The `NearEarthObject` with the desired primary designation, or `None`.
        """
        # TODO: Fetch an NEO by its primary designation.
        return self._neos_by_designation[designation] if designation in self._neos_by_designation else None

    def get_neo_by_name(self, name):
        """Find and return an NEO by its name.

        If no match is found, return `None` instead.

        Not every NEO in the data set has a name. No NEOs are associated with
        the empty string nor with the `None` singleton.

        The matching is exact - check for spelling and capitalization if no
        match is found.

        :param name: The name, as a string, of the NEO to search for.
        :return: The `NearEarthObject` with the desired name, or `None`.
        """
        # TODO: Fetch an NEO by its name.
        return self.get_neo_by_designation(self._neos_by_name[name][0]) if name in self._neos_by_name else None

    def query(self, filters):
        """Query close approaches to generate those that match a collection of filters.

        This generates a stream of `CloseApproach` objects that match all of the
        provided filters.

        If no arguments are provided, generate all known close approaches.

        The `CloseApproach` objects are generated in internal order, which isn't
        guaranteed to be sorted meaninfully, although is often sorted by time.

        :param filters: A collection of filters capturing user-specified criteria.
        :return: A stream of matching `CloseApproach` objects.
        """
        # TODO: Generate `CloseApproach` objects that match all of the filters.
        for approach in self._approaches:
            is_valid = True
            for f in filters:
                is_valid = is_valid and f(approach)
            if is_valid:
                yield approach
