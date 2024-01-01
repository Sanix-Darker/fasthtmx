from typing import List

from pydantic import ConfigDict, BaseModel


class BookBase(BaseModel):
    title: str
    pages: int
    author_id: int


class CreateBook(BookBase):
    pass


class Book(BookBase):
    id: str
    model_config = ConfigDict(from_attributes=True)


class AuthorBase(BaseModel):
    first_name: str
    last_name: str
    email: str


class AuthorCreate(AuthorBase):
    pass


class Author(AuthorBase):
    id: int
    books: List[Book] = []
    model_config = ConfigDict(from_attributes=True)
