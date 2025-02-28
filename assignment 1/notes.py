class NoteBook:
    def __init__(self):
        self.notes = {}
    
    def add(self, name: str, content: str) -> bool:
        '''
        Create a note, where a note has a name and a content.
        '''
        if name in self.notes:
            print('Fail to add note')
            return False

        self.notes[name] = content
        print('Note added')
        return True

    def list_notes(self) -> list:
        '''Return a list of all notes.'''
        return list(self.notes.keys())

    def find(self, term: str) -> list:
        '''Return a list of notes that match a search term.'''
        return [name for name in self.notes if term in self.notes[name]]
    
    def get(self, name: str) -> str:
        '''Return the content of a note identified by name.'''
        return self.notes.get(name, 'Note not found')
    