#!/usr/bin/python
# coding: utf-8

# #################################################################################
# Copyright (C) 2014 Francesco Giovannini, Neurosys - INRIA CR Nancy - Grand Est
# Authors: Francesco Giovannini
# email: francesco.giovannini@inria.fr
# website: http://neurosys.loria.fr/
# Permission is granted to copy, distribute, and/or modify this program
# under the terms of the GNU General Public License, version 3 or any
# later version published by the Free Software Foundation.
#
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
# Public License for more details
# #################################################################################



"""
    neuron
    ~~~~~~~~~~~~~
    This module contains an abstraction of a Brian-compatible neuron, represented as a cell with a list of :class:`IonicCurrent`'s.

    :copyright 2014 Francesco Giovannini, Neurosys - INRIA CR Nancy - Grand Est
    :licence GPLv3, see LICENCE for more details
"""


from utilities import utilities as utilities
import ioniccurrent.ioniccurrentfactory as icf

import yaml

## ***************************************************************************************************************** ##
class Neuron(object):
    """
    The :class:`Neuron` represents a biological neuron with a set of properties, and a list of :class:`IonicCurrent`'s flowing through its membrane.
    """

    ## ************************************************************ ##
    def __init__(self, parameters):
        """
        Default constructor.

        :param area: the area of the soma of the neural cell
        :type area: float
        :param conductance: the conductance of the neural cell
        :type conductance: float
        """

        # Initialise attributes
        self.parameters = parameters.values()[0]
        self.name = parameters.keys()[0]
        self.area = self.parameters['area']
        self.conductance = self.parameters['conductance']

        # Initialise list of defined currents - FG: fixes bug due to having an empty list of defined currents when including all the needed ones
        if 'defined' not in self.parameters['currents']: # Keyword 'defined' doesn't exists
            self.parameters['currents']['defined'] = []
        elif self.parameters['currents']['defined'] is None: # List of 'defined' currents is undefined/empty
            self.parameters['currents']['defined'] = []

        # Check for parameters specified as include files
        for f in self.parameters['currents'].get('included', []):
            try:
                with open(f) as curr:
                    # Load included currents from file
                    includes = yaml.load(curr)

                    # Add them the list of defined currents
                    self.parameters['currents'].get('defined', []).extend(includes)
            except IOError:
                raise IOError('Cannot load current parameter file named ' + f)
        # Remove list of includesd currents from dict of currents
        self.parameters['currents'].pop('included', [])

        # Initialise ionic current factory
        self.factory = icf.IonicCurrentFactory()

        # Build current list
        self.currents = []
        for currentParams in self.parameters['currents'].get('defined', []):
            tmpCurrent = self.factory.makeIonicCurrent(currentParams, self.area)
            self.currents.append(tmpCurrent)

        # Store safe string representation of parameters
        self._area = utilities.getSafeStringParam(self.area)
        self._conductance = utilities.getSafeStringParam(utilities.getSafeStringParam(self.conductance) + ' * '  + self._area)
    ## ************************************************************ ##


    ## ************************************************************ ##
    def getNeuronString(self):
        """
        Generate the string representation of the neural cell model.
        """

        res = ""

        # Neuron model equation
        dvdt = '''dv/dt = ('''

        # Add current equations
        for curr in self.currents:
            dvdt += ''' - ''' + curr.name # Add current name to dvdt equation
            res += curr.getIonicCurrentString() # Add current equation to neuron model

        dvdt += ''' + I_stim) / ''' + self._conductance + ''' : volt \n''' # Append conductance division

        # Check Voltage clamp
        if self.parameters.has_key('vClamp') and self.parameters['vClamp']:
            dvdt = '''v : volt \n'''

        # Stimulus current
        istim = '''I_stim : amp'''

        # Build final neuron model equation
        res = dvdt + res + istim

        return res
    ## ************************************************************ ##
## ***************************************************************************************************************** ##
