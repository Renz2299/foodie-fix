from foodiefix import db, login_manager
from sqlalchemy.orm import relationship
from sqlalchemy.types import TIMESTAMP
from flask_login import UserMixin, current_user
from datetime import date


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    # schema for the User model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.username


class Recipe(db.Model):
    # schema for the Recipes model
    id = db.Column(db.Integer, primary_key=True)
    recipe_title = db.Column(db.String(50), unique=True, nullable=False)
    recipe_description = db.Column(db.String(255), nullable=False)
    recipe_ingredients = db.Column(db.String(255), nullable=False)
    recipe_method = db.Column(db.Text, nullable=False)
    recipe_photo = db.Column(db.String(255), unique=True)
    created_at = db.Column(db.Date, default = date.strftime(date.today(), "%b %d %Y"))
    created_by = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"))  # noqa
    user_id = db.relationship("User", backref=db.backref("recipe", cascade="all, delete", lazy=True))  # noqa

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.created_by = current_user.id

    def save(self):
        self.created_at = self.created_at.date()
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Recipe: {1} | Description: {2}".format(
            self.id, self.recipe_title, self.recipe_description
        )
