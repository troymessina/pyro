from vpython import *

# 1. Canvas Setup
scene = canvas(title="3D Traveling Wave with Reference Grid",
               width=400, height=400, center=vec(0, 0, 0),
               background=color.black)
scene.camera.pos = vec(0, 0, 10)
scene.camera.axis = vec(0, 0, -10)

# 2. Parameters
A = 1.0          # Amplitude of the wave
wavelength = 4.0 # Distance between wave crests
k = 2 * pi / wavelength # Wavenumber
omega = 3.0      # Angular frequency
num_spheres = 60 # Number of particle indicators
x_max = 5*A      # Boundary limits for the grid and wave
dx = 0.5         # Grid spacing spacing

# 3. Create the Coordinate Reference Grid
def make_grid(extent, spacing):
    # Generates a flat ground grid utilizing curve objects
    #xz-plane x lines
#    for x_val in range_closed(-extent, extent, spacing):
#        # Vertical grid lines (parallel to Z-axis)
#        curve(pos=[vec(x_val, -A, -extent), vec(x_val, -A, extent)],
#              color=color.gray(0.3), radius=0.02)
    #xy-plane x lines
    for x_val in range_closed(-extent, extent, spacing):
        # Vertical grid lines (parallel to Z-axis)
        if x_val==-wavelength/2 or x_val==wavelength/2:
          curve(pos=[vec(x_val, -extent, 0), vec(x_val, extent, 0)],
              color=color.white, radius=0.02)
        else:
          curve(pos=[vec(x_val, -extent, 0), vec(x_val, extent, 0)],
              color=color.gray(0.25), radius=0.02)
    for y_val in range_closed(-extent, extent, spacing):
        # Vertical grid lines (parallel to Y-axis)
        if y_val==0:
          curve(pos=[vec(-extent, y_val, 0), vec(extent, y_val, 0)],
              color=color.white, radius=0.02)
        else:
          curve(pos=[vec(-extent, y_val, 0), vec(extent, y_val, 0)],
              color=color.gray(0.25), radius=0.02)
#    for z_val in range_closed(-extent, extent, spacing):
#        # Horizontal grid lines (parallel to X-axis)
#        curve(pos=[vec(-extent, -A, z_val), vec(extent, -A, z_val)],
#              color=color.gray(0.3), radius=0.02)

def range_closed(start, stop, step):
    # Helper function to include the final boundary point safely
    x = start
    while x <= stop + (step / 10):
        yield x
        x += step

make_grid(x_max, dx)

# 4. Create Wave Particles
# Generate a line of spheres along the X-axis
spheres = []
x_vals = []
x_start = -x_max

for i in range(num_spheres):
    x_pos = x_start + (i * (2 * x_max / num_spheres))
    # Instantiate spheres at the baseline height
    if i==19:
      s = sphere(pos=vec(x_pos, 0, 0), radius=0.12, color=color.magenta)
    else:
      s = sphere(pos=vec(x_pos, 0, 0), radius=0.12, color=color.cyan)
    spheres.append(s)
    x_vals.append(x_pos)
# 5. Allow pausing the simulation
running = True

def toggle_run(b):
    global running
    running = not running
    if running:
      b.text = "Pause"
    else:
      b.text = "Run"

button(text="Pause", bind=toggle_run)

# 6. Draw wavelength indicator
center = vector(0, 1.5*A, 0)
direction = vector(wavelength/2, 0, 0) # Right direction
# Create the two halves
arrow(pos=center, axis=direction, color=color.red)
arrow(pos=center, axis=-direction, color=color.red)
label(pos=vec(0, 2.0*A, 0), text='wavelength', box=False, height=16, border=4, font='sans')

# 7. Animation Loop
t = 0
dt = 0.01

while True:
    rate(100) # Throttles the loop execution speed
    if running:
      t += dt

      # Mathematical expression for a rightward traveling wave: y = A * sin(k*x - omega*t)
      for idx in range(num_spheres):
          x = x_vals[idx]
          y_pos = A * sin(k * x - omega * t)
          spheres[idx].pos.y = y_pos
