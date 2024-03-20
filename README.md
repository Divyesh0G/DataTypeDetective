# DataTypeDetective

**DataTypeDetective** is a web application designed to simplify data type inference and conversion for datasets using Python and Pandas. Powered by Django on the backend and React on the frontend, this project focuses on accurately identifying and converting data types in CSV and Excel files.

## Installation and Setup
Follow these steps to set up and run the application:

### Backend (Django)
1. Navigate to the backend directory in your terminal.
2. Create a virtual environment (optional but recommended):
    ```
    python -m venv myenv
    ```
3. Activate the virtual environment:
    - On Windows:
      ```
      myenv\Scripts\activate
      ```
    - On macOS/Linux:
      ```
      source myenv/bin/activate
      ```
4. Install Django and other dependencies:
    ```
    pip install -r requirements.txt
    ```
5. Make migrations and migrate the database:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
6. Run the Django server:
    ```
    python manage.py runserver
    ```

### Frontend (React)
1. Navigate to the frontend directory in another terminal window.
2. Install dependencies:
    ```
    npm install
    npm install axios
    ```
3. Run the frontend server:
    ```
    npm start
    ```

## Usage
1. Access the backend server at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
2. Access the frontend interface at [http://127.0.0.1:3000/](http://127.0.0.1:3000/).
3. Upload CSV or Excel files for data type inference and conversion.
4. Review and modify inferred data types as needed.
5. Enjoy seamless data processing and visualization!

## Project Scope and Tasks
- **Pandas Data Type Inference and Conversion (Backend Task):**
  - Develop a Python script using Pandas for inferring and converting data types.
  - Address common issues with data type inference, such as incorrect defaults and mixed data types.
  - Optimize the script for performance and memory efficiency.
- **Django Backend Development:**
  - Set up Django project incorporating the Python script for data processing.
  - Create Django models, views, and URLs for handling data processing logic and user interactions.
  - Implement a backend API for data input and output.
- **Frontend Development using React:**
  - Develop a frontend application using React to interact with the Django backend.
  - Allow users to upload data files, submit them for processing, and display the processed data.
  - Offer options to override inferred data types, enabling users to set custom data types for columns.

## Note on Data Cleaning 
Automating data cleaning tasks presents challenges due to the uniqueness of each dataset. While a comprehensive approach is necessary for automation, manual intervention or customization may be required for specific cases. Thorough testing is essential to ensure the accuracy and reliability of the solution.
