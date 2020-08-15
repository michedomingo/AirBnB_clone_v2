#!/usr/bin/python3
"""DB storage class for AirBnb """


from models.base_model import Base, BaseModel
import models
import sys
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """Class that saves data to a MySQL database """

    __engine = None
    __session = None

    def __init__(self):
        """initialize DBStorage class """
        # dialect+driver://username:password@host:port/database
        user = getenv('HBTN_MYSQL_USER')
        pwd = getenv('HBTN_MYSQL_PWD')
        host = getenv('HBTN_MYSQL_HOST')
        db = getenv('HBTN_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, pwd, host, db),
                                      pool_pre_ping=True)
        if getenv(HBTN_ENV) is 'test':
            Base.metadata.drop_call(self.__engine)
        else:
            Session = sessionmaker(bind=self.__engine)
            self.__session = Session()

    def all(self, cls=None):
        """
        returns all or one specific class object
        """
        classes = [User, State, City, Amenity, Place, Review]
        filt = {}
        all_data = {}
        if cls in classes:
            if isinstance(cls, str):
                filter_rcrd = self.__session.query(eval(cls)).all()
            else:
                filter_rcrd = self.__session.query(cls).all()
            for value in filter_rcrd:
                key = str(value.__class__.name) + "." + str(value.id)
                filt[key] = value
            return filt
        else:
            for cls in classes:
                all_data = self.__session.query(cls).all()

                for values in all_data:
                    key = str(values.__class__.__name__) + "." + str(values.id)
                    all_data[key] = values
                return all_data

        def new(self, obj):
            """ adds object to db session """
            self.__session.add(obj)

        def save(self):
            """
            save all changes of the current
            database session (self.__session)
            """
            self.__session.add(obj)

        def delete(self, obj=None):
            """ delete from the current database session obj if not None """
            if obj is not None:
                self.__session.delete(obj)
                self.save()

        def reload(self):
            """reload the database """
            try:
                Base.metadata.create_all(self.__enigine)
                s_factory = sessionmaker(bind=self.__engine,
                                         expire_on_commit=False)
                Session = scoped_session(s_factory)
                self.__session = Session
            except:
                pass

        def close(self):
            """remove the session """
            self.__session.close()
