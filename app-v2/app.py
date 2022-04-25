from flask import Flask, render_template

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def home():
    return(render_template('stars.html', title='Application v2'))

app.run(host='0.0.0.0', port=80)