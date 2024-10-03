import pytest
from projeto.models.medico import Medico
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import UnidadeFederativa
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.setor import Setor
from projeto.models.enums.estado_civil import EstadoCivil

@pytest.fixture
def medico_valido():
    return Medico(123, "Wagner", "71982345670", "wagner@gmail.com",
                      Endereco("Drena", "93", "casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome), 
                      Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "12345678900", 
                      "12435533", "4556", Setor.ENGENHARIA.nome, 2600, "CRM/SP 123355")


"""VALIDAÇÕES DOS DADOS DO USUARIO"""

def validar_id(medico_valido):
    assert medico_valido.id == 123

def validar_nome(medico_valido):
    assert medico_valido.nome == "Wagner"

def validar_telefone(medico_valido):
    assert medico_valido.telefone == "71982345670"

def validar_email(medico_valido):
    assert medico_valido.email == "wagner@gmail.com"

def validar_cpf(medico_valido):
    assert medico_valido.cpf == "12345678900"

def validar_rg(medico_valido):
    assert medico_valido.rg == "12435533"

def validar_matricula(medico_valido):
    assert medico_valido.matricula == "4556"

def validar_estado_civil(medico_valido):
    assert medico_valido.estado_civil == EstadoCivil.SOLTEIRO.nome

def validar_sexo(medico_valido):
    assert medico_valido.sexo == Sexo.MASCULINO.nome

def validar_data_de_nascimento(medico_valido):
    assert medico_valido.data_de_nascimento == "05/06/2005"

def validar_setor(medico_valido):
    assert medico_valido.setor == Setor.ENGENHARIA.nome

def validar_salario(medico_valido):
    assert medico_valido.salario == 2600

def validar_crea(medico_valido):
    assert medico_valido.crm == "CRM/SP 123355"


def validar_endereco(medico_valido):
    assert medico_valido.endereco.logadouro == "Drena"
    assert medico_valido.endereco.numero == "93"
    assert medico_valido.endereco.complemento == "casa"
    assert medico_valido.endereco.cidade == "Salvador"
    assert medico_valido.endereco.cep == "43900-000"
    assert medico_valido.endereco.uf == UnidadeFederativa.BAHIA.nome


""" TESTES PARA CPF"""
def test_cpf_vazio():
    with pytest.raises(ValueError, match="O CPF não deve estar vazio."):
        Medico(123, "Wagner", "71982345670", "wagner@gmail.com",
                      Endereco("Drena", "93", "casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome), 
                      Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "", 
                      "12435533", "4556", Setor.ENGENHARIA.nome, 2600, "CRM/SP 123355")

def test_cpf_tipo_invalido():
    with pytest.raises(TypeError, match="O CPF deve ser um texto."):
       Medico(123, "Wagner", "71982345670", "wagner@gmail.com",
                      Endereco("Drena", "93", "casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome), 
                      Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", 12345678900, 
                      "12435533", "4556", Setor.ENGENHARIA.nome, 2600, "CRM/SP 123355")

def test_cpf_formato_invalido():
    with pytest.raises(ValueError, match="O CPF deve conter 11 dígitos numéricos."):
        Medico(123, "Wagner", "71982345670", "wagner@gmail.com",
                      Endereco("Drena", "93", "casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome), 
                      Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "1234567890000", 
                      "12435533", "4556", Setor.ENGENHARIA.nome, 2600, "CRM/SP 123355")

"""TESTES PARA RG"""
def test_rg_vazio():
    with pytest.raises(ValueError, match="O RG não deve estar vazio."):
        Medico(123, "Wagner", "71982345670", "wagner@gmail.com",
                      Endereco("Drena", "93", "casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome), 
                      Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "12345678900", 
                      "", "4556", Setor.ENGENHARIA.nome, 2600, "CRM/SP 123355")

def test_rg_tipo_invalido():
    with pytest.raises(TypeError, match="O RG deve ser um texto."):
        Medico(123, "Wagner", "71982345670", "wagner@gmail.com",
                      Endereco("Drena", "93", "casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome), 
                      Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "12345678900", 
                      12435533, "4556", Setor.ENGENHARIA.nome, 2600, "CRM/SP 123355")
        

"""TESTES PARA MATRÍCULA"""
def test_matricula_vazio():
    with pytest.raises(ValueError, match="A matrícula não deve estar vazia."):
        Medico(123, "Wagner", "71982345670", "wagner@gmail.com",
                      Endereco("Drena", "93", "casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome), 
                      Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "12345678900", 
                      "12435533", "", Setor.ENGENHARIA.nome, 2600, "CRM/SP 123355")
        
def test_matricula_tipo_invalido():
    with pytest.raises(TypeError, match="A matrícula deve ser um texto."):
        Medico(123, "Wagner", "71982345670", "wagner@gmail.com",
                      Endereco("Drena", "93", "casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome), 
                      Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "12345678900", 
                      "12435533", 4556, Setor.ENGENHARIA.nome, 2600, "CRM/SP 123355")
        
"""TESTES PARA SALÁRIO"""
def test_salario_tipo_invalido():
    with pytest.raises(TypeError, match="O salário deve ser um número."):
        Medico(123, "Wagner", "71982345670", "wagner@gmail.com",
                      Endereco("Drena", "93", "casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome), 
                      Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "12345678900", 
                      "12435533", "4556", Setor.ENGENHARIA.nome, "Dois mil e quinhentos", "CRM/SP 123355")
def test_salario_negativo():
    with pytest.raises(ValueError, match="O salário não pode ser negativo."):
        Medico(123, "Wagner", "71982345670", "wagner@gmail.com",
                      Endereco("Drena", "93", "casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome), 
                      Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "12345678900", 
                      "12435533", "4556", Setor.ENGENHARIA.nome, -2600, "CRM/SP 123355")


"""TESTES PARA ENDEREÇO"""
def test_logradouro_vazio():
    with pytest.raises(TypeError, match="O logradouro não deve estar vazio."):
        Medico(123, "Wagner", "71982345670", "wagner@gmail.com",
                      Endereco("", "93", "casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome), 
                      Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "12345678900", 
                      "12435533", "4556", Setor.ENGENHARIA.nome, 2600, "CRM/SP 123355")

        
def test_logadouro_tipo_invalido():
     with pytest.raises(TypeError, match="O logradouro deve ser um texto."):
          Medico(123, "Wagner", "71982345670", "wagner@gmail.com",
                      Endereco(123, "93", "casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome), 
                      Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "12345678900", 
                      "12435533", "4556", Setor.ENGENHARIA.nome, 2600, "CRM/SP 123355")
          
def test_numero_tipo_invalido():
    with pytest.raises(TypeError, match="O número deve ser um texto."):
      Medico(123, "Wagner", "71982345670", "wagner@gmail.com",
                      Endereco("Drena", 93, "casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome), 
                      Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "12345678900", 
                      "12435533", "4556", Setor.ENGENHARIA.nome, 2600, "CRM/SP 123355")
      
def test_numero_vazio():
    with pytest.raises(TypeError, match="O número não deve estar vazio."):
     Medico(123, "Wagner", "71982345670", "wagner@gmail.com",
            Endereco("Drena", "", "casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome), 
                Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "12345678900", 
                    "12435533", "4556", Setor.ENGENHARIA.nome, 2600, "CRM/SP 123355")
      
def test_cep_tipo_invalido():
    with pytest.raises(TypeError, match="O CEP deve ser um texto."):
        Medico(123, "Wagner", "71982345670", "wagner@gmail.com",
            Endereco("Drena", "93", "casa", 43900000, "Salvador", UnidadeFederativa.BAHIA.nome), 
                Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "12345678900", 
                    "12435533", "4556", Setor.ENGENHARIA.nome, 2600, "CRM/SP 123355")

def test_cep_formato_invalido():
    with pytest.raises(ValueError, match="O formato do CEP é inválido."):
       Medico(123, "Wagner", "71982345670", "wagner@gmail.com",
                      Endereco("Drena", "93", "casa", "43900++-000", "Salvador", UnidadeFederativa.BAHIA.nome), 
                      Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "12345678900", 
                      "12435533", "4556", Setor.ENGENHARIA.nome, 2600, "CRM/SP 123355")
       
def test_cep_vazio():
    with pytest.raises(TypeError, match="O CEP não deve estar vazio."):
      Medico(123, "Wagner", "71982345670", "wagner@gmail.com",
            Endereco("Drena", "93", "casa", "", "Salvador", UnidadeFederativa.BAHIA.nome), 
                Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "12345678900", 
                    "12435533", "4556", Setor.ENGENHARIA.nome, 2600, "CRM/SP 123355")
      
def test_cidade_vazia():
    with pytest.raises(TypeError, match="A cidade não deve estar vazia."):
        Medico(123, "Wagner", "71982345670", "wagner@gmail.com",
                      Endereco("Drena", "93", "casa", "43900-000", "", UnidadeFederativa.BAHIA.nome), 
                      Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "12345678900", 
                      "12435533", "4556", Setor.ENGENHARIA.nome, 2600, "CRM/SP 123355")

def test_cidade_tipo_invalido():
    with pytest.raises(TypeError, match="A cidade deve ser um texto."):
        Medico(123, "Wagner", "71982345670", "wagner@gmail.com",
                      Endereco("Drena", "93", "casa", "43900-000",123, UnidadeFederativa.BAHIA.nome), 
                      Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "12345678900", 
                      "12435533", "4556", Setor.ENGENHARIA.nome, 2600, "CRM/SP 123355")
         
def test_complemento_tipo_invalido():
    with pytest.raises(TypeError, match="O complemento deve ser um texto."):
        Medico(123, "Wagner", "71982345670", "wagner@gmail.com",
                      Endereco("Drena", "93", 123, "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome), 
                      Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "12345678900", 
                      "12435533", "4556", Setor.ENGENHARIA.nome, 2600, "CRM/SP 123355")
        

"""TESTES PARA DATA DE NASCIMENTO"""    
def test_data_de_nascimento_vazio():
    with pytest.raises(ValueError, match="A data de nascimento não pode estar vazia."):
        Medico(123, "Wagner", "71982345670", "wagner@gmail.com",
                      Endereco("Drena", "93", "casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome), 
                      Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "", "12345678900", 
                      "12435533", "4556", Setor.ENGENHARIA.nome, 2600, "CRM/SP 123355")
        
def test_data_de_nascimento_tipo_invalido():
    with pytest.raises(TypeError, match="A data de nascimento deve ser em texto."):
        Medico(123, "Wagner", "71982345670", "wagner@gmail.com",
                      Endereco("Drena", "93", "casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome), 
                      Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, 562005, "12345678900", 
                      "12435533", "4556", Setor.ENGENHARIA.nome, 2600, "CRM/SP 123355")
        
def test_crm_tipo_invalido():
      with pytest.raises(TypeError, match="O CRM deve ser em texto"):
        Medico(123, "Wagner", "71982345670", "wagner@gmail.com",
                      Endereco("Drena", "93", "casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome), 
                      Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "12345678900", 
                      "12435533", "4556", Setor.ENGENHARIA.nome, 2600, 123)
        
def test_crm_vazio():
   with pytest.raises(ValueError, match="O CRM não deve estar vazio"):
    Medico(123, "Wagner", "71982345670", "wagner@gmail.com",
                        Endereco("Drena", "93", "casa", "43900-000", "Salvador", UnidadeFederativa.BAHIA.nome), 
                        Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "12345678900", 
                        "12435533", "4556", Setor.ENGENHARIA.nome, 2600, "")