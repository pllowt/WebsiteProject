from root import db, login_manager
from werkzeug.security import generate_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

 # Main account add to db
    user = User(email='emailnotrqd',username='user1',password='45d4rfsuperpass')
    db.session.add(user)
    db.session.commit()
    
class User(db.Model,UserMixin):
    '''
       Main class for user object in db
    '''
    __tablename__ = 'users'
    # A primary key ID column to give each user a unique indentifier
    id = db.Column(db.Integer, primary_key = True)
    # A column to store unique user email address, max 64 char. Not used for login
    email = db.Column(db.String(64),unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    # A column to store unique user 'salted' password hash, size = 128 char
    password_hash = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.email = email
        # Hash password using PBKDF2 and sha256 method and salt length of 16 char
        self.password_hash = generate_password_hash(password, method='pbkdf2:sha256', salt_length=16)

    def check_password(self, password):
        """Checks inputted password against password hash

        Args:
            password (string): user inputted password string

        Returns:
            bool: Checks against password hash
        """        
        return check_password_hash(self.password_hash, password)