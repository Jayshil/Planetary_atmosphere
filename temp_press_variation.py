#Jayshil Patel
#This program calculate the variation in temperature and,
#pressure by varying height

import numpy as np
import matplotlib.pyplot as plt
import astropy.constants as con
import astropy.units as u
import data as data
import temperature as tem
import atm_details as adet

#------------------------------------------------------------------
#----------Calculating Variation in temperature with height--------
#------------------------------------------------------------------
def t_r(x):
	r1 = np.linspace(0,20000,10000)*u.m
	gamma = adet.gamma(x)
	m_bar = adet.avg_mol_wt(x)
	(a,d,g,p0,m,r) = data.planet(x)
	T_0 = tem.temp_gh(x)
	T_r = T_0 + (((m_bar*g*(1-gamma)*r1)/(con.k_B*gamma))).decompose()
	return T_r

#------------------------------------------------------------------
#----------Calculating Variation in pressure with height-----------
#------------------------------------------------------------------
def p_r(x):
	r1 = np.linspace(0,20000,10000)*u.m
	m_bar = adet.avg_mol_wt(x)
	(a,d,g,p0,m,r) = data.planet(x)
	P_r = p0*(np.exp((-m_bar*g*r1)/(con.k_B*t_r(x))))
	return P_r
