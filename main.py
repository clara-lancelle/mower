from Mower import Mower

file1 = open('husqvarna.dat', 'r')
Lines = file1.readlines()

garden_boundaries = Lines[0]
mower_one = Mower(garden_boundaries, Lines[1])
mower_one.mow(Lines[2].strip())
mower_two = Mower(garden_boundaries, Lines[3])
mower_two.mow(Lines[4].strip())