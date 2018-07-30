#Jayshil Patel
#This program calculates the adiabatic ratio for any atmosphere
#And average molecular weight for any atmosphere

import numpy as np
import astropy.constants as con
import astropy.units as u
import data as dat

def gamma(x):
	gases = np.array(['o2','na','h2','he','k','co2','n2','so2','ar','h2o','co','ch4','nh3'])
	fraction = np.array(dat.planet_atm(x))
	cv = np.array([])
	for i in gases:
		cv1 = dat.c_v(i)
		cv = np.hstack((cv,cv1))
	cp = np.array([])
	for i in gases:
		cp1 = dat.c_p(i)
		cp = np.hstack((cp,cp1))
	t_cv = np.sum(fraction*cv)
	t_cp = np.sum(fraction*cp)
	gamma = t_cp/t_cv
	return gamma

def avg_mol_wt(x):
	gases = np.array(['o2','na','h2','he','k','co2','n2','so2','ar','h2o','co','ch4','nh3'])
	fraction = np.array(dat.planet_atm(x))
	wt = np.array([])
	for i in gases:
		wt1 = dat.atomic_wt(i)
		wt = np.hstack((wt,wt1))
	avg_wt = np.sum(fraction*wt)
	return avg_wt*u.kg
