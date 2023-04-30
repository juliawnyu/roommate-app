"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""

from flask import Flask, render_template, request,\
                    flash, redirect, url_for, session
from flask_restx import Resource, Api, Namespace, fields
from flask_session import Session
import db.db as db
import db.fields as flds
import db.users as usr
import db.quiz as quizDB
import secrets


app = Flask(__name__)

# Needed for session and other stuff
app.config['SECRET_KEY'] = secrets.token_urlsafe(32)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

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

USER_COMMON_BEDTIMES = f'/User_common_bedtimes/{LIST}'
USER_COMMON_BEDTIMES_NS = f'/{QUESTIONNAIRE_NS}/User_common_bedtimes/{LIST}'
USER_COMMON_BEDTIMES_NM = 'User_common_bedtimes_list'

USER_GUEST_PREFERENCES = f'/User_guest_preferences/{LIST}'
USER_GUEST_PREFERENCES_NS = (
        f'/{QUESTIONNAIRE_NS}'
        f'/User_guest_preferences/{LIST}'
    )
USER_GUEST_PREFERENCES_NM = 'User_guest_preferences_list'

USER_CLEANING_PREFERENCES = f'/User_cleaning_preferences/{LIST}'
USER_CLEANING_PREFERENCES_NS = (
        f'/{QUESTIONNAIRE_NS}'
        f'/User_cleaning_preferences/{LIST}'
    )
USER_CLEANING_PREFERENCES_NM = 'User_cleaning_preferences_list'

USER_SHARING_PREFERENCES = f'/User_sharing_preferences/{LIST}'
USER_SHARING_PREFERENCES_NS = (
        f'/{QUESTIONNAIRE_NS}'
        f'/User_sharing_preferences/{LIST}'
    )
USER_SHARING_PREFERENCES_NM = 'User_sharing_preferences_list'

USER_DORM_FREQUENCY = f'/User_dorm_frequency/{LIST}'
USER_DORM_FREQUENCY_NS = (
        f'/{QUESTIONNAIRE_NS}'
        f'/User_dorm_frequency/{LIST}'
    )
USER_DORM_FREQUENCY_NM = '/User_dorm_frequency_list'

USER_GENDER_PREFERENCE = f'/User_gender_preference/{LIST}'
USER_GENDER_PREFERENCE_NS = (
        f'/{QUESTIONNAIRE_NS}'
        f'/User_gender_preference/{LIST}'
    )
USER_GENDER_PREFERENCE_NM = '/User_gender_preference_list'

USER_ANIMAL_PREFERENCES = f'/User_animal_preference/{LIST}'
USER_ANIMAL_PREFERENCES_NS = (
        f'/{QUESTIONNAIRE_NS}'
        f'/User_animal_preference/{LIST}'
    )
USER_ANIMAL_PREFERENCES_NM = '/User_animal_preferences_list'

COOKING_PREFERENCES = f'/Cooking_preference/{LIST}'
COOKING_PREFERENCES_ADD = f'/Cooking_preference_add/{LIST}'
COOKING_PREFERENCES_NS = f'/{QUESTIONNAIRE_NS}/Cooking_preference/{LIST}'
COOKING_PREFERENCES_NM = '/Cooking_preference'

SHOWER_TIMES = f'/Shower_times/{LIST}'
SHOWER_TIMES_NS = f'/{QUESTIONNAIRE_NS}/Shower_times/{LIST}'
SHOWER_TIMES_NM = '/Shower_times'

DATING_PREFERENCES = f'/Dating_preferences/{LIST}'
DATING_PREFERENCES_NS = f'/{QUESTIONNAIRE_NS}/Dating_preferences/{LIST}'
DATING_PREFERENCES_NM = '/Dating_preferences'
never_dating = "never dating"
casually = "casually dating"
committed = "in a commited relationship"

USER_ALCOHOL_PREFERENCES = f'/User_alcohol_preferences/{LIST}'
USER_ALCOHOL_PREFERENCES_NS = (
    f'/{QUESTIONNAIRE_NS}'
    f'/User_alcohol_preferences/{LIST}'
    )
