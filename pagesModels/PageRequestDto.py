import re

class PageRequestDto:
    
    def __init__(self, page:int, size:int):
        self.__page:int = page
        self.__size:int = size
    
    def getPage(self) -> int:
        return self.__page
    
    def getSize(self) -> int:
        return self.__size
    
    class PageRequestDtoBuilder:

        __NOT_NUMBER_REGEX = r"\D"
        __DEFAULT_PAGE = 1
        __DEFAULT_PAGE_SIZE = 30
            
        def __init__(self):
            self.__page:int = 0
            self.__size:int = 0
        
        def setSize(self, size) -> "PageRequestDto.PageRequestDtoBuilder":
            DEFAULT_PAGE_SIZE = PageRequestDto.PageRequestDtoBuilder.__DEFAULT_PAGE_SIZE
            REGEX = PageRequestDto.PageRequestDtoBuilder.__NOT_NUMBER_REGEX
            aux = size if size is not None else DEFAULT_PAGE_SIZE
            aux = f"0{re.sub(REGEX,"",str(aux))}"
            aux = int(aux)
            self.__size = aux if aux > 0 else DEFAULT_PAGE_SIZE
            return self
        
        def setPage(self, page) -> "PageRequestDto.PageRequestDtoBuilder":
            DEFAULT_PAGE = PageRequestDto.PageRequestDtoBuilder.__DEFAULT_PAGE
            REGEX = PageRequestDto.PageRequestDtoBuilder.__NOT_NUMBER_REGEX
            aux = page if page is not None else DEFAULT_PAGE
            aux = f"0{re.sub(REGEX,"",str(aux))}"
            aux = int(aux)
            self.__page = aux if aux >= DEFAULT_PAGE else DEFAULT_PAGE
            return self

        def build(self) -> "PageRequestDto":
            return PageRequestDto(self.__page,self.__size)
        