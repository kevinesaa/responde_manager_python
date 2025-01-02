from .PageResponseModel import PageResponseModel

class pageResponseWrapperDto:
    """
    Data object model.
    Contains list items objects and Page info.
    { "items": [], "page": {"totalItems": 30} }
    """

    def __init__(self,items:list[object], page:PageResponseModel):
        
        self.__items = [] if items is None else items
        self.__page = page 
        
        if(page is not None and page.getCurrentPage() > 0 ):
            listSize = len(items)
            if(page.getSkip() < listSize):
                auxSize = page.getSkip() + page.getSize()
                if(auxSize <= listSize):
                    listSize = page.getSize()
                startIndex = page.getSkip()
                endIndex = listSize
                self.__items = items[startIndex:endIndex]
    
    def getItems(self) -> list[object]:
        return self.__items
    
    def getPage(self) -> PageResponseModel:
        return self.__page
    
    def toDict(self) -> dict[str,object]:
        
        myDict = {
            'items':self.__items
        }
        
        if(self.__page is not None):
            myDict['page'] = self.__page.toDict()
        
        return myDict
