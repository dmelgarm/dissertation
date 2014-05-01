from scipy.io import loadmat
from scipy.integrate import cumtrapz
import matplotlib.pyplot as pl

a=loadmat('/Users/dmelgarm/Documents/dissertation/figures/IWT009.e.mat')['a']
t=a[:,0]
a=a[:,1]
v=cumtrapz(a,t,initial=0)
d=cumtrapz(v,t,initial=0)

g=loadmat('/Users/dmelgarm/Documents/dissertation/figures/IWT009.egps.mat')['g']
tg=g[:,0]
g=g[:,1]

bl=loadmat('/Users/dmelgarm/Documents/dissertation/figures/IWT009.bl.mat')['bl']

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

pl.figure()
pl.plot(t,bl[:,1],t,bl[:,2],t,bl[:,3],t,bl[:,4],t,bl[:,5])
pl.plot(tg,g,'k')
pl.xlim(7,250)
pl.ylim(-1,4.5)
pl.grid(which='both')
pl.xlabel('Seconds after origin time')
pl.ylabel('East displacement $(m)$')
pl.legend(['$t_1=75s$','$t_1=100s$','$t_1=125s$','$t_1=150s$','20s highpass','GPS'],loc=2)
pl.savefig('/Users/dmelgarm/Documents/dissertation/figures/iwt009bl.eps')
pl.show()


