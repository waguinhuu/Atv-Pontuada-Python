from projeto.models.abstracts.funcionario import Funcionario
from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.setor import Setor
from projeto.models.enums.sexo import Sexo

class Advogado(Funcionario):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estado_civil: EstadoCivil, data_de_nascimento: str, cpf: str, rg: str, matricula: str, setor: Setor, salario: float, oab: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estado_civil, data_de_nascimento, cpf, rg, matricula, setor, salario)
        self.oab = self._verificar_oab(oab)


    def _verificar_oab(self, valor):
        self._verificar_oab_tipo_invalido(valor)

        self.oab = valor
        return self.oab
    
    
    def _verificar_oab_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O OAB deve ser em texto.")