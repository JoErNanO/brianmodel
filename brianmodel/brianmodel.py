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
    brianmodel
    ~~~~~~~~~~~~~
    This module contains an abstraction of the equations used in the Brian Simulator (http://briansimulator.org/)

    :copyright 2014 Francesco Giovannini, Neurosys - INRIA CR Nancy - Grand Est
    :licence GPLv3, see LICENCE for more details
"""


from neuron import neuron as nn

import yaml


## ***************************************************************************************************************** ##
class BrianModel(object):
    """
    The BrianModel represents an abstraction of the equation models used in the Brian Simulator.
    In particular a Brian model is represented as a list of Neuron objects, initialised with a parameter file.

    Initialised as:

    with arguments:
    """

    ## ************************************************************ ##
    ## Default constructor.
    def __init__(self, fileName):
        """
        Default constructor.

        :param fileName: the name of the file containing the model parameters
        :type area: string
        """
        # Initialise class attributes
        self.fileName = fileName
        self.parameters = {}
        self.neurons = []
    ## ************************************************************ ##

    ## ************************************************************ ##
    ## Read and parse the file containing model parameters.
    def readParameterFile(self):
        """
        Read and parse the file containing the model parameters.

        :returns: return code
        :rtype: int
        """
        # Parse the parameter file
        with open(self.fileName) as f:
            self.parameters = yaml.safe_load(f)

        # Build list of neurons
        for neuron, params in self.parameters['neurons'].iteritems():
            tmpNeuron = nn.Neuron({neuron : params})
            self.neurons.append(tmpNeuron)

        return 0
    ## ************************************************************ ##


    ## ************************************************************ ##
    ## Generate the Brian-compatible string representation of the model
    def getModelString(self):
        """
        Generate the string representation of the model equations for each
        neuron type in the model.

        :returns: the string representation of the model equations for each neuron type in the model
        :rtype: dict of strings
        """
        res = {}

        for neuron in self.neurons:
            res[neuron.name] = neuron.getNeuronString()

        return res
    ## ************************************************************ ##
## ***************************************************************************************************************** ##
