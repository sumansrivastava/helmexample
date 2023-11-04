from flask import Flask, request, render_template

app = Flask(__name)

@app.route('/welcome', methods=['POST'])
def welcome():
    username = request.form['username']
    return f'<h1>Welcome to my world, {username}!</h1>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
