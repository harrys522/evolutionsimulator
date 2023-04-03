
# do we think environment should be contain entity, or should they be seperate and call tick on environment
MALE = True
FEMALE = False
# digestion scale of 0-1 where an omnivore is 0.5, 0 is herbivore and 1 is carnivore which determines the efficiency of eating 
# other species vs food grow from say a tree

# the ability to move
class Locomotion:
        # dont know if i want the efficiency traits, maybe they exist but only get changed ever so very slightly
    def __init__(self, walking_efficiency, sprinting_efficiency, walking_speed, sprinting_speed):
        self.walking_efficiency = walking_efficiency
        self.sprinting_efficiency = sprinting_efficiency
        self.walking_speed = walking_speed
        self.sprinting_speed = sprinting_speed

# eventually include z, to like climb or fly and it is different planes
class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
class Vision:
    pass

class Hearing:
    pass

# wish some sort of coupling between resistance and damage class exists so if one gets a new trait, it adds to the other since
# resistance and damage are 2 sides of coin
class Resistance:
    def __init__(self, blunt_resist, sharp_resist):
        self.blunt_resist = blunt_resist
        self.sharp_resist = sharp_resist

class State:
    def __init__(self) -> None:
        pass

class Food:
    def __init__(self) -> None:
        pass

# for now the only damage type is blunt and sharp
class Entity:
    # take in all the parameters of the entity
    # previous task is some sort of state which is an enum of different things an entity could do
    def __init__(self, damage, damage_type, locomotion: Locomotion, task: 'State', location: Coordinate, size, resistance: Resistance, sex=MALE, health=100, stamina=100, diet=0.5, body_temp=33, nocturnal=False):
        self.sex = sex
        self.health = health
        self.stamina = stamina
        self.damage = damage
        self.damage_type = damage_type
        self.diet = diet
        self.locomotion = locomotion
        self.task = task # can access prevous task and current task bedepnding on the updates easily
        self.location = location
        self.body_temp = body_temp
        self.nocturnal = nocturnal # boolean
        self.size = size# used in formula for energy calculations and blunt and sharp resistance
        self.resistance = resistance
    



    def reproduce(self):
        pass
    def attack(self, enemy: 'Entity'):
        pass
    # food should be an interface hypothetically and be able to be inherited or be a super class
    def eat(self, object: 'Food'):
        pass
    # runs neural network that spits out the [Direction, Speed, Task]
    # will save the task
    # and then do an act
    # it will do the task if and only if the task location is the same as current location
    def think(self):
        # neural network computes [Direction, Speed, Task, Task Location]
        # store the data inside of the self
        # then something else will perform the 'do' and it will update and see if
        # Task Location is same as current and if so perform the functions inside of the entity
        pass
