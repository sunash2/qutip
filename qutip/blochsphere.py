#This file is part of QuTIP.
#
#    QuTIP is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#    QuTIP is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with QuTIP.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright (C) 2011, Paul D. Nation & Robert J. Johansson
#
###########################################################################

import os
from scipy import *
from matplotlib import pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
import matplotlib.ticker as ticker
mpl.rcParams['text.usetex'] = True
#setup plot
fig = plt.figure()
ax = Axes3D(fig)
ax.grid(on=False)


def blochsphere_plot(x_vec, y_vec, z_vec):
    #sphere
    u = linspace(0, 2*pi, 100)
    v = linspace(0, pi, 100)
    x = outer(cos(u), sin(v))
    y = outer(sin(u), sin(v))
    z = outer(ones(size(u)), cos(v))
    ax.plot_surface(x, y, z,  rstride=2, cstride=2,color='#FFDDDD',linewidth=0,alpha=0.3)
    #wireframe
    ax.plot_wireframe(x,y,z,rstride=5, cstride=5,color='gray',alpha=0.1)
    #equator
    ax.plot(1.0*cos(u),1.0*sin(u),zs=0, zdir='z',lw=1.0,color='gray')
    ax.plot(1.0*cos(u),1.0*sin(u),zs=0, zdir='x',lw=1.0,color='gray')
    #axes
    span=linspace(-1.0,1.0,10)
    ax.plot(span,0*span, zs=0, zdir='z', label='X',lw=1.0,color='gray')
    ax.plot(0*span,span, zs=0, zdir='z', label='Y',lw=1.0,color='gray')
    ax.plot(0*span,span, zs=0, zdir='y', label='Z',lw=1.0,color='gray')
    ax.set_xlim3d(-1.2,1.2)
    ax.set_ylim3d(-1.3,1.2)
    ax.set_zlim3d(-1.2,1.2)
    #axes labels
    ax.text(0, -1.2, 0, r"$x$", color='black',fontsize=18)
    ax.text(1.1, 0, 0, r"$y$", color='black',fontsize=18)
    ax.text(0, 0, 1.2, r"$\left|0\right>$", color='black',fontsize=18)
    ax.text(0, 0, -1.2, r"$\left|1\right>$", color='black',fontsize=18)
    for a in ax.w_xaxis.get_ticklines()+ax.w_xaxis.get_ticklabels():
        a.set_visible(False)
    for a in ax.w_yaxis.get_ticklines()+ax.w_yaxis.get_ticklabels():
        a.set_visible(False)
    for a in ax.w_zaxis.get_ticklines()+ax.w_zaxis.get_ticklabels():
        a.set_visible(False)    
    #vector,x and y axes are switched so the shading function works properly.
    ax.plot(real(x_vec), real(y_vec), real(z_vec), zs=0, zdir='z', label='Z', lw=0.5, marker='.', color='b')
    plt.show()


def blochsphere_animation(x_vec, y_vec, z_vec):
    #sphere
    u = linspace(0, 2*pi, 100)
    v = linspace(0, pi, 100)
    x = outer(cos(u), sin(v))
    y = outer(sin(u), sin(v))
    z = outer(ones(size(u)), cos(v))
    ax.plot_surface(x, y, z,  rstride=2, cstride=2,color='#FFDDDD',linewidth=0,alpha=0.3)
    #wireframe
    ax.plot_wireframe(x,y,z,rstride=5, cstride=5,color='gray',alpha=0.1)
    #equator
    ax.plot(1.0*cos(u),1.0*sin(u),zs=0, zdir='z',lw=1.0,color='gray')
    ax.plot(1.0*cos(u),1.0*sin(u),zs=0, zdir='x',lw=1.0,color='gray')
    #axes
    span=linspace(-1.0,1.0,10)
    ax.plot(span,0*span, zs=0, zdir='z', label='X',lw=1.0,color='gray')
    ax.plot(0*span,span, zs=0, zdir='z', label='Y',lw=1.0,color='gray')
    ax.plot(0*span,span, zs=0, zdir='y', label='Z',lw=1.0,color='gray')
    ax.set_xlim3d(-1.2,1.2)
    ax.set_ylim3d(-1.3,1.2)
    ax.set_zlim3d(-1.2,1.2)
    #axes labels
    ax.text(0, -1.2, 0, r"$x$", color='black',fontsize=18)
    ax.text(1.1, 0, 0, r"$y$", color='black',fontsize=18)
    ax.text(0, 0, 1.2, r"$\left|0\right>$", color='black',fontsize=18)
    ax.text(0, 0, -1.2, r"$\left|1\right>$", color='black',fontsize=18)
    for a in ax.w_xaxis.get_ticklines()+ax.w_xaxis.get_ticklabels():
        a.set_visible(False)
    for a in ax.w_yaxis.get_ticklines()+ax.w_yaxis.get_ticklabels():
        a.set_visible(False)
    for a in ax.w_zaxis.get_ticklines()+ax.w_zaxis.get_ticklabels():
        a.set_visible(False)    

    os.mkdir("bloch-plots")
    #vector,x and y axes are switched so the shading function works properly.
    for i in range(len(x_vec)):
        ax.plot([real(x_vec[i])], [real(y_vec[i])], [real(z_vec[i])], zs=0, zdir='z', label='Z', lw=0.5, marker='.', color='b')
        plt.savefig("bloch-plots/bloch_" + str(i) + ".jpg")

    plt.show()



