from app.main.database import db
from app.models.admin import Admin
from app.models.tax_payer import TaxAccountant
from app.models.tax_accountant import TaxAccountant
from app.models.utils import Country, State


from sqlalchemy.exc import IntegrityError, NoResultFound


def _extract_model_params(defaults, **kwargs):
  defaults = defaults or {}
  ret = {}
  ret.update(kwargs)
  ret.update(defaults)
  return ret


def _create_object_from_params(model, lookup, params, lock=False):
  obj = model(**params)
  db.session.add(obj)
  try:
    with db.session.begin_nested():
      db.session.flush()
  except IntegrityError:
    db.session.rollback()
    query = db.session.query(model).filter_by(**lookup)
    if lock:
      query = query.with_for_update()
    try:
      obj = query.one()
    except NoResultFound:
      raise
    else:
      return obj, False
  else:
    return obj, True


def get_or_create(
    model,
    defaults=None,
    **kwargs):
  try:
    return db.session.query(model).filter_by(**kwargs).one(), False
  except NoResultFound:
    params = _extract_model_params(defaults, **kwargs)
    return _create_object_from_params(model, kwargs, params)


def update_or_create(model, defaults=None, **kwargs):
  defaults = defaults or {}
  with db.session.begin_nested():
    try:
      obj = db.session.query(model).with_for_update().filter_by(**kwargs).one()
    except NoResultFound:
      params = _extract_model_params(defaults, **kwargs)
      obj, created = _create_object_from_params(
        db.session, model, kwargs, params, lock=True)
      if created:
        return obj, created
    for k, v in defaults.items():
      setattr(obj, k, v)
    db.session.add(obj)
    db.session.flush()
  return obj, False
