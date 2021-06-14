from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.room import Room
from schemas.room import RoomCreate, RoomUpdate


class CRUDRoom(CRUDBase[Room, RoomCreate, RoomUpdate]):

    def create(self, db: Session, *, obj_in: RoomCreate) -> Room:
        db_obj = Room(
            name=obj_in.name,
            company_id=obj_in.company_id
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: Room,
        obj_in: Union[RoomUpdate, Dict[str, Any]]
    ) -> Room:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)


room = CRUDRoom(Room)
