from datetime import datetime
from dataclasses import dataclass
import re

@dataclass
class field_info:
    status: bool
    detail: str


class FieldValidation:


    @classmethod
    def nome_turma_validation(cls, nome_turma:str)-> field_info:
        if len(nome_turma) > 70:
            return field_info(False, "Nome muito grande")
        elif len(nome_turma)==0:
            return field_info(False,"Nome vazio")
        return field_info(True, "Nome valido")           
    

    @classmethod
    def data_inicio(cls, data_inicio:str)-> field_info:
        if len(data_inicio) > 10:
            return field_info(False, "Data de inicio Errada")
        pattern = r'^\d{4}-\d{2}-\d{2}$'        
        if not re.match(pattern, data_inicio):
            return field_info(False, "Formato de dataInicio invalido")
        
        try:
            datetime.strptime(data_inicio,'%Y-%m-%d') 
        except Exception as e:
            return field_info(False, f"Data de inicio invalida({e})" )

        return field_info(True, "Data de Inicio valida")
    

    @classmethod
    def data_fim(cls, data_fim:str)-> field_info:
        if len(data_fim) > 10:
            return field_info(False, "Data de fim Errada")
        pattern = r'^\d{4}-\d{2}-\d{2}$'
        
        if not re.match(pattern,data_fim):
            return field_info(False, "Formato de dataFim invalido")
        try:
            datetime.strptime(data_fim,'%Y-%m-%d') 
        except Exception as e:
            return field_info(False, f"Data de inicio invalida({e})" )

        return field_info(True, "Data de Inicio valida")
   
   
    @classmethod
    def inicio_aula_validation(cls, inicio_aula:str)-> field_info:
        if len(inicio_aula) > 10:
            return field_info(False, "Inicio de aula muito grande")
        return field_info(True, "Inicio de aula valido")
    

    @classmethod
    def fim_aula_validation(cls, fim_aula:str)-> field_info:
        if len(fim_aula) > 10:
            return field_info(False, "Inicio de aula muito grande")
        return field_info(True, "Inicio de aula valido")
    

    @classmethod
    def professor_validation(cls, fk_professor:str)-> field_info:
        if len(fk_professor) > 100:
            return field_info(False, "Professor muito grande")
        return field_info(True, "Professor esta certo")
    

    @classmethod 
    def capacidade_validation(cls, capacidade: int)-> field_info:
        if capacidade == 0:
            return field_info(False, "A capacidade não pode ser nula") 
        return field_info(True, "Capacidade valida")
    
    @classmethod
    def codigo_validation(cls, codigo: int):
        if codigo == 0:
            return field_info(False, "A codigo não pode ser nulo") 
        return field_info(True, "Codigo valida")
    