import pytest
from projeto.models.cliente import Cliente
from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def cliente_valido():
    return Cliente(123, "Wagner","71982828222", "wagner@gmail.com",
        Endereco("Drena","93","casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", 4556)



"""VALIDAÇÕES DOS DADOS DO USUARIO"""

def validar_id(cliente_valido):
    assert cliente_valido.id == 123

def validar_nome(cliente_valido):
    assert cliente_valido.nome == "Wagner"

def validar_telefone(cliente_valido):
    assert cliente_valido.telefone ==  "71982828222"

def validar_email(cliente_valido):
    assert cliente_valido.email == "wagner@gmail.com"

def validar_sexo(cliente_valido):
    assert cliente_valido.sexo == Sexo.MASCULINO.nome

def validar_estado_civil(cliente_valido):
    assert cliente_valido.estado_civil == EstadoCivil.SOLTEIRO.nome

def validar_data_nascimento(cliente_valido):
    assert cliente_valido.data_de_nascimento == "05/06/2005"

def validar_protocolo_de_atendimento(cliente_valido):
    assert cliente_valido.protocolo_de_atendimento == 4556


def validar_endereco(cliente_valido):
    assert cliente_valido.endereco.logadouro == "Drena"
    assert cliente_valido.endereco.numero == "93"
    assert cliente_valido.endereco.complemento == "casa"
    assert cliente_valido.endereco.cidade == "Salvador"
    assert cliente_valido.endereco.cep == "43900-000"
    assert cliente_valido.endereco.uf == UnidadeFederativa.BAHIA.nome == "Bahia"

"""TESTES PARA NOME"""
def test_nome_tipo_invalido():
    with pytest.raises(TypeError, match="O nome deve ser um texto."):
         Cliente(123, 123, "71982828222", "wagner@gmail.com",
            Endereco("Drena","93","casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", 4556)

def test_nome_vazio_retorna_mensagem():
    with pytest.raises(TypeError, match="O nome não deve estar vazio."):
        Cliente(123, "", "71982828222", "wagner@gmail.com",
            Endereco("Drena","93","casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", 4556)

"""TESTES PARA TELEFONE"""
def test_comprimento_telefone_invalido():
    with pytest.raises(TypeError, match="Número de telefone deve conter 11 digitos."):
        Cliente(123, "Wagner","7198282822200", "wagner@gmail.com",
            Endereco("Drena","93","casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", 4556)
        
def test_telefone_tipo_invalido():
    with pytest.raises(TypeError, match="Coloque o número em forma de texto"):
        Cliente(123, "Wagner",71982828222, "wagner@gmail.com",
            Endereco("Drena","93","casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", 4556)

def test_telefone_com_texto():
    with pytest.raises(ValueError, match="O número de telefone deve conter apenas dígitos."):
        Cliente(123, "Wagner","71982828222PP", "wagner@gmail.com",
            Endereco("Drena","93","casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", 4556)

def test_telefone_vazio():
    with pytest.raises(TypeError, match="O telefone não deve estar vazio"):
        Cliente(123, "Wagner","", "wagner@gmail.com",
            Endereco("Drena","93","casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", 4556)

"""TESTES PARA PROTOCOLO DE ATENDIMENTO"""
def test_protocolo_de_atendimento_tipo_invalido():
    with pytest.raises(TypeError, match="O protocolo de atendimento deve ser número"):
        Cliente(123, "Wagner", "71982828222", "wagner@gmail.com",
            Endereco("Drena","93","casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "4556")

def test_protocolo_de_atendimento_valor_negativo_retorna_mensagem():
    with pytest.raises(ValueError, match="O protocolo de atendimento deve ser número positivo."):
        Cliente(123, "Wagner", "71982828222", "wagner@gmail.com",
             Endereco("Drena","93","casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", -4556)

"""TESTES PARA ID"""
def test_id_numero_em_string_retorna_mensagem():
    with pytest.raises(TypeError, match="O id deve ser número."):
        Cliente("123", "Wagner","71982828222", "wagner@gmail.com",
            Endereco("Drena","93","casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", 4556)

"""TESTES PARA EMAIL"""
def test_email_vazio_retorna_menagem():
    with pytest.raises(TypeError, match="O email não deve estar vazio."):
        Cliente(123, "Wagner","71982828222", "",
            Endereco("Drena","93","casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", 4556)

def test_email_formato_invalido():
    with pytest.raises(ValueError, match="O email é inválido."):
        Cliente(123, "Wagner","71982828222", 123,
            Endereco("Drena","93","casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", 4556)


"""TESTES PARA ENDEREÇO"""
def test_logradouro_vazio():
    with pytest.raises(TypeError, match="O logradouro não deve estar vazio."):
       Cliente(123, "Wagner","71982828222", "wagner@gmail.com",
            Endereco("","93","casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", 4556)

        
def test_logadouro_tipo_invalido():
     with pytest.raises(TypeError, match="O logradouro deve ser um texto."):
        Cliente(123, "Wagner","71982828222", "wagner@gmail.com",
            Endereco(123,"93","casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", 4556)


def test_numero_tipo_invalido():
    with pytest.raises(TypeError, match="O número deve ser um texto."):
       Cliente(123, "Wagner","71982828222", "wagner@gmail.com",
             Endereco("Drena",93,"casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", 4556)

def test_numero_vazio():
    with pytest.raises(TypeError, match="O número não deve estar vazio."):
        Cliente(123, "Wagner","71982828222", "wagner@gmail.com",
            Endereco("Drena","","casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", 4556)

def test_cep_tipo_invalido():
    with pytest.raises(TypeError, match="O CEP deve ser um texto."):
       Cliente(123, "Wagner","71982828222", "wagner@gmail.com",
             Endereco("Drena","93","casa", 43900000, "Salvador", UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", 4556)


def test_cep_formato_invalido():
    with pytest.raises(ValueError, match="O formato do CEP é inválido."):
        Cliente(123, "Wagner","71982828222", "wagner@gmail.com",
            Endereco("Drena","93","casa", "43900++-000", "Salvador", UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", 4556)


def test_cep_vazio():
    with pytest.raises(TypeError, match="O CEP não deve estar vazio."):
        Cliente(123, "Wagner","71982828222", "wagner@gmail.com",
            Endereco("Drena","93","casa", "", "Salvador", UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", 4556)


def test_cidade_vazia():
    with pytest.raises(TypeError, match="A cidade não deve estar vazia."):
        Cliente(123, "Wagner","71982828222", "wagner@gmail.com",
            Endereco("Drena","93","casa", "43900-000", "", UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", 4556)


def test_cidade_tipo_invalido():
    with pytest.raises(TypeError, match="A cidade deve ser um texto."):
        Cliente(123, "Wagner","71982828222", "wagner@gmail.com",
            Endereco("Drena","93","casa", "43900-000", 123, UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", 4556)

def test_complemento_tipo_invalido():
    with pytest.raises(TypeError, match="O complemento deve ser um texto."):
        Cliente(123, "Wagner","71982828222", "wagner@gmail.com",
            Endereco("Drena","93",123, "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome),Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", 4556)