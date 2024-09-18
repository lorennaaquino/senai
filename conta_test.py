import pytest
import conta

@pytest.fixture(autouse=True)
def reset_saldo():
    #reseta o saldo antes de cada teste
    conta.saldo = 0

def test_deposito_valido():
    conta.depositar(100)
    assert conta.verificar_saldo() == 150





def test_deposito_invalido():
    with pytest.raises(ValueError):
        conta.depositar(-50)



def test_saque_invalido():
    conta.depositar(100)
    with pytest.raises(ValueError):
       conta.sacar(150)

def test_saldo_inicial():
    assert conta.verificar_saldo()  == 0