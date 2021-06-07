from flask import Flask, abort
from flask_restful import Api, Resource, reqparse, inputs, marshal_with, fields
from flask_sqlalchemy import SQLAlchemy
import datetime
import sys


# Initialize app and db
app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///event.db'
resource_fields = {
    'id': fields.Integer,
    'event': fields.String,
    'date': fields.String
}


class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(80), nullable=False)
    date = db.Column(db.Date, nullable=False)


db.create_all()

# Define resources
api = Api(app)

# parsing params for GET /event endpoint
get_parser = reqparse.RequestParser()
get_parser.add_argument(
    'start_time',
    type=inputs.date
)
get_parser.add_argument(
    'end_time',
    type=inputs.date
)


# parsing params for POST /event endpoint
post_parser = reqparse.RequestParser()
post_parser.add_argument(
    'date',
    type=inputs.date,
    help="The event date with the correct format is required! The correct format is YYYY-MM-DD!",
    required=True
)
post_parser.add_argument(
    'event',
    type=str,
    help="The event name is required!",
    required=True
)


class EventGetResource(Resource):
    @marshal_with(resource_fields)
    def get(self):
        return Events.query.filter(Events.date == datetime.date.today()).all()


api.add_resource(EventGetResource, "/event/today")


class EventById(Resource):
    @marshal_with(resource_fields)
    def get(self, event_id):
        event = Events.query.filter(Events.id == event_id).first()
        if event is None:
            abort(404, "The event doesn't exist!")
        return event

    def delete(self, event_id):
        event = Events.query.filter(Events.id == event_id).first()
        if event is None:
            abort(404, "The event doesn't exist!")
        db.session.delete(event)
        db.session.commit()
        return {"message": "The event has been deleted!"}


api.add_resource(EventById, '/event/<int:event_id>')


class AllEventResource(Resource):
    @marshal_with(resource_fields)
    def get(self):
        args = get_parser.parse_args()
        if args['start_time'] and args['end_time']:
            print(type(args['start_time']))
            print(args['start_time'])
            print(Events.date)
            events = Events.query.filter(Events.date >= args['start_time'])\
                                    .filter(Events.date <= args['end_time']).all()
            return events
        else:
            return Events.query.all()

    def post(self):
        args = post_parser.parse_args()
        add_event = Events(event=str(args["event"]), date=args['date'])
        db.session.add(add_event)
        db.session.commit()
        return {"message": "The event has been added!",
                "event": args['event'],
                "date": str(args['date'].date())}


api.add_resource(AllEventResource, '/event')


# do not change the way you run the program
if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run()
