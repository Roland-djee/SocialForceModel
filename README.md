Social Force Model for Pedestrian Dynamics 
==========================================

This code is intended to simulate the dynamics of pedestrians.

***Last modified version 12/10/2015***

Social Force Model - Python library for pedestrian dynamics
===========================================================

Microsimulator solving for the free-space dynamics of pedestrians using a so-called "Social Force
Model" based on the article [Helbing & Molnar Phys. Rev. E 51, 4282 (1995)]. It includes the possibility 
to set a crude model of environment using defined walls and buildings.

- Includes JSON user interface for time-propagation and environmental settings.
- Includes pedestrian dynamics by solving time-dependent "Social Force Model" equations.

Installation
============

Requirements:

- Git
- Python and Numpy, Scipy dependencies
- JSON

The following instructions are for a Unix-like environment without 
root privileges.

In a terminal,

```sh
mkdir SocialForceModel
cd SocialForceModel
git clone https://github.com/UCLGuichard/SocialForceModel
```

This gets the code. Now let's run it.

```sh
cd SocialForceModel/src
python SocialForceModel.py
```

If all went well, you should now have a test case running.

***SocialForceModel has been developed and tested under Windows and Eclipse IDE with Python 2.7 and Anaconda interpreters.***

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

SocialForceModel is based on the seminar work by Helbing and coworkers 
cited above.

Acknowledgements
================

- Whoever involved in this project.

Contact
=======

[Roland Guichard] - <roland.guichard@ts.catapult.org.uk>


