from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.company import Company
from schemas.company import CompanyCreate, CompanyUpdate


class CRUDCompany(CRUDBase[Company, CompanyCreate, CompanyUpdate]):

    @staticmethod
    def get_by_name(db: Session, *, name: str) -> Optional[Company]:
        return db.query(Company).filter(Company.name == name).first()

    def create(self, db: Session, *, obj_in: CompanyCreate) -> Company:
        db_obj = Company(
            name=obj_in.name,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: Company,
        obj_in: Union[CompanyUpdate, Dict[str, Any]]
    ) -> Company:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)


company = CRUDCompany(Company)
