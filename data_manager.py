# Layer between the server and the data.
# Functions here should be called from the server.py and these should use generic functions from the connection.py.

import connection

question_collection = connection.question_reader()