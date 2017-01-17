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
    ioniccurrentcat
    ~~~~~~~~~~~~~
    This module contains various implementations of the neuronal transient, low-voltage-activated Calcium current.

    References:
        - Huguenard, J. R., & McCormick, D. A. (1992). Simulation of the Currents Involved in Rhythmic Oscillations in Thalamic Relay Neurons. Journal of Neurophysiology, 68(4).
            http://jn.physiology.org/content/68/4/1373
        - Mccormick, D. A., & Huguenard, J. R. (1992). A Model of the Electrophysiological Properties of Thalamocortical Relay Neurons. Journal of Neurophysiology, 68(4), 1384–1400.
            http://jn.physiology.org/content/68/4/1384

    :copyright 2015 Francesco Giovannini, Neurosys - INRIA CR Nancy - Grand Est
    :licence GPLv3, see LICENCE for more details
"""



from utilities import utilities as utilities
from ioniccurrent import IonicCurrent

## ***************************************************************************************************************** ##
class IonicCurrentCaTHuguenard(IonicCurrent):
    """
    The :class:`IonicCurrentCaTHuguenard`` represents the transient, low-voltage-activated Calcium current, as defined in (Huguenard et al.), and its string representation.

    Initialised as:

        IonicCurrentCaTHuguenard(area, parameters)

    with arguments:

        ``params``
        The model parameters for the :class:`IonicCurrent` (dict)

        ``area``
        The cell area (string)


    References:
        - Huguenard, J. R., & McCormick, D. A. (1992). Simulation of the Currents Involved in Rhythmic Oscillations in Thalamic Relay Neurons. Journal of Neurophysiology, 68(4).
            http://jn.physiology.org/content/68/4/1373
        - Mccormick, D. A., & Huguenard, J. R. (1992). A Model of the Electrophysiological Properties of Thalamocortical Relay Neurons. Journal of Neurophysiology, 68(4), 1384–1400.
            http://jn.physiology.org/content/68/4/1384
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
        self.q10 = params.get('q10', '3')   # Q10 of inactivation
        self.tempC = params.get('tempC', '36 * celsius')

        # Store safe string representation of parameters
        # self._tempK = utilities.getSafeStringParam(self.tempK)
        self._tau = utilities.getSafeStringParam(self.tau)
        self._caInf = utilities.getSafeStringParam(self.caInf)
        self._kUnit = utilities.getSafeStringParam(self.kUnit)
        self._kFaraday = utilities.getSafeStringParam(self.kFaraday)
        self._depth = utilities.getSafeStringParam(self.depth)
        self._tempC = utilities.getSafeStringParam(self.tempC)
        self._q10 = utilities.getSafeStringParam(self.q10)
    ## ************************************************************ ##


    ## ************************************************************ ##
    def getIonicCurrentString(self):
        """
        Generate the string representation of the ionic current.
        """

        calciumL = \
            self.name + ''' = ''' + self._g + ''' * (mCaT ** 2) * hCaT * (v - ''' + self._E  + ''') : amp
            dhCaT/dt = (hCaTInf - hCaT) / hCaTTau : 1
            mCaT = 1. / (1 + exp(-(v + (57 * mV)) / (6.2 * mV))) : 1
            hCaTInf = 1. / (1 + exp((v + (81 * mV)) / (4. * mV))) : 1
            hCaTTau = ((30.8 + (211.4 + exp((v + (113.2 * mV)) / (5 * mV))) / (1. + exp((v + (84 * mV)) / (3.2 * mV)))) / (hCaTPhi)) * ms : ms
            #hCaTPhi = ''' + self._q10 + ''' ** ((''' + self._tempC + ''' - (24 * celsius)) / (10 * celsius)) : 1
            hCaTPhi = 3.737192819 : 1

            ECa : volt
        '''

        calciumL += self.__calciumDecay()

        return calciumL
    ## ************************************************************ ##


    ## ************************************************************ ##
    def __calciumDecay(self):
        res = '''
            dCa_i/dt = driveChannel + (''' + self._caInf + ''' - Ca_i) /  ''' + self._tau  + ''' : mole * meter**-3
            #Ca_i : mole * meter**-3
            driveChannel = (-''' + self._kUnit + ''' * I_Ca / (cm ** 2)) / (2 * ''' + self._kFaraday + ''' * ''' + self._depth + ''') : mole * meter ** -3 * Hz
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
