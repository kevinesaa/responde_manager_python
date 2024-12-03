from exampleModule.ModuleStatusCodes import ModuleStatusCodes
from statusCodeResponses import StatusCodesBuilder
from responseWrapper import ResponseModel

if __name__ == "__main__":
    
    ModuleStatusCodes(StatusCodesBuilder.getInstance())
    
    response = (
        ResponseModel.Builder()
            .setStatusCodeModel(ModuleStatusCodes.MODULE_STATUS)
            .putAddionalHeader("token","12345")
            .setData({"id":"10","name":"murphy"})
            .build()
            .toDict()
    )

    print(response)