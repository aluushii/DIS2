# app/routes.py

from flask import Blueprint, render_template, request, redirect, url_for, flash
import re
from .db import get_db_connection

main = Blueprint('main', __name__)

@main.route('/')
def root_redirect():
    return redirect(url_for('main.home'))

@main.route('/home')
def home():
    return render_template('home.html')

@main.route('/recipe', methods=['GET'])
def recipe():
    conn = get_db_connection()
    cur = conn.cursor()

    # Hent unikke material_g-værdier (gerne float-værdier fra knitted_by)
    cur.execute("""
        SELECT DISTINCT kb.material_g
        FROM knitted_by kb
        ORDER BY kb.material_g;
    """)
    materials = [row[0] for row in cur.fetchall()]

    # Hent unikke nåle-størrelser
    cur.execute("""
        SELECT DISTINCT n.size
        FROM needles n
        JOIN knitted_by kb ON n.id = kb.needle_id
        ORDER BY n.size;
    """)
    needles = [row[0] for row in cur.fetchall()]

    # Hent unikke garn-navne
    cur.execute("""
        SELECT DISTINCT y.name
        FROM yarns y
        JOIN knitted_by kb ON y.id = kb.yarn_id
        ORDER BY y.name;
    """)
    yarns = [row[0] for row in cur.fetchall()]

    cur.close()
    conn.close()
    return render_template('recipe.html', materials=materials, needles=needles, yarns=yarns)

@main.route('/results', methods=['POST'])
def results():
    grams_input = request.form['material_g']
    needle_input = request.form['needle']
    yarn_input = request.form['yarn']

    # Valider at grammængden kun består af cifre
    if not re.match(r'^\d+$', grams_input):
        flash('Indtast venligst et gyldigt tal for gram garn.')
        return redirect(url_for('main.recipe'))

    material = float(grams_input)
    needle   = float(needle_input)
    yarn     = yarn_input

    conn = get_db_connection()
    cur = conn.cursor()

    query = """
        SELECT
          r.pattern_name,
          r.size,
          kb.material_g,
          n.size   AS needle_mm,
          y.name   AS yarn_name
        FROM recipes r
        JOIN knitted_by kb ON r.id = kb.recipe_id
        JOIN needles n   ON kb.needle_id = n.id
        JOIN yarns y     ON kb.yarn_id = y.id
        WHERE
          kb.material_g <= %s
          AND n.size       = %s
          AND y.name       = %s
        ORDER BY r.pattern_name, r.size;
    """
    cur.execute(query, (material, needle, yarn))
    matches = cur.fetchall()

    cur.close()
    conn.close()
    return render_template('results.html', matches=matches)
