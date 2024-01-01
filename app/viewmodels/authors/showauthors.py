from typing import List

from sqlalchemy.orm import Session

from app.services import db_service
from app.schema.schema import Author

from app.viewmodels.shared.viewmodelbase import ViewModelBase


class ShowAuthorsViewModel(ViewModelBase):
    def __init__(self, db: Session):
        super().__init__()
        self.authors: List[Author] = db_service.get_all_authors(db=db)
