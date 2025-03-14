from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base

# 사용자 테이블
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    google_id = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=True)
    username = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    translations = relationship("Translation", back_populates="user")

# 번역 기록 테이블
class Translation(Base):
    __tablename__ = "translations"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    original_text = Column(Text, nullable=False)
    translated_text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="translations")

# 자주 번역된 단어 테이블
class PopularWord(Base):
    __tablename__ = "popular_words"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    word = Column(String(255), unique=True, nullable=False)
    category = Column(Enum("신조어", "전문용어"), nullable=False)
    count = Column(Integer, default=1)
    last_updated = Column(DateTime, default=datetime.utcnow)
