class User(Base):
    __tablename__ = 'app_users'

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