USER_ALCOHOL_PREFERENCES_NM = '/User_alcohol_preferences'

USER_CONFRONTATION_STYLE = f'/User_confrontation_style/{LIST}'
USER_CONFRONTATION_STYLE_NS = (
    f'/{QUESTIONNAIRE_NS}'
    f'/User_confrontation_style/{LIST}'
    )
USER_CONFRONTATION_STYLE_NM = '/User_confrontation_style'
accommodating = "putting others before yourself"
avoiding = "completely evades conflict"
compromising = "attempts to reach middle ground"


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
        return flds.ROOMMATE_FIELDS[flds.USER_GRADES]


@questionnaire.route(DATING_PREFERENCES)
class DatingPreferences(Resource):
    """
    This will get a list of dating preferences.
    """
    def get(self):
        """
        Returns list of possible dating preferences.
        """
        return {'Title': 'DatingPreferences',
                'Type': 'Data',
                'Data': {1: committed, 2: casually,
                         3: never_dating}}


@questionnaire.route(COOKING_PREFERENCES)
class CookPreferences(Resource):
    """
    This will get a list of common cooking preferences.
    """
    def get(self):
        """
        Returns list of common cooking preferences.
        """
        return flds.ROOMMATE_FIELDS[flds.USER_COOKING_PREFERENCES]


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
class UserShowerPreferences(Resource):
    """
    This will get a list of when users like to shower
    """
    def get(self):
        """
        Returns list of possible shower times.
        """
        return flds.ROOMMATE_FIELDS[flds.USER_SHOWER_TIMES]


@questionnaire.route(USER_COMMON_BEDTIMES)
class UserCommonBedtimes(Resource):
    """
    This will get a list of common user bedtimes.
    """
    def get(self):
        """
        Returns list of possible bedtimes.
        """
        return flds.ROOMMATE_FIELDS[flds.USER_BEDTIMES]


@questionnaire.route(USER_GENDER_PREFERENCE)
class UserGenderPreference(Resource):
    """
    This will get a list of user gender preference
    """
    def get(self):
        """
        Returns list of gender preferences
        """
        return flds.ROOMMATE_FIELDS[flds.USER_GENDER_PREFERENCES]


@questionnaire.route(USER_GUEST_PREFERENCES)
class UserGuestPreferences(Resource):
    """
    This will get a list of user guest preferences.
    """
    def get(self):
        """
        Returns list of possible guest preferences.
        """
        return flds.ROOMMATE_FIELDS[flds.USER_GUEST_PREFERENCES]


@questionnaire.route(USER_CLEANING_PREFERENCES)
class UserCleaningPreferences(Resource):
    """
    This will get a list of user cleaning preferences.
    """
    def get(self):
        """
        Returns list of possible cleaning preferences.
        """
        return flds.ROOMMATE_FIELDS[flds.USER_CLEANING_PREFERENCES]


@questionnaire.route(USER_SHARING_PREFERENCES)
class UserSharingPreferences(Resource):
    """
    This will get a list of user sharing preferences.
    """
    def get(self):
        """
        Returns list of the three possible user sharing preferences.
        """
        return flds.ROOMMATE_FIELDS[flds.USER_SHARING_PREFERENCES]


@questionnaire.route(USER_DORM_FREQUENCY)
class UserDormFrequency(Resource):
    """
    This will get a list of user dorm frequency options.
    """
    def get(self):
        """
        Returns list of possible dorm frequency options.
        """
        return flds.ROOMMATE_FIELDS[flds.USER_DORM_FREQUENCY]


@questionnaire.route(USER_ANIMAL_PREFERENCES)
class UserAnimalPreferences(Resource):
    """
    This will get a list of a user's possible service animal preferences.
    """
    def get(self):
        """
        Returns list of possible animal preferences options.
        """
        return flds.ROOMMATE_FIELDS[flds.USER_ANIMAL_PREFERENCES]


