Social Force Model for Pedestrian Dynamics 
==========================================

This code is intended to simulate the coupled dynamics of pedestrians in a bespoke free-space environment. 

Social Force Model - C++ library for pedestrian dynamics
===========================================================

Microsimulator solving for the free-space dynamics of pedestrians using a so-called "Social Force
Model" based on the article [Helbing & Molnar Phys. Rev. E 51, 4282 (1995)]. It includes the possibility 
to set a crude model of environment using defined walls and buildings.

Installation
============

In a terminal,

```sh
mkdir SocialForceModel
cd SocialForceModel
git clone https://github.com/UCLGuichard/SocialForceModel
```

C++ core
--------

To build and install the C++ core, in the ``cpp/`` directory, run::

```sh
  mkdir build
  cd build
  cmake ..
  make install
```

Usage
-----

Testing
-------

Example
-------

Getting help
------------

License
=======

See LICENSE file for more details.

Citation
========

See CITATION file for more details.

Version
=======

1.0 (in progress)

History
=======

SocialForceModel is based on the work by Helbing and coworkers cited above.

Acknowledgements
================

- Whoever involved in this project.

Contact
=======

[Roland Guichard] - <r.guichard@ucl.ac.uk>


