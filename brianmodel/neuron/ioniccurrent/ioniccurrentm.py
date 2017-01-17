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
    ioniccurrentm
    ~~~~~~~~~~~~~
    This module contains various implementations of the cortical M non-inactivating potassium current.
    Being a potassium current, it uses the potassium reversal potential in its equations.

    References:
        - Wikipedia, M current, http://en.wikipedia.org/wiki/M_current
        - McCormick, D.A., Wang, Z. and Huguenard, J. Neurotransmitter control of neocortical neuronal activity and excitability. Cerebral Cortex 3: 387-398, 1993.


    :copyright 2014 Francesco Giovannini, Neurosys - INRIA CR Nancy - Grand Est
    :licence GPLv3, see LICENCE for more details
"""


from utilities import utilities as utilities
from ioniccurrent import IonicCurrent


## ***************************************************************************************************************** ##
class IonicCurrentMYamada(IonicCurrent):
    """
    The :class:`IonicCurrentMYamada`` represents the M current, as defined in (Yamada et al.), and its string representation.

    Initialised as:

        IonicCurrentMYamada(area, parameters)

    with arguments:

        ``params``
        The model parameters for the :class:`IonicCurrent` (dict)

        ``area``
        The cell area (string)


    References:
         - Yamada, W.M., Koch, C. and Adams, P.R.  Multiple  channels and calcium dynamics. In: Methods in Neuronal Modeling, edited by C. Koch and I. Segev, MIT press, 1989, p 97-134.
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

        # Store safe string representation of parameters
        self._tau = utilities.getSafeStringParam(self.tau)
    ## ************************************************************ ##


    ## ************************************************************ ##
    def getIonicCurrentString(self):
        """
        Generate the string representation of the ionic current.
        """

        m = \
            self.name + ''' = ''' + self._g + ''' * p * (v - ''' + self._E  + ''') : amp
            # dp/dt = alphap * (1 - p) - betap * p : 1
            # alphap = (1. / ''' + self._tau  + ''') * (3.3 * exp((v + 35 * mV) / (20. * mV)) + exp(-(v + 35 * mV) / (20. * mV)) / exp((-35 * mV - v) / (10 * mV)) + 1.) : Hz
            # betap = (1. / ''' + self._tau  + ''') * (3.3 * exp((v + 35 * mV) / (20. * mV)) + exp(-(v + 35 * mV) / (20. * mV))) * (1 - 1 / (exp((-35 * mV - v) / (10 * mV)) + 1.)): Hz
            dp/dt = (pInf - p) / pTau : 1
            pInf = 1. / (1 + exp(- (v + (35 * mV)) / (10 * mV))) : 1
            pTau = ''' + self._tau + ''' / (3.3 * exp((v + (35 * mV)) / (20 * mV)) + exp(- (v + (35 * mV)) / (20 * mV))) : ms
        '''

        return m
    ## ************************************************************ ##
## ***************************************************************************************************************** ##
