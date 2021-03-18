from flask_restful import Api
from topsecret import app
from topsecret.resources.topsecret import TopSecret

api = Api(app)

api.add_resource(TopSecret, '/topsecret')

if __name__ == '__main__':
    app.run(debug=True)
else:
    app.run(debug=False)
