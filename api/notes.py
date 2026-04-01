# api/notes.py
notes = []
def create_note(text):
    notes.append({"id": len(notes), "text": text})
