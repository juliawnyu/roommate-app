"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""

from flask_restx import Resource, Api, Namespace

#name sets the api path to 127.0.0.1/api
api = Namespace(name='api')

LIST = 'list'
HELLO = '/hello'
MESSAGE = 'message'

USER_GRADES = f'/User_grades/{LIST}'
USER_GRADES_NM = 'user_grades_list'
freshman = 'freshman'
sophomore = 'sophomore'
junior = 'junior'
senior = 'senior'



@api.route(HELLO)
class HelloWorld(Resource):
    """
    The purpose of the HelloWorld class is to have a simple test to see if the
    app is working at all.
    """
    def get(self):
        """
        A trivial endpoint to see if the server is running.
        It just answers with "hello world."
        """
        return {MESSAGE: 'hello world'}


@api.route(USER_GRADES)
class UserGrades(Resource):
    """
    This will get a list of user grades
    """
    def get(self):
        """
        Returns a list of possible grades.
        """
        return {USER_GRADES_NM: [freshman, sophomore, junior, senior]}


@api.route('/endpoints')
class Endpoints(Resource):
    """
    This class will serve as live, fetchable documentation of what endpoints
    are available in the system.
    """
    def get(self):
        """
        The `get()` method will return a list of available endpoints.
        """
        endpoints = ''
        # sorted(rule.rule for rule in api.app.url_map.iter_rules())
        return {"Available endpoints": endpoints}

