from datetime import datetime
from dataclasses import dataclass
import re

@dataclass
class fieldInfo:
    status: bool
    detail: str


class FieldValidation:


    @classmethod
    def nomeTurmaValidation(cls, nome_turma:str)-> fieldInfo:
        if len(nome_turma) > 70:
            return fieldInfo(False, "Nome muito grande")
        elif len(nome_turma)==0:
            return fieldInfo(False,"Nome vazio")
        return fieldInfo(True, "Nome valido")           
    

    @classmethod
    def data_inicio(cls, data_inicio:str)-> fieldInfo:
        if len(data_inicio) > 10:
            return fieldInfo(False, "Data de inicio Errada")
        pattern = r'^\d{4}-\d{2}-\d{2}$'        
        if not re.match(pattern, data_inicio):
            return fieldInfo(False, "Formato de dataInicio invalido")
        
        try:
            datetime.strptime(data_inicio,'%Y-%m-%d') 
        except Exception as e:
            return fieldInfo(False, f"Data de inicio invalida({e})" )

        return fieldInfo(True, "Data de Inicio valida")
    

    @classmethod
    def data_fim(cls, data_fim:str)-> fieldInfo:
        if len(data_fim) > 10:
            return fieldInfo(False, "Data de fim Errada")
        pattern = r'^\d{4}-\d{2}-\d{2}$'
        
        if not re.match(pattern,data_fim):
            return fieldInfo(False, "Formato de dataFim invalido")
        try:
            datetime.strptime(data_fim,'%Y-%m-%d') 
        except Exception as e:
            return fieldInfo(False, f"Data de inicio invalida({e})" )

        return fieldInfo(True, "Data de Inicio valida")
   
   
    @classmethod
    def inicioAulaValidation(cls, inicio_aula:str)-> fieldInfo:
        if len(inicio_aula) > 10:
            return fieldInfo(False, "Inicio de aula muito grande")
        return fieldInfo(True, "Inicio de aula valido")
    

    @classmethod
    def fimAulaValidation(cls, fim_aula:str)-> fieldInfo:
        if len(fim_aula) > 10:
            return fieldInfo(False, "Inicio de aula muito grande")
        return fieldInfo(True, "Inicio de aula valido")
    

    @classmethod
    def professorValidation(cls, fk_professor:str)-> fieldInfo:
        if len(fk_professor) > 100:
            return fieldInfo(False, "Professor muito grande")
        return fieldInfo(True, "Professor esta certo")
    

    @classmethod 
    def capacidadeValidation(cls, capacidade: int)-> fieldInfo:
        if capacidade == 0:
            return fieldInfo(False, "A capacidade não pode ser nula") 
        return fieldInfo(True, "Capacidade valida")
    
    @classmethod
    def codigoValidation(cls, codigo: int):
        if codigo == 0:
            return fieldInfo(False, "A codigo não pode ser nulo") 
        return fieldInfo(True, "Codigo valida")
    