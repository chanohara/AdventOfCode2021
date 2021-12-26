class Display:

    signalE = ''
    signalA = ''
    numberZero = ''
    numberOne = ''
    numberSix = ''
    numberTwo = ''
    numberFour = ''
    numberNine = ''
    numberThree = ''
    numberFive = ''

    def __init__(self, tenDigits, number):
        self.tenDigits = tenDigits
        self.number = number

    def determine_a(self):
        for digit in self.tenDigits:
            if len(digit) == 3:
                seven = digit
            elif len(digit) == 2:
                one = digit
        
        for signal in seven:
            if signal not in one:
                self.signalA = signal
                return
    
    def determine_e(self):
        fiveSignalNumbers = []

        for digits in self.tenDigits:
            if len(digits) == 5:
                fiveSignalNumbers.append(digits)

        fiveSignalNumbersTemp = fiveSignalNumbers.copy()

        for digit in self.numberFour:
            for counter, number in enumerate(fiveSignalNumbers):
                fiveSignalNumbers[counter] = fiveSignalNumbers[counter].replace(digit,'')

        for counter, number in enumerate(fiveSignalNumbers):
            if len(number) == 3:
                self.numberTwo = fiveSignalNumbersTemp[counter]

        numberTwo = self.numberTwo

        for number in fiveSignalNumbersTemp:
            if number == self.numberTwo:
                continue
            for digit in number:
                numberTwo = numberTwo.replace(digit,'')

        self.signalE = numberTwo[0]


    def determineNumberFour(self):
        for number in self.tenDigits:
            if len(number) == 4:
                self.numberFour = sorted(number)
                return

    def determineNumberTwo(self):
        fiveSignalNumbers = []
        for digits in self.tenDigits:
            if len(digits) == 5:
                fiveSignalNumbers.append(digits)

        for number in fiveSignalNumbers:
            if self.signalE in number:
                self.numberTwo = sorted(number)
                return

    def determineNumberNine(self):
        sixSignalNumbers = []
        for digits in self.tenDigits:
            if len(digits) == 6:
                sixSignalNumbers.append(digits)       

        for number in sixSignalNumbers:
            if self.signalE not in number:
                self.numberNine = sorted(number)
                return

    def determineNumerOne(self):
        for number in self.tenDigits:
            if len(number) == 2:
                self.numberOne = sorted(number)
                return

    def determineNumberZeroAndSix(self):
        sixSignalNumbers = []
        for digits in self.tenDigits:
            if len(digits) == 6 and sorted(digits) != self.numberNine:
                sixSignalNumbers.append(digits)    

        tempSixSignalNumbers = sixSignalNumbers.copy()

        for character in self.numberOne:
            tempSixSignalNumbers[0] = tempSixSignalNumbers[0].replace(character,'')

        if len(tempSixSignalNumbers[0]) == 4:
            self.numberZero = sorted(sixSignalNumbers[0])
            self.numberSix = sorted(sixSignalNumbers[1])
        else:
            self.numberZero = sorted(sixSignalNumbers[1])
            self.numberSix = sorted(sixSignalNumbers[0])           

    def determineNumberThreeAndFive(self):
        fiveSignalNumbers = []
        for digits in self.tenDigits:
            if len(digits) == 5 and sorted(digits) != self.numberTwo:
                fiveSignalNumbers.append(digits)

        tempFiveSignalNumbers = fiveSignalNumbers.copy()

        for character in self.numberOne:
            tempFiveSignalNumbers[0] = tempFiveSignalNumbers[0].replace(character,'')             

        if len(tempFiveSignalNumbers[0]) == 4:
            self.numberFive = sorted(fiveSignalNumbers[0])
            self.numberThree = sorted(fiveSignalNumbers[1])
        else:
            self.numberFive = sorted(fiveSignalNumbers[1])
            self.numberThree = sorted(fiveSignalNumbers[0])


    def determineDisplayedNumber(self):
        displayedNumber = ''
        for digit in self.number:
            if len(digit) == 2:
                displayedNumber += '1'
            elif len(digit) == 3:
                displayedNumber += '7'
            elif len(digit) == 7:
                displayedNumber += '8'
            elif len(digit) == 4:
                displayedNumber += '4'
            elif sorted(digit) == self.numberTwo:
                displayedNumber += '2'
            elif sorted(digit) == self.numberNine:
                displayedNumber += '9'
            elif sorted(digit) == self.numberSix:
                displayedNumber += '6'
            elif sorted(digit) == self.numberThree:
                displayedNumber += '3'
            elif sorted(digit) == self.numberFive:
                displayedNumber += '5'
            elif sorted(digit) == self.numberZero:
                displayedNumber += '0'

        return int(displayedNumber)

    def determineCustomMapping(self):
        self.determineNumberFour()
        self.determine_a()
        self.determine_e() 
        self.determineNumerOne()
        self.determineNumberTwo()
        self.determineNumberNine()
        self.determineNumberZeroAndSix()
        self.determineNumberThreeAndFive()

def calcResult(input):

    result = 0
    for line in input:
        display = Display(tenDigits=line.split('|')[0].split(),number=line.split('|')[1].split())
        display.determineCustomMapping()
        result += display.determineDisplayedNumber()

    return result

input = open( "/Users/dennisgauss/Documents/Coding/AdventOfCode2021/input_ex8.txt" ,"r").read().split('\n')
print(calcResult(input))