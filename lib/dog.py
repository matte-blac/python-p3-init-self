#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed='Mutt'):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f'Woof! My name is {self.name} and I am a {self.breed}')
    pass