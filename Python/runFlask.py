from flask import Flask

def createApp(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    
    from main import apiBP
    app.register_blueprint(apiBP, url_prefix='/api')

    from doqu import db
    db.init_app(app)

    return app


if __name__ == "__main__":
    app = createApp("app")
    app.run(debug=True)