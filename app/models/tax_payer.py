import logging

from app.main.database import db
from sqlalchemy import Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy_utils import EmailType
from werkzeug.security import generate_password_hash, check_password_hash
from .utils import Country, State


class TaxAccountant(db.Model):
  """
  This is a Tax Payer Model
  """
  __tablename__ = 'taxPayer'

  idx = db.Column(Integer, primary_key=True, autoincrement="auto")
  username = db.Column(String(25), nullable=False, unique=True)
  email = db.Column(EmailType(), nullable=False, unique=True)
  password = db.Column(Text, nullable=False)

  country_id = db.Column(Integer, ForeignKey("country.idx"), nullable=True)
  country = relationship(Country)
  state_id = db.Column(Integer, ForeignKey("state.idx"), nullable=True)
  state = relationship(State)

  is_active = db.Column(db.Boolean(), default=True)
  created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
  updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

  def __init__(self, username, password, email, country_id, state_id):
    self.username = username
    self.password = self.__set_password(password)
    self.email = email
    self.country_id = country_id
    self.state_id = state_id

  @classmethod
  def serialize(cls, data):
    return {
      "username": data['username'],
      "email": data['email'],
      "password": data['password'],
      "country_id": data.get('country', None),
      "state_id": data.get('state', None)
    }

  def deserialize(self):
    country_result = Country.query.filter_by(idx=self.country_id).first()
    state_result = State.query.filter_by(idx=self.state_id).first()
    return {
      "id": self.idx,
      "username": self.username,
      "email": self.email,
      "country": country_result.name if country_result is not None else None,
      "state": state_result.name if state_result is not None else None,
      "is_active": self.is_active,
      "created_at": self.created_at.strftime('%m/%d/%Y'),
      "updated_at": self.updated_at.strftime('%m/%d/%Y')
    }

  @property
  def is_active(self):
    """True, as all users are active."""
    return True

  def save(self):
    db.session.add(self)
    db.session.commit()

  def __set_password(self, password):
    return generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password, password)

  @classmethod
  def get_or_404(cls, idx):
    return cls.query.get_or_404(idx)

  def __repr__(self):
    return "<Tax Payer (username='%s')>" % self.username
