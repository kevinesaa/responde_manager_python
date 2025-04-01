
import json
from statusCodeResponses import StatusCodeModel

class ResponseModel:

    def __init__(self):
        self.__http_code :int = None
        self.__headers:dict = None
        self.__body:object = None
    
    def getHttpCode(self) -> int:
        return self.__http_code
    
    def getHeaders(self) -> dict:
        return self.__headers
    
    def getBody(self) -> object:
        return self.__body 
    
    def _setHttpCode(self, httpCode:int) -> None:
        self.__http_code = httpCode
    
    def _setHeaders(self, headers:dict) -> None:
        self.__headers = headers
    
    def _setBody(self, body) -> None:
        self.__body = body
    
    def toDict(self) -> dict[str,object]:
        
        model = {
            'statusCode': self.__http_code,
        }
        
        if(self.__headers is not None):
            model['headers'] = self.__headers
        
        if(self.__body is not None):
            model['body'] = self.__body
        
        return  model

    class Builder:
        
        
        __KEY_STATUS_NAME = "app_status_name"
        __KEY_STATUS_MESSAGE = "app_status_message"
        __KEY_DATA = "data"
        __KEY_ACCESS_CONTROL_ORIGIN = "Access-Control-Allow-Origin"
        __KEY_ACCESS_CONTROL_CREDENTIALS = "Access-Control-Allow-Credentials"
        __KEY_ACCESS_CONTROL_HEADERS = "Access-Control-Allow-Headers"
        __KEY_ACCESS_CONTROL_METHODS = "Access-Control-Allow-Methods"
        

        def __init__(self):
            self.__http_code:int = None
            self.__headers:dict = None
            self.__body:dict = None
            self.__stringifyBody:bool = False
            
         
        def setStatusCodeModel(self, model:StatusCodeModel) -> "ResponseModel.Builder":
            self.setHttpCode(model.getHttpCode())
            self.setAppStatusName(model.getStatusCodeName())
            self.setAppStatusMessage(model.getStatusMessage())
            return self
        
        def setHttpCode(self, httpCode:int) -> "ResponseModel.Builder":
            self.__http_code = httpCode
            return self
        
        def setAppStatusName(self, statusName:str) -> "ResponseModel.Builder":
            KEY_STATUS_NAME = ResponseModel.Builder.__KEY_STATUS_NAME
            self.__body = self.__addElement(self.__body, KEY_STATUS_NAME, statusName)
            self.__headers = self.__addElement(self.__headers, KEY_STATUS_NAME, statusName)
            return self
        
        def setAppStatusMessage(self, statusMessage:str) -> "ResponseModel.Builder":
            KEY_STATUS_MESSAGE = ResponseModel.Builder.__KEY_STATUS_MESSAGE
            self.__body = self.__addElement(self.__body, KEY_STATUS_MESSAGE, statusMessage)
            self.__headers = self.__addElement(self.__headers, KEY_STATUS_MESSAGE, statusMessage)
            return self
        
        def concatToAppStatusMessage(self, text:str) -> "ResponseModel.Builder":
            KEY_STATUS_MESSAGE = ResponseModel.Builder.__KEY_STATUS_MESSAGE
            if (self.__body is None or self.__headers is None): 
                self.setAppStatusMessage("")
            current = self.__body.get(KEY_STATUS_MESSAGE,"")
            self.setAppStatusMessage(f"{current}{text}")
            return self
        
        def setControlOrigin(self, controlOrigin:str="*") -> "ResponseModel.Builder":
            KEY_CONTROL_ORIGIN = ResponseModel.Builder.__KEY_ACCESS_CONTROL_ORIGIN
            self.__headers = self.__addElement(self.__headers, KEY_CONTROL_ORIGIN, controlOrigin)
            return self
        
        def setControlCredentials(self, controlCredential:bool=True) -> "ResponseModel.Builder":
            KEY_CONTROL_CREDENTIALS = ResponseModel.Builder.__KEY_ACCESS_CONTROL_CREDENTIALS
            self.__headers = self.__addElement(self.__headers, KEY_CONTROL_CREDENTIALS, controlCredential)
            return self
        
        def setControlHeaders(self, controlHeaders:str="Content-Type") -> "ResponseModel.Builder":
            KEY_CONTROL_HEADERS = ResponseModel.Builder.__KEY_ACCESS_CONTROL_HEADERS
            self.__headers = self.__addElement(self.__headers, KEY_CONTROL_HEADERS, controlHeaders)
            return self
        
        def setControlMethods(self, controlMethods:list[str]) -> "ResponseModel.Builder":
            KEY_CONTROL_METHODS = ResponseModel.Builder.__KEY_ACCESS_CONTROL_METHODS
            if (controlMethods is not None and isinstance(controlMethods,list) and len(controlMethods) > 0):
                methods = [ item.upper() for item in controlMethods]
                methods = ",".join(methods)
                self.__headers  = self.__addElement(self.__headers, KEY_CONTROL_METHODS, methods)
            
            return self
        
        def putAddionalHeader(self, key:str, value) -> "ResponseModel.Builder":
            self.__headers = self.__addElement(self.__headers,key,value)
            return self
        
        def putAddionalHeadersFromDict(self, extraHeaders:dict) -> "ResponseModel.Builder":
            for key, value in extraHeaders.items():
                self.putAddionalHeader(key,value)
            return self
        
        def setData(self, data:dict[str,object]) -> "ResponseModel.Builder":
            KEY_DATA = ResponseModel.Builder.__KEY_DATA
            self.__body = self.__addElement(self.__body, KEY_DATA, data)
            return self
        
        def setStringifyBody(self, stringifyBody:bool) -> "ResponseModel.Builder":
            self.__stringifyBody = stringifyBody
            return self
        

        def __addElement(self, current:dict, key:str, value) -> dict:
        
            newValue:dict =  None
            if(current is not None):
                newValue =  dict(current)
            
            if(value is not None):
                
                if(current is None):
                    newValue =  dict()
                
                newValue[key] = value
        
            return newValue
        
        def build(self) -> "ResponseModel":
            
            model = ResponseModel()
            
            httpCode = self.__http_code
            body = self.__body
            headers = self.__headers
            
            if(body is not None and self.__stringifyBody):
                body = json.dumps(body)

            model._setHttpCode(httpCode)
            model._setBody(body)
            model._setHeaders(headers)

            return model
        