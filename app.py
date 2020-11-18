from flask import (
    Flask,
    render_template,
)
from gevent.pywsgi import WSGIServer

app = Flask(__name__)


@app.route('/')
def root():
    return render_template('index.html')


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8080, debug=True)
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()