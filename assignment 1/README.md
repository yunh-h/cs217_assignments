# Assignment 1
This project is a note-taking application that includes three different interfaces: FastAPI, Flask, and Streamlit. Each interface allows you to add note, list all notes, search term, and view notes. Below are the instructions on how to set up and run each interface.

## Dependencies
To run this project, you need to have the following dependencies installed:

- Python 3.10+
- FastAPI
- Flask
- Streamlit
- Uvicorn
- Pydantic

You can install the required dependencies using pip:
```sh
pip install fastapi flask streamlit uvicorn pydantic
```

## FastAPI
To run the FastAPI server, follow these steps:

- Navigate to the directory containing api.py.

- Run the FastAPI server using Uvicorn:
```sh
uvicorn api:app --reload
```

- Open your web browser and go to http://127.0.0.1:8000 to access the FastAPI endpoints.

### FastAPI Endpoints
- `GET /`: Welcome message and list of endpoints.
- `GET /list`: List all note names.
- `GET /find?term=<term>`: Find notes that match the search term.
- `GET /note/<name>`: Get the content of a specific note.
- `POST /add`: Add a new note.

## Flask
To run the Flask server, follow these steps:

- Navigate to the directory containing app.py.

- Run the Flask server:
```sh
python app.py
```

- Open your web browser and go to http://127.0.0.1:8001 to access the Flask web interface.

### Flask Routes
- `/`: Main page to list, add, and search notes.
- `/note`: View the content of a specific note.

## Streamlit
To run the Streamlit app, follow these steps:

- Navigate to the directory containing stream.py.

- Run the Streamlit app:
```sh
streamlit run stream.py
```

- Open your web browser and go to the URL provided by Streamlit to access the Streamlit interface.

### Streamlit Features
- Add a note.
- List all notes.
- Search for notes.
- View the content of a selected note.
