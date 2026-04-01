# api/notes.py
notes = []
def create_note(save(notes)):
    notes.append({"id": len(notes), "text": text})
def list_notes():
    return notes
def get_note(note_id):
    for note in notes:
        if note["id"] == note_id:
            return note
def update_note(note_id, new_text):
    for note in notes:
        if note["id"] == note_id:
            note["text"] = new_text
def delete_note(note_id):
    global notes
    notes = [n for n in notes if n["id"] != note_id]
from api.storage import load, save

notes = load()
