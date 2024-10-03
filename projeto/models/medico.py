from projeto.models.abstracts.funcionario import Funcionario
from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.setor import Setor
from projeto.models.enums.sexo import Sexo

class Medico(Funcionario):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estado_civil: EstadoCivil, data_de_nascimento: str, cpf: str, rg: str, matricula: str, setor: Setor, salario: float, crm: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estado_civil, data_de_nascimento, cpf, rg, matricula, setor, salario)
        self.crm = self._verificar_crm(crm)

    def _verificar_crm(self, valor):
        self._verificar_crm_tipo_invalido(valor)
        self._verificar_crm_vazio(valor)

        self.crm = valor
        return self.crm
    
    def _verificar_crm_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O CRM deve ser em texto")
    
    def _verificar_crm_vazio(self, valor):
        if not valor.strip():
            raise ValueError("O CRM não deve estar vazio")