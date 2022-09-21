import re
from pydantic import BaseModel, validator, constr
from app.models import Admin


class AdminPostModel(BaseModel):
  # https://pydantic-docs.helpmanual.io/usage/types/#constrained-types
  username: constr(max_length=20)
  email: constr(min_length=3, max_length=30)
  password: constr()

  class Config:
    orm_mode = True

  @validator('username')
  def username_valid(self, v):
    username = v
    if Admin.query.filter_by(username=username).first():
      raise ValueError('User already exist')

  @validator('email')
  def email_valid(cls, v):
    email = v.lower()
    if re.match(
        '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email
    ) is None:
      raise ValueError('email provided is not valid')
    if Admin.query.filter_by(email=email).first():
      raise ValueError('email already registered')
    return email
