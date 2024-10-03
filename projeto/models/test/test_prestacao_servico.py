import pytest
from projeto.models.prestacao_servico import PrestacaoServico
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def prestacao_servico_valido():
    return PrestacaoServico(123, "Wagner", "71912345678","wagner@gmail.com",
            Endereco("Drena", "93","casa","43900-000","Salvador",UnidadeFederativa.BAHIA.nome),"14.796.606/0001-90","445","05/06/2024","05/06/2029")

def validar_id(prestacao_servico_valido):
    assert prestacao_servico_valido.id == 123

def validar_nome(prestacao_servico_valido):
    assert prestacao_servico_valido.nome == "Wagner"

def validar_telefone(prestacao_servico_valido):
    assert prestacao_servico_valido.telefone ==  "71912345678"

def validar_email(prestacao_servico_valido):
    assert prestacao_servico_valido.email == "wagner@gmail.com"

def validar_cnpj(prestacao_servico_valido):
    assert prestacao_servico_valido.cnpj == "14.796.606/0001-90"

def validar_inscricao(prestacao_servico_valido):
    assert prestacao_servico_valido.inscricao == "445"

def validar_contrato_inicio(prestacao_servico_valido):
    assert prestacao_servico_valido.contrato_inicio == "05/06/2024"

def validar_contrato_fim(prestacao_servico_valido):
    assert prestacao_servico_valido.contrato_fim == "05/06/2029"


def validar_endereco(prestacao_servico_valido):
    assert prestacao_servico_valido.endereco.logadouro == "Drena"
    assert prestacao_servico_valido.endereco.numero == "93"
    assert prestacao_servico_valido.endereco.complemento == "casa"
    assert prestacao_servico_valido.endereco.cidade == "Salvador"
    assert prestacao_servico_valido.endereco.cep == "43900-000"
    assert prestacao_servico_valido.endereco.uf == UnidadeFederativa.BAHIA.nome



"""TESTE DATA DE CONTRATAÇÃO"""
def test_data_contrato_inicio_vazio():
    with pytest.raises(ValueError, match="A data do contrato inicio não deve estar vazia."):
        PrestacaoServico(123, "Wagner", "71912345678","wagner@gmail.com",
            Endereco("Drena", "93","casa","43900-000","Salvador",UnidadeFederativa.BAHIA.nome),"14.796.606/0001-90","445","","05/06/2029")
        
def test_data_contrato_inicio_tipo_invalido():
    with pytest.raises(TypeError, match="A data do contrato inicio deve ser uma string."):
        PrestacaoServico(123, "Wagner", "71912345678","wagner@gmail.com",
            Endereco("Drena", "93","casa","43900-000","Salvador",UnidadeFederativa.BAHIA.nome),"14.796.606/0001-90","445",562024,"05/06/2029")
        
def test_data_contrato_fim_vazio():
    with pytest.raises(ValueError, match="A data do contrato fim não deve estar vazia."):
        PrestacaoServico(123, "Wagner", "71912345678","wagner@gmail.com",
            Endereco("Drena", "93","casa","43900-000","Salvador",UnidadeFederativa.BAHIA.nome),"14.796.606/0001-90","445","05/06/2024","")
        
def test_data_contrato_fim_tipo_invalido():
    with pytest.raises(TypeError, match="A data do contrato fim deve ser uma string."):
        PrestacaoServico(123, "Wagner", "71912345678","wagner@gmail.com",
            Endereco("Drena", "93","casa","43900-000","Salvador",UnidadeFederativa.BAHIA.nome),"14.796.606/0001-90","445","05/06/2024",562029)


"""TESTE PARA ENDEREÇO"""
def test_logradouro_vazio():
    with pytest.raises(TypeError, match="O logradouro não deve estar vazio."):
        PrestacaoServico(123, "Wagner", "71912345678","wagner@gmail.com",
            Endereco("", "93","casa","43900-000","Salvador",UnidadeFederativa.BAHIA.nome),"14.796.606/0001-90","445","05/06/2024","05/06/2029")

        
def test_logadouro_tipo_invalido():
     with pytest.raises(TypeError, match="O logradouro deve ser um texto."):
          PrestacaoServico(123, "Wagner", "71912345678","wagner@gmail.com",
            Endereco(123, "93","casa","43900-000","Salvador",UnidadeFederativa.BAHIA.nome),"14.796.606/0001-90","445","05/06/2024","05/06/2029")
          
def test_numero_tipo_invalido():
    with pytest.raises(TypeError, match="O número deve ser um texto."):
      PrestacaoServico(123, "Wagner", "71912345678","wagner@gmail.com",
            Endereco("Drena", 93,"casa","43900-000","Salvador",UnidadeFederativa.BAHIA.nome),"14.796.606/0001-90","445","05/06/2024","05/06/2029")
      
def test_numero_vazio():
    with pytest.raises(TypeError, match="O número não deve estar vazio."):
      PrestacaoServico(123, "Wagner", "71912345678","wagner@gmail.com",
            Endereco("Drena", "","casa","43900-000","Salvador",UnidadeFederativa.BAHIA.nome),"14.796.606/0001-90","445","05/06/2024","05/06/2029")
      
def test_cep_tipo_invalido():
    with pytest.raises(TypeError, match="O CEP deve ser um texto."):
       PrestacaoServico(123, "Wagner", "71912345678","wagner@gmail.com",
            Endereco("Drena", "93","casa",43900000,"Salvador",UnidadeFederativa.BAHIA.nome),"14.796.606/0001-90","445","05/06/2024","05/06/2029")
        

def test_cep_formato_invalido():
    with pytest.raises(ValueError, match="O formato do CEP é inválido."):
       PrestacaoServico(123, "Wagner", "71912345678","wagner@gmail.com",
            Endereco("Drena", "93","casa","43900-++000","Salvador",UnidadeFederativa.BAHIA.nome),"14.796.606/0001-90","445","05/06/2024","05/06/2029")
       
def test_cep_vazio():
    with pytest.raises(TypeError, match="O CEP não deve estar vazio."):
      PrestacaoServico(123, "Wagner", "71912345678","wagner@gmail.com",
            Endereco("Drena", "93","casa","","Salvador",UnidadeFederativa.BAHIA.nome),"14.796.606/0001-90","445","05/06/2024","05/06/2029")
def test_cidade_vazia():
    with pytest.raises(TypeError, match="A cidade não deve estar vazia."):
        PrestacaoServico(123, "Wagner", "71912345678","wagner@gmail.com",
            Endereco("Drena", "93","casa","43900-000","",UnidadeFederativa.BAHIA.nome),"14.796.606/0001-90","445","05/06/2024","05/06/2029")

def test_cidade_tipo_invalido():
    with pytest.raises(TypeError, match="A cidade deve ser um texto."):
        PrestacaoServico(123, "Wagner", "71912345678","wagner@gmail.com",
            Endereco("Drena", "93","casa","43900-000",123,UnidadeFederativa.BAHIA.nome),"14.796.606/0001-90","445","05/06/2024","05/06/2029")
         
def test_complemento_tipo_invalido():
    with pytest.raises(TypeError, match="O complemento deve ser um texto."):
        PrestacaoServico(123, "Wagner", "71912345678","wagner@gmail.com",
            Endereco("Drena", "93",123,"43900-000","Salvador",UnidadeFederativa.BAHIA.nome),"14.796.606/0001-90","445","05/06/2024","05/06/2029")