from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import UnidadeFederativa
import pytest

@pytest.fixture
def endereco_valido():
    return Endereco("Drena", "93","casa","43900-000","Salvador",UnidadeFederativa.BAHIA.nome)


def tevalidar_endereco(endereco_valido):
    assert endereco_valido.logadouro == "Drena"
    assert endereco_valido.numero == "93"
    assert endereco_valido.complemento == "casa"
    assert endereco_valido.cep == "43900-000"
    assert endereco_valido.cidade == "Salvador"
    assert endereco_valido.uf == UnidadeFederativa.BAHIA.nome



def test_logradouro_vazio():
    with pytest.raises(TypeError, match="O logradouro não deve estar vazio."):
        Endereco("","93","casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome)

        
def test_logadouro_tipo_invalido():
     with pytest.raises(TypeError, match="O logradouro deve ser um texto."):
            Endereco(123,"93","casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome)

def test_numero_tipo_invalido():
    with pytest.raises(TypeError, match="O número deve ser um texto."):
        Endereco("Drena",123,"casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome)


def test_numero_vazio():
    with pytest.raises(TypeError, match="O número não deve estar vazio."):
        Endereco("Drena","","casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome)

def test_cep_tipo_invalido():
    with pytest.raises(TypeError, match="O CEP deve ser um texto."):
        Endereco("Drena","93","casa", 43900000, "Salvador", UnidadeFederativa.BAHIA.nome)


def test_cep_formato_invalido():
    with pytest.raises(ValueError, match="O formato do CEP é inválido."):
        Endereco("Drena","93","casa", "-=-43900-000", "Salvador", UnidadeFederativa.BAHIA.nome)

def test_cep_vazio():
    with pytest.raises(TypeError, match="O CEP não deve estar vazio."):
         Endereco("Drena","93","casa", "", "Salvador", UnidadeFederativa.BAHIA.nome)

def test_cidade_vazia():
    with pytest.raises(TypeError, match="A cidade não deve estar vazia."):
          Endereco("Drena","93","casa", "43900-000", "", UnidadeFederativa.BAHIA.nome)


def test_cidade_tipo_invalido():
    with pytest.raises(TypeError, match="A cidade deve ser um texto."):
            Endereco("Drena","93","casa", "43900-000", 9090, UnidadeFederativa.BAHIA.nome)

def test_complemento_tipo_invalido():
    with pytest.raises(TypeError, match="O complemento deve ser um texto."):
         Endereco("Drena","93",123, "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome)