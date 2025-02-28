from flask import Flask, request, render_template
from notes import NoteBook

app = Flask(__name__)
nb = NoteBook()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        content = request.form['content']
        success = nb.add(name, content)

        if not success:
            return 'Fail to add note'
        
    all_notes = nb.list_notes()
    term = request.args.get('term', '')

    if term:
        results = nb.find(term)
        if not results:
            message = f'No notes found for "{term}"'
        else:
            message = None
    else:
        results = []
        message = None

    return render_template('index.html', all_notes=all_notes, results=results, term=term, message=message)

@app.route('/note')
def note_detail():
    name = request.args.get('name')
    content = nb.get(name)
    
    if content == 'Note not found':
        return 'Note not found', 404
    
    return render_template('note.html', name=name, content=content)

if __name__ == '__main__':
    app.run(debug=True, port=8001)