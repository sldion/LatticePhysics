import numpy as np
import math as m
import random as rand

lattice = np.zeros((500,500))

lattice[1:500][1:500] = rand.randrange(-1,2,2)
