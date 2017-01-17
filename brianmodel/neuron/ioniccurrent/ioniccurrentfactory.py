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
    ioniccurrentfactory
    ~~~~~~~~~~~~~
    This module contains a factory class to generate :class:`IonicCurrent` objects.

    :copyright 2014 Francesco Giovannini, Neurosys - INRIA CR Nancy - Grand Est
    :licence GPLv3, see LICENCE for more details
"""


import ioniccurrenthhtraub as ichhtr
import ioniccurrenthhwang as ichhwa
import ioniccurrentm as icm
import ioniccurrentcal as iccal
import ioniccurrentcat as iccat
import ioniccurrentcan as iccan
import ioniccurrentsynexp as icsynexp


## ***************************************************************************************************************** ##
class IonicCurrentFactory(object):
    """
    The :class:`IonicCurrentFactory` represents a factory to generate class:`IonicCurrent` objects.
    """

    ## ************************************************************ ##
    def __init__(self):
        """
        Default constructor.
        """
        pass
    ## ************************************************************ ##


    ## ************************************************************ ##
    @staticmethod
    def makeIonicCurrent(parameters, area):
        """
        Create an :class:`IonicCurrent` instance using the given parameters.

        :param parameters: the current parameters
        :type g: dict
        :param area: the area of the neuron
        :type area: string

        :return current: the :class:`IonicCurrent` instance

        :raises: TypeError if the supplied currentType cannot be instantiated
        """

        # Get current type
        currentType = parameters.get('class', [])

        # Instantiate current
        if currentType == 'IonicCurrentHHTraubLeak':
            current = ichhtr.IonicCurrentHHTraubLeak(parameters, area)
        elif currentType == 'IonicCurrentHHTraubK':
            current = ichhtr.IonicCurrentHHTraubK(parameters, area)
        elif currentType == 'IonicCurrentHHTraubNa':
            current = ichhtr.IonicCurrentHHTraubNa(parameters, area)
        elif currentType == 'IonicCurrentMYamada':
            current = icm.IonicCurrentMYamada(parameters, area)
        elif currentType == 'IonicCurrentCaLReuveni':
            current = iccal.IonicCurrentCaLReuveni(parameters, area)
        elif currentType == 'IonicCurrentCaTHuguenard':
            current = iccat.IonicCurrentCaTHuguenard(parameters, area)
        elif currentType == 'IonicCurrentCANDestexhe':
            current = iccan.IonicCurrentCANDestexhe(parameters, area)
        elif currentType == 'IonicCurrentSynExp':
            current = icsynexp.IonicCurrentSynExp(parameters, area)
        elif currentType == 'IonicCurrentHHWangLeak':
            current = ichhwa.IonicCurrentHHWangLeak(parameters, area)
        elif currentType == 'IonicCurrentHHWangK':
            current = ichhwa.IonicCurrentHHWangK(parameters, area)
        elif currentType == 'IonicCurrentHHWangNa':
            current = ichhwa.IonicCurrentHHWangNa(parameters, area)
        else:
            raise TypeError("Could not create an instance of a IonicCurrent with the supplied currentType: " + currentType)

        return current
    ## ************************************************************ ##
## ***************************************************************************************************************** ##
