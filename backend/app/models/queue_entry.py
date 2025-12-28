from sqlalchemy import Column, Integer, String, DateTime, Enum as SQLAlchemyEnum
from sqlalchemy.sql import func
from app.database import Base
from app.constants.enums import QueueStatus

class QueueEntry(Base):
    __tablename__ = "queue_entries"

    id = Column(Integer, primary_key=True, autoincrement=True)
    token = Column(String(10), unique=True, nullable=False)
    customer_name = Column(String(100), nullable=False)
    phone_number = Column(String(10), unique=True, nullable=False)
    party_size = Column(Integer, nullable=False)
    status = Column(SQLAlchemyEnum(QueueStatus), default=QueueStatus.WAITING, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<QueueEntry {self.id} (token: {self.token}, name: {self.customer_name} \
            phone: {self.phone_number}, party_size: {self.party_size}, status: {self.status} \
            created_at: {self.created_at})>"
    