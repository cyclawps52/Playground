# Playground

| Project | Link | Description | Requirements |
| - | - | - | - |
| Speech Recognition | [Source (Py3)](https://github.com/cyclawps52/Playground/blob/master/Hackathon2018/hackathon2018.py) | Records 5 second audio clips and uses Google's speech recognition platform to return a string. The string is then searched for keywords to run various commands | speechrecognition, pyaudio |
| Markov Chain | [Source (Py3)](https://github.com/cyclawps52/Playground/blob/master/Markov/markov.py) | Takes the inputted dictionary and creates a random Markov sentence. Sentence is outputted to terminal as well as read aloud | Markovify |
| Metronome | [Source (Py3)](https://github.com/cyclawps52/Playground/blob/master/Metronome/metronome.py) | Exponential metronome (requested by a friend). Increases by set amount every x seconds | winsound| 
| Live CTF Scoreboard | [Source (Py2)](https://github.com/cyclawps52/Playground/blob/master/Live%20CTF%20Scoreboard/liveScoreboard.py) | Pulls data from a Google Spreadsheet. Requires creds.json file from Google's API Network and the spreadsheet key from the URL [(this is inserted on line 41)](https://github.com/cyclawps52/Playground/blob/master/Live%20CTF%20Scoreboard/liveScoreboard.py#L41) | gspread, oauth2client, PyOpenSSL |