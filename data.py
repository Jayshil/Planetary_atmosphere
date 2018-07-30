#Jayshil Patel
#This file contains data of planets,
#Its atmosphere, fraction of gases in atmosphere,
#Specific heats of gases at constant volume and pressure


import numpy as np
import astropy.constants as con
import astropy.units as u
import astropy.units.cds as cds
cds.enable()

def planet(x):
	if (x == 'Mercury') or (x == 'mercury'):
		a = 0.119*u.m/u.m
		d = (0.387*u.au).si
		g = 0.378*con.g0
		p0 = ((10**(-15))*cds.atm).si
		m = 0.0553*con.M_earth
		r = ((4879/2)*u.km).si
	elif (x == 'Venus') or (x == 'venus'):
		a = 0.75*u.m/u.m
		d = (0.723*u.au).si
		g = 0.905*con.g0
		p0 = ((92)*cds.atm).si
		m = 0.815*con.M_earth
		r = ((12104/2)*u.km).si
	elif (x == 'Earth') or (x == 'earth'):
		a = 0.306*u.m/u.m
		d = (1.00*u.au).si
		g = 1.000*con.g0
		p0 = ((1.000)*cds.atm).si
		m = 1*con.M_earth
		r = ((12742/2)*u.km).si
	elif (x == 'Mars') or (x == 'mars'):
		a = 0.25*u.m/u.m
		d = (1.524*u.au).si
		g = 0.379*con.g0
		p0 = ((0.0065)*cds.atm).si
		m = 0.107*con.M_earth
		r = ((6779/2)*u.km).si
	elif (x == 'Jupiter') or (x == 'jupiter'):
		a = 0.343*u.m/u.m
		d = (5.203*u.au).si
		g = 2.530*con.g0
		p0 = ((10000000)*cds.atm).si
		m = 317.83*con.M_earth
		r = ((139822/2)*u.km).si
	elif (x == 'Saturn') or (x == 'saturn'):
		a = 0.342*u.m/u.m
		d = (9.537*u.au).si
		g = 1.065*con.g0		
		p0 = ((1000000)*cds.atm).si
		m = 95.159*con.M_earth
		r = ((116464/2)*u.km).si
	elif (x == 'Uranus') or (x == 'uranus'):
		a = 0.300*u.m/u.m
		d = (19.191*u.au).si
		g = 0.905*con.g0
		p0 = ((100000)*cds.atm).si
		m = 14.536*con.M_earth
		r = ((50724/2)*u.km).si
	elif (x == 'Neptune') or (x == 'neptune'):
		a = 0.29*u.m/u.m
		d = (30.069*u.au).si
		g = 1.14*con.g0
		p0 = ((10000)*cds.atm).si
		m = 17.147*con.M_earth
		r = ((49244/2)*u.km).si
	return a,d,g,p0,m,r


def planet_atm(x):
	if (x == 'Mercury') or (x == 'mercury'):
		o2 = 0.42
		na = 0.29
		h2 = 0.22
		he = 0.06
		k = 0.005
		co2 = 0
		n2 = 0
		so2 = 0
		ar = 0
		h2o = 0
		co = 0
		ch4 = 0
		nh3 = 0
	elif (x == 'Venus') or (x == 'venus'):
		o2 = 0
		na = 0
		h2 = 0
		he = 0.001/100
		k = 0
		co2 = 0.965
		n2 = 0.035
		so2 = 0.015/100
		ar = 0.007/100
		h2o = 0.002/100
		co = 0.002/100
		ch4 = 0
		nh3 = 0
	elif (x == 'Earth') or (x == 'earth'):
		o2 = 0.2095
		na = 0
		h2 = 0
		he = 0
		k = 0
		co2 = 0.038/100
		n2 = 0.7808
		so2 = 0
		ar = 0.934/100
		h2o = 0
		co = 0
		ch4 = 0
		nh3 = 0
	elif (x == 'Mars') or (x == 'mars'):
		o2 = 0.13/100
		na = 0
		h2 = 0
		he = 0
		k = 0
		co2 = 0.9532
		n2 = 0.027
		so2 = 0
		ar = 0.016
		h2o = 0.021/100
		co = 0.008/100
		ch4 = 0
		nh3 = 0
	elif (x == 'Jupiter') or (x == 'jupiter'):
		o2 = 0
		na = 0
		h2 = 0.898
		he = 0.102
		k = 0
		co2 = 0
		n2 = 0
		so2 = 0
		ar = 0
		h2o = 0
		co = 0
		ch4 = 0.3/100
		nh3 = 0.026/100
	elif (x == 'Saturn') or (x == 'saturn'):
		o2 = 0
		na = 0
		h2 = 0.963
		he = 0.325
		k = 0
		co2 = 0
		n2 = 0
		so2 = 0
		ar = 0
		h2o = 0
		co = 0
		ch4 = 0.45/100
		nh3 = 0.0125/100
	elif (x == 'Uranus') or (x == 'uranus'):
		o2 = 0
		na = 0
		h2 = 0.825
		he = 0.152
		k = 0
		co2 = 0
		n2 = 0
		so2 = 0
		ar = 0
		h2o = 0
		co = 0
		ch4 = 0.023
		nh3 = 0
	elif (x == 'Neptune') or (x == 'neptune'):
		o2 = 0
		na = 0
		h2 = 0.8
		he = 0.19
		k = 0
		co2 = 0
		n2 = 0
		so2 = 0
		ar = 0
		h2o = 0
		co = 0
		ch4 = 0.015
		nh3 = 0
	return o2,na, h2, he, k, co2, n2, so2, ar, h2o, co, ch4, nh3

