from Conversion import Conversion


class Main:
    def run(self) -> None:
        option = 2

        while (option != 0):
            option = int(input("Deseja converter um numero em algarismo " +
                               "romano?\n  (1) Sim.\n  (0) Nao.\n"))

            match option:
                case 0:
                    print("  ...saindo...")
                    option = 0
                case 1:
                    number = int(input("  Digite o numero:"))
                    conversion = Conversion(number)
                    print(conversion.output())
                    option = 0
                case _:
                    print("  Escolha uma opcao valida.")


main = Main()
main.run()
