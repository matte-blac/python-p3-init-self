#!/usr/bin/env python3

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Hello! My name is {self.name}')

    def walk(self):
        print(f'{self.name} is walking')
    pass
