from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import String, Integer

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "tgusers"

    tgid: Mapped[str] = mapped_column(String, primary_key=True)
    register_date: Mapped[int] = mapped_column(Integer)
    # The original DB has a typo "cock_lenght", we map it to a properly named attribute
    cock_length: Mapped[int] = mapped_column("cock_lenght", Integer, default=0)
    last_cock: Mapped[int] = mapped_column(Integer, default=0)
    old_cock: Mapped[int] = mapped_column(Integer, default=0)
    first_name: Mapped[str | None] = mapped_column(String, nullable=True)
    last_name: Mapped[str | None] = mapped_column(String, nullable=True)
    username: Mapped[str | None] = mapped_column(String, nullable=True)
    
    @property
    def full_name(self) -> str:
        if self.last_name and self.last_name != "None":
            return f"{self.first_name} {self.last_name}"
        return self.first_name if self.first_name and self.first_name != "None" else "Unknown"

class CacheRecord(Base):
    __tablename__ = "cache_records"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    tgid: Mapped[str | None] = mapped_column(String, nullable=True)
    chat_id: Mapped[str] = mapped_column(String)
    message_id: Mapped[int] = mapped_column(Integer)
    date: Mapped[int] = mapped_column(Integer)
    text: Mapped[str | None] = mapped_column(String, nullable=True)
