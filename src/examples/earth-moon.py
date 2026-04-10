GlowScript 3.2 VPython
scene.height=600
scene.width=500
#View in plane of orbit by uncommenting next line
#scene.camera.rotate(angle=90, axis=vec(1,1,1)) 

f1=series()
#constants in meters, kilograms, seconds
G=6.7e-11 #gravitational constant
M=5.94e24 #mass of the Earth
m=7.36e22 #mass of the moon
REM=3.84e8 #initial Earth-moon distance
RE=6.37e6 #Earth radius
RM=1.74e6 #moon radius

#Show the xyz unit vectors in this world and label them
xunit = arrow(pos=vec(-0.25,-0.25,-0.25)*REM, axis=vec(0.1*REM,0,0), color=color.green)
yunit = arrow(pos=vec(-0.25,-0.25,-0.25)*REM, axis=vec(0,0.1*REM,0), color=color.green)
zunit = arrow(pos=vec(-0.25,-0.25,-0.25)*REM, axis=vec(0,0,0.1*REM), color=color.green)
xlabel = label( pos=vec(-0.10,-0.25,-0.25)*REM, text='x', box=False )
ylabel = label( pos=vec(-0.25, -0.10,-0.25)*REM, text='y', box=False )
zlabel = label( pos=vec(-0.25,-0.25,-0.10)*REM, text='z', box=False )

#create objects
Earth=sphere(pos=vec(0,0,0), radius=RE, color=color.cyan)
attach_trail(Earth, type='points', color=color.cyan) #Leaves a motion trail
moon=sphere(pos=vec(REM, 0,0), radius=RM*5, color=color.white)
attach_trail(moon, type='points')
Earth.m=M #give the Earth object the property of mass
Earth.p=Earth.m * vec(0,0,0) #give the Earth an initial momentum = 0
moon.m=m #give the moon object mass
vel = sqrt(G*M/REM)
#print(vel)
moon.p = moon.m * vec(0,vel,0) #give the moon an initial momentum

#Do some initial calculations
r = moon.pos - Earth.pos #get the radial vector from Earth to moon
Fg = G * Earth.m * moon.m * r / mag(r)**3 #Newton's gravitation
aEnext = Fg/Earth.m #Earth acceleration
amnext = -Fg/moon.m #moon acceleration
t = 0 #define total time passed
dt = 5 #define the time step for updating pos, momentum, accel

#Loop the calculations for some total amount of time
while t<25920000: #30 days = 2592000 seconds
    rate(200000)
    Fg = G * Earth.m * moon.m * r / mag(r)**3 #Newton's gravitation
    aE = Fg/Earth.m #Earth acceleration
    am = -Fg/moon.m #moon acceleration
    rcm = (Earth.m*Earth.pos + moon.m*moon.pos)/(Earth.m+moon.m)
    Earth.pos = Earth.pos + Earth.p*dt/Earth.m + 0.5*aE*dt**2 - rcm
    moon.pos = moon.pos + moon.p*dt/moon.m + 0.5*am*dt**2 + rcm
    r = moon.pos - Earth.pos #get the radial vector from Earth to moon
    Fg = G * Earth.m * moon.m * r / mag(r)**3 #Newton's gravitation
    aEnext = Fg/Earth.m #Earth acceleration
    amnext = -Fg/moon.m #moon acceleration
    Earth.p = Earth.p + (aE+aEnext)/2*dt*Earth.m
    moon.p = moon.p + (am+amnext)/2*dt*moon.m
  #  f1.plot(t, G*M*m/mag(r))
    t = t + dt
