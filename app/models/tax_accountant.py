from sqlalchemy import Integer, String, Text
from sqlalchemy.sql import func
from sqlalchemy_utils import EmailType
from werkzeug.security import generate_password_hash, check_password_hash
from app.main.database import db


class TaxAccountant(db.Model):
  """
  This is a TaxAccountant Model
  """
  __tablename__ = 'taxAccountant'

  idx = db.Column(Integer, primary_key=True, autoincrement="auto")
  username = db.Column(String(25), nullable=False, unique=True)
  email = db.Column(EmailType(), nullable=False, unique=True)
  password = db.Column(Text, nullable=False)

  is_active = db.Column(db.Boolean(), default=True)
  created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
  updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

  def __init__(self, username, password, email):
    self.username = username
    self.password = self.__set_password(password)
    self.email = email

  @classmethod
  def serialize(cls, data):
    return {
      "username": data['username'],
      "email": data['email'],
      "password": data['password'],
    }

  def deserialize(self):
    return {
      "id": self.idx,
      "username": self.username,
      "email": self.email,
      "is_active": self.is_active,
      "created_at": self.created_at.strftime('%m/%d/%Y'),
      "updated_at": self.updated_at.strftime('%m/%d/%Y')
    }

  @property
  def is_active(self):
    """True, as all users are active."""
    return True

  # def save(self):
  #   db.session.add(self)
  #   db.session.commit()

  def __set_password(self, password):
    return generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password, password)

  @classmethod
  def get_or_404(cls, idx):
    return cls.query.get_or_404(idx)

  def __repr__(self):
    return "<Tax Accountant(fullname='%s', username='%s')>" % (
      self.fullname, self.username)
