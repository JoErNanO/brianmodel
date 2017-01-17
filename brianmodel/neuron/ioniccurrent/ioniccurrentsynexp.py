#!/usr/bin/python
# coding: utf-8

# #################################################################################
# Copyright (C) 2015 Francesco Giovannini, Neurosys - INRIA CR Nancy - Grand Est
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
    ioniccurrentsynexp
    ~~~~~~~~~~~~~~~~~~
    This module contains the implementation of a synaptic current based on exponential synapses.
    The resulting synaptic current is excitatory or inhibitory depending on the reversal
    potential of the ion channel:
        - Reversal potential < membrane resting potential yields inhibitory synapse
        - Reversal potential > membrane resting potential yields excitatory synapse

    :copyright 2015 Francesco Giovannini, Neurosys - INRIA CR Nancy - Grand Est
    :licence GPLv3, see LICENCE for more details
"""


from utilities import utilities as utilities
from ioniccurrent import IonicCurrent


## ***************************************************************************************************************** ##
class IonicCurrentSynExp(IonicCurrent):
    """
    The :class:`IonicCurrentSynExp`` represents a synaptic current based on exponential synapses.

    Initialised as:

        IonicCurrentSynExp(area, parameters)

    with arguments:

        ``params``
        The model parameters for the :class:`IonicCurrent` (dict)

        ``area``
        The cell area (string)


    References:
    """

    ## ************************************************************ ##
    def __init__(self, params, area):
        """
        Default constructor.

        :param parameters: the model parameters for the :class:`IonicCurrent`
        :type parameters: dictionary
        :param area: the cell area
        :type area: string
        """

        # Initialise attributes
        IonicCurrent.__init__(self, params, area)
        self.tau = params['tau']

        # Initialise attributes
        IonicCurrent.__init__(self, params, area)
        self._tau = utilities.getSafeStringParam(self.tau)
    ## ************************************************************ ##


    ## ************************************************************ ##
    def getIonicCurrentString(self):
        """
        Generate the string representation of the ionic current.
        """

        ISyn = \
            self.name + ''' = + ''' + self.g + ''' * (v - ''' + self._E  + ''') : amp
            d''' + self.g + '''/dt = -''' + self.g  + ''' * (1. / ''' + self._tau + ''') : siemens
        '''

        return ISyn
    ## ************************************************************ ##
## ***************************************************************************************************************** ##
