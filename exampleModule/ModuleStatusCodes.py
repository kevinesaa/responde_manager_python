from statusCodeResponses import StatusCodesBuilder
from statusCodeResponses import CommonStatusCodes
from statusCodeResponses import StatusCodeModel

class ModuleStatusCodes(CommonStatusCodes):
    
    __module_sync : bool = False
    
    def __init__(self, statusCodesBuilder: StatusCodesBuilder):
        super().__init__(statusCodesBuilder)

    def isModuleSync(self) -> bool:
        return ModuleStatusCodes.__module_sync
    
    def markModuleAsSync(self):
        ModuleStatusCodes.__module_sync = True

    def startModule(self,statusCodesBuilder:StatusCodesBuilder):
        
        ModuleStatusCodes.MODULE_STATUS = statusCodesBuilder.generateStatusModel(400,"MODULE_STATUS","test")

    MODULE_STATUS: StatusCodeModel