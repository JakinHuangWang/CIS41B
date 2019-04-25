#Class country: Which includes Country Name, Continent, Population, and Literacy Rate.
class country:
    def __init__(self, line):
        index_Difference = line.rfind('\"') - line.find('\"')
        if(index_Difference != 0):
            line = line.replace('\"', '')
            line = line[0:index_Difference-1].replace(',', ';') + line[index_Difference-1:len(line)]
        line = line.rstrip().rstrip(',')
        line_list = line.split(',')
        self.countryName = line_list[0].rstrip()
        self.continent = line_list[1].rstrip()
        self.pop = float(line_list[2].rstrip())
        if(len(line_list) == 3):
            self.lit = 0
        else:
            self.lit = float(line_list[3].rstrip())   
    #For the method print(countryObj)        
    def __str__(self):
        return self.countryName
    def getCountryName(self):
        return self.countryName
    def getContinent(self):
        return self.continent
    def getPop(self):
        return self.pop
    def getLit(self):
        return self.lit
        