#Jayshil Patel
#This program will calculate the equilibrium temperature,
#greenhouse temperature and will plot the variation in temperature and,
#pressure by varying height

import numpy as np
import matplotlib.pyplot as plt
import astropy.constants as con
import astropy.units as u
import data as data
import temperature as tem
import atm_details as adet
import temp_press_variation as tpv

#Choosing Planets
print("------------------------Choosing Planet-----------------------------------")
print("--------------------------------------------------------------------------")
x = input("Enter the name of planet for which you want to calculate equilibrium temperature, greenhouse temperature and variation in temperature and pressure with height: ")
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

t_p = tem.temp(x)
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

r1 = np.linspace(0,20000,10000)*u.m

#---------------------------------------------------------
#-------------For Plotting Temperature Variation----------
#---------------------------------------------------------

T_r=tpv.t_r(x)
plt.plot(r1.to(u.km), T_r, 'blue', label = 'Variation in Temperature with height')
plt.legend(loc='best', fontsize='medium')
plt.title('Variation in temperature with height on the Planet ' + x, fontsize=20)
plt.xlabel('Height above the surface (in km)')
plt.ylabel('Temperature (in K)')
plt.show()


#---------------------------------------------------------
#-------------For Plotting Pressure Variation----------
#---------------------------------------------------------

P_r=tpv.p_r(x)
plt.plot(r1.to(u.km), P_r.to(u.kPa), 'red', label = 'Variation in Pressure with height')
plt.legend(loc='best', fontsize='medium')
plt.title('Variation in pressure with height on the Planet ' + x, fontsize=20)
plt.xlabel('Height above the surface (in km)')
plt.ylabel('Pressure (in kPa)')
plt.show()
