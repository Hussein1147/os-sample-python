from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://hussein1147:Jumper1147@@http://mysql-bubblehop.7e14.starter-us-west-2.openshiftapps.com:3306'
app.config['SECURITY_PASSWORD_HASH'] = 'pbkdf2_sha512'
app.config['SECURITY_PASSWORD_SALT'] = 'requiem_for_a_dream'
app.config['SECURITY_TRACKABLE'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['WTF_CSRF_ENABLED'] = False
app.config['SECRET_KEY'] = 'super secret key'
db = SQLAlchemy(app)
 
roles_users = db.Table('roles_users',db.Column('user_id', db.Integer(), db.ForeignKey('auth_user.id')),db.Column('role_id', db.Integer(), db.ForeignKey('auth_role.id')))

class Base(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer(), primary_key=True)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow())
    modified_at = db.Column(db.DateTime(), default = datetime.utcnow())

class Role(Base, RoleMixin):
    __tablename__ ='auth_role'
    name = db.Column(db.String(80), nullable = False, unique =True)
    description = db.Column(db.String(255))
    
    def __init__ (self, name):
        self.name = name
        
    def __repr__ (self):
        return '<Role %r>' % self.name
 
class User(Base, UserMixin):
    __tablename__ = 'auth_user'
       
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(45))
    current_login_ip = db.Column(db.String(45))
    login_count = db.Column(db.Integer)
    stpak = db.Column(db.String(255))
    custid = db.Column(db.String(255))
    authTok = db.Column(db.String(255))
    transfer= db.relationship('Transfers',backref='auth_user')
    roles = db.relationship('Role', secondary= roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    def __repr__(self):
        return '<User % >' % self.email

 
@app.before_first_request
def create_user():
    db.create_all()
   