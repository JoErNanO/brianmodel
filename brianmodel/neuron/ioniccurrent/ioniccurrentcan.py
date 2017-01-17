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
    ioniccurrentcan
    ~~~~~~~~~~~~~~~
    This module contains various implementations of the neuronal Ca_2+-activated nonselective cationic CAN current.

    References:
        - L.D. Partridge, D. Swandulla, Calcium-activated non-specific cation channels, Trends in Neurosciences, Volume 11, Issue 2, 1988, Pages 69-72, ISSN 0166-2236, http://dx.doi.org/10.1016/0166-2236(88)90167-1. http://www.sciencedirect.com/science/article/pii/0166223688901671
        - L.Donald Partridge, Thomas H. Müller, Dieter Swandulla, Calcium-activated non-selective channels in the nervous system, Brain Research Reviews, Volume 19, Issue 3, August 1994, Pages 319-325, ISSN 0165-0173, http://dx.doi.org/10.1016/0165-0173(94)90017-5. (http://www.sciencedirect.com/science/article/pii/0165017394900175

    :copyright 2014 Francesco Giovannini, Neurosys - INRIA CR Nancy - Grand Est
    :licence GPLv3, see LICENCE for more details
"""


from utilities import utilities as utilities
from ioniccurrent import IonicCurrent

## ***************************************************************************************************************** ##
class IonicCurrentCANDestexhe(IonicCurrent):
    """
    The :class:`IonicCurrentCANDestexhe`` represents the L-type Calcium current, as defined in (Desthexe 1992), and its string representation.

    Initialised as:

        IonicCurrentCANDestexhe(area, parameters)

    with arguments:

        ``params``
        The model parameters for the :class:`IonicCurrent` (dict)

        ``area``
        The cell area (string)


    References:
    - Destexhe, A., Contreras, D., Sejnowski, T. J., & Steriade, M. (1994). A model of spindle rhythmicity in the isolated thalamic reticular nucleus. Journal of Neurophysiology, 72(2), 803-18. http://www.ncbi.nlm.nih.gov/pubmed/7527077
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
        self.beta = params['beta']
        self.cac = params['cac']
        self.tempAdj = "3.0 ** ((" + params['temp'] + " -22) / 10)"


        # Store safe string representation of parameters
        self._beta = utilities.getSafeStringParam(self.beta)
        self._cac = utilities.getSafeStringParam(self.cac)
        self._tempAdj = utilities.getSafeStringParam(self.tempAdj)
    ## ************************************************************ ##


    ## ************************************************************ ##
    def getIonicCurrentString(self):
        """
        Generate the string representation of the ionic current.
        """

        can = \
            self.name + ''' =  ''' +  self._g + ''' * mCAN ** 2 * (v - ''' + self._E  + ''') : amp
            #ds/dt = (alphas * (1 - mCAN)) - (betas * mCAN) : 1
            #alphas = alpha2(Ca_i) * tempAdj : Hz
            #betas = betaCan * tempAdj : Hz
            dmCAN/dt = (mCANInf - mCAN) / mCANTau : 1
            mCANInf = alpha2 / (alpha2 + ''' + self._beta + ''') : 1
            mCANTau = 1. / (alpha2 + ''' + self._beta + ''') / ''' + self._tempAdj  + ''' : second
        '''

        can += self.__alpha2()

        return can
    ## ************************************************************ ##


    ## ************************************************************ ##
    def __alpha2(self):
        res = '''alpha2 = ''' + self._beta + ''' * (Ca_i / ''' + self._cac  + ''') ** 2 : Hz \n'''
        return res
    ## ************************************************************ ##
## ***************************************************************************************************************** ##
