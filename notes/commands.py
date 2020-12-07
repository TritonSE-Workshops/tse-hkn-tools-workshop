import pymongo

from datetime import datetime


def view_notes(db: pymongo.database.Database, args: [str]):
    if len(args) > 0:
        print("No arguments need to be provided.")
        return
    notes = db['notes']
    print("ID\t\t\t\tTIME\t\t\t\tNOTE")
    print("--\t\t\t\t----\t\t\t\t----")
    for note in notes.find().sort('created_at', pymongo.ASCENDING):
        nid = note['_id']
        timestamp = note['created_at']
        content = note['content']
        print("{}\t{}\t{}".format(nid, timestamp, content))


def add_note(db: pymongo.database.Database, args: [str]):
    if len(args) == 0:
        print("Your note cannot be empty")
        return
    content = ' '.join(args)
    notes = db['notes']
    note = {
        "created_at": datetime.now(),
        "content": content
    }
    insertion = notes.insert_one(note)
    print("Note {} was successfully saved.".format(insertion.inserted_id))


def delete_note(db: pymongo.database.Database, args: [str]):
    '''
    Given args = ['{ID}', ...], calling `delete_note` will delete
    the note object with the specified _id equalling {ID}. If a note
    with {ID} does not exist, then nothing will be deleted. The user
    should be notified if the deletion operation was successful.

    For example:

    >>> add this is a note
    Note XXXXXXX was successfully saved.

    >>> view
    ID				TIME				NOTE
    --				----				----
    5fcda19580501595e7e5379d	2020-12-07 03:29:25.462000	this is a note

    >>> delete XXXXXXX
    Note XXXXXXX was successfully deleted.

    >>> view
    ID				TIME				NOTE
    --				----				----
    '''
    # TODO: Your job is to implement this function
    pass
