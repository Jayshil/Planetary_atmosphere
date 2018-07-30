#Jayshil Patel
#Temperature Calculation of Planet

import numpy as np
import astropy.constants as con
import astropy.units as u
import data as data
import temperature as tem

#Choosing Planets
print("------------------------Choosing Planet-----------------------------------")
print("--------------------------------------------------------------------------")
x = input("Enter the name of planet for which you want to calculate temperature: ")
print("--------------------------------------------------------------------------")

#Taking data from data file
(a,d,g,p0,m,r) = data.planet(x)
#--------------------------

print("---------------------Fetching Data of Entered Planet----------------------")
print("--------------------------------------------------------------------------")
print("Selected Planet is " + x)
print("Albedo of " + x + " is " + str(a))
print("Distance of " + x + " from sun is " + str(d))
print("--------That's it what we need to calculate equilibrium temperature-------")
print("--------------------------------------------------------------------------")


#Calculation of Equilibrium Temperature of any planet,...
#... considering it has no atmosphere.

t_p = tem.temp(a,d)
t_p_c = t_p.to(u.deg_C, equivalencies=u.temperature())
print("----------------------Equilibrium Temperature-----------------------------")
print("--------------------------------------------------------------------------")
print("Equilibrium Temperature of " + x + " is " + str(t_p) + " (" + str(t_p_c) + " )")
print("--------------------------------------------------------------------------")

#Calculating Greenhouse Temperature of any planet

t_g = tem.temp_gh(x)
t_g_c = t_g.to(u.deg_C, equivalencies=u.temperature())
print("--------------------------------------------------------------------------")
print("Greenhouse temperature of " + x + " is " + str(t_g)+ " (" + str(t_g_c) + " )")
print("--------------------------------------------------------------------------")
