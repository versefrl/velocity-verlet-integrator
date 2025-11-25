import numpy as np

#constants
mu = 398600.4418
r0 = 7000.0

#initial state
v_circ = np.sqrt(mu/r0)
T = 2*np.pi*np.sqrt(r0**3/mu)

dt = 1.0
x = r0
y = 0.0
vx = 0.0
vy = v_circ
r = np.sqrt(x*x+y*y)
ax = -mu*(x/r**3)
ay = -mu*(y/r**3)

steps = int(np.ceil(T/dt))

#math

vel = np.zeros((steps+1, 2), dtype=float)
accel = np.zeros((steps+1, 2), dtype=float)
r_values = np.zeros((steps+1), dtype=float)
pos_x = np.zeros(steps+1,dtype=float)
pos_y = np.zeros(steps+1, dtype=float)
energy = np.zeros(steps+1, dtype=float)

vel[0] = [vx, vy]
accel[0] = [ax, ay]
r_values[0] = r
pos_x[0] = x
pos_y[0] = y

speed2_0 = vx*vx + vy*vy
K0 = 0.5 * speed2_0
U0 = -mu / r
energy[0] = K0 + U0


for i in range(steps):
    r = np.sqrt(x*x + y*y)
    ax = -mu * x / r**3
    ay = -mu * y / r**3

    x_new = x + vx*dt + 0.5*ax*dt*dt
    y_new = y + vy*dt + 0.5*ay*dt*dt
    
    r_new = np.sqrt(x_new*x_new + y_new*y_new)
    ax_new = -mu * x_new / r_new**3
    ay_new = -mu * y_new / r_new**3

    vx = vx + 0.5*(ax + ax_new)*dt
    vy = vy + 0.5*(ay + ay_new)*dt

    x = x_new
    y = y_new

    vel[i+1]   = [vx, vy]
    accel[i+1] = [ax_new, ay_new]
    r_values[i+1] = r_new
    pos_x[i+1] = x
    pos_y[i+1] = y

    speed2 = vx*vx + vy*vy
    K = 0.5 * speed2
    U = -mu / r_new
    energy[i+1] = K + U
	
#outputs

print("E[0]      =", energy[0])
print("E[steps//4] =", energy[steps//4])
print("E[steps//2] =", energy[steps//2])
print("E[-1]       =", energy[-1])

print("energy_amp =", energy.max() - energy.min())

r_initial = r_values[0]
r_final = r_values[-1]
print("r_initial =", r_initial)
print("r_final   =", r_final)
print("delta r   =", r_final - r_initial)


print(vel)
print(accel)
print(r_values)
print(pos_x)
print(pos_y)