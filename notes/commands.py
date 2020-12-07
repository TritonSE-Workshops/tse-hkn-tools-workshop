import pymongo

from datetime import datetime


def view_notes(db: pymongo.database.Database, args: [str]):
    if len(args) > 0:
        print("No arguments need to be provided.")
        return
    notes = db['notes']
    if notes.count() == 0:
        print("No notes are saved.")
        return
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
    # TODO: Your job is to implement this action
    print("UNIMPLEMENTED")
