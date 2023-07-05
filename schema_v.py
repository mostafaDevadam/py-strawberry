from __future__ import annotations


import typing
import strawberry
#import book
#import author


#

# type Book
@strawberry.type 
class Book: 
    title: str 
    author: Author 
    
# type Author
@strawberry.type 
class Author:
    name: str 
    books: typing.List[Book]
    

dic = []

# get all books
def get_books() -> Book:
    bk = [Book]
    print("get: ", dic)
    return dic
            
            
# get all authors 
def get_authors() -> Auhtor:
   
    return dic    
    
    
    
# input    
@strawberry.input 
class AddBookInput: 
    title: str 
    author: str
    name: str        
#
# Query    
@strawberry.type 
class Query: 
    books: typing.List[Book] = strawberry.field(resolver = get_books)
    authors: typing.List[Author] = strawberry.field(resolver = get_authors )
    
    
    
# Mutation
@strawberry.type 
class Mutation: 
    @strawberry.field 
    def add_book(self, book: AddBookInput) -> Book: 
        print("add: ", book)
        dic.append(book)
        print("dic: ", dic)
        return book
                


schema = strawberry.Schema(query=Query, mutation=Mutation)