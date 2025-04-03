
import py_wake
import matplotlib.pyplot as plt

from py_wake.examples.data.hornsrev1 import Hornsrev1Site, V80, wt_x, wt_y, wt16_x, wt16_y
from py_wake import NOJ

windTurbines = V80()
site = Hornsrev1Site()
noj = NOJ(site,windTurbines)
simulationResult = noj(wt_x,wt_y)
aep_result = simulationResult.aep().sum()

plt.figure()
plt.scatter(wt_x,wt_y, marker = '2')
plt.show()

print('AEP:', aep_result)

print('done')
