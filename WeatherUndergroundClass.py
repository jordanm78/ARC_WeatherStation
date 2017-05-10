import time, requests, configparser, logging


class WeatherUnderground(object):#The WeatherUnderground class is an object


    def __init__(self, config):
        #load password and ID from config file
        self.__ID = config.get('WeatherUnderground', 'ID')
        self.__password = config.get('WeatherUnderground', 'password')


    def update(self, weatherData):
        
        #Send the weather data to the normal wunderground website
        self.__sendDataToWebsite(weatherData, "https://weatherstation.wunderground.com/weatherstation/updateweatherstation.php")

    def updateRealtime(self, weatherData):

        #Add two name/value pairs to the data
        weatherData.update({'realtime': 1, 'rtfreq': 2.5})


        #Send the data to the wunderground realtime website
        self.__sendDataToWebsite(weatherData, "https://rtupdate.wunderground.com/weatherstation/updateweatherstation.php")


    def __sendDataToWebsite(self, weatherData, URL):
        
        """
        create a dictionary with the weather underground password,
        key, UTC Time, and update:raw data.

        Use requests to send the data to weather underground.
        """

        weatherUndergroundDictionary = {
            "action":"updateraw",
            "ID":self.__ID,
            "PASSWORD":self.__password,
            "dateutc":self.__getDateTimeString()}

        #Append weather data onto the weather underground dictionary
        weatherUndergroundDictionary.update(weatherData)
        
        #print(str(weatherUndergroundDictionary))

        response = requests.get(URL, params=weatherUndergroundDictionary)
        logging.info("I connected to the following URL: %s" %response.url)
        return response



    def __getDateTimeString(self):

        #Get the UTC time, as a struct_time structure
        #See https://www.tutorialspoint.com/python/python_date_time.htm
        timeUTC = time.gmtime(time.time())
    
        #Parse the time structure into numbers
        year = timeUTC.tm_year
        month = timeUTC.tm_mon
        day = timeUTC.tm_mday
        hour = timeUTC.tm_hour
        minute = timeUTC.tm_min
        second = timeUTC.tm_sec


        """

        The date / time string has to be escaped so that it can be put into a URL.
        So, for instance,

        2001-01-01 10:32:35

        becomes

        2000-01-01+10%3A32%3A35

        See http://wiki.wunderground.com/index.php/PWS_-_Upload_Protocol

        """
        dateTimeString = "%d-%02d-%02d+%02d%s%02d%s%02d" % (year, month, day, hour,
                                                            "%3A", minute, "%3A", second)
        return dateTimeString

if __name__ == "__main__":
    logging.basicConfig(filename='WeatherUndergroundClass.log', level=logging.DEBUG)
    myConfig = configparser.SafeConfigParser()
    myConfig.read('configFile.txt')
    wu = WeatherUnderground(myConfig)
    wu.update({})
    
        
