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
    ioniccurrenthhtraub
    ~~~~~~~~~~~~~
    This module contains the Hodgkin-Huxley neuron ionic currents, as defined in (Traub and Miles).
    These are leak, Potassium (K) and Sodium (Na) currents.


    References:
        - Traub and Miles, Neuronal Networks of the Hippocampus, Cambridge, 1991


    :copyright 2014 Francesco Giovannini, Neurosys - INRIA CR Nancy - Grand Est
    :licence GPLv3, see LICENCE for more details
"""


from utilities import utilities as utilities
from ioniccurrent import IonicCurrent


## ***************************************************************************************************************** ##
class IonicCurrentHHTraubLeak(IonicCurrent):
    """
    The :class:`IonicCurrentHHTraubLeak`` represents the Hodgkin-Huxley neuron leak current, as defined in (Traub and Miles), and its string representation.

    Initialised as:

        IonicCurrentHHTraubLeak(params, area)

    with arguments:

        ``params``
        The model parameters for the :class:`IonicCurrent` (dict)

        ``area``
        The cell area (string)
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
    ## ************************************************************ ##


    ## ************************************************************ ##
    def getIonicCurrentString(self):
        """
        Generate the string representation of the ionic current.
        """

        leak = self.name + ''' = ''' + self._g + ''' * (v - ''' + self._E  + ''') : amp \n'''

        return leak
    ## ************************************************************ ##
## ***************************************************************************************************************** ##


## ***************************************************************************************************************** ##
class IonicCurrentHHTraubK(IonicCurrent):
    """
    The :class:`IonicCurrentHHTraubK` represents the Hodgkin-Huxley neuron Potassium current, as defined in (Traub and Miles), and its string representation.

    Initialised as:

        IonicCurrentHHTraubK(params, area)

    with arguments:

        ``params``
        The model parameters for the :class:`IonicCurrent` (dict)

        ``area``
        The cell area (string)
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
        self.vT = params['vT']

        # Store safe string representation of parameters
        self._vT = utilities.getSafeStringParam(self.vT)
    ## ************************************************************ ##


    ## ************************************************************ ##
    def getIonicCurrentString(self):
        """
        Generate the string representation of the ionic current.
        """

        potassium = \
            self.name + ''' = ''' + self._g + ''' * (n ** 4) * (v - ''' + self._E  + ''') : amp
            dn/dt = alphan * (1 - n) - betan * n : 1
            alphan =  - 0.032 * (mV ** -1) * (v  - ''' + self._vT + ''' - 15 * mV) / (exp(- (v - ''' + self._vT + ''' - 15 * mV) / (5 * mV)) - 1.) / ms : Hz
            betan = 0.5 * exp( - (v - ''' + self._vT + ''' - 10 * mV) / (40 * mV)) / ms : Hz
        '''

        return potassium
    ## ************************************************************ ##
## ***************************************************************************************************************** ##


## ***************************************************************************************************************** ##
class IonicCurrentHHTraubNa(IonicCurrent):
    """
    The :class:`IonicCurrentHHTraubNa` represents the Hodgkin-Huxley neuron Sodium current, as defined in (Traub and Miles), and its string representation.

    Initialised as:

        IonicCurrentHHTraubNa(params, area)

    with arguments:

        ``params``
        The model parameters for the :class:`IonicCurrent` (dict)

        ``area``
        The cell area (string)
    """

    ## ************************************************************ ##
    def __init__(self,params, area):
        """
        Default constructor.

        :param parameters: the model parameters for the :class:`IonicCurrent`
        :type parameters: dictionary
        :param area: the cell area
        :type area: string
        """

        # Initialise attributes
        IonicCurrent.__init__(self, params, area)
        self.vT = params['vT']

        # Store safe string representation of parameters
        self._vT = utilities.getSafeStringParam(self.vT)
    ## ************************************************************ ##


    ## ************************************************************ ##
    def getIonicCurrentString(self):
        """
        Generate the string representation of the ionic current.
        """

        sodium = \
            self.name + ''' = ''' + self._g + ''' * (m ** 3) * h * (v - ''' + self._E  + ''') : amp
            dm/dt = alpham * (1 - m) - betam * m : 1
            dh/dt = alphah * (1 - h) - betah * h : 1
            alpham = - 0.32 * (mV ** -1) * (v - ''' + self._vT + ''' - 13 * mV) / (exp(- (v - ''' + self._vT + ''' - 13 * mV) / (4 * mV)) - 1.) / ms : Hz
            betam = 0.28 * (mV ** -1) * (v - ''' + self._vT + ''' - 40 * mV) / (exp((v - ''' + self._vT + ''' - 40 * mV) / (5 * mV)) - 1.) / ms : Hz
            alphah = 0.128 * exp(- (v - ''' + self._vT + ''' - 17 * mV) / (18 * mV)) / ms : Hz
            betah = 4. / (1 + exp(- (v - ''' + self._vT + ''' - 40 * mV) / (5 * mV))) / ms : Hz
        '''

        return sodium
    ## ************************************************************ ##
## ***************************************************************************************************************** ##
