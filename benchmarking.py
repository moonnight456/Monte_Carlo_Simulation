import timeit

count = 10

orig_time = timeit.timeit("""
from random import randint

r=1000
circle_scale=(r**2)/4
square_scale=r**2

dot=5000
sim=10
pi_sum=0

#print("Simulation Starts")

for n in range(1,sim+1):
    inn=0
    for i in range(dot):
        x=randint(1,r)
        y=randint(1,r)
        length=(x**2+y**2)**(1/2)
        if length<=r:
            inn+=1
        #print(f"loop : {i}")
    pi=(inn*square_scale)/(circle_scale*dot)
    #print(f"test{n} : {pi}")
    pi_sum+=pi
pi_sum/=sim
#print(f"PI : {pi_sum}")
""", number=count)

print("Original Runtime:", orig_time/count, "s")

opt_time = timeit.timeit("""
import numpy as np

r = 1000
dot = 5000
sim = 10

x = np.random.randint(1, r+1, size=(sim, dot))
y = np.random.randint(1, r+1, size=(sim, dot))

inn = np.sum(x*x + y*y <= r*r, axis=1)
pi_estimates = 4 * inn / dot

for i, val in enumerate(pi_estimates, 1):
    #print(f"test{i} : {val}")
    pass

#print("PI :", np.mean(pi_estimates))

""", number=count)

print("Runtime after Optimization:", opt_time/count, "s")