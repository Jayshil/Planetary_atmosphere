#Jayshil Patel
#This program will plot the variation in temperature and,
#pressure by varying height

import numpy as np
import matplotlib.pyplot as plt
import astropy.constants as con
import astropy.units as u
import data as data
import temperature as tem
import atm_details as adet
import temp_press_variation as tpv

x = input("Enter the name of planet: ")

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
