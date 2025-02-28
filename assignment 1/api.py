from fastapi import FastAPI
from notes import NoteBook
from pydantic import BaseModel

app = FastAPI()
nb = NoteBook()

class Note(BaseModel):
    name: str
    content: str

@app.get('/')
async def home():
    return {'message': 'Welcome to the note app',
            'endpoints': [{'/list': 'list all note names'}, 
                          {'/find?term=<term>': 'a dictionary including all notes that match the search term'},
                          {'/note/<name>': 'the text from a specific note'}]}

@app.get('/list')
async def list_notes():
    return nb.list_notes()

@app.get('/find')
async def find_notes(term):
    return {'term': term, 'matching notes': nb.find(term)}

@app.get('/note/{name}')
async def get_note(name):
    return nb.get(name)

@app.post('/add')
async def add_note(note: Note):
    success = nb.add(note.name, note.content)
    if success:
        return {'message': 'Note added'}
    else:
        return {'message': 'Fail to add note'}