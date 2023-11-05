from flask import flash, render_template, request, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from foodiefix import app, db
from foodiefix.models import User, Recipe


@app.route("/")
def home():
    recipes = list(Recipe.query.order_by(Recipe.recipe_title).all())
    return render_template("recipes.html", recipes=recipes)


@app.route("/my_recipes")
def my_recipes():
    recipes = list(Recipe.query.order_by(Recipe.recipe_title).all())
    return render_template("my_recipes.html", recipes=recipes)


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():

    if "user" not in session:
        flash("You must be logged in to add recipes")
        return redirect(url_for("home"))
    
    if request.method == "POST":
        recipe = Recipe(
            recipe_title=request.form.get("recipe_title"),
            recipe_description=request.form.get("recipe_description"),
            recipe_ingredients=request.form.get("recipe_ingredients"),
            recipe_method=request.form.get("recipe_method"),
            recipe_photo=request.form.get("recipe_photo")
        )
        db.session.add(recipe)
        db.session.commit()
        return redirect(url_for("my_recipes"))
    return render_template("add_recipe.html")


@app.route("/view_recipe/<int:recipe_id>")
def view_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    return render_template("recipe.html", recipe=recipe)


@app.route("/edit_recipe/<int:recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    if request.method == "POST":
        recipe.recipe_title = request.form.get("recipe_title")
        recipe.recipe_description = request.form.get("recipe_description")
        recipe.recipe_ingredients = request.form.get("recipe_ingredients")
        recipe.recipe_method = request.form.get("recipe_method")
        recipe.recipe_photo = request.form.get("recipe_photo")
        recipe.created_at = request.form.get("created_at")
        recipe.created_by = request.form.get("created_by")
        db.session.commit()
        return redirect(url_for("view_recipe", recipe_id=recipe.id))
    return render_template("edit_recipe.html", recipe=recipe)


@app.route("/delete_recipe/<int:recipe_id>")
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    db.session.delete(recipe)
    db.session.commit()
    return redirect(url_for("my_recipes"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = User.query.filter(User.username == \
                                           request.form.get("username").lower()).all()
        
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("login"))
        
        user = User(
            username=request.form.get("username").lower(),
            password=generate_password_hash(request.form.get("password"))
        )
        
        db.session.add(user)
        db.session.commit()

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("home", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = User.query.filter(User.username == \
                                           request.form.get("username").lower()).all()

        if existing_user:
            print(request.form.get("username"))
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user[0].password, request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        return redirect(url_for(
                            "home", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Username doesn't exist")
            return redirect(url_for("register"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))