from wtforms import Form, StringField, TextAreaField


class PostForm(Form):
    title = StringField('Title')
    body = TextAreaField('Body')
    country = TextAreaField('Country')
    year = TextAreaField('Year')
    genre = TextAreaField('Genre')
    picture = TextAreaField('Picture')
