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
    ioniccurrentcal
    ~~~~~~~~~~~~~~~
    This module contains various implementations of the neuronal Calcium current flowing through L-type channels.

    References:
        - http://en.wikipedia.org/wiki/L-type_calcium_channel
        - Reuveni I; Friedman A; Amitai Y; Gutnick MJ. Stepwise repolarization from Ca2+ plateaus in neocortical pyramidal cells: evidence for nonhomogeneous distribution of HVA Ca2+ channels in dendrites. Journal of Neuroscience, 1993 Nov, 13(11):4609-21.

    :copyright 2014 Francesco Giovannini, Neurosys - INRIA CR Nancy - Grand Est
    :licence GPLv3, see LICENCE for more details
"""


from utilities import utilities as utilities
from ioniccurrent import IonicCurrent

## ***************************************************************************************************************** ##
class IonicCurrentCaLReuveni(IonicCurrent):
    """
    The :class:`IonicCurrentCaLReuveni`` represents the L-type Calcium current, as defined in (Reuveni et al.), and its string representation.

    Initialised as:

        IonicCurrentCaLReuveni(area, parameters)

    with arguments:

        ``params``
        The model parameters for the :class:`IonicCurrent` (dict)

        ``area``
        The cell area (string)


    References:
        - Reuveni I; Friedman A; Amitai Y; Gutnick MJ. Stepwise repolarization from Ca2+ plateaus in neocortical pyramidal cells: evidence for nonhomogeneous distribution of HVA Ca2+ channels in dendrites. Journal of Neuroscience, 1993 Nov, 13(11):4609-21.
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
        # self.tempK = "(" + params['temp'] + " + 273.15) * kelvin"
        self.tau = params['tau']
        self.caInf = params['caInf']
        self.kUnit = params['kUnit']
        self.kFaraday = params['kFaraday']
        self.depth = params['depth']

        # Store safe string representation of parameters
        # self._tempK = utilities.getSafeStringParam(self.tempK)
        self._tau = utilities.getSafeStringParam(self.tau)
        self._caInf = utilities.getSafeStringParam(self.caInf)
        self._kUnit = utilities.getSafeStringParam(self.kUnit)
        self._kFaraday = utilities.getSafeStringParam(self.kFaraday)
        self._depth = utilities.getSafeStringParam(self.depth)
    ## ************************************************************ ##


    ## ************************************************************ ##
    def getIonicCurrentString(self):
        """
        Generate the string representation of the ionic current.
        """

        calciumL = \
            self.name + ''' = ''' + self._g + ''' * (mCaL ** 2) * hCaL * (v - ''' + self._E  + ''') : amp
            dmCaL/dt = (alphamCaL * (1 - mCaL)) - (betamCaL * mCaL) : 1
            dhCaL/dt = (alphahCaL * (1 - hCaL)) - (betahCaL * hCaL) : 1
            alphamCaL = (0.055 * mV ** -1) * ((-27 * mV) - v) / (exp(((-27 * mV) - v) / (3.8 * mV)) - 1.) / ms : Hz
            betamCaL = 0.94 * exp(((-75 * mV) - v) / (17 * mV)) / ms : Hz
            alphahCaL = 0.000457 * exp(((-13 * mV) - v) / (50 * mV)) / ms : Hz
            betahCaL = 0.0065 / (exp(((-15 * mV) - v) / (28 * mV)) + 1.) / ms : Hz
            #ECa : volt
        '''

        calciumL += self.__calciumDecay()

        return calciumL
    ## ************************************************************ ##


    ## ************************************************************ ##
    def __calciumDecay(self):
        res = '''
            dCa_i/dt = driveChannel + (''' + self._caInf + ''' - Ca_i) /  ''' + self._tau  + ''' : mole * meter**-3
            #Ca_i : mole * meter**-3
            driveChannel = (-''' + self._kUnit + ''' * ''' + self.name + ''' / (cm ** 2)) / (2 * ''' + self._kFaraday + ''' * ''' + self._depth + ''') : mole * meter ** -3 * Hz
        '''

        return res
    ## ************************************************************ ##


    ## ************************************************************ ##
    def driveChannel(self, I_Ca):
        res = (-self.kUnit * I_Ca / ExcP['area']) / (2 * self.kFaraday * depthCa)
        res = (-kUnit * I_Ca / (cm ** 2)) / (2 * kFaraday * depthCa)

        # Cannot pump inward
        if not isinstance(res, Quantity):   # Check for first parser pass - upon initialisation this is a Quant#
            res[res < 0] = 0

        return res
    ## ************************************************************ ##
## ***************************************************************************************************************** ##
