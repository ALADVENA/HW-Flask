import os
import datetime
from sqlalchemy import create_engine, Integer, String, Datetime, func
from sqlalchemy.org import sessionmaker, DeclarativeBase, mapped_column, Mapped


POSTGRES_USER=os.getenv('POSTGRES_USER', 'postgres')
POSTGRES_PASSWORD=os.getenv('POSTGRES_PASSWORD', 'postgres')
POSTGRES_DB=os.getenv('POSTGRES_DB', 'flask')
POSTGRES_HOST=os.getenv('POSTGRES_HOST', '127.0.0.1')
POSTGRES_PORT=os.getenv('POSTGRES_PORT', '5431')

engine = create_engine(f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}'@
                       f'{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}')

Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'app_advertisements'

    id: Mapped[int] = mapped_column(Intager, primer_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    owner: Mapped[str] = mapped_column(String, nullable=False)
    registration_time: Mapped[datetime.datetime] = mapped_column(
        DateTime,

        # default=datetime.datetime.now покажет время сервера, но 
        # оно может по факту отличаться от врмени bd)

        server_default=func.now()
        # указывает время самой db
    )

def json(self):
    return {
        'id': self.id,
        'title': self.title,
        'description': self.description,
        'owner': self.owner,
        'registration_time': self.registration_time.isoformat()
        # json не поддерживает формат дата -> преобразуем в формат стандартов iso

    }

Base.metadata.create_all(bind=engine)