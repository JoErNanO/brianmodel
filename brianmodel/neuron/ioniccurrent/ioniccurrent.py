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
    ioniccurrent
    ~~~~~~~~~~~~~
    This module contains the abstract base class for Brian-compatible ionic currents flowing through the membrane of a neural cell.

    :copyright 2014 Francesco Giovannini, Neurosys - INRIA CR Nancy - Grand Est
    :licence GPLv3, see LICENCE for more details
"""


from utilities import utilities as utilities

from abc import ABCMeta, abstractmethod


## ***************************************************************************************************************** ##
class IonicCurrent(object):
    """
    The :class:`IonicCurrent` represents the ionic currents flowing through the cell membrane, and their Brian-compatible string representation.
    This is the base class for various types of currents.
    """

    # Define this as an abstract class
    __metaclass__ = ABCMeta


    ## ************************************************************ ##
    def __init__(self, parameters, area):
        """
        Default constructor.

        :param parameters: the model parameters for the :class:`IonicCurrent`
        :type parameters: dictionary
        :param area: the cell area
        :type area: string
        """

        # Initialise attributes
        self.name = parameters['name']
        self.g = parameters['g']
        self.E = parameters['E']

        # Store safe string representation of parameters
        self._g = utilities.getSafeStringParam(utilities.getSafeStringParam(self.g) + ' * '  + utilities.getSafeStringParam(area))
        self._E = utilities.getSafeStringParam(self.E)
    ## ************************************************************ ##


    ## ************************************************************ ##
    @abstractmethod
    def getIonicCurrentString(self):
        """
        Generate the string representation of the ionic current.
        """

        pass
    ## ************************************************************ ##
## ***************************************************************************************************************** ##
