import logging

from flask import jsonify, make_response
from flask_pydantic import validate
from app.main.database import db
from flask_restful import Resource, request
from app.validators.tax_payer import TaxPayerPostModel
from app.models import get_or_create, update_or_create, TaxAccountant


class TaxPayerController(Resource):
  def __init__(self, *args, **kwargs):
    pass

  def get(self):
    if request.args.get('id', None):
      idx = request.args.get('id')
      tax_payer = db.session.query(TaxAccountant).get(idx)
    elif request.args.get('username', None):
      username = request.args.get('username')
      tax_payer = db.session.query(TaxAccountant).filter_by(username=username).first()
    else:
      return {"error": "Bad Request to GET method. Use query string."}, 400
    if tax_payer is None:
      return {"error": "Tax Payer object does not exist"}, 404
    return {"response": tax_payer.deserialize()}, 200

  @validate(body=TaxPayerPostModel)
  def post(self):
    tax_payer, created = get_or_create(
      TaxAccountant,
      TaxAccountant.serialize(data=request.json)
    )
    if created:
      db.session.commit()
      return {"response": "Tax Payer object created."}, 200
    else:
      db.session.rollback()
      return {"error": "Tax Payer object already exist"}, 400

  def delete(self):
    if request.args.get('id', None):
      idx = request.args.get('id')
      tax_payer = db.session.query(TaxAccountant).get(idx)
    else:
      return {"error": "Bad Request to DELETE method. Use query string."}, 400
    if tax_payer is None:
      return {"error": "Tax Payer object does not exist"}, 404
    db.session.delete(tax_payer)
    db.session.commit()
    return {"response": "Tax Payer object deleted"}, 204


class TaxPayerListController(Resource):
  def get(self):
    pass

  def post(self):
    pass
