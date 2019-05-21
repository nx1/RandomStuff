# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#The Class is the building block of Object oriented programming.
#A class is like a blueprint for an object

#An obejct is an instance of a class.

#When a class is defined it takes up no memory until it is instantiated.
class BrickHouse:
    material = 'brick'
    
    def __init__(self, floors, rooms, chairs, stairs, shelves, location):
        self.floors = floors
        self.rooms = rooms
        self.chairs = chairs
        self.stairs = stairs
        self.shelves = shelves
        self.location = location        
    def describe(self):
        return 'The {} House has {} floors, {} rooms, {} chairs and {} shelves'\
    .format(self.location, self.floors, self.rooms, self.chairs, self.shelves)

    def inventory(self):
        cost = 0
        price_dict = {self.rooms: 1000,
                      self.chairs: 30,
                      self.floors: 3000,
                      self.stairs: 200,
                      self.shelves : 5}
        for i in price_dict:
            cost += i * price_dict[i]
        return  cost
    
class Shape:
    def __init__(self, color, size):
        self.color = color
        self.size = size

class Cube(Shape):
    shape_type = 'Cube'
    faces = 6
    edges = 12 
    vertices = 8
    interior_angle = 90
    def grow(self, factor):
        self.size = self.size * factor
        return print('{} grew by {} to {}'.format(self.shape_type, factor, self.size))
    

class Dog:
    species = 'mammal'

    def __init__(self, name, color, strength,mental_state):
        self.name = name        
        self.color = color
        self.strength = strength
        self.mental_state = mental_state
        
    def scream(self, words):
        word_upper = str.upper(words)
        return '{}!!! shouted {} the {}'.format(word_upper, self.name, 
                self.mental_state)
    
#Inheriting parent classes
class GermanShepard(Dog):
    def sprint(self):
        return '{} the German Shepard starts sprinting...'.format(self.name)
    def guard(self):
        self.strength = 75
        self.aggresive = True
    
    
north_house = BrickHouse(2,5,6,1,20, 'North')
south_house = BrickHouse(1,3,2,0,1, 'South')

bilo = Dog('bilO', 'blue', 99, 'retard')
gali = GermanShepard('Gali', 'Brown', 30, 'attentive')

green_cube = Cube('green', 1)

green_cube.grow(2)
green_cube.grow(4)
green_cube.grow(6)
green_cube.grow(9)



