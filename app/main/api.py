from flask_restx import Api
from app.controllers.tax_payer import (
    TaxPayerListController, TaxPayerController)
from app.controllers.country import CountryController
from app.controllers.state import StateController
from app.controllers.tax_accountant import  TaxAccountantController
from app.main.errors import errors

# Flask API Configuration
api = Api(
    catch_all_404s=True,
    errors=errors,
    prefix='/api'
)

api.add_resource(TaxPayerController, '/taxPayer')
api.add_resource(TaxAccountantController, '/taxAccountant')
api.add_resource(CountryController, '/country')
api.add_resource(StateController, '/state')
