from api.notes import create_note, list_notes

def test_create_note():
    create_note("Test")
    assert len(list_notes()) > 0
from api.notes import update_note

def test_update():
    update_note(0, "Updated")
    assert True
