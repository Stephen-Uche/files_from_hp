import dataclasses

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# from usecases.i_company_profile import ICompanyProfile
from ..usecases import ICompanyProfile


@dataclasses.dataclass
class DataAdapter(ICompanyProfile):
    def __init__(self, data_source):
        self.data_source = data_source

    
    def get_profile(self, model_class) -> dict:
        return self.data_source.read(model_class, read_first=True)
    

    def get_offerings(self, model_class) -> list:
        return self.data_source.read(model_class)
    

    def get_address(self, model_class) -> list:
        return self.data_source.read(model_class, read_first=True)
    

    def get_core_values(self, model_class) -> list:
        return self.data_source.read(model_class)
    

    def set_profile(self, profile: dict, model_class):
        phone_column_to_update = profile.get("phone")
        if phone_column_to_update:
            profile["phone"] = phone_column_to_update.phone_number
        return self.data_source.update(model_class, profile)
    

    def set_offerings(self, offerings: list, model_class):
        for offering in offerings:
            self.data_source.update(model_class, offering)
        return offerings

    
    def set_address(self, address: dict, model_class):
        address_column_to_update = address.get("address")
        if address_column_to_update:
            address["address"] = address_column_to_update.address
        return self.data_source.update(model_class, address)


    def set_core_values(self, core_values: list, model_class):
        for core_value in core_values:
            self.data_source.update(model_class, core_value)
        return core_values
    
    def get_articles(self, *args, **kwargs):
        # this method is implemented because of the below Traceback
        """
        Traceback (most recent call last):
          File "main.py", line 7, in <module>
            app = create_flask_app(DevelopmentConfig)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          File "app/__init__.py", line 112, in create_flask_app
            Company(usecase_factory)
          File "app/usecases/company.py", line 18, in __init__
            self.get_resources()
          File "app/usecases/company.py", line 33, in get_resources
            self.offerings = self.company_profile.get_articles(self.offering_model_class)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        AttributeError: 'DataAdapter' object has no attribute 'get_articles'
        """
        pass
    