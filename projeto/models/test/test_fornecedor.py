import pytest
from projeto.models.fornecedor import Fornecedor
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import UnidadeFederativa



@pytest.fixture
def fornecedor_valido():
    return Fornecedor(123, "Wagner", "71912345678","wagner@gmail.com",
            Endereco("Drena", "93","casa","43900-000","Salvador",UnidadeFederativa.BAHIA.nome),"14.796.606/0001-90","445","Manga")


"""VALIDAÇÕES DOS DADOS DO USUARIO"""
def validar_id(fornecedor_valido):
    assert fornecedor_valido.id == 123

def validar_nome(fornecedor_valido):
    assert fornecedor_valido.nome == "Wagner"

def validar_telefone(fornecedor_valido):
    assert fornecedor_valido.telefone ==  "71912345678"

def validar_email(fornecedor_valido):
    assert fornecedor_valido.email == "wagner@gmail.com"

def validar_cnpj(fornecedor_valido):
    assert fornecedor_valido.cnpj == "14.796.606/0001-90"

def validar_inscricao(fornecedor_valido):
    assert fornecedor_valido.inscricao == "445"

def validar_produto(fornecedor_valido):
    assert fornecedor_valido.produto == "Manga"

def validar_endereco(fornecedor_valido):
    assert fornecedor_valido.endereco.logadouro == "Drena"
    assert fornecedor_valido.endereco.numero == "93"
    assert fornecedor_valido.endereco.complemento == "casa"
    assert fornecedor_valido.endereco.cep == "43900-000"
    assert fornecedor_valido.endereco.cidade == "Salvador"
    assert fornecedor_valido.endereco.uf == UnidadeFederativa.BAHIA.nome


"""TESTES NOME"""
def test_nome_tipo_invalido():
    with pytest.raises(TypeError, match="O nome deve ser um texto."):
        Fornecedor(123, 123, "71912345678","wagner@gmail.com",
            Endereco("Drena", "93","casa","43900-000","Salvador",UnidadeFederativa.BAHIA.nome),"14.796.606/0001-90","445","Manga")
        
def test_nome_vazio_retorna_mensagem():
    with pytest.raises(TypeError, match="O nome não deve estar vazio."):
        Fornecedor(123, "", "71912345678","wagner@gmail.com",
            Endereco("Drena", "93","casa","43900-000","Salvador",UnidadeFederativa.BAHIA.nome),"14.796.606/0001-90","445","Manga")   
        

"""TESTES PARA ID"""
def test_id_numero_em_string_retorna_mensagem():
    with pytest.raises(TypeError, match="O id deve ser número."):
        Fornecedor("123", "Wagner", "71912345678","wagner@gmail.com",
            Endereco("Drena", "93","casa","43900-000","Salvador",UnidadeFederativa.BAHIA.nome),"14.796.606/0001-90","445","Manga")
        
"""TESTES PARA EMAIL"""
def test_email_vazio_retorna_menagem():
    with pytest.raises(TypeError, match="O email não deve estar vazio."):
        Fornecedor(123, "Wagner", "71912345678","",
            Endereco("Drena", "93","casa","43900-000","Salvador",UnidadeFederativa.BAHIA.nome),"14.796.606/0001-90","445","Manga")
        
def test_email_formato_invalido():
    with pytest.raises(ValueError, match="O email é inválido."):
        Fornecedor(123, "Wagner", "71912345678",123,
            Endereco("Drena", "93","casa","43900-000","Salvador",UnidadeFederativa.BAHIA.nome),"14.796.606/0001-90","445","Manga")
        

