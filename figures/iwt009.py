from scipy.io import loadmat
from scipy.integrate import cumtrapz
import matplotlib.pyplot as pl

a= a=loadmat('/Users/dmelgarm/Documents/dissertation/figures/IWT009.e.mat')['a']
t=a[:,0]
a=a[:,1]
v=cumtrapz(a,t,initial=0)
d=cumtrapz(v,t,initial=0)

pl.rc('font', family='serif')
pl.close("all")
pl.figure()
pl.subplot(311)
pl.plot(t,a,'k')
pl.ylabel('a $(m/s^2)$')
pl.grid(which='both')
pl.xlim(7,300)
pl.subplot(312)
pl.plot(t,v,'k')
pl.ylabel('v $(m/s)$')
pl.grid(which='both')
pl.xlim(7,300)
pl.subplot(313)
pl.plot(t,d,'k')
pl.ylabel('d $(m)$')
pl.grid(which='both')
pl.xlim(7,300)
pl.xlabel('Seconds after origin time')
pl.savefig('/Users/dmelgarm/Documents/dissertation/figures/iwt009.eps')
pl.show()