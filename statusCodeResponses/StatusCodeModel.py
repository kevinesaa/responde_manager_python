
class StatusCodeModel:
    
    def __init__(self):
        self.__http_code:int = None
        self.__app_status_code:int = None
        self.__app_status_name:str = None
        self.__app_status_message:str = None
    
    def getHttpCode(self) -> int:
        return self.__http_code 
        
    def getStatusCodeNumber(self) -> int:
        return self.__app_status_code 
    
    def getStatusCodeName(self) -> str:
        return self.__app_status_name
    
    def getStatusMessage(self) -> str:
        return self.__app_status_message

    def _setHttpCode(self,httpCode:int) -> None:
        self.__http_code = httpCode
        
    def _setStatusCodeNumber(self, statusCodeNumber:int) -> None:
        self.__app_status_code = statusCodeNumber
    
    def _setStatusCodeName(self, statusCodeName:str) -> None:
        self.__app_status_name = statusCodeName
    
    def _setStatusMessage(self,message:str) -> None:
        self.__app_status_message = message
        
    
    class Builder:
        
        def __init__(self):
            self.__http_code:int = None
            self.__app_status_code:int = None
            self.__app_status_name:str = None
            self.__app_status_message:str = None

        def setHttpCode(self,httpCode:int) -> "StatusCodeModel.Builder":
            self.__http_code = httpCode
            return self
        
        def setStatusCodeNumber(self, statusCodeNumber:int) -> "StatusCodeModel.Builder":
            self.__app_status_code = statusCodeNumber
            return self
        
        def setStatusCodeName(self, statusCodeName:str) -> "StatusCodeModel.Builder":
            self.__app_status_name = statusCodeName
            return self
        
        def setStatusMessage(self,message:str) -> "StatusCodeModel.Builder":
            self.__app_status_message = message
            return self
        
        def build(self) -> "StatusCodeModel":
            model = StatusCodeModel()
            model._setHttpCode(self.__http_code)
            model._setStatusCodeNumber(self.__app_status_code)
            model._setStatusCodeName(self.__app_status_name)
            model._setStatusMessage(self.__app_status_message)
            
            return model