def atomic_wt(x):
	if x == 'o2':
		wt = (15.999*u.u).si
	elif x == 'na':
		wt = (22.99*u.u).si
	elif x == 'h2':
		wt = (2.015*u.u).si
	elif x == 'he':
		wt = (4.003*u.u).si
	elif x == 'k':
		wt = (39.0983*u.u).si
	elif x == 'co2':
		wt = (44.01*u.u).si
	elif x == 'n2':
		wt = (14.0067*u.u).si
	elif x == 'so2':
		wt = (64.066*u.u).si
	elif x == 'ar':
		wt = (39.948*u.u).si
	elif x == 'h2o':
		wt = (18.015*u.u).si
	elif x == 'co':
		wt = (28.01*u.u).si
	elif x == 'ch4':
		wt = (16.04*u.u).si
	elif x == 'nh3':
		wt = (17.031*u.u).si
	return wt

def c_v(x):
	if x == 'o2':
		cv = (0.659*u.kJ/(u.kg*u.K)).decompose()
	elif x == 'na':
		cv = (0*u.kJ/(u.kg*u.K)).decompose()
	elif x == 'h2':
		cv = (10.16*u.kJ/(u.kg*u.K)).decompose()
	elif x == 'he':
		cv = (3.12*u.kJ/(u.kg*u.K)).decompose()
	elif x == 'k':
		cv = (0*u.kJ/(u.kg*u.K)).decompose()
	elif x == 'co2':
		cv = (0.655*u.kJ/(u.kg*u.K)).decompose()
	elif x == 'n2':
		cv = (0.743*u.kJ/(u.kg*u.K)).decompose()
	elif x == 'so2':
		cv = (0.51*u.kJ/(u.kg*u.K)).decompose()
	elif x == 'ar':
		cv = (0.312*u.kJ/(u.kg*u.K)).decompose()
	elif x == 'h2o':
		cv = (0*u.kJ/(u.kg*u.K)).decompose()
	elif x == 'co':
		cv = (0.72*u.kJ/(u.kg*u.K)).decompose()
	elif x == 'ch4':
		cv = (1.70*u.kJ/(u.kg*u.K)).decompose()
	elif x == 'nh3':
		cv = (1.66*u.kJ/(u.kg*u.K)).decompose()
	return cv

def c_p(x):
	if x == 'o2':
		cp = (0.919*u.kJ/(u.kg*u.K)).decompose()
	elif x == 'na':
		cp = (0*u.kJ/(u.kg*u.K)).decompose()
	elif x == 'h2':
		cp = (14.32*u.kJ/(u.kg*u.K)).decompose()
	elif x == 'he':
		cp = (5.19*u.kJ/(u.kg*u.K)).decompose()
	elif x == 'k':
		cp = (0*u.kJ/(u.kg*u.K)).decompose()
	elif x == 'co2':
		cp = (0.844*u.kJ/(u.kg*u.K)).decompose()
	elif x == 'n2':
		cp = (1.04*u.kJ/(u.kg*u.K)).decompose()
	elif x == 'so2':
		cp = (0.64*u.kJ/(u.kg*u.K)).decompose()
	elif x == 'ar':
		cp = (0.520*u.kJ/(u.kg*u.K)).decompose()
	elif x == 'h2o':
		cp = (0*u.kJ/(u.kg*u.K)).decompose()
	elif x == 'co':
		cp = (1.02*u.kJ/(u.kg*u.K)).decompose()
	elif x == 'ch4':
		cp = (2.22*u.kJ/(u.kg*u.K)).decompose()
	elif x == 'nh3':
		cp = (2.19*u.kJ/(u.kg*u.K)).decompose()
	return cp
