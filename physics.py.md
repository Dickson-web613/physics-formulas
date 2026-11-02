PHYSICS FORMULAS

Five basic physics formulas in Python.

"""



def calculate\_speed(distance, time):

&#x20;   """Speed = Distance / Time"""

&#x20;   if time == 0:

&#x20;       raise ValueError("Time cannot be zero")

&#x20;   return distance / time





def calculate\_force(mass, acceleration):

&#x20;   """Force = Mass \* Acceleration"""

&#x20;   return mass \* acceleration





def calculate\_weight(mass, gravity=9.81):

&#x20;   """Weight = Mass \* Gravity"""

&#x20;   return mass \* gravity





def calculate\_kinetic\_energy(mass, velocity):

&#x20;   """Kinetic Energy = 1/2 \* Mass \* Velocity squared"""

&#x20;   return 0.5 \* mass \* velocity \*\* 2





def calculate\_work(force, distance):

&#x20;   """Work Done = Force \* Distance"""

&#x20;   return force \* distance





if \_\_name\_\_ == "\_\_main\_\_":

&#x20;   print("PHYSICS FORMULA CALCULATOR")

&#x20;   print("--------------------------")



&#x20;   print("Speed:", calculate\_speed(100, 10), "m/s")

&#x20;   print("Force:", calculate\_force(10, 5), "N")

&#x20;   print("Weight:", calculate\_weight(10), "N")

&#x20;   print("Kinetic Energy:",

&#x20;         calculate\_kinetic\_energy(10, 5), "J")

&#x20;   print("Work Done:", calculate\_work(20, 5), "J")

