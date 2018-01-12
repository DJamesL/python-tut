import os
import sys

class human:
    __name = ""  #"__" denotes private variable
    __weight = 0
    __height = 0
    __sex = ""
    xname ="james"

    def __init__(self, name, weight, height, sex):
        self.__name = name
        self.__weight = weight
        self.__height = height
        self.__sex = sex

    def set_name(self, name):
        self.__name = name

    def set_weight(self, weight):
        self.__weight = weight

    def set_height(self, taas):
        self.__height = taas

    def set_sex(self, kasarian):
        self.__sex = kasarian

    def get_name(self):
        return self.__name

    def get_weight(self):
        return self.__weight

    def get_height(self):
        return self.__height

    def get_sex(self):
        return self.__sex

    def get_type(self):
        print("Human")

    def display(self):
        return "My names is {}. I am a {}, with {} in heigh , and {}kgs.".format(self.__name,
                                                                                  self.__sex,
                                                                                  self.__height,
                                                                                  self.__weight)



anna = human("anna", 45, 90, "Female")

print(anna.get_name())
print(anna.get_type())
print(anna.display())


class android(human): #inheritance, Class Android has all Human properties
    __serialNum = 0

    def __init__(self, name, weight, height, sex, serial):
        super().__init__(name,weight,height,sex)
        self.__serialNum = serial

    def set_serial(self, serial):
        self.__serialNum = serial

    def get_serial(self):
        return self.__serialNum

    def lagyu(self):
        return self.__name

    def get_type(self):
        return "Android"

    def display(self):
        return "My names is {}.".format(self._human__name)

robocop = android("robocop", 1000, 999, "Male", 3213)
print(robocop.get_type())
print(robocop.get_name())
print(robocop.display())


'''
POLYmorphism
'''

class LifeTesting:
    def get_type(self, human):
        human.get_type()

wallE = LifeTesting()
wallE.get_type(robocop)
wallE.get_type(anna)

