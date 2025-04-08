from flask import Blueprint, request, render_template, redirect, url_for
from .models import db, Note, Comment

routes = Blueprint('routes', __name__)


@routes.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        content = request.form['content']
        success = Note.add(name, content)

        if not success:
            return 'Fail to add note'
        
    all_notes = Note.query.all()
    term = request.args.get('term', '')

    if term:
        results = Note.search(term)
        if not results:
            message = f'No notes found for "{term}"'
        else:
            message = None
    else:
        results = []
        message = None

    return render_template('index.html', all_notes=all_notes, results=results, term=term, message=message)


@routes.route('/note')
def note_detail():
    name = request.args.get('name')
    note = Note.query.filter_by(name=name).first()
    
    if not note:
        return 'Note not found', 404
    
    comments = Comment.query.filter_by(note_id=note.id).all()
    return render_template('note.html', name=note.name, content=note.content, date=note.date, comments=comments)


@routes.route('/note/<name>/comment', methods=['POST'])
def add_comment(name):
    note = Note.query.filter_by(name=name).first()
    if not note:
        return 'Note not found', 404

    content = request.form['content']
    success = Comment.add(note.id, content)

    if not success:
        return 'Fail to add comment'

    return redirect(url_for('routes.note_detail', name=name))


@routes.route('/note/<name>/delete', methods=['POST'])
def delete_note_and_comments(name):
    success = Note.delete(name)
    if not success:
        return 'Note not found', 404

    return redirect(url_for('routes.index'))
