import requests

#insert your own Gitlab user ID at ":user_id"
response = requests.get("http://gitlab.com/api/v4/users/dennis885/projects")
my_projects = response.json()

for project in my_projects:
    print(f"Project Name: {project['name']}\nProject Url: {project['web_url']}\n")


