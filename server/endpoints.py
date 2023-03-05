"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""

from flask import Flask, render_template, request, flash, redirect, url_for
from flask_restx import Resource, Api, Namespace, fields
import db.db as db
import db.users as usr
import db.quiz as quizDB
import secrets


app = Flask(__name__)

# Needed for session and other stuff
app.config['SECRET_KEY'] = secrets.token_urlsafe(32)

API_PATH = '/api'
DOC_PATH = '/api/doc/'
api = Api(app, prefix=API_PATH, doc=DOC_PATH)

db_manager = db.DB_Manager()

MAIN_MENU = '/main_menu'
MAIN_MENU_NM = 'Main Menu'

QUESTIONNAIRE_NS = 'questionnaire'
DORMS_NS = 'dorms'
USERS_NS = 'users'

questionnaire = Namespace(QUESTIONNAIRE_NS, 'Questionnaire')
api.add_namespace(questionnaire)
dorms = Namespace(DORMS_NS, 'Dorms')
api.add_namespace(dorms)

LIST = 'list'
DICT = 'dict'
DETAILS = 'details'
HELLO = '/hello'
MESSAGE = 'message'
ADD = 'add'

DORMS_DICT = f'/{DICT}'
DORMS_DICT_W_NS = f'{DORMS_NS}/{DICT}'
DORMS_DETAILS = f'{DORMS_NS}/{DETAILS}'
DORMS_DETAILS_W_NS = f'{DORMS_NS}/{DETAILS}'
DORMS_ADD = f'/{DORMS_NS}/{ADD}'

USER_LIST = f'/{USERS_NS}/{LIST}'
USER_LIST_NM = f'{USERS_NS}_list'
USER_DETAILS = f'/{USERS_NS}/{DETAILS}'
USER_ADD = f'/{USERS_NS}/{ADD}'

USER_GRADES = f'/User_grades/{LIST}'
USER_GRADES_NS = f'/{QUESTIONNAIRE_NS}/User_grades/{LIST}'
USER_GRADES_NM = 'User_grades_list'
freshman = 'freshman'
sophomore = 'sophomore'
junior = 'junior'
senior = 'senior'

USER_COMMON_BEDTIMES = f'/User_common_bedtimes/{LIST}'
USER_COMMON_BEDTIMES_NS = f'/{QUESTIONNAIRE_NS}/User_common_bedtimes/{LIST}'
USER_COMMON_BEDTIMES_NM = 'User_common_bedtimes_list'
early = '7-9pm'
late = '10-12'
very_late = '1+'

USER_GUEST_PREFERENCES = f'/User_guest_preferences/{LIST}'
USER_GUEST_PREFERENCES_NS = f'/{QUESTIONNAIRE_NS}\
    /User_guest_preferences/{LIST}'
USER_GUEST_PREFERENCES_NM = 'User_guest_preferences_list'
no_guests = 'no guests'
few_guests = 'a few guests'
lots_of_guests = 'any amount of guests'

USER_CLEANING_PREFERENCES = f'/User_cleaning_preferences/{LIST}'
USER_CLEANING_PREFERENCES_NS = f'/{QUESTIONNAIRE_NS}\
    /User_cleaning_preferences/{LIST}'
USER_CLEANING_PREFERENCES_NM = 'User_cleaning_preferences_list'
clean_tidy = 'clean and tidy'
clean_messy = 'clean but messy'
messy = 'messy'

USER_SHARING_PREFERENCES = f'/User_sharing_preferences/{LIST}'
USER_SHARING_PREFERENCES_NS = f'/{QUESTIONNAIRE_NS}\
    /User_sharing_preferences/{LIST}'
USER_SHARING_PREFERENCES_NM = 'User_sharing_preferences_list'
sharing = 'willing to share items'
no_sharing = 'not willing to share items'

USER_DORM_FREQUENCY = f'/User_dorm_frequency/{LIST}'
USER_DORM_FREQUENCY_NS = f'/{QUESTIONNAIRE_NS}\
    /User_dorm_frequency/{LIST}'
USER_DORM_FREQUENCY_NM = '/User_dorm_frequency_list'
never = 'just to sleep'
often = 'often'
always = 'always'

USER_GENDER_PREFERENCE = f'/User_gender_preference/{LIST}'
USER_GENDER_PREFERENCE_NS = f'/{QUESTIONNAIRE_NS}\
    /User_gender_preference/{LIST}'
USER_GENDER_PREFERENCE_NM = '/User_gender_preference_list'
male = 'male'
female = 'female'
any_gender = 'any'

USER_ANIMAL_PREFERENCES = f'/User_animal_preference/{LIST}'
USER_ANIMAL_PREFERENCES_NS = f'/{QUESTIONNAIRE_NS}\
    /User_animal_preference/{LIST}'
USER_ANIMAL_PREFERENCES_NM = '/User_animal_preferences_list'
comfortable = "comfortable with service animals"
not_comfortable = "uncomfortable with service animals"

