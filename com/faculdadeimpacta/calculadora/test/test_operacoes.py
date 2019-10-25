from com.faculdadeimpacta.calculadora import operacoes


def test_soma():
    assert operacoes.soma(20,30) == 50, 'Should be 50' 