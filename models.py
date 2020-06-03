from app import db
from datetime import datetime
import re

from flask_security import UserMixin, RoleMixin


def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)


post_tags = db.Table('post_tags',
                     db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
                     db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
                     )


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    country = db.Column(db.Text)
    year = db.Column(db.String(4))
    genre = db.Column(db.String(100))
    picture = db.Column(db.String(200))
    # trailer = db.Column(db.String(200))
    created = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()

    tags = db.relationship('Tag', secondary=post_tags, backref=db.backref('posts', lazy='dynamic'))

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return '<Post id: {}, title: {}>'.format(self.id, self.title)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    location = db.Column(db.String(200))
    time = db.Column(db.String(100))
    slug = db.Column(db.String(100))

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.name:
            self.slug = slugify(self.name)

    def __repr__(self):
        return '{}'.format(self.id, self.name)


# Flask-Security #

roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
                       )


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(255))


# # Cinemas and Sessions
#
# session_cinema = db.Table('session_cinema',
#                           db.Column('cinema_id', db.Integer(), db.ForeignKey('cinema.id')),
#                           db.Column('session_id', db.Integer(), db.ForeignKey('session.id')),
#                           db.Column('time', db.String())
#                           )
#
#
# class Cinema(db.Model):
#     id = db.Column(db.Integer(), primary_key=True)
#     name = db.Column(db.String(300))
#     location = db.Column(db.String(500))
#     days_work = db.Column(db.String(300))
#     sessions = db.relationship('Session', secondary=session_cinema, backref=db.backref('cinemas', lazy='dynamic'))
#
#
# class Session(db.Model):
#     id = db.Column(db.Integer(), primary_key=True)
#     time = db.Column(db.String(100))
