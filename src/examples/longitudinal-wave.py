from vpython import *

# --- Simulation Parameters ---
#num_particles = 40
particle_radius = 0.3
amplitude = 0.5
wavelength = 8.0
frequency = 1.0
C = 5.0 # Wave speed

# Create the canvas
scene = canvas(title="Longitudinal Wave Simulation", width=800, height=400)
scene.range = 15

# --- Create Particles ---
cols = 40 #x locations
rows = 11 #y locations
particles = [[None for x in range(cols)] for y in range(rows)]
x_initials = []
y_initials = []

for i in range(cols):
    # Space out particles equally along the x-axis
    x_pos = -cols/2 + i#-12 + (i * 24 / cols)
    for j in range(rows):
      y_pos = -5 + j
      particles[j][i] = sphere(pos=vector(x_pos, y_pos, 0), radius=particle_radius, color=color.cyan)
      y_initials.append(y_pos)

    x_initials.append(x_pos)

# --- Animation Loop ---
t = 0
dt = 0.01

while True:
    rate(100) # Frames per second

    for i in range(cols):
        x0 = x_initials[i]
        # Longitudinal wave function: x = x0 + A * cos(k*x0 - w*t)
        # Where k = 2*pi/lambda and w = 2*pi*f
        x_new = x0 + amplitude * cos(2*pi/wavelength * x0 - 2*pi*frequency * t)
        for j in range(rows):
          particles[j][i].pos.x = x_new

          # Dynamically color the particles based on compression (stretching)
          if i < cols - 1:
            dx = particles[j][i+1].pos.x - particles[j][i].pos.x
            # Brighter color when compressed (dx < 24 / num_particles)
            compression = 1.0 - (dx / (cols/2 / cols))
            particles[j][i].color = vector(0.5 + compression, 0.5 - compression, 1.0)

    t = t + dt
