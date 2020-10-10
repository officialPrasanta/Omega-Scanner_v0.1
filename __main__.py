from core.app import app
# from flask_bootstrap import Bootstrap
if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'cBRzmuqekeC7YtvNr93tXyERbUfblgJv'
    app.run(debug=True)