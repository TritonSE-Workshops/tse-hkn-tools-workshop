import pymongo

from commands import view_notes, add_note, delete_note


class CommandLine:

    def __init__(self, mongo_uri):
        components = pymongo.uri_parser.parse_uri(mongo_uri)
        client = pymongo.MongoClient(mongo_uri)
        self.db = client[components['database']]

    def run(self):
        print('-' * 60)
        print('Welcome to the TSE x HKN note-taking app!')
        print('Please type "help" for a list of commands.')
        print('-' * 60)
        while True:
            try:
                line = input('\n>>> ')
            except EOFError:
                print('\nbye')
                return
            args = line.split(' ')
            if len(args) == 0:
                continue
            command = args[0].lower()
            if command == 'help':
                print('COMMAND\t\tDESCRIPTION')
                print('-------\t\t-----------')
                print('help\t\tLists all available commands')
                print('view\t\tView all of the notes you have created')
                print('add [TEXT..]\tAdds a note comprising of the given text')
                print('delete [ID]\tDeletes the note referenced by said ID')
            elif command == 'view':
                view_notes(self.db, args[1:])
            elif command == 'add':
                add_note(self.db, args[1:])
            elif command == 'delete':
                delete_note(self.db, args[1:])
            else:
                print('Command not recognized.')
