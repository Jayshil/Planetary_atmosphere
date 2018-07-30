import numpy as np
import matplotlib.pyplot as plt
import astropy.constants as con

t_p=4.6                             #Age of the sun, in multiple of Billion years
t=np.linspace(1,4.6,1000)           #Creating Array of time
d_e=np.linspace(1,1,1000)           #Distance of the Earth from the Sun
d_v=np.linspace(0.723,0.723,1000)   #Distance of the Venus from the Sun
d_m=np.linspace(1.524,1.524,1000)   #Distance of the Mars from the Sun

#Required formulae
f_t=(1+((0.4)*(1-(t/t_p))))
d_0=(((con.L_sun)/(f_t*16*np.pi*273.15))**0.5)/149597871000
d_100=(((con.L_sun)/(f_t*16*np.pi*373.15))**0.5)/149597871000


# Create plots with pre-defined labels.
fig, ax = plt.subplots()

ax.plot(t, d_0, 'k--', label='Boundary of Habitable Zone at which temperature is 273.15 K')
ax.plot(t, d_100, 'r:', label='Boundary of Habitable Zone at which temperature is 373.15 K')
ax.plot(t, d_e, 'blue', label='Average distance of the Earth from the Sun')
ax.plot(t, d_v, 'brown', label='Average distance of the Venus from the Sun')
ax.plot(t, d_m, 'green', label='Average distance of the Mars from the Sun')

legend = ax.legend(loc='best', fontsize='medium')

plt.title('Change in Habitable Zone around the Sun with time', fontsize=20)
plt.xlabel('Time (In multiple of Billion Years)')
plt.ylabel('Distance from the Sun (in AU)')

plt.show()

