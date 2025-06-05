## Initialization 
1. git clone https://github.com/aluushii/DIS2
2. navigate to the CORE folder
3. docker-compose up --build
4. The web app will be available at http://localhost:5050/home.

# Example of using the app
1. Click "Get Started" on the home page to get to the recipe page
2. Fill in 800 in the Material (g) box, 4.0 in the Needle (mm) dropdown box and 
Peer Gynt fra Sandnes Garn in the Yarn dropdown box.
3. Click Find Recipes and get directed to the results page showing what recipes are possible using the input from above.


# Knitting Recipes Web App

A simple Flask-based web application for browsing and filtering knitting recipes by yarn type, needle size, and material weight. Built with Docker and PostgreSQL for easy deployment.

## Features

- Filter knitting patterns by:
  - Yarn type
  - Needle size
  - Material weight (in grams)
- Responsive front-end styled with custom CSS
- Persistent PostgreSQL database with preloaded schema and data

## Tech Stack

- **Backend**: Python, Flask
- **Database**: PostgreSQL
- **Frontend**: HTML/CSS
- **Containerization**: Docker + Docker Compose

## Project Structure

```plaintext
CORE/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── run.py
├── generate_data_load_sql.py
├── app/
├── yarn_ER_model.jpg
│   ├── db.py
│   ├── routes.py
│   └── templates/
│       ├── home.html
│       ├── recipe.html
│       └── results.html
├── static/
│   ├── css/
│   │   └── home.css
│   └── img/
├── data/
│   └── Final_recipees.csv
├── sql/
│   ├── 01_schema.sql
│   └── 02_data_load.sql