COOKING_PREFERENCES = f'/Cooking_preference/{LIST}'
COOKING_PREFERENCES_ADD = f'/Cooking_preference_add/{LIST}'
COOKING_PREFERENCES_NS = f'/{QUESTIONNAIRE_NS}/Cooking_preference/{LIST}'
COOKING_PREFERENCES_NM = '/Cooking_preference'
always_cooking = "you cook every day"
sometimes_cooking = "you sometimes cook"
never_cook = "you stay away from the kitchen"

SHOWER_TIMES = f'/Shower_times/{LIST}'
SHOWER_TIMES_NS = f'/{QUESTIONNAIRE_NS}/Shower_times/{LIST}'
SHOWER_TIMES_NM = '/Shower_times'
morning = "shower in the morning"
midday = "shower midday"
night = "shower at night"

DATING_PREFERENCES = f'/Dating_preferences/{LIST}'
DATING_PREFERENCES_NS = f'/{QUESTIONNAIRE_NS}/Dating_preferences/{LIST}'
DATING_PREFERENCES_NM = '/Dating_preferences'
never_dating = "never dating"
casually = "casually dating"
committed = "in a commited relationship"


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


@questionnaire.route(USER_GRADES)
class UserGrades(Resource):
    """
    This will get a list of user grades.
    """
    def get(self):
        """
        Returns a list of possible grades.
        """
        return {'Title': 'UserGrades',
                'Type': 'Data',
                'Data': {1: freshman, 2: sophomore, 3: junior, 4: senior}}


@questionnaire.route(DATING_PREFERENCES)
class DatingPreferences(Resource):
    """
    This will get a list of dating preferences.
    """
    def get(self):
        """
        Returns list of possible dating preferences.
        """
        return {'Title': 'CookPreferences',
                'Type': 'Data',
                'Data': {1: always_cooking, 2: sometimes_cooking,
                         3: never_cook}}


@questionnaire.route(COOKING_PREFERENCES)
class CookPreferences(Resource):
    """
    This will get a list of common cooking preferences.
    """
    def get(self):
        """
        Returns list of common cooking preferences.
        """
        return {'Title': 'DatingPreferences',
                'Type': 'Data',
                'Data': {1: committed, 2: casually,
                         3: never_dating}}


user_quiz = quizDB.COOKING = fields.String


@questionnaire.route(COOKING_PREFERENCES_ADD)
class AddCooking(Resource):
    """
    adds user cooking preferences.
    """
    @api.expect(user_quiz)
    def post(self):
        """
        Adding a user cookinf pref.
        """
        print(f'{request.json=}')


@questionnaire.route(SHOWER_TIMES)
class ShowerTimes(Resource):
    """
    This will get a list of when users like to shower
    """
    def get(self):
        """
        Returns list of possible shower times.
        """
        return {'Title': 'ShowerTimes',
                'Type': 'Data',
                'Data': {1: morning, 2: midday, 3: night}}


@questionnaire.route(USER_COMMON_BEDTIMES)
class UserCommonBedtimes(Resource):
    """
    This will get a list of common user bedtimes.
    """
    def get(self):
        """
        Returns list of possible bedtimes.
        """
        return {'Title': 'UserCommonBedtimes',
                'Type': 'Data',
                'Data': {1: early, 2: late, 3: very_late}}


@questionnaire.route(USER_GENDER_PREFERENCE)
class UserGenderPreference(Resource):
    """
    This will get a list of user gender preference
    """
    def get(self):
        """
        Returns list of gender preferences
        """
        return {'Title': 'UserGenderPreference',
                'Type': 'Data',
                'Data': {1: male, 2: female, 3: any_gender}}


@questionnaire.route(USER_GUEST_PREFERENCES)
class UserGuestPreferences(Resource):
    """
    This will get a list of user guest preferences.
    """
    def get(self):
        """
        Returns list of possible guest preferences.
        """
        return {'Title': 'UserGuestPreferences',
                'Type': 'Data',
                'Data': {1: no_guests, 2: few_guests, 3: lots_of_guests}}


@questionnaire.route(USER_CLEANING_PREFERENCES)
class UserCleaningPreferences(Resource):
    """
    This will get a list of user cleaning preferences.
    """
    def get(self):
        """
        Returns list of possible cleaning preferences.
        """
        return {'Title': 'UserCleaningPreferences',
                'Type': 'Data',
                'Data': {1: clean_tidy, 2: clean_messy, 3: messy}}


@questionnaire.route(USER_SHARING_PREFERENCES)
class UserSharingPreferences(Resource):
    """
    This will get a list of user sharing preferences.
    """
    def get(self):
        """
        Returns list of the two possible user sharing preferences.
        """
        return {'Title': 'UserSharingPreferences',
                'Type': 'Data',
                'Data': {1: sharing, 2: no_sharing}}


@questionnaire.route(USER_DORM_FREQUENCY)
class UserDormFrequency(Resource):
    """
    This will get a list of user dorm frequency options.
    """
    def get(self):
        """
        Returns list of possible dorm frequency options.
        """
        return {'Title': 'UserDormFrequency',
                'Type': 'Data',
                'Data': {1: never, 2: often, 3: always}}


