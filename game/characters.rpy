# characters are defined here

init python:
    class Char:
        def __init__(self, character, name, affection=None):
            self.c = character
            self.name = name
            self.affection = affection
            

define Cam = Char(Character("[povname]"), "[povname]")
define Student = Char(Character("Student A"), "Student A", 0)
define Bill = Char(Character("William 'Bill' Ceriph"), "Bill", 0)
define Eve = Char(Character("Eve"), "Eve", 0)
define Prof = Char(Character("Professor Muskerburg"), "Professor Muskerburg", 0)

image Cam neutral = "green normal.png"