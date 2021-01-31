from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from model import predict_weight, predict_height

app = Flask(__name__)
api = Api(app)
CORS(app)

predict_weight_args = reqparse.RequestParser()
predict_weight_args.add_argument(
    'height', type=float, help='Height of human in CM', required=True)

predict_height_args = reqparse.RequestParser()
predict_height_args.add_argument(
    'weight', type=float, help='Weight of human in KG', required=True)


class PredictWeight(Resource):
    def post(self):
        args = predict_weight_args.parse_args()
        predict = predict_weight(
            args['height']
        )
        predict = round(float(predict), 1)
        return {'predict': predict}, 201


class PredictHeight(Resource):
    def post(self):
        args = predict_height_args.parse_args()
        predict = predict_height(
            args['weight'],
        )
        predict = round(float(predict), 1)
        return {'predict': predict}, 201


api.add_resource(PredictWeight, '/weight')
api.add_resource(PredictHeight, '/height')

if __name__ == '__main__':
    app.run()
