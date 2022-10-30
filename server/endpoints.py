"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""

from flask import Flask, render_template
from flask_restx import Resource, Api, Namespace
# import db.db as db


app = Flask(__name__)

API_PATH = '/api'
DOC_PATH = '/api/doc/'
api = Api(app, prefix=API_PATH, doc=DOC_PATH)

QUIZ_NS = 'quiz'

quiz = Namespace(QUIZ_NS, 'Quiz')
api.add_namespace(quiz)

LIST = 'list'
HELLO = '/hello'
MESSAGE = 'message'

USER_GRADES = f'/User_grades/{LIST}'
USER_GRADES_NS = f'/{QUIZ_NS}/User_grades/{LIST}'
USER_GRADES_NM = 'user_grades_list'
freshman = 'freshman'
sophomore = 'sophomore'
junior = 'junior'
senior = 'senior'

USER_COMMON_BEDTIMES = f'/User_common_bedtimes/{LIST}'
USER_COMMON_BEDTIMES_NS = f'/{QUIZ_NS}/User_common_bedtimes/{LIST}'
USER_COMMON_BEDTIMES_NM = 'user_common_bedtimes_list'
early = '7-9pm'
late = '10-12'
very_late = '1+'

USER_GUEST_PREFERENCES = f'/User_guest_preferences/{LIST}'
USER_GUEST_PREFERENCES_NS = f'/{QUIZ_NS}/User_guest_preferences/{LIST}'
USER_GUEST_PREFERENCES_NM = 'user_guest_preferences_list'
no_guests = 'no guests'
few_guests = 'a few guests'
lots_of_guests = 'any amount of guests'

USER_CLEANING_PREFERENCES = f'/User_cleaning_preferences/{LIST}'
USER_CLEANING_PREFERENCES_NS = f'/{QUIZ_NS}/User_cleaning_preferences/{LIST}'
USER_CLEANING_PREFERENCES_NM = 'user_cleaning_preferences_list'
clean_tidy = 'clean and tidy'
clean_messy = 'clean but messy'
messy = 'messy'

USER_SHARING_PREFERENCES = f'/User_sharing_preferences/{LIST}'
USER_SHARING_PREFERENCES_NS = f'/{QUIZ_NS}/User_sharing_preferences/{LIST}'
USER_SHARING_PREFERENCES_NM = 'user_sharing_preferences_list'
sharing = 'willing to share items'
no_sharing = 'not willing to share items'

USER_DORM_FREQUENCY = f'/User_dorm_frequency/{LIST}'
USER_DORM_FREQUENCY_NS = f'/{QUIZ_NS}/User_dorm_frequency/{LIST}'
USER_DORM_FREQUENCY_NM = '/user_dorm_frequency_list'
never = 'just to sleep'
often = 'often'
always = 'always'


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


@quiz.route(USER_GRADES)
class UserGrades(Resource):
    """
    This will get a list of user grades.
    """
    def get(self):
        """
        Returns a list of possible grades.
        """
        return {USER_GRADES_NM: [freshman, sophomore, junior, senior]}


@quiz.route(USER_COMMON_BEDTIMES)
class UserCommonBedtimes(Resource):
    """
    This will get a list of common user bedtimes.
    """
    def get(self):
        """
        Returns list of possible bedtimes.
        """
        return {USER_COMMON_BEDTIMES_NM: [early, late, very_late]}


@quiz.route(USER_GUEST_PREFERENCES)
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


@quiz.route(USER_CLEANING_PREFERENCES)
class UserCleaningPreferences(Resource):
    """
    This will get a list of user cleaning preferences.
    """
    def get(self):
        """
        Returns list of possible cleaning preferences.
        """
        return {USER_CLEANING_PREFERENCES_NM:
                [clean_tidy, clean_messy, messy]}


@quiz.route(USER_SHARING_PREFERENCES)
class UserSharingPreferences(Resource):
    """
    This will get a list of user sharing preferences.
    """
    def get(self):
        """
        Returns list of the two possible user sharing preferences.
        """
        return {USER_SHARING_PREFERENCES_NM: [sharing, no_sharing]}


@quiz.route(USER_DORM_FREQUENCY)
class UserDormFrequency(Resource):
    """
    This will get a list of user dorm frequency options.
    """
    def get(self):
        """
        Returns list of possible dorm frequency options.
        """
        return {USER_DORM_FREQUENCY_NM: [never, often, always]}


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    The login page for our app.
    """
    return render_template('login.html')


@app.route('/')
def user_homepage():
    """
    The landing page for our app.
    """
    return render_template('user_homepage.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    The register page for new users to our app.
    """
    return render_template('register.html')


@app.route('/quiz')
def quiz():
    """
    app route for the roommate quiz we use for matching
    """
    return render_template('quiz.html')


@app.route('/clark')
def clark_info():
    """
    The Clark info  page for our app.
    """
    return render_template('clark.html')
