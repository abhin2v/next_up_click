from sqlalchemy import Column, Integer, ForeignKey, DateTime, Enum as SQLAlchemyEnum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base
from app.constants.enums import AssignmentStatus

class Assignment(Base):
    __tablename__ = "assignments"
    
    id = Column(Integer, primary_key=True, autoincrement=True) 
    queue_entry_id = Column(Integer, ForeignKey("queue_entries.id"), nullable=False)
    table_id = Column(Integer, ForeignKey("tables.id"), nullable=False, index=True)  
    status = Column(
        SQLAlchemyEnum(AssignmentStatus),
        default=AssignmentStatus.ASSIGNED,
        nullable=False
    )
    assigned_at = Column(DateTime(timezone=True), server_default=func.now())
    seated_at = Column(DateTime(timezone=True), nullable=True)
    completed_at = Column(DateTime(timezone=True), nullable=True, index=True)     
    
    queue_entry = relationship("QueueEntry", backref="assignments")
    table = relationship("Table", backref="assignments")
    
    def __repr__(self):
        return f"<Assignment queue:{self.queue_entry_id} → table:{self.table_id} ({self.status.value})>"