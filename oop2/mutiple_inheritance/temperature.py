class Temperature:
    def setcelciues(self,celcius:float):
        self.celcius = celcius

    def getcelcius(self):
        return self.celcius
        
    def getfahrenheit(self):
        return self.celcius * 1.8 + 32

    def getweather(self):
        if self.celcius <= 0:
            return f'Freezing'
        elif self.celcius <= 18:
            return f'Cold '
        elif self.celcius <= 28:
            return f'Warm'
        else:
            return f'Hot'