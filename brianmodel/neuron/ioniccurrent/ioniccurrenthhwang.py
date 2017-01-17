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
    ioniccurrenthhwang
    ~~~~~~~~~~~~~
    This module contains the Hodgkin-Huxley neuron ionic currents, as defined by Wang and Buzsaki in [1].
    The current equations have been modified by Kopell et al. in [2] to factor out the phi parameter introduced in the original W-B model.
    These are leak, Potassium (K) and Sodium (Na) currents.


    References:
        - [1] Wang X-J, Buzsáki G: Gamma oscillation by synaptic inhibition in a hippocampal interneuronal network model. J Neurosci 1996, 16:6402–13.
        - [2] Kopell NJ, Boergers C, Pervouchine D, Malerba P, Tort A: Gamma and theta rhythms in biophysical models of hippocampal circuits. In Hippocampal Microcircuits A Computational Modeler’s Resource Book. Edited by Cutsuridis V, Graham B, Cobb S, Vida I. New York, NY: Springer New York; 2010:423–457.


    :copyright 2015 Francesco Giovannini, Neurosys - INRIA CR Nancy - Grand Est
    :licence GPLv3, see LICENCE for more details
"""


from utilities import utilities as utilities
from ioniccurrent import IonicCurrent


## ***************************************************************************************************************** ##
class IonicCurrentHHWangLeak(IonicCurrent):
    """
    The :class:`IonicCurrentHHWangLeak`` represents the Hodgkin-Huxley neuron leak current, as defined in (Wang and Buzsaki), and its string representation.

    Initialised as:

        IonicCurrentHHWangLeak(params, area)

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
class IonicCurrentHHWangK(IonicCurrent):
    """
    The :class:`IonicCurrentHHWangK` represents the Hodgkin-Huxley neuron Potassium current, as defined in (Wang and Buzsaki), and its string representation.

    Initialised as:

        IonicCurrentHHWangK(params, area)

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

        :return potassium: string representation of the Potassium current
        :type: string
        """

        potassium = \
            self.name + ''' = ''' + self._g + ''' * (n ** 4) * (v - ''' + self._E  + ''') : amp
            dn/dt = (n_inf - n) / tau_n : 1
            n_inf = alphan / (alphan + betan) : 1
            tau_n = 0.2 / (alphan + betan) : ms
            alphan = 0.01 * (mV ** -1) * (v  + 34 * mV) / (1. - exp(- 0.1 * (mV ** -1) * (v + 34 * mV))) / ms : Hz
            betan = 0.125 * exp( - (v + 44 * mV) / (80 * mV)) / ms : Hz
        '''

        return potassium
    ## ************************************************************ ##
## ***************************************************************************************************************** ##


## ***************************************************************************************************************** ##
class IonicCurrentHHWangNa(IonicCurrent):
    """
    The :class:`IonicCurrentHHWangNa` represents the Hodgkin-Huxley neuron Sodium current, as defined in (Wang and Buzsaki), and its string representation.

    Initialised as:

        IonicCurrentHHWangNa(params, area)

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
    ## ************************************************************ ##


    ## ************************************************************ ##
    def getIonicCurrentString(self):
        """
        Generate the string representation of the ionic current.
        The m gating variable should be replaced by its steady state value m_inf as in the W-B model.
        Brian doesn't like this as it makes the equations stiff, and gives rise to the mind-numbingly useless "TypeError: General implicit methods are not implemented yet." error message.

        :return sodium: string representation of the Sodium current
        :type: string
        """

        sodium = \
            self.name + ''' = ''' + self._g + ''' * (m ** 3) * h * (v - ''' + self._E  + ''') : amp
            dm/dt = (m_inf - m) / tau_m : 1
            dh/dt = (h_inf - h) / tau_h : 1
            m_inf = alpham / (alpham + betam)  : 1
            tau_m = 0.2 / (alpham + betam) : ms
            h_inf = alphah / (alphah + betah) : 1
            tau_h = 0.2 / (alphah + betah) : ms
            alpham = 0.1 * (mV ** -1) * (v + 35 * mV) / (1. - exp(- (v + 35 * mV) / (10 * mV))) / ms : Hz
            betam = 4 * exp(- (v + 60 * mV) / (18 * mV)) / ms : Hz
            alphah = 0.07 * exp(- (v + 58 * mV) / (20 * mV)) / ms : Hz
            betah = 1. / (exp((- 0.1 * (mV ** -1)) * (v + 28 * mV)) + 1.) / ms : Hz
        '''

        return sodium
    ## ************************************************************ ##
## ***************************************************************************************************************** ##
