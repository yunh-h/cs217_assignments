from datetime import datetime


class NoteBook:
    def __init__(self):
        self.notes = {}
        self.comments = {}
    
    def add_note(self, name: str, content: str) -> bool:
        """
        Create a note, where a note has a name and a content.
        """
        if name in self.notes:
            print('Fail to add note')
            return False

        self.notes[name] = {'content': content, 'date': datetime.now()}
        self.comments[name] = []
        print('Note added')
        return True

    def list_notes(self) -> list:
        """Return a list of all notes."""
        return list(self.notes.keys())

    def find(self, term: str) -> list:
        """Return a list of notes that match a search term."""
        return [name for name in self.notes if term in self.notes[name]]
    
    def get(self, name: str) -> str:
        """Return the content of a note identified by name."""
        return self.notes.get(name, 'Note not found')
    
    def add_comment(self, name: str, comment: str) -> bool:
        """Add a comment to a note."""
        if name not in self.notes:
            print('Fail to add comment')
            return False
        
        self.comments[name].append({'comment': comment, 'date': datetime.now()})
        print('Comment added') 
        return True
    
    def delete(self, name:str) -> bool:
        """Delete a note."""
        if name not in self.notes:
            print('Note not found')
            return False
        
        del self.notes[name]
        del self.comments[name]
        print('Note and comments deleted')
        return True
    