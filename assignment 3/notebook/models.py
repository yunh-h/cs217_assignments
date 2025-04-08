from sqlalchemy.exc import IntegrityError
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


def current_time():
    return datetime.now().replace(microsecond=0)


class Note(db.Model):
    """A note with a name and content"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=current_time)

    def __repr__(self):
        return f'<Note: {self.name}>'

    @classmethod
    def add(cls, name, content):
        """Add a new note"""
        try:
            new_note = cls(name=name, content=content)
            db.session.add(new_note)
            db.session.commit()
            return new_note
        except IntegrityError as e:
            db.session.rollback()
            return e

    @classmethod
    def delete(cls, name):
        """Delete a note and all its comments"""
        note = cls.query.filter_by(name=name).first()
        if not note:
            return False
        Comment.query.filter_by(note_id=note.id).delete()
        db.session.delete(note)
        db.session.commit()
        return True
    
    @classmethod
    def search(cls, term):
        """Find notes (including comments) containing a search term"""
        notes = cls.query.filter(cls.content.contains(term)).all()
        comments = Comment.query.filter(Comment.content.contains(term)).all()
        note_names = {note.name for note in notes}
        note_names.update(comment.note.name for comment in comments)
        return list(note_names)


class Comment(db.Model):
    """A comment on a note"""
    id = db.Column(db.Integer, primary_key=True)
    note_id = db.Column(db.Integer, db.ForeignKey('note.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=current_time)
    note = db.relationship('Note', backref=db.backref('comments'))

    def __repr__(self):
        return f'<Comment: {self.content[:20]}... (on Note {self.note_id})>'
    
    @classmethod
    def add(cls, note_id, content):
        """Add a new comment"""
        try:
            new_comment = cls(note_id=note_id, content=content)
            db.session.add(new_comment)
            db.session.commit()
            return new_comment
        except IntegrityError as e:
            db.session.rollback()
            return e
