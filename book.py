import typing
import strawberry
import author

#
@strawberry.type 
class Book: 
   title: str 
   author: author
    
    
    