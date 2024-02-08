from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    API_KEY = '9a2dbc54383b4f9793de1008ab638cbae1ffa9c4e85d477b9909ac297990610a'
    CHARACTER_NAME = 'Sonnet Miyumi'
    DATA_CENTER = 'Excalibur'

    response = requests.get(f'https://xivapi.com/character/search?name={CHARACTER_NAME}&server={DATA_CENTER}&private_key={API_KEY}')
    
    if response.status_code == 200:
        data = response.json()['Results'][0]  # Assuming the first result is the correct character
        character_id = data['ID']
        character_data = requests.get(f'https://xivapi.com/character/{character_id}?private_key={API_KEY}').json()
        
        name = character_data['Character']['Name']
        job = character_data['Character']['ActiveClassJob']['Job']['Name']
        level = character_data['Character']['ActiveClassJob']['Level']
        server = character_data['Character']['Server']
        
        return render_template('dashboard.html', name=name, job=job, level=level, server=server)
    else:
        return 'Error fetching character data'

if __name__ == '__main__':
    app.run(debug=True)
