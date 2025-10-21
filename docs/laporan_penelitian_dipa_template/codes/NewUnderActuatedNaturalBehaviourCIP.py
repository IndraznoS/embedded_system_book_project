import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import minimize
import cvxpy as cp

#Latex plot
import matplotlib.pyplot as plt
import scienceplots
plt.style.use(['science', 'ieee'])
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": "cm"
})

# matplotlib imports
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
plt.rcParams['animation.ffmpeg_path'] = \
    '/Users/indrazno/Documents/FFMPEG/ffmpeg'


M = 1.0
m = 1.0
l = 1.0
g = 9.8
b1 = 0.1
b2 = 0.1

Tfinal = 20
fps = 30
t =  np.linspace(0, Tfinal, Tfinal*fps)
dt = t[1] - t[0]

def dynamics(t, x, u):
    """
    Implements the system's differential equations and returns
    state derivatives given current time and state
    """
    theta = x[1]
    xM_dot = x[2]
    theta_dot = x[3]
    xM_ddot = (-b1*l*xM_dot - b2*theta_dot*np.cos(theta) + \
               0.5*g*l*m*np.sin(2.0*theta) - \
                l**2*m*theta_dot**2*np.sin(theta) + l*u)/ \
                    (l*(M + m*np.sin(theta)**2))
    theta_ddot = (-M*b2*theta_dot + M*g*l*m*np.sin(theta) - \
                  b1*l*m*xM_dot*np.cos(theta) - b2*m*theta_dot + \
                    g*l*m**2*np.sin(theta) - 
                  0.5*l**2*m**2*theta_dot**2*np.sin(2.0*theta) + \
                    l*m*u*np.cos(theta))/ \
                        (l**2*m*(M + m*np.sin(theta)**2))
    return np.array([xM_dot, theta_dot, xM_ddot, theta_ddot])


def pend_pos(x_cart, theta):
    return (x_cart - l*np.sin(theta),  l * np.cos(theta))

# initial condition d, theta, d_dot, theta_dot
x0 = np.array([0, np.radians(30), 0, 0])
xsim = np.zeros((len(t),np.shape(x0)[0]))
xsim[0,:] = x0
xstep = x0
for i in range(1, len(t)):
    # span for next time step
    tspan = [t[i-1],t[i]]
    # solve for next step
    sol = solve_ivp(dynamics, tspan, xstep, args=(0,))
    xstep = sol.y[:, -1]
    xstep[1] = (xstep[1] + np.pi) % (2*np.pi) - np.pi
    xsim[i,:] = xstep


# create figure
plt.figure(1, figsize=(4,6))
plt.subplot(2, 1, 1)
plt.plot(t, xsim[:, 0], lw=0.5)
plt.ylabel(r'$x(t)$')
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(t, xsim[:, 1], lw=0.5)
plt.ylabel(r'$\theta (t)$')
plt.grid()
plt.savefig('NaturalResponse.pdf')


# create figure
fig = plt.figure(2)
ax = fig.add_subplot(aspect='equal')
ax.set_xlim(-1, 1)
ax.set_ylim(-1.5, 1.5)
#ax.grid()

x1, y1 = pend_pos(x0[0], x0[1])
cart_width = 0.5
cart_height = 0.25

#'ro--'
cart = ax.add_patch(plt.Rectangle((x0[0] - cart_width/2, \
                                   -cart_height/2), cart_width, \
                                    cart_height, fc='b', zorder=2))
line, = ax.plot([x0[0], x1], [0, y1], 'ro-', lw=2, markersize=8)

# animate each frame "i"
def animate(i):
    xsim[:, 0]
    x1,y1 = pend_pos(xsim[i, 0], xsim[i, 1])
    line.set_data([xsim[i, 0], x1], [0, y1])
    cart.set_xy((xsim[i, 0]- cart_width/2, -cart_height/2))
#    #circle1.set_center((x1, y1))

# save a video: 30 fps
aniswing = animation.FuncAnimation(fig, animate, frames=len(t))
ffmpeg_writer = animation.FFMpegWriter(fps=fps)
aniswing.save('cartinvertedpendnew.mp4', writer=ffmpeg_writer)