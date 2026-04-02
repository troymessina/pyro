from vpython import *

naught = 0
length = 1
shift = length*1.05
shift2 = 0
#Show the xyz unit vectors in this world and label them
xunit = arrow(pos=vec(naught,naught,naught), axis=vec(length,0,0), color=color.green)
yunit = arrow(pos=vec(naught,naught,naught), axis=vec(0,length,0), color=color.blue)
zunit = arrow(pos=vec(naught,naught,naught), axis=vec(0,0,length), color=color.red)
xlabel = label( pos=vec(shift,shift2,shift2), text='x', box=False, opacity=0 )
ylabel = label( pos=vec(shift2, shift,shift2), text='y', box=False, opacity=0 )
zlabel = label( pos=vec(shift2,shift2,shift), text='z', box=False, opacity=0 )

#Students enter code below
