from vpython import *
# ── Scene setup ────────────────────────────────────────────────────────────────
scene = canvas(
    title="<b>Horizontal Spring-Mass System</b>",
    width=800, height=400,
    background=color.white,
    center=vector(0, 0, 0),
)
# ── Starting Parameters ─────────────────────────────────────────────────────────
x0 = 1.0  # relaxed length of spring
A = 0.25
ks = 5  # spring stiffness
m = 0.05  # mass of the block

attachpoint = vector(-x0, 0, 0)  ## where spring is attached to wall

track = box(pos=vector(0,-0.075,0), length=1.5, height=0.05, width=0.10)
wall = box(pos=vector(-x0,0.2,0), length=0.01, height=0.5, width=0.1 )
block = box(pos=attachpoint + vector(x0+A, 0, 0), length=0.1, width=0.1, height=0.1, color=color.blue)
spring = helix(pos=attachpoint, axis= block.pos-attachpoint, radius=0.03,
               color=color.orange, coils=25, thickness=0.01)
block.m = m
block.vel = vector(0,0,0)#mass velocity
block.acc = vector(0,0,0)#mass acceleration

# ── Equilibrium reference line ─────────────────────────────────────────────────

eq_line = cylinder(
    pos=vector(0, 0.25, 0),
    axis=vector(0, -0.25, 0),
    radius=0.005,
    color=color.green,
    opacity=0.5,
)
label(
    pos=vector(0, 0.3, 0),
    text="Equilibrium",
    color=color.black,
    height=16,
    box=False,
    opacity=0,
)

# ── A reference line ─────────────────────────────────────────────────
A_line = cylinder(pos=vector(A, 0.25, 0),  axis=vector(0, -0.25, 0), radius=0.005, color=color.black, opacity=0.5)
Alabel = label(pos=vector(A, 0.3, 0), text="+A", color=color.black, height=16, box=False, opacity=0)
Aneg_line = cylinder(pos=vector(-A, 0.25, 0),  axis=vector(0, -0.25, 0), radius=0.005, color=color.black, opacity=0.5)
Aneglabel = label(pos=vector(-A, 0.3, 0), text="-A", color=color.black, height=16, box=False, opacity=0)

deltat = 0.0001
t = 0

scene.pause() # wait for a click
a_now = vec(0,0,0)
while True:#t<5:
    rate(2000)
    block.acc = -ks*block.pos/block.m
    block.pos = block.pos + block.vel*deltat + 0.5*block.acc*deltat**2
    spring.axis = block.pos-attachpoint
    acc_next = -ks*block.pos/block.m
    block.vel = block.vel + (block.acc+acc_next)/2*deltat
    t = t + deltat
