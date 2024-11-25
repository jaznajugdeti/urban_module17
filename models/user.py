## После описания моделей попробуйте распечатать SQL запрос в консоль при помощи CrateTable (аналогично видео).
class User(Base):

    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)

    tasks = relationship('Task17', back_populates='user17')


from sqlalchemy.schema import CreateTable
print(CreateTable(User.__table__))












