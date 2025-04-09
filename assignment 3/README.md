# Assignment 3
This project is a note-taking application that allows users to create, view, search, and manage notes. The application is built using Flask and SQLAlchemy, providing a web interface to interact with the notes. Users can add comments to notes, search for notes and comments, and delete notes along with their associated comments. The application now includes Docker support for easy deployment and ensures database persistence outside the container.

## Dependencies
To run this project, you need to have the following dependencies installed:

- Python 3.10+
- Flask
- Flask-SQLAlchemy
- SQLAlchemy
- Docker (for containerization)

You can install the required Python dependencies using the `requirements.txt` file:

```sh
pip install -r requirements.txt
```

## Running the Application with Docker
To run the application using Docker, follow these steps:

1. **Build the Docker Image:**
```sh
docker build -t notebook .
```

2. **Run the Docker Container:**
```sh
docker run --rm -it -p 8080:8080 -v "$(pwd)/instance:/app/instance" notebook
```

3. **Access the Application:** Open your web browser and go to http://127.0.0.1:8080.

## Flask Routes
- `/`: Main page to list, add, and search notes.
- `/note`: View the content of a specific note.

### Web Page Features:
- Add notes to the notebook.
- Add comments to notes.
- Display notes with their comments.
- Search terms in notes and comments.
- Delete a note along with all its comments.

