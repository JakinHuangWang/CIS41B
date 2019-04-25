#Author: Jakin Wang; Description: Read countries from a file and put them in a list
#Allows printing in descending order of literacy rate and population density
from country import country
import collections
DEFAULT_FILENAME = 'lab1in.csv'

#Function getData(filename) reads in the file, stores and counts country inside countryList
def getData(filename, countryList):
    try:
        with open(filename) as infile:
            countryList = [country(line) for line in infile]
            print("Read In ", len(countryList), " Countries\n")
    except IOError:
        print("Error Opening File " + filename)
        raise SystemExit
    return countryList
#Function printAll() Lists out all countries in the countryList
def printAll(countryList):
    for index in range(len(countryList)):
        print(index + 1, countryList[index])
#Function getChoice() Presents a prompt to the user and return the response accordingly       
def getChoice():
    prompt =  "\n==============================================\n"\
    "l. print countries in descending order of literacy rate\n" \
	      "d. print countries based on population density\n" \
	      "q. quit\n" \
              "Enter Your Choice: "
    userChoice = input(prompt).lower()
    while(userChoice not in ['l', 'd', 'q']):
        print("Wrong Input!!! Please Try Again!!")
        userChoice = input(prompt).lower()
    return userChoice
#Function retVal(someFunc) is a decorator for the function popDensity()
def retVal(someFunc):
    def printResult(*args, **kwargs):
        print("\n" + "*" * 12)
        result = print(someFunc(*args, **kwargs))
        print("*" * 12)        
        return result
    return printResult
#Function popDensity() creates a dictionary with the value being a list with length: 2.
#According to continents and population and find max and min.
@retVal
def popDensity(countryList):
    continentPopDict = collections.defaultdict(lambda: [0,0])
    for c in countryList:
        continent = c.getContinent()
        if "EUROPE" in continent:
            continent = "EUROPE"
        elif "AFRICA" in continent:
            continent = "AFRICA"
        continentPopDict[continent][0] += 1
        continentPopDict[continent][1] += c.getPop()    
    for k, v in sorted(continentPopDict.items()):
        print("%s: %.1f" % (k, v[1]/v[0]))
    return max([c.getPop() for c in countryList]), min([c.getPop() for c in countryList])
#Function getCountry() is a generator that yields a list of countries according to the boundary
def genCountry(countryList):
    boundary = 100
    while True:
        yield [c for c in sorted(countryList, key=lambda c:c.lit, reverse=True) if c.lit <= boundary and c.lit > boundary - 10]
        boundary -= 10
#Function litRate() utilizes the generator and prints out the list of countries      
def litRate(gen):
    userChoice = input("Press Enter to see countries and literacy rates, anything else to quit: ").lower()
    while(userChoice == ''):
        litLst = next(gen)
        if(len(litLst) == 0):
            print("No Data At this range!!!")
        else:
            for lit in litLst:
                print(lit, str(lit.getLit()) + '%')
        userChoice = input("Press Enter to see countries and literacy rates, anything else to quit: ").lower()
 #Function main to call getData, printAll, retVal, and getChoice.       
def main():
    countryList = []    
    countryList = getData(DEFAULT_FILENAME, countryList)
    printAll(countryList)
    gen = genCountry(countryList)
    funcDict = {'l':[litRate, gen], 'd':[popDensity, countryList]}
    userChoice = getChoice()
    while(userChoice != 'q'):
        funcDict[userChoice][0](funcDict[userChoice][1])
        userChoice = getChoice()
    print("Program Terminated!!!")
main()
        
    
    