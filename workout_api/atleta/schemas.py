from typing import Annotated, Optional
from pydantic import Field, PositiveFloat, UUID4
from workout_api.contrib.schemas import BaseSchema, OutMixin
from workout_api.categorias.schemas import CategoriaIn, CategoriaOut
from workout_api.centro_treinamento.schemas import CentroTreinamentoAtleta, CentroTreinamentoOut


class AtletaIn(BaseSchema):
    nome: Annotated[str, Field(description='Nome do atleta', example='Joao', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta', example='12345678900', max_length=11)]
    idade: Annotated[int, Field(description='Idade do atleta', example=25)]
    peso: Annotated[PositiveFloat, Field(description='Peso do atleta', example=75.5)]
    altura: Annotated[PositiveFloat, Field(description='Altura do atleta', example=1.70)]
    sexo: Annotated[str, Field(description='Sexo do atleta', example='M', max_length=1)]
    categoria: CategoriaIn
    centro_treinamento: CentroTreinamentoAtleta


class AtletaOut(BaseSchema):
    id: Annotated[UUID4, Field(description='Identificador do atleta')]
    nome: str
    cpf: str
    idade: int
    peso: float
    altura: float
    sexo: str
    categoria: CategoriaOut
    centro_treinamento: CentroTreinamentoOut

    class Config:
        from_attributes = True


class AtletaUpdate(BaseSchema):
    nome: Annotated[Optional[str], Field(None, description='Nome do atleta', example='Joao', max_length=50)]
    idade: Annotated[Optional[int], Field(None, description='Idade do atleta', example=25)]
    peso: Annotated[Optional[PositiveFloat], Field(None, description='Peso do atleta', example=75.5)]
    altura: Annotated[Optional[PositiveFloat], Field(None, description='Altura do atleta', example=1.70)]
    sexo: Annotated[Optional[str], Field(None, description='Sexo do atleta', example='M', max_length=1)]
    categoria: Optional[CategoriaIn]
    centro_treinamento: Optional[CentroTreinamentoAtleta]