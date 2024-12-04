from Conversion import Conversion


class Main:
    def run(self) -> None:
        numbers = [9, 95, 955, 9555, 1, 11, 111, 1111, 4,
                   44, 444, 4444, 7, 77, 777, 7777]

        for number in numbers:
            conversion = Conversion(number)
            print(conversion.output())


main = Main()
main.run()
