
class PageResponseModel:
    """
    Data model object Page. 
    Include it as additional metadata to paginable response list items.
    """
    
    __DEFAULT_PAGE_SIZE = 30
    
    def __init__(self, totalItems:int, currentPage:int, pageSize:int):
        
        self.__currentPage:int = 1
        self.__size:int = 0
        self.__maxPages:int = 0
        self.__totalItems:int = 0
        self.__skip:int = 0

        limit : int = pageSize if pageSize > 0 else PageResponseModel.__DEFAULT_PAGE_SIZE
        skips : int = abs(limit * (currentPage - 1))
        myMax : int = int(totalItems/limit)
        if(totalItems > 0 and myMax <=0):
            myMax = 1
        
        self.__maxPages = myMax
        self.__currentPage = currentPage
        self.__totalItems = totalItems
        self.__size = limit
        self.__skip = skips

    
    def getMaxPages(self) -> int:
        return self.__maxPages
        
    def getCurrentPage(self) -> int:
        return self.__currentPage
        
    def getTotalItems(self) -> int:
        return self.__totalItems
        
    def getSize(self) -> int:
        return self.__size
        
    def getSkip(self) -> int:
        return self.__skip
    
    def toDict(self) -> dict[str,int]:
        return {
            'maxPages':self.__maxPages,
            'currentPage':self.__currentPage,
            'totalItems':self.__totalItems,
            'size':self.__size,
            'skip':self.__skip
        }
        
