from sqlalchemy import Column, Integer, String, DateTime, Enum as SQLAlchemyEnum
from sqlalchemy.sql import func
from app.database import Base
from app.constants.enums import TableStatus

class Table(Base):
    __tablename__ = "tables"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    table_number = Column(String(10), unique=True, nullable=False)
    capacity = Column(Integer, nullable=False)
    status = Column(
        SQLAlchemyEnum(TableStatus),
        default=TableStatus.AVAILABLE,
        nullable=False
    )
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    def __repr__(self):
        return f"<Table {self.table_number} (capacity: {self.capacity})>"