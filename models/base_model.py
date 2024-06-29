#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    # class attributes
    id = Column(String(60), primary_key=True, nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        else:
            self.id = kwargs.get('id', str(uuid.uuid4()))
            kwargs['updated_at'] = datetime.strptime(
                kwargs.get('updated_at', datetime.now().isoformat()),
                '%Y-%m-%dT%H:%M:%S.%f'
            )
            kwargs['created_at'] = datetime.strptime(
                kwargs.get('created_at', datetime.now().isoformat()),
                '%Y-%m-%dT%H:%M:%S.%f'
            )

            for key, value in kwargs.items():
                if key not in ('create_at', 'updated_at'):
                    self.__dict__[key] = value
                if key != "__class__":
                    setattr(self, key, value)
            kwargs.pop('__class__', None)
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = type(self).__name__
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary['__class__'] = type(self).__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """Delete current instance from the storage"""
        models.storage.delete(self)
