from cli import CommandLine

import os

CommandLine(os.getenv('MONGO_URI')).run()
