from abc import ABCMeta, abstractmethod
"""
ABC is an Abstract Base Class.

Any child classes must override methods marked @abstractmethod.
"""

class WeatherInstrument(object): #The WeatherInstrument class is an object

    __metaclass__ = ABCMeta

    def __init__(self, json):
        #This method should be overidden to read class data from a config file
        print("I am a weather instrument")

    def start(self):
        #This method can be overridden to start any processes that will run continuously
        pass  #Python requires a statement here, but I don't want to do anything.
              #The pass statement is a statement that does nothing.


    def stop(self):
        #This method should end any processes that were started in the start method
        pass


    @abstractmethod
    def getData(self):
        #This method should return a dictionary with name/value pairs of data
        return dict()
