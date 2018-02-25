# 14. Kinetic Energy

# Functions
def kinetic_energy(mass,velocity):
    ke = .5 * mass * (velocity ** 2)
    return ke


# Program
mass = float(input("Enter the mass: "))
velocity = float(input("Enter the velocity: "))

print("The kinectic energy is",kinetic_energy(mass,velocity))
