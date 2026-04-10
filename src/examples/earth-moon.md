# Earth-Moon Orbit

Classic orbital motion using Newton's Law of Gravitation. A mass of the moon is given an initial velocity to create a stable, circular orbit.

## What You'll See

- The moon begins orbiting with an initial velocity.
- A visible trail showing the moon's trajectory.
- The Earth also orbits the center of mass of the system.
- A set of vectors defining x, y, and z.

## Physics

- **Stable Orbit**: Initial velocity provides a stable orbit.
- **Masses and Distances**: The masses and distances are for the Earth-Moon system.
- **Forces**: Drag force proportional to v², opposing velocity
  - \( F_{g} = G * \frac{M_E  *M_M}{ r^2}\hat{r} \)

## Key Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| Earth mass| 5.94e24 | mass of Earth |
| Moon mass | 7.36e22 | mass of Moon |
| Earth-Moon Distance | 3.84e8 | initial separation distance of Earth and Moon |
| Initial velocity | \(\sqrt{G M/r\) | Moon's initial speed in the y-direction |

## Tips

- Change `Earth.m` or `moon.m` to explore dependence on masses.
- Change `REM` to explore dependence on Earth-Moon distance.
- Change `vel` independent of the above parameters to explore orbit stability.
- The simulation runs for 300 days.

