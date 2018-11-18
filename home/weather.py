import re
import urllib.request

class Weather:
    def fun_weather(self):
        file = open("WeatherData.txt", 'r')
        var_city = file.read()
        var_city = str(var_city)
        city = var_city.upper()
        file.close()
        url = "https://www.weather-forecast.com/locations/"+city+"/forecasts/latest"
        data = urllib.request.urlopen(url).read()
        data = data.decode('utf-8')

        m = re.search('span class="phrase"', data)

        start = m.end()

        end = start + 100

        maxtemp = re.search('max',str(data[start:end]))
        mintemp = re.search('min',str(data[start:end]))
        temp1 = maxtemp.start()
        temp2 = mintemp.start()
        newString = data[start+temp1:start+temp1+6]
        newString1 = data[start+temp2:start+temp2+6]
        #print(newString + "\u2103",newString1 + "\u2103")
        output = newString + "\u2103",newString1 + "\u2103"
        return output, city
