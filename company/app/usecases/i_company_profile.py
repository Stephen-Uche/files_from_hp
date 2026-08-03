from abc import ABCMeta, abstractmethod


class ICompanyProfile(metaclass=ABCMeta):
    @abstractmethod
    def get_profile(self, model_class):
        pass
    

    @abstractmethod
    def get_offerings(self, model_class):
        pass
    

    @abstractmethod
    def set_profile(self, profile: dict, model_class):
        raise NotImplementedError()
    

    @abstractmethod
    def set_offerings(self, offerings: list, model_class):
        raise NotImplementedError()