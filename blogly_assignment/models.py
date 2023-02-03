



from flask_sqlalchemy import SQLAlchemy
from datetime import date


db = SQLAlchemy()                                                    

def connect_db(app):
    db.app = app                                                                           
    db.init_app(app)




# MODELS ARE BELOW!


class User(db.Model):

    __tablename__ = 'users'





    def __repr__(self):
        u = self
        return f"<user_id={u.id}, first_name={u.first_name}, last_name={u.last_name}, image_url={u.image_url}>"




    id = db.Column(db.Integer,                            
                    primary_key = True,                           
                    autoincrement = True)                                
                                                                
    first_name = db.Column(db.String(20),                             
                        nullable = False,                            
                        unique = False)                               

    last_name = db.Column(db.String(20),                             
                        nullable = False,                            
                        unique = False)


    image_url = db.Column(db.String, nullable=False)


    posts = db.relationship("Post", backref='user')


    


class Post(db.Model):

    __tablename__ = 'posts'




    def __repr__(self):
        p = self
        return f"<post_id={p.id}, title={p.title}, content={p.content}, created_at={p.created_at}, user_id={p.user_id}>"




    id = db.Column(db.Integer, primary_key = True, autoincrement = True)                                                                                             
    title = db.Column(db.String(20), nullable = False, unique = False)                               
    content = db.Column(db.String(40), nullable = False, unique = False)
    today = date.today()
    
    created_at = db.Column(db.String, nullable=True, default=today)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
