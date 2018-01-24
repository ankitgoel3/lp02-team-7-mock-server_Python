# lp02-team-7-mock-server_Python
Python Server Code

### Documentation to Read
1. Read the Flask server docs
    - http://flask.pocoo.org/
2. Read the SQL Alchemy getting started docs
    - https://www.pythoncentral.io/introductory-tutorial-python-sqlalchemy/

### Getting Started
1. Make sure you are running at least Python > 3.4, preferably 3.6
1. Install `virtualenv` through `pip`
    - `pip install virtualenv`
1. Create a virtual environment in the root directory of this project with `virtualenv venv`
1. Activate the virtual environment with the following command:
    - `. ./venv/bin/activate`
    - For Windows OS(then only packages will be downloaded into virtual environment):
     `venv\Scripts\activate`
    
1. Use `pip install -r requirements.txt` to install all required libraries
2. Copy the `env.example.ini` file to `env.ini`
    - `cp env.example.ini env.ini`
    - Update `env.ini` to have your local Postgres DB credentials
      * Note: Have this point to your current Postgres DB that you were using for the mock server (check the .env file for the `DATABASE_URL` value). This is setup to read from the old database so everything just works!
3. Start up the Flask server
    - `set FLASK_APP=server.py`
    - `flask run`
4. Profit!
    - Visit `http://localhost:5000/users` and see a JSON response with a list of all the Users in your Users table.

Dev Notes:
  - Add this as the last line of your `server.py` file to get hot reloading:
    ```python
    app.run(debug=True)
    ```