@questionnaire.route(USER_ANIMAL_PREFERENCES)
class UserAnimalPreferences(Resource):
    """
    This will get a list of a user's possible service animal preferences.
    """
    def get(self):
        """
        Returns list of possible animal preferences options.
        """
        return {'Title': 'UserAnimalPreferences',
                'Type': 'Data',
                'Data': {1: comfortable, 2: not_comfortable}}


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


user_fields = api.model('NewUser', {
    usr.NAME: fields.String,
    usr.EMAIL: fields.String
})


@api.route(USER_ADD)
class AddUser(Resource):
    """
    Add a user.
    """
    @api.expect(user_fields)
    def post(self):
        """
        Adding a user.
        """
        print(f'{request.json=}')
        name = request.json[usr.NAME]
        del request.json[usr.NAME]
        usr.add_user(name, request.json)


@api.route(MAIN_MENU)
class MainMenu(Resource):
    """
    This will deliver our main menu.
    """
    def get(self):
        """
        Gets the main game menu.
        """
        return {'Title': MAIN_MENU_NM,
                'Default': 1,
                'Choices': {
                    '1': {'url': f'/{API_PATH}{USER_GRADES_NS}',
                          'method': 'get',
                          'text': 'List User Grades'},
                    '2': {'url': f'/{API_PATH}{USER_COMMON_BEDTIMES_NS}',
                          'method': 'get',
                          'text': 'List User Common Bedtimes'},
                    '3': {'url': f'/{API_PATH}{USER_GUEST_PREFERENCES_NS}',
                          'method': 'get',
                          'text': 'List User Guest Preferences'},
                    '4': {'url': f'/{API_PATH}{USER_CLEANING_PREFERENCES_NS}',
                          'method': 'get',
                          'text': 'List User Cleaning Preferences'},
                    '5': {'url': f'/{API_PATH}{USER_SHARING_PREFERENCES_NS}',
                          'method': 'get',
                          'text': 'List User Sharing Preferences'},
                    '6': {'url': f'/{API_PATH}{USER_DORM_FREQUENCY_NS}',
                          'method': 'get',
                          'text': 'List User Dorm Frequency'},
                    '7': {'url': f'/{API_PATH}{USER_ANIMAL_PREFERENCES}',
                          'method': 'get',
                          'text': 'List User Service Animal Preferences'},
                    '8': {'url': f'/{API_PATH}{USER_GENDER_PREFERENCE}',
                          'method': 'get',
                          'text': 'List User Gender Preferences'},
                    'X': {'text': 'Exit'},
                }}


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
    if request.method == 'POST':
        netID = request.form['netID']
        password = request.form['password']

        login_correct = False
        try:
            login_correct = db_manager.login_correct(netID, password)
        except Exception as error:
            print(f"Error logging in: {error}")

        if login_correct:
            success = "Logged in successfully!"
            flash(success)
            # should be updated to post-login profile / account page
            return redirect(url_for('user_homepage'))
        else:
            error = "Failed to log in."
            flash(error)
            return redirect(url_for('home'))

    elif request.method == 'GET':
        return render_template('login.html')


@app.route('/user_homepage')
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
    if request.method == 'POST':
        netID = request.form['netID']
        password = request.form['password']
        grade = request.form['grade']

        user_exists = False
        if db_manager.get_user(netID):
            user_exists = True

        if not user_exists:
            user_created = False
            try:
                db_manager.add_user(netID, password, grade)
                user_created = True
            except Exception as error:
                print(f"Error registering new user: {error}")

        if user_exists:
            error = "Account with that netID already exists!"
            flash(error)
        elif user_created:
            success = "Account created successfully!"
            flash(success)
        else:
            error = "Failed to create new account."
            flash(error)

        return redirect(url_for('home'))

    elif request.method == 'GET':
        return render_template('register.html')


@app.route('/quiestionnaire', methods=['GET', 'POST'])
def questionnaire():
    """
    app route for the roommate quiz we use for matching
    """
    if request.method == 'POST':
        sleep = request.form['sleep']
        guests = request.form['guests']
        social = request.form['social']

        db_manager.add_quiz(sleep, guests, social)
        return redirect('results.html')

    elif request.method == 'GET':
        return render_template('quiz.html')


@app.route('/results')
def results():
    """
    app route for the results page for after users take quiz
    """
    return render_template('results.html')


@app.route('/clark')
def clark_info():
    """
    The Clark info  page for our app.
    """
    return render_template('clark.html')


@app.route('/othmer')
def othmer_info():
    """
    The Othmer info  page for our app.
    """
    return render_template('othmer.html')


@app.route('/gramercy')
def gramercy_info():
    """
    The gramercy green info  page for our app.
    """
    return render_template('gramercy.html')


@app.route('/alumni')
def alumni_info():
    """
    The alumni hall info  page for our app.
    """
    return render_template('alumni.html')
