import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# Leggo file csv per creare un DataFrame corrispondente
pianeti = pd.read_csv('kplr010666592-2011240104155_slc.csv')

#creo il data frame corrispondente
print(pianeti)

#stampo il nome delle colonne del DataFrame
print(pianeti.columns)

#grafico del flusso in funzione del tempo

x=pianeti['TIME']
y=pianeti['PDCSAP_FLUX']

plt.plot(x,y)
plt.xlabel('tempo')
plt.ylabel('flusso')

plt.show()

#grafico del flusso in funzione del tempo coi punti del grafico demarcati da un simbolo 

plt.plot(x, y, 'o',  color='red' ,      label='flusso' )

plt.xlabel('tempo')
plt.ylabel('flusso')
plt.legend()
plt.show()

#produco un grafico del flusso in funzione del tempo con barre di errore e salvo il risultato in un file png e/o pdf

err=pianeti['PDCSAP_FLUX_ERR']
plt.errorbar(x, y, yerr=err, fmt='o' )

plt.xlabel('tempo')
plt.ylabel('flusso')
plt.title('grafico_barre_di_errore')

plt.savefig("grafico_barre_di_errore.png", dpi=300)   # Salva come PNG
plt.savefig("grafico_barre_di_errore.pdf")            # Salva anche come PDF

plt.show()

#grafico simile al precedente selezionando un intervallo temporale attorno ad uno dei minimi

minimo=pianeti.loc[( pianeti['TIME'] > 947.95) & ( pianeti['TIME'] < 948.3)]
x_m=minimo['TIME']
y_m=minimo['PDCSAP_FLUX']
plt.plot(x_m, y_m, 'o',  color='pink' ,      label='flusso' )

plt.xlabel('time')
plt.ylabel('flux')
plt.legend()
plt.show()

#grafico con riquadro
fig, ax = plt.subplots(figsize=(12, 6))

plt.title('Flusso in funzione del tempo (con barre di errore)')

plt.errorbar(x, y, xerr = 0, yerr = err , fmt = 'o', color = 'palevioletred')

plt.xlabel('Tempo [s]', fontsize = 20)
plt.ylabel('Flusso [$e^- /s$]' , fontsize = 20)

riquadro = inset_axes(ax, width='30%', height='20%', loc='upper right')
riquadro.errorbar(x_m, y_m, yerr=minimo['PDCSAP_FLUX_ERR'], fmt='o', color='thistle')
riquadro.set_title('Zoom attorno al minimo', fontsize=10)

plt.show()
