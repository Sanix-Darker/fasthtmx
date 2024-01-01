from typing import List

from sqlalchemy.orm import Session

from app.services import db_service
from app.schema.schema import Book

from app.viewmodels.shared.viewmodelbase import ViewModelBase


class HomeViewModel(ViewModelBase):
    def __init__(self, db: Session):
        super().__init__()
        self.books: List[Book] = db_service.list_books(db=db)
