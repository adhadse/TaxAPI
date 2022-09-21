from pydantic import BaseModel, constr, PositiveInt


class CountryPostModel(BaseModel):
  # https://pydantic-docs.helpmanual.io/usage/types/#constrained-types
  name: constr(max_length=100)
  central_tax: PositiveInt

  class Config:
    orm_mode = True
