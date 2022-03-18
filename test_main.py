import pytest
from main import suma, invertir, palindroma, arraySuma, sumaMatriz

def test_suma():
    assert suma(2, 2) == 4

@pytest.mark.parametrize(
    "input_a, input_b, expected",
    [
        (3, 2, 5),
        (2, 3, 5),
        (suma(3, 2), 5, 10),
        (3, suma(2, 5),10)
    ]
)
def test_suma_multi(input_a, input_b, expected):
    assert suma(input_a, input_b) == expected

def test_invertir():
    assert invertir('memo')=='omem'

def test_palindroma():
    assert palindroma('anitalavalatina')=='La cadena es palindroma'

def test_palindroma():
    assert palindroma('estanoespalindroma')=='La cadena no es palindroma'

def test_arraySuma():
    assert arraySuma([1,2,3,4]) == 10

def test_sumaMat():
    assert sumaMatriz([[1,2,3],[4,5,6],[9,8,9]],3) == 2