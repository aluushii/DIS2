# app/routes.py

from flask import Blueprint, render_template, request, redirect, url_for

from .db import get_db_connection


main = Blueprint('main', __name__)

#Start ved home
@main.route('/')
def root_redirect():
    return redirect(url_for('main.home'))

@main.route('/home')
def home():
    return render_template('home.html')

# Route for recipe page
@main.route('/recipe', methods=['GET'])
def recipe():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT DISTINCT material_g FROM recipes ORDER BY material_g;")
    materials = [row[0] for row in cur.fetchall()]

    cur.execute("SELECT DISTINCT needle FROM recipes ORDER BY needle;")
    needles = [row[0] for row in cur.fetchall()]

    cur.execute("SELECT DISTINCT yarn FROM recipes ORDER BY yarn;")
    yarns = [row[0] for row in cur.fetchall()]

    cur.close()
    conn.close()

    return render_template('recipe.html', materials=materials, needles=needles, yarns=yarns)

# Route for resultatet af recipe page
@main.route('/results', methods=['POST'])
def results():
    material = float(request.form['material_g'])
    needle = float(request.form['needle'])
    yarn = request.form['yarn']

    conn = get_db_connection()
    cur = conn.cursor()

    query = """
        SELECT recipe, size, material_g, needle, yarn
        FROM recipes
        WHERE material_g <= %s AND needle = %s AND yarn = %s
    """
    cur.execute(query, (material, needle, yarn))
    matches = cur.fetchall()

    cur.close()
    conn.close()

    return render_template('results.html', matches=matches)

