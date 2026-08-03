# app/schemas.py
from marshmallow import validate

from app.db import ma
from .company_model import Company, Addresses, CoreValues, Offerings
    

class CompanySchema(ma.SQLAlchemySchema):
    class Meta:
        model = Company
        description = 'This schema represents a company profile'
        
    id = ma.auto_field(dump_only=True)
    name = ma.String(required=True,
                             validate=validate.Length(min=2, max=100))
    about = ma.String(required=False)
    mission_statement = ma.String(required=False)
    vision = ma.String(required=False)
    contact_email = ma.String(required=True, validate=[validate.Length(max=120),
                        validate.Email()],
                        error_messages = {
                                'required': 'Missing data for required field.',
                                'null': 'Field may not be null.',
                            } )
    phone = ma.Integer(required=False)
    created_by = ma.auto_field(dump_only=True)

    # address = fields.Nested("AddressSchema", many=True, exclude=("company_id",))
    # offerings = fields.Nested("OfferingsSchema", many=True, exclude=("company_id",))
    # core_values = fields.Nested("CorevaluesSchema", many=True, exclude=("company_id",))


class UpdateCompanySchema(ma.SQLAlchemySchema):
    class Meta:
        model = Company
        
    id = ma.Integer(required=True)
    name = ma.String(required=False,
                             validate=validate.Length(min=2, max=100))
    about = ma.String(required=False)
    mission_statement = ma.String(required=False)
    vision = ma.String(required=False)
    contact_email = ma.String(required=False, validate=[validate.Length(max=120),
                        validate.Email()],
                        error_messages = {
                            'required': 'Missing data for required field.',
                            'null': 'Field may not be null.',
                        } )
    phone = ma.String(required=False)
    created_by = ma.auto_field(dump_only=True)


class AddressSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Addresses
        description = 'This schema represents a company address'
    
    id = ma.auto_field(dump_only=True)
    company_id = ma.Integer(required=True)
    address = ma.String(required=True)
    country = ma.String(required=False)
    city = ma.String(required=False)
    postal_code = ma.Integer(required=False)


class UpdateAddressSchema(ma.Schema):
    class Meta:
        model = Addresses
    
    id = ma.Integer(required=True)
    company_id = ma.Integer(required=True)
    address = ma.String(required=True)
    country = ma.String(required=False)
    city = ma.String(required=False)
    postal_code = ma.Integer(required=False)



class CorevaluesSchema(ma.SQLAlchemySchema):
    class Meta:
        model = CoreValues
        description = 'This schema represents a company core values'
    
    id = ma.auto_field(dump_only=True)
    company_id = ma.Integer(required=True)
    value = ma.String(required=True)
    description = ma.String(required=True)


class UpdateCorevalueSchema(ma.SQLAlchemySchema):
    class Meta:
        model = CoreValues
    
    id = ma.Integer(required=True)
    company_id = ma.auto_field(dump_only=True)
    value = ma.String(required=False)
    description = ma.String(required=False)


class UpdateCorevaluesSchema(ma.SQLAlchemySchema):
    core_values = ma.List(ma.Nested(UpdateCorevalueSchema))


class OfferingSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Offerings
        description = 'This schema represents a company offerings and services'
    
    id = ma.auto_field(dump_only=True)
    company_id = ma.Integer(required=True)
    offering = ma.String(required=True)
    description = ma.String(required=True)


class OfferingsSchema(ma.SQLAlchemySchema):
    offerings = ma.List(ma.Nested(OfferingSchema))


class UpdateOfferingSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Offerings
    
    id = ma.Integer(required=True)
    company_id = ma.auto_field(dump_only=True)
    offering = ma.String(required=False)
    description = ma.String(required=False)


class UpdateOfferingsSchema(ma.SQLAlchemySchema):
    offerings = ma.List(ma.Nested(UpdateOfferingSchema))