"""TESTES PARA PRODUTO"""
def test_produto_tipo_invalido():
    with pytest.raises(TypeError, match="O produto deve ser um texto."):
        Fornecedor(123, "Wagner", "71912345678", "wagner@gmail.com",
                   Endereco("Drena", "93", "casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome), 
                   "14.796.606/0001-90", "445", 9090)

def test_produto_vazio():
    with pytest.raises(ValueError, match="O produto não deve estar vazio."):
        Fornecedor(123, "Wagner", "71912345678", "wagner@gmail.com",
                   Endereco("Drena", "93", "casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome), 
                    "14.796.606/0001-90", "445", "")


"""TESTES PARA TELEFONE"""
def test_comprimento_telefone_invalido():
    with pytest.raises(TypeError, match="Número de telefone deve conter 11 digitos."):
        Fornecedor(123, "Wagner", "71912345678000","wagner@gmail.com",
            Endereco("Drena", "93","casa","43900-000","Salvador",UnidadeFederativa.BAHIA.nome),"14.796.606/0001-90","445","Manga")

        
def test_telefone_tipo_invalido():
    with pytest.raises(TypeError, match="Coloque o número em forma de texto"):
        Fornecedor(123, "Wagner", 71912345678,"wagner@gmail.com",
            Endereco("Drena", "93","casa","43900-000","Salvador",UnidadeFederativa.BAHIA.nome),"14.796.606/0001-90","445","Manga")

def test_telefone_com_texto():
    with pytest.raises(ValueError, match="O número de telefone deve conter apenas dígitos."):
        Fornecedor(123, "Wagner", "71912345678PP","wagner@gmail.com",
            Endereco("Drena", "93","casa","43900-000","Salvador",UnidadeFederativa.BAHIA.nome),"14.796.606/0001-90","445","Manga")

def test_telefone_vazio():
    with pytest.raises(TypeError, match="O telefone não deve estar vazio"):
        Fornecedor(123, "Wagner", "","wagner@gmail.com",
            Endereco("Drena", "93","casa","43900-000","Salvador",UnidadeFederativa.BAHIA.nome),"14.796.606/0001-90","445","Manga")
       

"""TESTES DE ENDEREÇO"""
def test_logradouro_vazio():
    with pytest.raises(TypeError, match="O logradouro não deve estar vazio."):
       Fornecedor(123, "Wagner", "71912345678","wagner@gmail.com",
            Endereco("", "93","casa","43900-000","Salvador",UnidadeFederativa.BAHIA.nome),"14.796.606/0001-90","445","Manga")


        
def test_logadouro_tipo_invalido():
     with pytest.raises(TypeError, match="O logradouro deve ser um texto."):
            Fornecedor(123, "Wagner", "71912345678","wagner@gmail.com",
            Endereco(123, "93","casa","43900-000","Salvador",UnidadeFederativa.BAHIA.nome),"14.796.606/0001-90","445","Manga")


def test_numero_tipo_invalido():
    with pytest.raises(TypeError, match="O número deve ser um texto."):
       Fornecedor(123, "Wagner", "71912345678","wagner@gmail.com",
            Endereco("Drena", 93,"casa","43900-000","Salvador",UnidadeFederativa.BAHIA.nome),"14.796.606/0001-90","445","Manga")



def test_numero_vazio():
    with pytest.raises(TypeError, match="O número não deve estar vazio."):
        Fornecedor(123, "Wagner", "71912345678","wagner@gmail.com",
            Endereco("Drena", "","casa","43900-000","Salvador",UnidadeFederativa.BAHIA.nome),"14.796.606/0001-90","445","Manga")

def test_cep_tipo_invalido():
    with pytest.raises(TypeError, match="O CEP deve ser um texto."):
       Fornecedor(123, "Wagner", "71912345678","wagner@gmail.com",
            Endereco("Drena", "93","casa", 43900000,"Salvador",UnidadeFederativa.BAHIA.nome),"14.796.606/0001-90","445","Manga")



def test_cep_formato_invalido():
    with pytest.raises(ValueError, match="O formato do CEP é inválido."):
        Fornecedor(123, "Wagner", "71912345678","wagner@gmail.com",
            Endereco("Drena", "93","casa","43900-++000","Salvador",UnidadeFederativa.BAHIA.nome),"14.796.606/0001-90","445","Manga")


def test_cep_vazio():
    with pytest.raises(TypeError, match="O CEP não deve estar vazio."):
         Fornecedor(123, "Wagner", "71912345678","wagner@gmail.com",
            Endereco("Drena", "93","casa","","Salvador",UnidadeFederativa.BAHIA.nome),"14.796.606/0001-90","445","Manga")


def test_cidade_vazia():
    with pytest.raises(TypeError, match="A cidade não deve estar vazia."):
        Fornecedor(123, "Wagner", "71912345678","wagner@gmail.com",
            Endereco("Drena", "93","casa","43900-000","",UnidadeFederativa.BAHIA.nome),"14.796.606/0001-90","445","Manga")


def test_cidade_tipo_invalido():
    with pytest.raises(TypeError, match="A cidade deve ser um texto."):
           Fornecedor(123, "Wagner", "71912345678","wagner@gmail.com",
            Endereco("Drena", "93","casa","43900-000",123,UnidadeFederativa.BAHIA.nome),"14.796.606/0001-90","445","Manga")

def test_complemento_tipo_invalido():
    with pytest.raises(TypeError, match="O complemento deve ser um texto."):
        Fornecedor(123, "Wagner", "71912345678","wagner@gmail.com",
            Endereco("Drena", "93",123,"43900-000","Salvador",UnidadeFederativa.BAHIA.nome),"14.796.606/0001-90","445","Manga")

"""TESTE PARA CNPJ"""
def test_cnpj_vazio():
    with pytest.raises(ValueError, match="O cnpj não deve estar vazio."):
         Fornecedor(123, "Wagner", "71912345678","wagner@gmail.com",
            Endereco("Drena", "93","casa","43900-000","Salvador",UnidadeFederativa.BAHIA.nome),"","445","Manga")

"""TESTE PARA INSCRIÇÃO"""
def test_inscricao_vazio():
    with pytest.raises(ValueError, match="A inscrição não deve estar vazio."):
         Fornecedor(123, "Wagner", "71912345678","wagner@gmail.com",
            Endereco("Drena", "93","casa","43900-000","Salvador",UnidadeFederativa.BAHIA.nome),"14.796.606/0001-90","","Manga")
         
def test_inscricao_tipo_invalido():
     with pytest.raises(TypeError, match="A inscrição deve ser texto."):
        Fornecedor(123, "Wagner", "71912345678","wagner@gmail.com",
            Endereco("Drena", "93","casa","43900-000","Salvador",UnidadeFederativa.BAHIA.nome),"14.796.606/0001-90",445,"Manga")