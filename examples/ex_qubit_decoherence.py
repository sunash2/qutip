#
# Textbook example: Rabi oscillation in the dissipative Jaynes-Cummings model.
# 
#
from qutip import *
from qutip import blochsphere
from pylab import *
import time

def qubit_integrate(w, theta, gamma1, gamma2, psi0, tlist):

    # Hamiltonian
    sx = sigmax()
    sy = sigmay()
    sz = sigmaz()

    H = w * (cos(theta) * sz + sin(theta) * sx)
        
    # collapse operators
    c_op_list = []

    n_th_a = 0.0 # zero temperature

    rate = gamma1
    if rate > 0.0:
        c_op_list.append(sqrt(rate) * sx)

    rate = gamma2
    if rate > 0.0:
        c_op_list.append(sqrt(rate) * sz)

    # evolve and calculate expectation values
    expt_list = me_ode_solve(H, psi0, tlist, c_op_list, [sx, sy, sz])  

    return expt_list[0], expt_list[1], expt_list[2]
    
#
# set up the calculation
#
w     = 1.0 * 2 * pi   # qubit angular frequency
theta = 0.0 * pi       # qubit angle from sigma_z axis (toward sigma_x axis)

gamma1 = 0.1      # qubit relaxation rate
gamma2 = 0.2      # qubit dephasing rate

# initial state
a = 0.7
psi0 = (a* basis(2,0) + (1-a)*basis(2,1))/(sqrt(a**2 + (1-a)**2))

tlist = linspace(0,20,250)

start_time = time.time()
sx, sy, sz = qubit_integrate(w, theta, gamma1, gamma2, psi0, tlist)
print 'time elapsed = ' +str(time.time() - start_time) 

figure(1)
blochsphere.blochsphere_animation(sx, sy, sz)

figure(2)
plot(tlist, real(sx))
plot(tlist, real(sy))
plot(tlist, real(sz))
legend((r'$\sigma_x$', r'$\sigma_y$', r'$\sigma_z$'))
xlabel('Time')
ylabel('')
title('Qubit decoherence')
savefig("qubit_decoherence.jpg", format="jpg")
show()


