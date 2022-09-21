import logging

from flask_pydantic import validate
from app.main.database import db
from flask import jsonify
from flask_restful import Resource, request
from app.validators.state import StatePostModel
from app.models import get_or_create, update_or_create, State
from sqlalchemy.orm.exc import ObjectDeletedError


class StateController(Resource):
  def __init__(self, *args, **kwargs):
    pass

  def get(self):
    if request.args.get('id', None):
      idx = request.args.get('id')
      state = db.session.query(State).get(idx)
    elif request.args.get('name', None):
      name = request.args.get('name')
      state = db.session.query(State).filter_by(name=name).first()
    else:
      return {"error": "Bad Request to GET method. Use query string."}, 400
    if state is None:
      return {"error": "State object does not exist"}, 404
    return {"response": state.deserialize()}, 200

  @validate(body=StatePostModel)
  def post(self):
    state, created = get_or_create(
      State,
      State.serialize(data=request.json)
    )
    if created:
      db.session.commit()
      return {"response": "State object created."}, 200
    else:
      db.session.rollback()
      return {"error": "State object already exist"}, 400

  def delete(self):
    if request.args.get('id', None):
      idx = request.args.get('id')
      state = db.session.query(State).get(idx)
    else:
      return {"error": "Bad Request to DELETE method. Use query string."}, 400
    if state is None:
      return {"error": "State object does not exist"}, 404
    db.session.delete(state)
    db.session.commit()
    return {"response": "State object deleted"}, 204

