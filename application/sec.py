from flask_security import SQLAlchemyUserDatastore, Security, hash_password
from database.tables import User, Role
from database.common import db

datastore = SQLAlchemyUserDatastore(db, User, Role)