from abc import ABC, abstractmethod
from .StatusCodesBuilder import StatusCodesBuilder
from .StatusCodeModel import StatusCodeModel

class CommonStatusCodes(ABC):
    
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
            CommonStatusCodes.OK = statusCodesBuilder.generateStatusModel(200,"OK",None)
            CommonStatusCodes.UNKNOWN_ERROR = statusCodesBuilder.generateStatusModel(500,"UNKNOWN_ERROR","ups!")
            CommonStatusCodes.BAD_FORMAT_EMAIL = statusCodesBuilder.generateStatusModel(400,"BAD_FORMAT_EMAIL","not valid email format")
            CommonStatusCodes.__common_sync = True
    
    OK:StatusCodeModel
    BAD_FORMAT_EMAIL:StatusCodeModel
    UNKNOWN_ERROR:StatusCodeModel