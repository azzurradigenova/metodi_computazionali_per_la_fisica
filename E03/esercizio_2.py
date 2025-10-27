import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#leggo il file csv
pianeti = pd.read_csv('ExoplanetsPars_2025.csv', comment='#')

print(pianeti)

#stampo i nomi delle colonne
print(pianeti.columns)

#stampo un estratto del contenuto del DataFrame
estratto=pianeti.iloc[2:8]
print(estratto)

#grafico con assi logaritmici della massa del pianeta in funzione del periodo orbitale
x=pianeti['pl_orbper']
y=pianeti['pl_bmassj']

plt.scatter( x, y, color='pink', s=32, label='pianeta')
plt.ylabel('massa dei pianeti', fontsize=16)
plt.xlabel('periodo orbitale', fontsize=16)
plt.xscale('log')
plt.yscale('log')
plt.legend(fontsize=14)
plt.show()

#grafico con assi logaritmici della grandezza Rˆ2/m in funzione del periodo orbitale
ay=pianeti['pl_orbsmax']**2/pianeti['st_mass']

plt.scatter( x, ay, color='yellow', s=32, label='pianeta')
plt.ylabel('R^2/m*', fontsize=16)
plt.xlabel('periodo orbitale', fontsize=16)
plt.xscale('log')
plt.yscale('log')
plt.legend(fontsize=14)
plt.show()

#grafico con assi logaritmici della massa del pianeta in funzione del periodo orbitale distinguendo gli esopianeti per metodo di scoperta (Transit o Radial Velocity) con la corrispondente legenda 
Transit = pianeti.loc[(pianeti['discoverymethod'] =='Transit')]
Radial_velocity = pianeti.loc[(pianeti['discoverymethod'] =='Radial Velocity')]

plt.scatter(Transit['pl_orbper'], Transit['pl_bmassj'], color='pink', s=32, label='Transit', alpha=0.7)
plt.scatter(Radial_velocity['pl_orbper'],  Radial_velocity['pl_bmassj'], color='fuchsia',    s=32, label='Radial Velocity', alpha=0.2)
plt.xlabel('periodo', fontsize=16)
plt.ylabel('massa', fontsize=16)
plt.legend(fontsize=14)
plt.show()

#istogramma sovrapposto della massa del pianeta distinguendo gli esopianeti per metodo di scoperta (Transit o Radial Velocity) con la corrispondente legenda
Transit_istogramma= plt.hist(Transit['pl_bmassj'], bins=50, range=(0, 80), color='pink', alpha=0.7 )
Radial_istogramma= plt.hist(Radial_velocity['pl_bmassj'], bins=50, range=(0, 80), color='fuchsia', alpha=0.2 )
plt.xlabel('massa', fontsize=16)
plt.show()

#grafico analogo al precedente per il logaritmo in base 10 della massa del pianeta
Transit_log= plt.hist(np.log10(Transit['pl_bmassj']), bins=50, range=(0, 2), color='pink', alpha=0.7 )
Radial_log= plt.hist(np.log10(Radial_velocity['pl_bmassj']), bins=50, range=(0, 2), color='fuchsia', alpha=0.2 )
plt.xlabel('logaritmo base dieci della massa', fontsize=16)
plt.show()