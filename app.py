from flask import Flask
app = Flask(__name__)

@app.route('/')
def root_test():
    return 'Root!'

if __name__ == '__main__':
    app.run()
