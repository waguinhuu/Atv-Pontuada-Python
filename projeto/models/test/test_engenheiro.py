import pytest
from projeto.models.engenheiro import Engenheiro
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import UnidadeFederativa
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.setor import Setor
from projeto.models.enums.estado_civil import EstadoCivil

@pytest.fixture
def engenheiro_valido():
    return Engenheiro(123, "Wagner", "71982345670", "wagner@gmail.com",
                      Endereco("Drena", "93", "casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome), 
                      Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "12345678900", 
                      "12435533", "4556", Setor.ENGENHARIA.nome, 2600, "crea")


"""VALIDAÇÕES DOS DADOS DO USUARIO"""

def validar_id(engenheiro_valido):
    assert engenheiro_valido.id == 123

def validar_nome(engenheiro_valido):
    assert engenheiro_valido.nome == "Wagner"

def validar_telefone(engenheiro_valido):
    assert engenheiro_valido.telefone == "71982345670"

def validar_email(engenheiro_valido):
    assert engenheiro_valido.email == "wagner@gmail.com"

def validar_cpf(engenheiro_valido):
    assert engenheiro_valido.cpf == "12345678900"

def validar_rg(engenheiro_valido):
    assert engenheiro_valido.rg == "12435533"

def validar_matricula(engenheiro_valido):
    assert engenheiro_valido.matricula == "4556"

def validar_estado_civil(engenheiro_valido):
    assert engenheiro_valido.estado_civil == EstadoCivil.SOLTEIRO.nome

def validar_sexo(engenheiro_valido):
    assert engenheiro_valido.sexo == Sexo.MASCULINO.nome

def validar_data_de_nascimento(engenheiro_valido):
    assert engenheiro_valido.data_de_nascimento == "05/06/2005"

def validar_setor(engenheiro_valido):
    assert engenheiro_valido.setor == Setor.ENGENHARIA.nome

def validar_salario(engenheiro_valido):
    assert engenheiro_valido.salario == 2600

def validar_crea(engenheiro_valido):
    assert engenheiro_valido.crea == "crea"


def validar_endereco(engenheiro_valido):
    assert engenheiro_valido.endereco.logadouro == "Drena"
    assert engenheiro_valido.endereco.numero == "93"
    assert engenheiro_valido.endereco.complemento == "casa"
    assert engenheiro_valido.endereco.cidade == "Salvador"
    assert engenheiro_valido.endereco.cep == "43900-000"
    assert engenheiro_valido.endereco.uf == UnidadeFederativa.BAHIA.nome

""" TESTES PARA CPF"""
def test_cpf_vazio():
    with pytest.raises(ValueError, match="O CPF não deve estar vazio."):
        Engenheiro(123, "Wagner", "71982345670", "wagner@gmail.com", 
                    Endereco("Drena", "93", "casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome), 
                    Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "", 
                    "12435533", "4556", Setor.ENGENHARIA.nome, 2600, "crea")

def test_cpf_tipo_invalido():
    with pytest.raises(TypeError, match="O CPF deve ser um texto."):
        Engenheiro(123, "Wagner", "71982345670", "wagner@gmail.com",
                    Endereco("Drena", "93", "casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome),
                    Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", 12345678900,
                    "12435533", "4556", Setor.ENGENHARIA.nome, 2600, "crea")

def test_cpf_formato_invalido():
    with pytest.raises(ValueError, match="O CPF deve conter 11 dígitos numéricos."):
        Engenheiro(123, "Wagner", "71982345670", "wagner@gmail.com",
                    Endereco("Drena", "93", "casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome),
                    Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "123456789",
                    "12435533", "4556", Setor.ENGENHARIA.nome, 2600, "crea")

"""TESTES PARA RG"""
def test_rg_vazio():
    with pytest.raises(ValueError, match="O RG não deve estar vazio."):
        Engenheiro(123, "Wagner", "71982345670", "wagner@gmail.com",
                    Endereco("Drena", "93", "casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome),
                    Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "12345678900",
                    "", "4556", Setor.ENGENHARIA.nome, 2600, "crea")


def test_rg_tipo_invalido():
    with pytest.raises(TypeError, match="O RG deve ser um texto."):
        Engenheiro(123, "Wagner", "71982345670", "wagner@gmail.com",
                    Endereco("Drena", "93", "casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome),
                    Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "12345678900",
                    123456, "4556", Setor.ENGENHARIA.nome, 2600, "crea")
        

"""TESTES PARA MATRÍCULA"""
def test_matricula_vazio():
    with pytest.raises(ValueError, match="A matrícula não deve estar vazia."):
        Engenheiro(123, "Wagner", "71982345670", "wagner@gmail.com",
                    Endereco("Drena", "93", "casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome),
                    Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "12345678900",
                    "12435533", "", Setor.ENGENHARIA.nome, 2600, "crea")

def test_matricula_tipo_invalido():
    with pytest.raises(TypeError, match="A matrícula deve ser um texto."):
        Engenheiro(123, "Wagner", "71982345670", "wagner@gmail.com",
                    Endereco("Drena", "93", "casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome),
                    Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "12345678900",
                    "12435533", 4556, Setor.ENGENHARIA.nome, 2600, "crea")
        
"""TESTES PARA SALÁRIO"""
def test_salario_tipo_invalido():
    with pytest.raises(TypeError, match="O salário deve ser um número."):
        Engenheiro(123, "Wagner", "71982345670", "wagner@gmail.com",
                    Endereco("Drena", "93", "casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome),
                    Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "12345678900",
                    "12435533", "4556", Setor.ENGENHARIA.nome, "dois mil e quinhentos", "crea")

def test_salario_negativo():
    with pytest.raises(ValueError, match="O salário não pode ser negativo."):
        Engenheiro(123, "Wagner", "71982345670", "wagner@gmail.com",
                    Endereco("Drena", "93", "casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome),
                    Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "12345678900",
                    "12435533", "4556", Setor.ENGENHARIA.nome, -2600.0, "crea")


"""TESTES PARA ENDEREÇO"""
def test_logradouro_vazio():
    with pytest.raises(TypeError, match="O logradouro não deve estar vazio."):
        Engenheiro(123, "Wagner", "71982345670", "wagner@gmail.com",
                      Endereco("", "93", "casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome), 
                      Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "12345678900", 
                      "12435533", "4556", Setor.ENGENHARIA.nome, 2600, "crea")

        
def test_logadouro_tipo_invalido():
     with pytest.raises(TypeError, match="O logradouro deve ser um texto."):
          Engenheiro(123, "Wagner", "71982345670", "wagner@gmail.com",
                      Endereco(123, "93", "casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome), 
                      Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "12345678900", 
                      "12435533", "4556", Setor.ENGENHARIA.nome, 2600, "crea")
          
def test_numero_tipo_invalido():
    with pytest.raises(TypeError, match="O número deve ser um texto."):
      Engenheiro(123, "Wagner", "71982345670", "wagner@gmail.com",
                      Endereco("Drena", 93, "casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome), 
                      Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "12345678900", 
                      "12435533", "4556", Setor.ENGENHARIA.nome, 2600, "crea")
      
def test_numero_vazio():
    with pytest.raises(TypeError, match="O número não deve estar vazio."):
      Engenheiro(123, "Wagner", "71982345670", "wagner@gmail.com",
                      Endereco("Drena", "", "casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome), 
                      Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "12345678900", 
                      "12435533", "4556", Setor.ENGENHARIA.nome, 2600, "crea")
      
def test_cep_tipo_invalido():
    with pytest.raises(TypeError, match="O CEP deve ser um texto."):
        Engenheiro(123, "Wagner", "71982345670", "wagner@gmail.com",
                      Endereco("Drena", "93", "casa", 43900000, "Salvador", UnidadeFederativa.BAHIA.nome), 
                      Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "12345678900", 
                      "12435533", "4556", Setor.ENGENHARIA.nome, 2600, "crea")
        

def test_cep_formato_invalido():
    with pytest.raises(ValueError, match="O formato do CEP é inválido."):
       Engenheiro(123, "Wagner", "71982345670", "wagner@gmail.com",
                      Endereco("Drena", "93", "casa", "43900-++000", "Salvador", UnidadeFederativa.BAHIA.nome), 
                      Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "12345678900", 
                      "12435533", "4556", Setor.ENGENHARIA.nome, 2600, "crea")
       
def test_cep_vazio():
    with pytest.raises(TypeError, match="O CEP não deve estar vazio."):
      Engenheiro(123, "Wagner", "71982345670", "wagner@gmail.com",
                      Endereco("Drena", "93", "casa", "", "Salvador", UnidadeFederativa.BAHIA.nome), 
                      Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "12345678900", 
                      "12435533", "4556", Setor.ENGENHARIA.nome, 2600, "crea")
      
def test_cidade_vazia():
    with pytest.raises(TypeError, match="A cidade não deve estar vazia."):
        Engenheiro(123, "Wagner", "71982345670", "wagner@gmail.com",
                      Endereco("Drena", "93", "casa", "43900-000", "", UnidadeFederativa.BAHIA.nome), 
                      Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "12345678900", 
                      "12435533", "4556", Setor.ENGENHARIA.nome, 2600, "crea")

def test_cidade_tipo_invalido():
    with pytest.raises(TypeError, match="A cidade deve ser um texto."):
         Engenheiro(123, "Wagner", "71982345670", "wagner@gmail.com",
                      Endereco("Drena", "93", "casa", "43900-000", 123, UnidadeFederativa.BAHIA.nome), 
                      Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "12345678900", 
                      "12435533", "4556", Setor.ENGENHARIA.nome, 2600, "crea")
         
def test_complemento_tipo_invalido():
    with pytest.raises(TypeError, match="O complemento deve ser um texto."):
        Engenheiro(123, "Wagner", "71982345670", "wagner@gmail.com",
                      Endereco("Drena", "93", 123, "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome), 
                      Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "12345678900", 
                      "12435533", "4556", Setor.ENGENHARIA.nome, 2600, "crea")
        
"""TESTE PARA CREA"""
def test_crea_vazio():
    with pytest.raises(ValueError, match="O crea não deve estar vazio"):
        Engenheiro(123, "Wagner", "71982345670", "wagner@gmail.com",
                        Endereco("Drena", "93", "casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome), 
                        Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "12345678900", 
                        "12435533", "4556", Setor.ENGENHARIA.nome, 2600, "")

"""TESTES PARA DATA DE NASCIMENTO"""    
def test_data_de_nascimento_vazio():
    with pytest.raises(ValueError, match="A data de nascimento não pode estar vazia."):
        Engenheiro(123, "Wagner", "71982345670", "wagner@gmail.com",
                        Endereco("Drena", "93", "casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome), 
                        Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "", "12345678900", 
                        "12435533", "4556", Setor.ENGENHARIA.nome, 2600, "crea")
        
def test_data_de_nascimento_tipo_invalido():
    with pytest.raises(TypeError, match="A data de nascimento deve ser em texto."):
        Engenheiro(123, "Wagner", "71982345670", "wagner@gmail.com",
                        Endereco("Drena", "93", "casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome), 
                        Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, 562005, "12345678900", 
                        "12435533", "4556", Setor.ENGENHARIA.nome, 2600, "crea")