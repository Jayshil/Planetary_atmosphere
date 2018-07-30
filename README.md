# Planetory_atmosphere
This repository has codes that will calculate the equilibrium temperature, and variation in temperature and pressure with height

The codes in this repository needs some initial data to run themselves.

Such data is stored in data.py file.

Here's what data.py file contains:
1) Albedo
2) Distance from sun
3) Acceleration due to gravity at surface
4) Surface Pressure
5) Mass
6) Radius
7) Atmospheric composition

These details for each planet in our solar system. In addition to this, this file also contains,
- Atomic Weight
- Specific heat at constant temperature and pressure
for gases those are in the atmosphere of each planet.

Another important file is Atm_details.py file.

This file will calculate the gamma value (cp/cv) for atmosphere of given planet.

Also this file can calculate the average molecular weight for gases in atmosphere of any planet.

Main file is temp_press_variation.py

This file will calculate the variation in temperature and pressure with varying height.

This repository also includes hab_zone.py file. This file will calculate the variation in habitable zone around the sun over the age of the sun.