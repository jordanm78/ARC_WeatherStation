import logging
from weather_station.WeatherInstruments.WeatherInstrumentClass import WeatherInstrument

class Anemometer(WeatherInstrument):

    
    def __init__(self, json):
        super().__init__(json)
        print("I am an anemometer")


    def getData(self):
        return {"windspeedmph": self.getWindSpeed()}
    

    def getWindSpeed(self):
        #  Fill in code here that actually gets the wind speed.
        pass
        
        


if __name__ == "__main__":
    logging.basicConfig(filename='WeatherUndergroundClass.log', level=logging.DEBUG)
    a = Anemometer("Hello")
    print(str(a.getData()))
