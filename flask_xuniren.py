from flask import Flask, request, render_template

app = Flask(__name__)

refresh = '0'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/danmu')
def danmu():
    global refresh
    refresh = '1'
    return 'Done. ' + request.args.get('msg')

@app.route('/check')
def check():
    global refresh
    snapshot = refresh
    refresh = '0'
    print(snapshot)
    return snapshot


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=7860, threaded=True)
