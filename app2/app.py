from flask import request, Flask
import json, socket

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is backend  ! ' + str(socket.gethostname()) + ' \n'

@app.route("/compute", methods=["POST"])
def compute():
    return "From : <" + str(socket.gethostname()) + ">  " + request.form['heads'] + "\n"
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
