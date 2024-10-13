# Flask MySQL MVC Application

This is a simple Flask application that demonstrates the MVC architecture with MySQL as the database. 
The application manages users and their associated posts, allowing for basic CRUD operations.

## About

The application consists of two main tables:
- **Users**: Stores user information including name and birthday.
- **Posts**: Stores posts associated with users, including title, content, created date, and updated date.

The application calculates the user's age based on their birthday.

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ponnipa-PJ/python-mysql.git
   cd python-mysql

2. **Create a virtual environment:**
   ```bash
   python -m venv myenv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     myenv\Scripts\activate
     ```

   - On macOS/Linux:
     ```bash
     source myenv/bin/activate
     ```

4. **Install the required packages:**
   ```bash
   pip install -r requirements.txt

6. **Configure the database in app.py:**
   ```bash
   app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://username:password@localhost/database'
   ```
## Usage 
    
    python app.py
    
       
## API Endpoints
### User Endpoints ###
- **Get all users:** ```GET /users```
    - Returns a list of all users with their names, birthdays, and ages.
- **Create a new user**: ```POST /users```
  ```json
  {
  "name": "John Doe",
  "birthDate": "2000-01-01"
  }
  ```
    - Returns the created user information.
- **Update a user**: ```PUT /users/<id>```
  ```json
  {
  "name": "Jane Doe",
  "birthDate": "1995-05-05"
  }
  ```
    - Returns the updated user information.
- **Delete a user**: ```DELETE /users/<id>```
    - Deletes the specified user and returns a 204 No Content response.
 
### Post Endpoints ### 
- **Get all posts:** ```GET /posts```
    - Returns a list of all posts with their titles, contents, and creation dates.
- **Create a new post**: ```POST /posts```
  ```json
  {
  "userId": 1,
  "title": "First Post",
  "content": "This is the content."
  }
  ```
    - Returns the created post information.
- **Update a post**: ```PUT /posts/<id>```
  ```json
  {
  "userIdd": 1,
  "title": "First Post",
  "content": "This is the content of the first post."
  }
  ```
    - Returns the updated post information.
- **Delete a post**: ```DELETE /posts/<id>```
  - Deletes the specified post and returns a 204 No Content response.





