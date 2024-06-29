"""DBStorage"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_base import Base


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Create the database engine and session"""
        user = os.getenv("HBNB_MYSQL_USER")
        pwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST", "localhost")
        db = os.getenv("HBNB_MYSQL_DB")

        # Create SQLAlchemy engine
        self.__engine = create_engine(f"mysql+mysqldb://{user}:{pwd}@{host}/{db}",
                                      pool_pre_ping=True)

        # Drop all tables if HBNB_ENV is set to "test"
        if os.getenv("hbnb_env") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects from the database"""
        # Create a session
        session = self.__session_factory()

        # Query all objects on the provided class
        if cls is not None:
            query = session.query(cls)
        else:
            query = session.query(Base)

        objects = query.all()

        # Create a dictionary to store objects
        obj_dict = {}
        for obj in objects:
            key = f"{obj.__class__.__name__}.{obj.id}"
            obj_dict[key] = obj

        # Close the session
        session.close()
        return obj_dict

    def new(self, obj):
        pass

    def save(self):
        pass

    def delete(self, obj=None):
        pass

    def reload(self):
        pass
