from flask import render_template, request, redirect, url_for
from foodiefix import app, db
from foodiefix.models import User, Recipe


@app.route("/")
def home():
    return render_template("recipes.html")


@app.route("/my_recipes")
def my_recipes():
    recipes = list(Recipe.query.order_by(Recipe.recipe_title).all())
    return render_template("my_recipes.html", recipes=recipes)


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
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
