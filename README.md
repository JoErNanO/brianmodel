# BrianModel
Library of neuron models and ionic currents for the [BRIAN](http://briansimulator.org/) simulator.
The purpose of these is to speed up simulation set-up time and reduce code duplication across simulation scripts.

## Spiking Neuron Templates
Template neurons are defined by the ionic currents that flow through their membrane.
Implemented templates include:
    
- Hodgkin-Huxley pyramidal neuron (leak, sodium and potassium)
- Hodgkin-Huxley pyramidal neuron with CAN receptors (leak, sodium, potassium, m-current, calcium, CAN)
- Hodgkin-Huxley fast-spiking inhibitory hippocampal (leak, sodium, potassium, m-current)

### Ionic Currents
Implemented ionic current libraries include:

- Traub and Miles Hodgkin-Huxley (I_<sub>Leak</sub>, I_<sub>K</sub>, I_<sub>Na</sub>) implementation \cite{Traub1991}
- M-Current (I_M) implementation described in \cite{Yamada1989}
- Calcium current (I_<sub>L</sub>) implementation by Reuveni et al. \cite{Reuveni1993}
- Calcium pump mechanisms ($\frac{\mathrm{d}Ca}{\mathrm{d}t}$) implementation by Reuveni et al. \cite{Reuveni1993}
- Calcium-activated non-selective current (I_<sub>CAN</sub>) implementation by Destexhe et al. \cite{Destexhe1994}
- Wang and Buszáki inhibitory Hodgkin-Huxley (I_<sub>Leak</sub>, I_<sub>K</sub>, I_<sub>Na</sub>) implementation \cite{Wang1996}

The current library is easily extensible by third-party users due to its hierarchical design.
The template neurons and their currents are defined as [YAML](http://www.yaml.org/) files, which are conveniently parsed by a Python library which acts as an interface to the [BRIAN](http://briansimulator.org/) simulator API's.

# Installation
1. Download the repository as it is in your home directory
    ~/brianmodel

2. Create a file called *brianmodel.pth* in your python path (the path is located somewhere in local/lib/python2.7/site-packages/, be it global (/usr/) or locally depending on your configuration)

3. Include the library by copying the path to brianmodel in the created .pth file as follows:
    ~/brianmodel/brianmodel/

# Sample Usage
## Model Parameter File
Your model neuron is defined as a list of currents and their parameters.
You will have to create a YAML parameter file containing all the neuron models used in your simulations.
The sample file below (which can be found in includes/) defines two model neurons -- pyramidal and fast-spiking inhibitory -- and their associated currents and parameters.

Typically, a neuron is defined by the area of the cell, the conductance across the cell membrane, and a list of transmembranal ionic currents.
This takes the form:

```yaml
neurons:
    model1:
        area: "1e3 * umetre ** 2"
        conductance: "1 * ufarad ** cm ** -2"

        defined: 
                - class: "IonicCurrentHHTraubLeak"
                  name: "I_leak"
                  g: "1e-5 * siemens * cm ** -2"
                  E: "-70 * mV"
                
                - class: "IonicCurrentHHTraubK"
                  name: "I_K"
                  g: "5 * msiemens * cm ** -2"
                  E: "-100 * mV"
                  vT: "-55 * mV"


```

Here, "model1" is the identifier of the model neuron, and "defined" contains the list of ionic currents.
The neuron of type "model1" contains a leak current and a sodium current.
Each individual entry in the current list contains the name of the current class to be instantiated, the name used to identify the current in the [BRIAN](http://briansimulator.org/) script, and the parameters of that current equation (the conductance "g", the reversal potential "E", and the Traub constant, in the case of "IonicCurrentHHTraubK").



```yaml
# ******************************************************************************* ##
# Model parameters for two interconnected neural populations.
#
#   1. A population of CAN-equipped pyramidal neurons with the following currents:
#       leak, Na, K, M, CaL, CAN, SynE, SynI
#   2. A population of inhibitory interneurons with the following currents:
#       leak, Na, K, SynE, SynI
#
# :copyright 2015 Francesco Giovannini, Neurosys - INRIA CR Nancy - Grand Est
# :licence GPLv3, see LICENCE for more details
#

neurons:
    pyramidal:
        area: "29e3 * umetre ** 2"
        conductance: "1 * ufarad * cm ** -2"

        currents:
            included: [paramsSynExpExc.yml, paramsSynExpInh.yml]

            defined:
                - class: "IonicCurrentHHTraubLeak"
                  name: "I_leak"
                  g: "1e-5 * siemens * cm ** -2"
                  E: "-70 * mV"

                - class: "IonicCurrentHHTraubK"
                  name: "I_K"
                  g: "5 * msiemens * cm ** -2"
                  E: "-100 * mV"
                  vT: "-55 * mV"

                - class: "IonicCurrentHHTraubNa"
                  name: "I_Na"
                  g: "50 * msiemens * cm ** -2"
                  E: "50 * mV"
                  vT: "-55 * mV"

    interneuron:
        area: "14e3 * umetre ** 2"
        conductance: "1 * ufarad * cm ** -2"

        currents:
            included: [paramsSynExpExc.yml, paramsSynExpInh.yml]

            defined:
                - class: "IonicCurrentHHWangLeak"
                  name: "I_leak"
                  g: "0.1e-3 * siemens * cm ** -2"
                  E: "-65 * mV"

                - class: "IonicCurrentHHWangK"
                  name: "I_K"
                  g: "9e-3 * siemens * cm ** -2"
                  E: "-90 * mV"

                - class: "IonicCurrentHHWangNa"
                  name: "I_Na"
                  g: "35e-3 * siemens * cm ** -2"
                  E: "55 * mV"

# ******************************************************************************* ##
```

This defines a neuron model called "pyramidal" with its area, conductance and its ionic currents: three defined and two included.
The defined currents are the leak, sodium and potassium current of the Traub model.
The included currents are mono-exponential synaptic currents which are defined in separate files (paramsSynExpExc.yml, paramsSynExpInh.yml):

```yaml
# ******************************************************************************* ##
# Model parameters for single exponential excitatory synaptic current.
#
#
# :copyright 2015 Francesco Giovannini, Neurosys - INRIA CR Nancy - Grand Est
# :licence GPLv2, see LICENCE for more details
#

- class: "IonicCurrentSynExp"
  name: "I_SynE"
  g: "ge"
  E: "0 * mV"
  tau: "5 * ms"
# ******************************************************************************* ##
```

```yaml
# ******************************************************************************* ##
# Model parameters for single exponential inhibitory synaptic current.
#
#
# :copyright 2015 Francesco Giovannini, Neurosys - INRIA CR Nancy - Grand Est
# :licence GPLv2, see LICENCE for more details
#

- class: "IonicCurrentSynExp"
  name: "I_SynI"
  g: "gi"
  E: "-80 * mV"
  tau: "10 * ms"
# ******************************************************************************* ##
```

The path to included currents can be either absolute or relative.
Parameter files follow standard [YAML](http://www.yaml.org/) syntax.


## Simulation Script
1. Import the library in your python [BRIAN](http://briansimulator.org/) simulation script:
    import brianmodel as bm

2. Read the neuron model parameters file and create the string-formatted model equations from it:
    # Read parameters from file
    mod = bm.BrianModel(args.params)
    mod.readParameterFile()
    modeq = mod.getModelString()

3. This creates a dictionary of string-formatted model equations which you can access by key as standard in Pythong.

4. You can now pass the equations to the [BRIAN](http://briansimulator.org/) Simulator. The command below creates a population of 100 neurons defined by the model strings contained in the list identified by "pyramidal"
    eqPyram = Equations(modeq['pyramidal'])
    Pyr = NeuronGroup(100, model=eqPyram, threshold=EmpiricalThreshold(threshold= -20 * mV, refractory=3 * ms), implicit=True, freeze=True)
    
