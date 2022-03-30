
from flask import Flask, request, render_template, jsonify
import format
import A
import B


application = Flask(__name__)
application.register_blueprint(A.application, url_prefix='/A')
application.register_blueprint(B.application, url_prefix='/B')


@application.route('/return_string', methods=['GET'])
def return_string():
    return 'Hello World'


@application.route('/upload_file', methods=['POST'])
def upload_file():
    uploaded_file = request.files['image']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
        print(uploaded_file)
    return "receive image, ok"


@application.route('/html_example', methods=['GET', 'POST'])
def show_html_example():
    if request.method == 'GET':
        print('Client sent a request to server')
        return "<form method='post' action='/html_example'>"\
            "<h3>Input a String</h3>"\
            "<input type='text' name='username' />" \
            "</br></br>" \
            "<button type='submit'>Submit</button></form>"

    elif request.method == 'POST':
        return 'Hello '+request.values['username']


@application.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        print('Client sent a request to server')
        return "<form method='post' action='/html_example'>"\
            "<h3>Login Simulation</h3>"\
            "<label for='username'>username </label>"\
            "<input type='text' name='username' />" \
            "</br>"\
            "<label for='password'>password </label>"\
            "<input type='text' name='password' />" \
            "</br></br>" \
            "<button type='Login'>Login</button>"\
            "<button type='Register'>Register</button></form>"

    elif request.method == 'POST':
        return 'Hello '+request.values['username']


@application.route('/jinja_user/<username>')
def jinja_user(username):
    '''
    Get the information from URL and sent to front page
    '''
    return render_template('output_Jinja.html', HTMLmessage=username)


@application.route('/get_json_get', methods=['GET'])
def get_json_get():
    client_header = request.headers
    client_message = request.json
    print(client_header)
    print(client_message)
    backend_message = format.TestFormat("backend", "hello, client").get_json()
    return jsonify(backend_message)  # jsonify: turn json to request form


@application.route('/get_json_post', methods=['POST'])
def get_json_post():
    client_header = request.headers
    client_message = request.json
    print(client_header)
    print(client_message)
    backend_message = format.TestFormat("backend", "hello, client").get_json()
    return jsonify(backend_message)  # jsonify: turn json to request form


@application.route('/hello_string', methods=['GET', 'POST'])
def hello_string():
    if request.method == 'GET':
        print('Request Method: GET')
        return render_template('hello_string_input.html')
    else:
        print('Method: POST')
        return render_template('hello_string_output.html',
                               user_template=request.values['username'])


@application.route('/get_username', methods=['GET', 'POST'])
def get_username():
    if request.method == 'GET':
        return "<form method='post' action='/get_username'>"\
            "<h3>Input a String</h3>"\
            "<input type='text' name='username' />" \
            "</br></br>" \
            "<button type='submit'>Submit</button></form>"
    else:
        return render_template('output.html', user_template=request.values['username'])


@application.route('/return_page', methods=['GET', 'POST'])
def return_page():
    if request.method == 'GET':
        print('Client sent a request to server')
        return "<form method='post' action='/return_page'>"\
            "<h3>Input a String</h3>"\
            "<input type='text' name='username' />" \
            "</br></br>" \
            "<button type='submit'>Submit</button></form>"
    else:
        print('Server sent a request to client')
        return 'Hello '+request.values['username']


@application.route('/get_jinja_message/<username>')
def get_jinja_message(username):
    return render_template('output_Jinja.html', HTMLmessage=username)


@application.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@application.route('/blueprint')
def blueprint():
    '''
    http://0.0.0.0:5000/blueprint
    http://0.0.0.0:5000/A/page
    http://0.0.0.0:5000/B/page
    '''
    return "<h3> Blueprint Example <h3>"


@application.errorhandler(404)
def error_404(e):
    return render_template('404.html'), 404


@application.route('/flame_detection/v1', methods=["GET", "POST"])
def leedarson_example():
    return "ok"

    # get image
    img_data = request.get_json()["image"]

    # send image
    url = 'http://172.25.11.127:5000/flame_detection/v1'
    payload = {
        "image": img_data  # base64 image
    }
    res = requests.post(url, json=payload)
    # print(res.text)
    return res.text


@application.route('/get_image_base64', methods=['GET', 'POST'])
def get_image_base64():
    '''
    Set the size limitation of passing file
    application.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 10MB
    '''
    return jsonify({'msg': 'ok'}), 200
    logging.info("request.headers: %s", request.headers)
    logging.info("request.files: %s", request.files)
    logging.info("request.files[file]: %s", request.files['file'])
    attached_file = request.files['file']
    image_file = attached_file.read()   # image file
    filename = attached_file.filename   # image name
    print(filename)
    encoded_img = base64.b64encode(image_file)
    img_b64decode = base64.b64decode(encoded_img)
    img_array = np.fromstring(img_b64decode, np.uint8)
    img = cv2.imdecode(img_array, cv2.COLOR_BGR2RGB)
    cv2.imwrite('./server.jpg', img)  # save image
    return jsonify({'msg': 'ok'}), 200


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000, debug=True)
