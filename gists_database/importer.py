import requests

def import_gists_to_database(db, username, commit=True):
    #grabbing gist from api based on username
   
    resp = requests.get('https://api.github.com/users/{}/gists'.format(username))
    if not resp:
        raise requests.HTTPError
   
    resp_dict = resp.json()
 
    #inserting data into table 
    if commit:
        for row in resp_dict:
            params = {'id': row['id'],
			'html_url': row['html_url'],
			'git_pull_url': row['git_pull_url'],
			'git_push_url': row['git_push_url'],
			 'commits_url': row['commits_url'],
			 'forks_url': row['forks_url'],
			 'public': row['public'],
			 'created_at':row['created_at'],
			 'updated_at':row['updated_at'],
			 'comments': row['comments'],
			 'comments_url': row['comments_url']
			 }
            
            cursor = db.execute('''
			INSERT INTO gists
				(github_id, html_url, git_pull_url,
				git_push_url, commits_url,forks_url,
				public, created_at, updated_at, comments ,
				comments_url)
				
				VALUES
					(:id, :html_url, :git_pull_url,
					 :git_push_url, :commits_url, :forks_url,
					   :public, :created_at, :updated_at, :comments,
					    :comments_url)
				''', params)
            
    
