from datetime import datetime
from typing import Tuple

from pydantic import BaseModel, EmailStr, validate_email, PositiveFloat, PositiveInt, validator
from enum import Enum

class ProdutoEnum(str, Enum):
    produto1 = "ZapFlow com Gemini"
    produto2 = "ZapFlow com chatGPT"
    produto3 = "ZapFlow com Llama3.0"

class Vendas(BaseModel):
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutoEnum

    @validator('produto')
    def categoria_deve_estar_no_enum(cls, v):
        return v
