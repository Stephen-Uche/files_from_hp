import logging
import os
import pathlib
from datetime import datetime

from apifairy import body, response, other_responses
from flask import Flask, Blueprint, redirect, url_for, jsonify
from flask_migrate import Migrate

from .adapters import UsecaseFactory, AdapterFactory, SqlAlchemyAdapter
from .db import sqlalchemy, ma
from .entities import Telephone, Address, ITelephone, IAddress
from .usecases import Company

migrate = Migrate(compare_type=True)


def setup_log():
    dt = datetime.now() 
    date_format = dt.strftime("%Y-%m-%d")

    logs_path = pathlib.Path(__file__).parent.resolve() / "logs"
    if not logs_path.is_dir():
        os.makedirs(logs_path)
            
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(pathname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename=f"logs/company-{date_format}.log",
    )


# sqlalchemy = SQLAlchemy()
sqlalchemy_adapter = SqlAlchemyAdapter(sqlalchemy)
# migrate = MigrateCompany(compare_type=True)

route_blueprints = Blueprint('route_blueprints', __name__)
def create_blueprint(app):
	app.register_blueprint(route_blueprints, url_prefix="/company/v1")
	return app


def register_routes(rest_adapter):
    from .adapters.models.schemas import CompanySchema, UpdateCompanySchema, \
        UpdateOfferingsSchema, UpdateCorevaluesSchema, AddressSchema, \
        UpdateAddressSchema

    @route_blueprints.route('/')
    def health_check():
        return jsonify({"message": "Company API Module"})

    @route_blueprints.route('/offerings', methods=['GET'])
    def get_offerings_subscription():
        return rest_adapter.rest({"request": "get_offerings"})
    

    @route_blueprints.route('/profile', methods=['GET'])
    @response(CompanySchema)
    def get_profile_subscription():
        return rest_adapter.rest({"request": "get_profile"})
    

    @route_blueprints.route('/core-values', methods=['GET'])
    def get_core_values_subscription():
        return rest_adapter.rest({"request": "get_core_values"})
    

    @route_blueprints.route('/address', methods=['GET'])
    @response(AddressSchema)
    def get_address_subscription():
        return rest_adapter.rest({"request": "get_address"})


    @route_blueprints.route('/offerings', methods=['PATCH'])
    @body(UpdateOfferingsSchema)
    @other_responses({400: 'Bad Request'})
    @other_responses({401: 'Unauthorized'})
    def set_offerings_subscription(offerings):
        return rest_adapter.rest(args={"request": "set_offerings"}, data=offerings)


    @route_blueprints.route('/profile', methods=['PATCH'])
    @body(UpdateCompanySchema)
    def set_profile_subscription(profile):
        return rest_adapter.rest(args={"request": "set_profile"}, data=profile)
    
    
    @route_blueprints.route('/address', methods=['PATCH'])
    @body(UpdateAddressSchema)
    @other_responses({400: 'Bad Request'})
    def set_address_subscription(address):
        return rest_adapter.rest(args={"request": "set_address"}, data=address)

    
    @route_blueprints.route('/core-values', methods=['PATCH'])
    @body(UpdateCorevaluesSchema)
    @other_responses({400: 'Bad Request'})
    def set_core_values_subscription(core_values):
        return rest_adapter.rest(args={"request": "set_core_values"}, data=core_values)


def create_flask_app(config_class)-> Flask:
    app = Flask(__name__)

    app.config.from_object(config_class)
    # CORS(app, support_credentials=True)

    with app.app_context():
        sqlalchemy.init_app(app)
        ma.init_app(app)
        # migrate.init_app(app, sqlalchemy)

        usecase_factory = UsecaseFactory(sqlalchemy_adapter)
        Company(usecase_factory)
        
        rest_adapter = usecase_factory.create_request()
        register_routes(rest_adapter)
        create_blueprint(app)

        return app
    
from .adapters.models.company_model import Company as CompanyModel, Offerings, CoreValues, Addresses