@questionnaire.route(USER_ALCOHOL_PREFERENCES)
class UserAlcoholPreferences(Resource):
    """
    This will get a list of a user's possible alcohol preferences.
    """
    def get(self):
        """
        Returns list of possible alcohol preferences options.
        """
        return flds.ROOMMATE_FIELDS[flds.USER_ALCOHOL_PREFERENCES]


@questionnaire.route(USER_CONFRONTATION_STYLE)
class UserConfrontationStyle(Resource):
    """
    This will get a list of a user's confrontation style preferences.
    """
    def get(self):
        """
        Returns list of possible confrontation style preferences options.
        """
        return {'Title': 'UserConfrontationStyle',
                'Type': 'Data',
                'Data': {
                    1: accommodating,
                    2: avoiding,
                    3: compromising}
                }


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
                    '9': {'url': f'/{API_PATH}{USER_CONFRONTATION_STYLE}',
                          'method': 'get',
                          'text': 'List User Confrontation Styles'},
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
            session['netID'] = netID
            success = "Logged in successfully!"
            flash(success)
            if netID == "admin":
                return redirect(url_for('admin_page'))
            else:
                return redirect(url_for('user_homepage'))
        else:
            error = "Failed to log in."
            flash(error)
            return redirect(url_for('login'))

    elif request.method == 'GET':
        return render_template('login.html')


@app.route('/logout', methods=['GET'])
def logout():
    """
    The logout function
    """
    if request.method == 'GET':
        session['netID'] = None
        session.pop('_flashes', None)
        success = "You have been logged out."
        flash(success)
        return redirect(url_for('home'))


@app.route('/admin_page')
def admin_page():
    """
    The admin page intended for devs.
    """
    if session['netID'] != 'admin':
        session['netID'] = None
        session.pop('_flashes', None)
        return render_template('home.html')
    users_list = db_manager.get_all()
    return render_template('admin_page.html', users_list=users_list)


@app.route('/user_homepage')
def user_homepage():
    """
    The landing page for our app.
    """
    if session['netID'] is None:
        session.pop('_flashes', None)
        return render_template('home.html')
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


def clean_up_json(resp):
    """
    function to clean up messy json response that endpoints return.
    takes dictionary and turns into list of responses.
    """
    data = resp['Data']
    resp_lst = []
    for item in data.keys():
        resp_lst.append(data[item])
    return resp_lst


@app.route('/questionnaire', methods=['GET', 'POST'])
def questionnaire():
    """
    app route for the roommate quiz we use for matching
    """
    if request.method == 'POST':
        netID = session['netID']
        sleep = request.form['sleep']
        guests = request.form['guests']
        clean = request.form['clean']
        gender = request.form['gender']
        animal = request.form['animal']
        sharing = request.form['sharing']
        shower = request.form['shower']
        db_manager.add_quiz_results(
            netID,
            sleep,
            guests,
            clean,
            gender,
            animal,
            sharing,
            shower
        )
        return redirect(url_for('results'))

    elif request.method == 'GET':
        sleep_options_lst = clean_up_json(UserCommonBedtimes().get())
        guests_options_lst = clean_up_json(UserGuestPreferences().get())
        clean_options_lst = clean_up_json(UserCleaningPreferences().get())
        gender_options_lst = clean_up_json(UserGenderPreference().get())
        animal_options_lst = clean_up_json(UserAnimalPreferences().get())
        sharing_options_lst = clean_up_json(UserSharingPreferences().get())
        shower_options_lst = clean_up_json(UserShowerPreferences().get())
        return render_template(
            'questionnaire.html',
            sleep_options=sleep_options_lst,
            guests_options=guests_options_lst,
            clean_options=clean_options_lst,
            gender_options=gender_options_lst,
            animal_options=animal_options_lst,
            sharing_options=sharing_options_lst,
            shower_options=shower_options_lst,
        )


@app.route('/results')
def results():
    """
    app route for the results page for after users take quiz
    """
    return render_template('results.html')


@app.route('/browse')
def browse():
    """
    app route for browsing potential roommate matches
    """
    user = db_manager.get_user(session['netID'])
    quiz_results = user.get('quiz_results')
    return render_template('browse.html', quiz_results=quiz_results)


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
