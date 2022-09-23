import os
from bottle import route, run

def start_web():
    HTTP_PORT=os.environ.get('HTTP_PORT', 80)
    REDIS_HOST=os.environ.get('REDIS_HOST')
    REDIS_PORT=os.environ.get('REDIS_PORT')
    @route('/')
    def index():
        return "Hello"
    @route('/info')
    def hello():
        return "Hello World >> %s <<!" % REDIS_HOST
    run(host='0.0.0.0', port=HTTP_PORT, debug=False)
