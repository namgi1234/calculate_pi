# calculate_pi

## Before reading

Think of a circle as a regular polygon with infinite sides.

## calculate circumference!

We have a circle that radius is 1.
So if we know the number of sides, we can find the circumference.

<pre>
<code>
circumference = sin(360/(one of the side)) * (number of sides)
</code>
</pre>

## calculate Pi!
Pi is circumference/diameter

<pre>
<code>
Pi = (sin(360/(one of the side)) * (number of sides))/2
</code>
</pre>

## Code

<pre>
<code>
import math

number_of_side = int(input())

angle = 360/number_of_side

pi = (math.sin(math.radians(angle))*number_of_side)/2

print(pi)
</code>
</pre>
