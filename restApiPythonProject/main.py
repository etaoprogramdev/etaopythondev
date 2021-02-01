from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# making resource

names = {"tim": {"age": 19, "gender": "male"},
         "etao": {"age": 16, "gender": "male"}}


class HelloWorld(Resource):
    def get(self, name):
        return names[name]


# add a resource to the api, and defined that inorder toa access it, it is located at /helloworld
api.add_resource(HelloWorld, "/helloworld/<string:name>")


if __name__ == "__main__":
    app.run(debug=True)
