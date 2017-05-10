import logging, random
from weather_station.WeatherInstruments.ConcreteWeatherInstruments.AnemometerClass import Anemometer



class test_Anemometer(Anemometer):

    
    def __init__(self,json):
        super().__init__(json)
        print("I am a dummy anemometer")



    def getWindSpeed(self):
        return 20*random.random()
    

if __name__ == "__main__":
    logging.basicConfig(filename='WeatherUndergroundClass.log', level=logging.DEBUG)
    d = DummyAnemometer("Hello")
    print(str(d.getData()))
