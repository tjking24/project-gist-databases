from .models import Gist
from datetime import datetime


def search_gists(db_connection, **kwargs): 
    string = ''
    if 'github_id' in kwargs:
        cursor = db_connection.execute('''SELECT * FROM gists WHERE github_id = :github_id''',kwargs)
    
    elif 'created_at' in kwargs:
        cursor = db_connection.execute('''SELECT * FROM gists WHERE datetime(created_at) == datetime(:created_at)''',kwargs)
    
    else:
        cursor = db_connection.execute('SELECT * FROM gists')
    
    return[Gist(row) for row in cursor.fetchall()]
    
   
    
    

  