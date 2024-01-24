import time

import pytest


@pytest.mark.slow
def test_slow_marker():
    time.sleep(4)

# pytest -m MARKEXPR <--- adiciona ou remove a seleção de um ou mais marcadores
# pytest -m 'not slow' -vv  <--- para rodar todos os teste menos o slow
# SE HOUVER WARNING adicionar o código abaixo no confitest.py
# def pytest_configure(config):
#     config.addinivalue_line(
#       "markers", "slow: marks tests as slow"
#     )
