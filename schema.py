import typing
import strawberry

@strawberry.type 
class Book:
    title: str
    author: str
    
# define function to get books
def get_books(): 
    return [
        Book(
            title='The Great Gatsby 1',
            author='F. Scott Fitzgerald 1'
        ),
        Book(
            title='The Great Gatsby 2',
            author='F. Scott Fitzgerald 2'
        ),
        Book(
            title='The Great Gatsby 3',
            author='F. Scott Fitzgerald 3'
        )
    ]


    
@strawberry.type
class Query: 
    book: typing.List[Book] = strawberry.field(resolver = get_books)
    
    
    
# create the schema
schema = strawberry.Schema(query=Query)    