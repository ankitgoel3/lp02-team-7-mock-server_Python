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
### Guideline how Save Endpoint works
1. I used try except block in Python to handle the exceptions
1. Three things are happening inside the `createUser` method
    - Checking for already existing user by showing following message :
       ```python
       Email already exists
       ```
    - Showing message if user added successfully
       ```python
       User Added
       ```
    - Showing message if something went wrong
       ```python
       Something went wrong! Please try again
       ```
1. To test the end point you can use the following JSON data:
    ```python
    {
        "first_name":"Test",
        "last_name":"Person",
        "email":"Test.Person@cognizant.com",
        "admin":true,
        "password":"testpassword",
        "photo_url":"https://res.cloudinary.com/hs7ycros0/image/upload/v1511452210/lp02team07mock/Test.jpg",
        "slack_handle":"@Test",
        "nickname":"Test",
        "title":"Developer",
        "location":"IN",
        "manager_id":13,
        "about_me":"I have been a project manager for the past 5 years",
        "interests":"cricket,football,golf"
    }
    ```

### Getting Started with PyLint
1. Install `pylint` through `pip`
    - `pip install pylint`
1. Code lay-out
    - Indentation 
      * Use 4 spaces per indentation level)
      * Spaces are the preferred indentation method. Tabs should be used solely to remain consistent with code that    is already indented with tabs. Python 3 disallows mixing the use of tabs and spaces for indentation.
    - Maximum Line Length
      * Limit all lines to a maximum of 79 characters.
    - Blank Lines
      * Surround top-level function and class definitions with two blank lines.
      * Method definitions inside a class are surrounded by a single blank line.
    - Imports
      * Imports should usually be on separate lines, e.g.
        Yes: import os
             import sys
        No:  import sys, os
    - For more visit ``https://www.python.org/dev/peps/pep-0008/``

1. On the command line, navigate to your project root and run the following command to generate a 
   configuration file:
   ```python
   pylint --generate-rcfile > .pylintrc
   ```
1. To run the python file for linting errors, run the following command
   ```python
   pylint server.py
   ```
1. Parallel execution of Pylint....
   ```python
   pylint -j 4 mymodule1.py mymodule2.py mymodule3.py mymodule4.py
   ```
   * This will spawn 4 parallel Pylint sub-process, where each provided module will be checked in parallel.