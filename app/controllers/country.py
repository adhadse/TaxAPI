from flask_pydantic import validate
from app.main.database import db
from flask import jsonify
from flask_restful import Resource, request
from app.validators.country import CountryPostModel
from app.models import get_or_create, update_or_create, Country
from sqlalchemy.orm.exc import ObjectDeletedError


class CountryController(Resource):
  def __init__(self, *args, **kwargs):
    pass

  def get(self):
    if request.args.get('id', None):
      idx = request.args.get('id')
      country = db.session.query(Country).get(idx)
    elif request.args.get('name', None):
      name = request.args.get('name')
      country = db.session.query(Country).filter_by(name=name).first()
    else:
      return {"error": "Bad Request to GET method. Use query string."}, 400
    if country is None:
      return {"error": "Country object does not exist"}, 404
    return {"response": country.deserialize()}, 200

  @validate(body=CountryPostModel)
  def post(self):
    country, created = get_or_create(
      Country,
      Country.serialize(data=request.json)
    )
    if created:
      db.session.commit()
      return {"response": "Country object created."}, 200
    else:
      db.session.rollback()
      return {"error": "Country object already exist"}, 400

  def delete(self):
    if request.args.get('id', None):
      idx = request.args.get('id')
      country = db.session.query(Country).get(idx)
    else:
      return {"error": "Bad Request to DELETE method. Use query string."}, 400
    if country is None:
      return {"error": "Country object does not exist"}, 404
    db.session.delete(country)
    db.session.commit()
    db.session.flush()
    return {"response": "Country object deleted"}, 204

