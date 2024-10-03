from projeto.models.abstracts.funcionario import Funcionario
from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.setor import Setor
from projeto.models.enums.sexo import Sexo

class Engenheiro(Funcionario):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estado_civil: EstadoCivil, data_de_nascimento: str, cpf: str, rg: str, matricula: str, setor: Setor, salario: float, crea: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estado_civil, data_de_nascimento, cpf, rg, matricula, setor, salario)
        self.crea = self._verificar_crea(crea)


    def _verificar_crea(self, valor):
        self._verificar_crea_vazio(valor)

        self.crea = valor
        return self.crea
    
    def _verificar_crea_vazio(self, valor):
        if not valor.strip():
            raise ValueError("O crea não deve estar vazio")