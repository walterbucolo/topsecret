from flask_restful import Api
from topsecret import app
from topsecret.resources.topsecret import TopSecret
from topsecret.resources.topsecret_split import TopSecretSplit

api = Api(app)

api.add_resource(TopSecret, '/topsecret')
api.add_resource(TopSecretSplit, '/topsecret_split', '/topsecret_split/<satellite>')

if __name__ == '__main__':
    app.run(debug=True)
