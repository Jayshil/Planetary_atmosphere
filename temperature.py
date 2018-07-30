#Jayshil Patel
#This code will calculate equilibrium temperature and
#Greenhouse temperature of any planet

import numpy as np
import astropy.constants as con
import astropy.units as u
import data as data

def temp(x):
	(a,d,g,p0,m,r) = data.planet(x)
	t_p = ((((1-a)*con.L_sun)/(16*np.pi*con.sigma_sb*d*d))**0.25).decompose()
	return t_p

def temp_gh(x):
	if (x == 'Venus') or (x == 'venus'):
		tau = 60.0	
	elif (x == 'Earth') or (x == 'earth'):
		tau = 0.83
	elif (x == 'Mars') or (x == 'mars'):
		tau = 0.2
	elif (x == 'Mercury') or (x == 'mercury'):
		tau = 0	
	else:
		print("This will give the approximate results for Jovian Planets as their data is not totally available")
		tau = 0
	t_g = ((((temp(x))**4)*(1+(0.75*tau)))**0.25).decompose()
	return t_g
