# Tests all of the code for service #4

# Imports --------------------------------------------------------------

from src.service4.service4 import Note


# Tests ----------------------------------------------------------------

def test_default_note_object():
    """
    Our two apis will come together in order to make some kind of note.
    This note could be replicated as a class object.
    """
    test_note = Note()
    assert test_note.rhythm == 4
    assert test_note.ova == 0
    assert test_note.pitch == 'r'


def test_api_generated_note_object():
    # TODO: Add test for API generated note, after implemented.
    assert True
