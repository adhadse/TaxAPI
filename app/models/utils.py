import logging

from app.main.database import db
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Country(db.Model, Base):
  __tablename__ = "country"

  idx = db.Column(Integer, primary_key=True)
  name = db.Column(String(100), unique=True, nullable=False)
  central_tax = db.Column(Integer, nullable=False)

  def __init__(self, name, central_tax):
    self.name = name.lower()
    self.central_tax = central_tax

  @classmethod
  def get_or_404(cls, idx):
    return cls.query.get_or_404(idx)

  @classmethod
  def serialize(cls, data):
    return {
      "name": data['name'],
      "central_tax": data['central_tax']
    }

  def deserialize(self):
    return {
      "id": self.idx,
      "name": self.name,
      "tax": self.central_tax,
    }

  def __repr__(self):
    return "<Country (id=%d, name='%s', tax=%d)>" % (
      self.idx, self.name, self.central_tax)


class State(db.Model, Base):
  __tablename__ = "state"

  idx = db.Column(Integer, primary_key=True)
  name = db.Column(String(100), unique=True, nullable=False)
  union_territory = db.Column(db.Boolean, nullable=False, default=False)
  state_tax = db.Column(Integer, nullable=False)

  country_id = db.Column(Integer, ForeignKey("country.idx"), nullable=False)
  country = relationship(Country)

  def __init__(self, name, country_id, state_tax, union_territory=False):
    self.name = name.lower()
    self.country_id = country_id
    self.union_territory = union_territory
    if self.union_territory:
      self.state_tax = 0
    else:
      self.state_tax = state_tax

  @classmethod
  def get_or_404(cls, idx):
    return cls.query.get_or_404(idx)

  @classmethod
  def serialize(cls, data):
    return {
      "name": data['name'],
      "state_tax": data['state_tax'],
      "country_id": data['country'],
      "union_territory": data.get("union_territory", False)
    }

  def deserialize(self):
    return {
      "id": self.idx,
      "name": self.name,
      "tax": self.state_tax,
    }

  def __repr__(self):
    return "<State (id=%d, name='%s', tax=%d)>" % (self.idx, self.name, self.state_tax)
