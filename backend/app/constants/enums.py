from enum import Enum

class TableStatus(str, Enum):
    """Table Status Enumeration"""
    AVAILABLE   = "available"
    OCCUPIED    = "occupied"
    RESERVED    = "reserved"
    CLEANING    = "cleaning"

class QueueStatus(str, Enum):
    """Queue entry status enumeration"""
    WAITING     = "waiting"
    ASSIGNED    = "assigned"
    SEATED      = "seated"
    COMPLETED   = "completed"
    CANCELLED   = "cancelled"
    NO_SHOW     = "no_show"

class AssignmentStatus(str, Enum):
    ASSIGNED    = "assigned"
    SEATED      = "seated"
    COMPLETED   = "completed"
    CANCELLED   = "cancelled"