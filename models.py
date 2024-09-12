from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from datetime import datetime

class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id = Column(Integer, primary_key=True, index=True)
    sender = Column(String(100))
    message = Column(String(500))
    receiver = Column(String(100), nullable=True)
    timestamp = Column(DateTime, default=datetime.now)
