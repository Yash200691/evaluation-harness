from pydantic import BaseModel, Field

class Product(BaseModel):
    product_id: str
    name:str
    category:str
    price:float=Field(gt=0)
    ram_gb:int=Field(gt=0)
    stock:int=Field(ge=0)