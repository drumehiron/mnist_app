from flask import (
    Flask,
    render_template,
)
from gevent.pywsgi import WSGIServer
import os

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')


if __name__ == '__main__':
    # app.run()
    # app.run(host='0.0.0.0', port=8080, debug=True)
    port = int(os.environ.get('PORT', 5000))
    http_server = WSGIServer(("0.0.0.0", port), app)
    http_server.serve_forever()
