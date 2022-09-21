from typing import Optional

from pydantic import BaseModel, constr, PositiveInt, validator


class StatePostModel(BaseModel):
  # https://pydantic-docs.helpmanual.io/usage/types/#constrained-types
  name: constr(max_length=100)
  country: PositiveInt
  state_tax: PositiveInt
  union_territory: Optional[bool] = False

  class Config:
    orm_mode = True
    validate_assignment = True

  @validator('union_territory')
  def set_union_territory(cls, union_territory):
    return union_territory or False
