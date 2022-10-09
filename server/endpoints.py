"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""

from flask import Flask, render_template
from flask_restx import Resource, Api
# import db.db as db


app = Flask(__name__)

API_PATH = '/api'
DOC_PATH = '/api/doc/'
api = Api(app, prefix=API_PATH, doc=DOC_PATH)

LIST = 'list'
HELLO = '/hello'
MESSAGE = 'message'

USER_GRADES = f'/User_grades/{LIST}'
USER_GRADES_NM = 'user_grades_list'
freshman = 'freshman'
sophomore = 'sophomore'
junior = 'junior'
senior = 'senior'

USER_COMMON_BEDTIMES = f'/User_common_bedtimes/{LIST}'
USER_COMMON_BEDTIMES_NM = 'user_common_bedtimes_list'
early = '7-9pm'
late = '10-12'
very_late = '1+'

USER_GUEST_PREFERENCES = f'/User_guest_preferences/{LIST}'
USER_GUEST_PREFERENCES_NM = 'user_guest_preferences_list'
no_guests = 'no guests'
few_guests = 'a few guests'
lots_of_guests = 'any amount of guests'


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
    This will get a list of user grades.
    """
    def get(self):
        """
        Returns a list of possible grades.
        """
        return {USER_GRADES_NM: [freshman, sophomore, junior, senior]}


@api.route(USER_COMMON_BEDTIMES)
class UserCommonBedtimes(Resource):
    """
    This will get a list of common user bedtimes.
    """
    def get(self):
        """
        Returns list of possible bedtimes.
        """
        return {USER_COMMON_BEDTIMES_NM: [early, late, very_late]}


@api.route(USER_GUEST_PREFERENCES)
class UserGuestPreferences(Resource):
    """
    This will get a list of user guest preferences.
    """
    def get(self):
        """
        Returns list of possible guest preferences.
        """
        return {USER_GUEST_PREFERENCES_NM:
                [no_guests, few_guests, lots_of_guests]}


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


@app.route('/')
def home():
    """
    The landing page for our app.
    """
    return render_template('home.html')


@app.route('/login')
def login():
    """
    The login page for our app.
    """
    # username = request.form['username']
    # password = request.form['password'] #might have to hash this passoword###############
	

	# #cursor used to send queries
    # with conn.cursor() as cursor:
	# #cursor = conn.cursor()
	# #executes query
    #     query = 'SELECT * FROM users WHERE user = %s and password = %s'
    #     cursor.execute(query, (username, password))
    #     #stores the results in a variable
    #     data = cursor.fetchone()
	# #use fetchall() if you are expecting more than 1 data row

    # error = None
    # if(data):
	# 	#creates a session for the the user
	# 	#session is a built in
    #     session['username'] = username
    #     session['type'] = 'Users' 
    #     return render_template('home.html')
		
    # else:
	# 	#returns an error message to the html page
    #     error = 'Invalid login or username'
    #     return render_template('login.html', error=error)
        
    return render_template('login.html')

    


