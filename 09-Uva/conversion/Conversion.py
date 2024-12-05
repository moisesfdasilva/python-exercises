class Conversion:
    def __init__(self, number):
        self._numberToConvert = number

    def output(self) -> str:
        romanNumeral = ""
        number = self._numberToConvert

        while (number > 0):
            if (number >= 1000):
                romanNumeral += "M"
                number -= 1000
            elif (number >= 100 and number < 1000):
                if (number >= 900):
                    romanNumeral += "CM"
                    number -= 900
                elif (number < 900 and number >= 500):
                    romanNumeral += "D"
                    number -= 500
                elif (number < 500 and number >= 400):
                    romanNumeral += "CD"
                    number -= 400
                else:
                    romanNumeral += "C"
                    number -= 100
            elif (number >= 10 and number < 100):
                if (number >= 90):
                    romanNumeral += "XC"
                    number -= 90
                elif (number < 90 and number >= 50):
                    romanNumeral += "L"
                    number -= 50
                elif (number < 50 and number >= 40):
                    romanNumeral += "XL"
                    number -= 40
                else:
                    romanNumeral += "X"
                    number -= 10
            else:
                if (number == 9):
                    romanNumeral += "IX"
                    number -= 9
                elif (number < 9 and number >= 5):
                    romanNumeral += "V"
                    number -= 5
                elif (number == 4):
                    romanNumeral += "IV"
                    number -= 4
                else:
                    romanNumeral += "I"
                    number -= 1

        return romanNumeral
