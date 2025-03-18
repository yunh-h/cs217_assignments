# Assignment 2
This project is a note-taking application that allows users to create, view, search, and manage notes. The application is built using Flask and SQLAlchemy, providing a web interface to interact with the notes. Users can add comments to notes, search for notes and comments, and delete notes along with their associated comments.

## Dependencies
To run this project, you need to have the following dependencies installed:

- Python 3.10+
- Flask
- Flask-SQLAlchemy
- SQLAlchemy

You can install the required dependencies using pip:
```sh
pip install Flask Flask-SQLAlchemy SQLAlchemy
```

## Running Flask Server
To run the Flask server, follow these steps:

- Navigate to the directory containing app.py.

- Run the Flask server:
```sh
python run.py
```

- Open your web browser and go to http://127.0.0.1:8080 to access the Flask web interface.

### Flask Routes
- `/`: Main page to list, add, and search notes.
- `/note`: View the content of a specific note.

### New functionality for the note-taking application
The note-taking application was able to do the following in the previous version:

- Create a note, where a note has a name and a content.
- Return a list of all notes.
- Return a list of notes that match a search term.
- Return the content of a note identified by name.

#### New functionalities for the application:

- Allow comments on a note.
- Add a date to each note and comment.
- Delete a note and all of its comments.

#### New functionalities for the web page:

- Display the note with its comments.
- "Search Term" also search comments.
- Add comments.
- Delete a note with its comments.
