from random import randint

r=1000
circle_scale=(r**2)/4
square_scale=r**2

dot=1_000_000
sim=10
pi_sum=0

print("Simulation Starts")

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
    print(f"test{n} : {pi}")
    pi_sum+=pi
pi_sum/=sim
print(f"PI : {pi_sum}")