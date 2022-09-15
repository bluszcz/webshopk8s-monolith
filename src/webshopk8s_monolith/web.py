from bottle import route, run

def start_web():
    @route('/hello')
    def hello():
        return "Hello World!"
    run(host='localhost', port=8080, debug=True)
