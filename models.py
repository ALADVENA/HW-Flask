import os
inport datetime
from sqlalchemy import create_engine, Integer, String, Datetime
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

        server_default=func.now()
    )

def json(self):
    return {
        'id': self.id,
        'title': self.title,
        'description': self.description,
        'owner': self.owner,
        'registration_time': self.registration_time.isoformat()

    }

Base.metadata.create_all(bind=engine)