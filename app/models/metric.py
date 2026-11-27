from app.database.base import Base
from datetime import datetime
from sqlalchemy import Float , ForeignKey , DateTime , func
from sqlalchemy.orm import mapped_column , Mapped
class Metric(Base):
    __tablename__ = "metrics"
    id : Mapped[int] = mapped_column(primary_key= True)
    agent_id : Mapped[int] = mapped_column(ForeignKey("agents.id") , nullable= False)
    cpu_usage: Mapped[float] = mapped_column(Float, nullable=False)
    memory_usage: Mapped[float] = mapped_column(Float, nullable=False)
    disk_usage: Mapped[float] = mapped_column(Float, nullable=False)
    recorded_at: Mapped[datetime] = mapped_column(DateTime(timezone=True) , server_default= func.now())