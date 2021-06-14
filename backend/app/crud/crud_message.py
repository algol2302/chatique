from typing import Any, Dict, Union

from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.message import Message
from schemas.message import MessageCreate, MessageUpdate


class CRUDMessage(CRUDBase[Message, MessageCreate, MessageUpdate]):

    def create(self, db: Session, *, obj_in: MessageCreate) -> Message:
        db_obj = Message(
            text=obj_in.text,
            room_id=obj_in.room_id
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: Message,
        obj_in: Union[MessageUpdate, Dict[str, Any]]
    ) -> Message:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)


message = CRUDMessage(Message)
