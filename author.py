import typing
import strawberry
import book 


@strawberry.type 
class Author:
    name: str
    books: typing.List[book]