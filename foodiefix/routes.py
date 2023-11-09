from flask import flash, render_template, request, redirect, session, url_for
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from foodiefix import app, db
from foodiefix.models import User, Recipe
import datetime


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = User.query.filter_by(username=request.form.get("username").lower()).first()

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("login"))

        hashed_password = generate_password_hash(request.form.get("password"), method='sha256')
        user = User(
            username=request.form.get("username").lower(),
            password=hashed_password
        )

        db.session.add(user)
        db.session.commit()

        # log the new user in
        login_user(user)
        flash("Registration Successful!")
        return redirect(url_for("my_recipes", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = User.query.filter_by(username=request.form.get("username").lower()).first()

        if existing_user and check_password_hash(existing_user.password, request.form.get("password")):
            login_user(existing_user)
            flash("Login successful!")
            return redirect(url_for("my_recipes", username=session["user"]))
        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
            
    return render_template("login.html")


@app.route("/logout")
def logout():
    logout_user()
    flash("You have been logged out")
    return redirect(url_for("home"))


@app.route("/")
def home():
    recipes = Recipe.query.order_by(Recipe.recipe_title).all()
    return render_template("recipes.html", recipes=recipes)


@app.route("/my_recipes")
def my_recipes():
    recipes = Recipe.query.filter_by(created_by=current_user.id).order_by(Recipe.recipe_title).all()
    return render_template("my_recipes.html", recipes=recipes)


@app.route("/account")
def account():
    return render_template("account.html")


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
            recipe_photo=request.form.get("recipe_photo"),
            created_at=request.form.get("created_at"),
            created_by=current_user.id
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
    if recipe.created_by == current_user.id:
        if request.method == "POST":
            recipe.recipe_title = request.form.get("recipe_title")
            recipe.recipe_description = request.form.get("recipe_description")
            recipe.recipe_ingredients = request.form.get("recipe_ingredients")
            recipe.recipe_method = request.form.get("recipe_method")
            recipe.recipe_photo = request.form.get("recipe_photo")
            db.session.commit()
            return redirect(url_for("view_recipe", recipe_id=recipe.id))
    
    else:
        flash("Not permitted to edit this recipe")
        return redirect(url_for("my_recipes"))
    
    return render_template("edit_recipe.html", recipe=recipe)


@app.route("/delete_recipe/<int:recipe_id>")
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    if recipe.created_by == current_user.id:
        db.session.delete(recipe)
        db.session.commit()
        return redirect(url_for("my_recipes"))
        
    else:    
        flash("Not permitted to delete this recipe")
        return redirect(url_for("my_recipes"))
    

@app.route("/edit_account/<int:user_id>", methods=["GET", "POST"])
def edit_account(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == "POST":
        user.username = request.form.get("username")
        db.session.commit()
        return redirect(url_for("account"))
    return render_template("account")


@app.route("/delete_account/<int:user_id>")
def delete_account(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("home"))
