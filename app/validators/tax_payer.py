import re
from typing import Optional

from pydantic import BaseModel, validator, constr
from app.models import TaxAccountant


class TaxPayerPostModel(BaseModel):
  # https://pydantic-docs.helpmanual.io/usage/types/#constrained-types
  username: constr(max_length=20)
  email: constr(min_length=3, max_length=30)
  password: constr()
  country: Optional[int] = None
  state: Optional[int] = None

  class Config:
    orm_mode = True
    validate_assignment = True

  @validator('country')
  def set_country(cls, country):
    return country or None

  @validator('state')
  def set_state(cls, state):
    return state or None

  @validator('username')
  def username_valid(cls, v):
    username = v
    if TaxAccountant.query.filter_by(username=username).first():
      raise ValueError('User already exist')

  @validator('email')
  def email_valid(cls, v):
    email = v.lower()
    if re.match(
        '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email
    ) is None:
      raise ValueError('email provided is not valid')
    if TaxAccountant.query.filter_by(email=email).first():
      raise ValueError('email already registered')
    return email
