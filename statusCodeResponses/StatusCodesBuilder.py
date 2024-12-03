from .StatusCodeModel import StatusCodeModel

class StatusCodesBuilder:

    __currentIndex:int = 999
    __appStatusNames:set = None
    __instance : "StatusCodesBuilder" = None
    
    def __init__(self) -> None:
        pass
    
    @classmethod
    def getInstance(cls) -> "StatusCodesBuilder":
        if (cls.__instance is None):
            cls.__instance = StatusCodesBuilder()
            cls.__instance.__appStatusNames = set()

        return StatusCodesBuilder.__instance
    
    @classmethod
    def generateStatusModel(cls,httpCode:int,statusCodeName:str, message:str) -> StatusCodeModel:
        
        if(statusCodeName in cls.__instance.__appStatusNames):
            t = f"The status code name {statusCodeName} already exist"
            raise RuntimeError(t)
        
        index = cls.__instance.__currentIndex + 1
        cls.__instance.__currentIndex = index
        cls.__instance.__appStatusNames.add(statusCodeName)

        model = (
            StatusCodeModel.Builder()
                .setHttpCode(httpCode)
                .setStatusCodeNumber(index)
                .setStatusCodeName(statusCodeName)
                .setStatusMessage(message)
                .build()
        )
        
        return model

