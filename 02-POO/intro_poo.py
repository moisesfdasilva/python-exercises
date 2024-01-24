var_int: int = 1
var_float: float = 0.75
var_str: str = "abc"

# DICAS
# tipo int é inferido sem que eu precise deixar explícito
var1 = 1
# não faça isso, é verboso e desnecessário
var2: int = 1
# importante deixar explícito que começa como int, mas pode mudar para float
var3: int | float = 1

my_list: list[int] = [1, 2, 3]
my_dict: dict[str, float] = {"key1": 1.5, "key2": 2.3}
my_tuple: tuple(str, int) = ("abc", 322)


def my_func(parameter: str) -> int:
    response: str = parameter.count()
    return response

# def my_func(parameter: Union[int, str]):
# def my_func(parameter: int | str):

# def my_func() -> Optional[int] --> pode ser int ou None
# def my_func(param: Callable[[int, str], float]) --> função


def add_two_numbers(num1: int, num2: int) -> int:
    return num1 + num2


class Person:
    def __init__(self, name: str, age: int, height: float) -> None:
        self.name = name
        self.age = age
        self.height = height
