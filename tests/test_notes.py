from api.notes import create_note, list_notes

def test_create_note():
    create_note("Test")
    assert len(list_notes()) > 0
