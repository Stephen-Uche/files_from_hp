from .i_usecase_factory import IUsecaseFactory
from ..adapters.models.company_model import Addresses as AddressesModel, \
    Offerings as OfferingModel, \
    Company as CompanyModel, \
    CoreValues as CoreValuesModel

class Company:  
    def __init__(self, usecase_factory: IUsecaseFactory):
        self.usecase_factory = usecase_factory
        print("Company created!")
        self.offering_model_class = OfferingModel
        self.profile_model_class = CompanyModel
        self.address_model_class = AddressesModel
        self.core_values_model_class = CoreValuesModel
        self.request = self.usecase_factory.create_request()
        self.company_profile = self.usecase_factory.create_profile()

        self.get_resources()
        self.subscribe_to_requests()

    def subscribe_to_requests(self):
        self.request.get_offerings_subscription(self.get_offerings_callback)
        self.request.get_profile_subscription(self.get_profile_callback)
        self.request.get_address_subscription(self.get_address_callback)
        self.request.get_core_values_subscription(self.get_core_values_callback)
        self.request.set_profile_subscription(self.set_profile_callback)
        self.request.set_offerings_subscription(self.set_offerings_callback)
        self.request.set_address_subscription(self.set_address_callback)
        self.request.set_core_values_subscription(self.set_core_values_callback)

    
    def get_resources(self):
        self.offerings = self.company_profile.get_articles(self.offering_model_class)
        self.profile = self.company_profile.get_profile(self.profile_model_class)
        self.address = self.company_profile.get_address(self.address_model_class)
        self.core_values = self.company_profile.get_core_values(self.core_values_model_class)


    def get_offerings_callback(self):
        return self.offerings
    

    def get_profile_callback(self):
        return self.profile
    

    def get_address_callback(self):
        return self.address
    

    def get_core_values_callback(self):
        return self.core_values


    def set_profile_callback(self, profile: dict):
        phone = profile.get('phone')
        if phone:
            phone.validate_telephone()
        return self.company_profile.set_profile(profile, self.profile_model_class)
    

    def set_offerings_callback(self, offerings: list):
        return self.company_profile.set_offerings(offerings, self.offering_model_class)


    def set_address_callback(self, address: dict):
        _address = address.get('address')
        if _address:
            _address.validate_address()
        return self.company_profile.set_address(address, self.address_model_class)


    def set_core_values_callback(self, core_values: list):
        return self.company_profile.set_core_values(core_values, self.core_values_model_class)
