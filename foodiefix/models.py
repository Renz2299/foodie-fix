from foodiefix import db


class User(db.Model):
    # schema for the User model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    favourite_cuisine = db.Column(db.String(255), nullable=False)
    profile_photo = db.Column(db.String(255), unique=True)
    recipes = db.relationship("Recipe", backref="user", cascade="all, delete", lazy=True)  # noqa

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
    created_at = db.Column(db.Date)
    created_by = db.Column(db.String(20), db.ForeignKey("user.username", ondelete="CASCADE"))  # noqa

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Recipe: {1} | Description: {2}".format(
            self.id, self.recipe_title, self.recipe_description
        )
