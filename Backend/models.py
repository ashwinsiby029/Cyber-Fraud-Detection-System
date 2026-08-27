from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base
from datetime import datetime
import pytz

ist = pytz.timezone('Asia/Kolkata')

class FraudReport(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    description = Column(Text)
    category = Column(String(50)) 
    risk_score = Column(Integer)
    status = Column(String(20), default="Pending")

    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(ist)
    )