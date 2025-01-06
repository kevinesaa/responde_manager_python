from abc import ABC, abstractmethod
from .StatusCodesBuilder import StatusCodesBuilder
from .StatusCodeModel import StatusCodeModel

class CommonStatusCodes(ABC):
    """
    It include the commons status to add over all the modules.
    This class will grow up adding more status over the time.
    To add specific module status, write a new class that inherit from this.
    """
    
    __common_sync = False
    
    def __init__(self, statusCodesBuilder:StatusCodesBuilder):
        CommonStatusCodes.__start(statusCodesBuilder)
        if (not self.isModuleSync()):
            self.startModule(statusCodesBuilder)
            self.markModuleAsSync()
    
    @abstractmethod
    def startModule(self,statusCodesBuilder:StatusCodesBuilder):
        pass

    @abstractmethod
    def isModuleSync(self) -> bool:
        pass

    @abstractmethod
    def markModuleAsSync(self):
        pass

    def __start(statusCodesBuilder:StatusCodesBuilder):
        if(not CommonStatusCodes.__common_sync):
            CommonStatusCodes.OK = statusCodesBuilder.generateStatusModel(200,"OK","ok")
            CommonStatusCodes.BODY_NOT_FOUND = statusCodesBuilder.generateStatusModel(400,"BODY_NOT_FOUND","the request body is required")
            CommonStatusCodes.FAIL_PARSING_JSON_BODY = statusCodesBuilder.generateStatusModel(400,"FAIL_PARSING_JSON_BODY","not valid format body")
            CommonStatusCodes.INTERNAL_SERVER_ERROR = statusCodesBuilder.generateStatusModel(500,"INTERNAL_SERVER_ERROR","ups! this should be not happening")
            CommonStatusCodes.UNKNOWN_ERROR = statusCodesBuilder.generateStatusModel(500,"UNKNOWN_ERROR","ups!")
            
            CommonStatusCodes.__common_sync = True
    
    # can be use in all my life
    OK:StatusCodeModel
    BODY_NOT_FOUND:StatusCodeModel
    FAIL_PARSING_JSON_BODY:StatusCodeModel
    INTERNAL_SERVER_ERROR:StatusCodeModel
    UNKNOWN_ERROR:StatusCodeModel
