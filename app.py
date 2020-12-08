from flask import Flask
from flask import Flask, jsonify

DEBUG = True
PORT = 8000

# Initialize an instance of the Flask class.
# This starts the website!
app = Flask(__name__)

# The default URL ends in / ("my-website.com/").
@app.route('/')
def index():
    return 'Muse Flask Backend'

@app.route('/json')
def dog():
    return jsonify( title = "New Kid In Town",
                    artist = "Eagles",
                    album = "Hotel California",
                    created_at = "12/20/2020"
                  )

# Run the app when the program starts!
if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)

