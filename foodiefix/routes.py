from flask import flash, render_template, request, redirect, session, url_for
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from foodiefix import app, db
from foodiefix.models import User, Recipe


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = User.query.filter_by(
            username=request.form.get("username").lower()).first()

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        hashed_password = generate_password_hash(request.form.get("password"), method='sha256')
        user = User(
            username=request.form.get("username").lower(),
            password=hashed_password,
            favourite_cuisine=request.form.get("favourite_cuisine"),
            profile_photo=request.form.get("profile_photo")
        )

        db.session.add(user)
        db.session.commit()

        # log the new user in
        login_user(user)
        flash("Registration Successful!")
        return redirect(url_for("my_recipes"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = User.query.filter_by(
            username=request.form.get("username").lower()).first()

        if existing_user and check_password_hash(existing_user.password, request.form.get("password")):
            login_user(existing_user)
            flash("Login Successful!")
            return redirect(url_for("my_recipes"))
        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out")
    return redirect(url_for("home"))


@app.route("/")
def home():
    recipes = Recipe.query.order_by(Recipe.recipe_title).all()
    return render_template("recipes.html", recipes=recipes)


@app.route("/my_recipes")
@login_required
def my_recipes():
    recipes = Recipe.query.filter_by(created_by=current_user.id).order_by(Recipe.recipe_title).all()
    return render_template("my_recipes.html", recipes=recipes)


@app.route("/account")
@login_required
def account():
    return render_template("account.html")


@app.route("/add_recipe", methods=["GET", "POST"])
@login_required
def add_recipe():
    if request.method == "POST":
        recipe = Recipe(
            recipe_title=request.form.get("recipe_title"),
            recipe_description=request.form.get("recipe_description"),
            recipe_ingredients=request.form.get("recipe_ingredients"),
            recipe_method=request.form.get("recipe_method"),
            recipe_photo=request.form.get("recipe_photo"),
            created_by=current_user.id
        )
        db.session.add(recipe)
        db.session.commit()
        flash("Recipe successfully added!")
        return redirect(url_for("my_recipes"))
    return render_template("add_recipe.html")


@app.route("/view_recipe/<int:recipe_id>")
def view_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    return render_template("recipe.html", recipe=recipe)


@app.route("/edit_recipe/<int:recipe_id>", methods=["GET", "POST"])
@login_required
def edit_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    if recipe.created_by != current_user.id:
        flash("You do not have permission to edit this recipe.")
        return redirect(url_for("my_recipes"))

    if request.method == "POST":
        recipe.recipe_title = request.form.get("recipe_title")
        recipe.recipe_description = request.form.get("recipe_description")
        recipe.recipe_ingredients = request.form.get("recipe_ingredients")
        recipe.recipe_method = request.form.get("recipe_method")
        recipe.recipe_photo = request.form.get("recipe_photo")
        db.session.commit()
        flash("Recipe successfully updated!")
        return redirect(url_for("view_recipe", recipe_id=recipe.id))
    return render_template("edit_recipe.html", recipe=recipe)


@app.route("/delete_recipe/<int:recipe_id>")
@login_required
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    if recipe.created_by != current_user.id:
        flash("You do not have permission to delete this recipe.")
        return redirect(url_for("my_recipes"))

    db.session.delete(recipe)
    db.session.commit()
    flash("Recipe successfully deleted!")
    return redirect(url_for("my_recipes"))
