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
    setup
    ~~~~~~~~~~~~~
    This module contains the setup config for the brianmodel package.

    :copyright 2014 Francesco Giovannini, Neurosys - INRIA CR Nancy - Grand Est
    :licence GPLv3, see LICENCE for more details
"""



from setuptools import setup

setup(name='brianmodel',
      version='1.2',
      description='An adapter of the model Equations for the Brian spiking neural network simulator.',
      url='',
      author='Francesco Giovannini',
      author_email='francesco.giovannini@inria.fr',
      license='GPLv3',
      packages=['brianmodel'],
      install_requires=['pyaml'],
      zip_safe=False)
