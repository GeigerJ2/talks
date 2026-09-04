from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# 1️⃣ Create the base class
Base = declarative_base()

# 2️⃣ Define your ORM model
class User(Base):
    __tablename__ = "users"  # Table name in the database

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)

# 3️⃣ Create an engine (SQLite in this case)
engine = create_engine("sqlite:///example.db")

# 4️⃣ Create the tables in the database
Base.metadata.create_all(engine)

# 5️⃣ Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# 🚀 Example usage: Add a new user
new_user = User(name="Alice", age=30)
session.add(new_user)
session.commit()

# 🔍 Query the user
user = session.query(User).filter_by(name="Alice").first()
print(user)  # User(id=1, name='Alice', age=30)


# TODO: Show `DbNode` from AiiDA