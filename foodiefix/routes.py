from flask import render_template, request, redirect, url_for
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
        return redirect(url_for("recipe.html"))
    return render_template("edit_recipe.html", recipe=recipe)
