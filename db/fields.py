
TYPE = 'Type'
DATA = 'Data'
TITLE = 'Title'

USER_GRADES = 'UserGrades'
FRESHMAN = 'freshman'
SOPHOMORE = 'sophomore'
JUNIOR = 'junior'
SENIOR = 'senior'
GRAD = 'graduate student'

USER_BEDTIMES = 'UserBedtimes'
EARLY_BEDTIME = 'before 9pm'
LATER_BEDTIME = 'after 9pm-before 12am'
LATE_BEDTIME = 'after midnight'

USER_GUEST_PREFERENCES = 'UserGuestPreferences'
NO_GUESTS = 'no guests'
FEW_GUESTS = 'a few guests'
NO_GUEST_PREFERENCE = 'any amount of guests'

USER_CLEANING_PREFERENCES = 'UserCleaningPreferences'
CLEAN_TIDY = 'clean and tidy always'
CLEAN_MESSY = 'clean but messy'
MESSY = 'messy'

USER_SHARING_PREFERENCES = 'UserSharingPreferences'
SHARING = 'willing to share items'
NO_SHARING = 'not willing to share items'
SOME_SHARING = 'willing to share select items'

USER_DORM_FREQUENCY = 'UserDormFrequency'
NEVER_AT_DORM = 'just to sleep'
OFTEN_AT_DORM = 'often'
ALWAYS_AT_DORM = 'always'

USER_GENDER_PREFERENCES = 'UserGenderPreferences'
MALE = 'male'
FEMALE = 'female'
ANY_GENDER = 'any'

USER_ANIMAL_PREFERENCES = 'UserAnimalPreferences'
COMFORTABLE_WITH_ANIMAL = 'comfortable with service animals'
UNCOMFORTABLE_WITH_ANIMAL = 'uncomfortable with service animals'

USER_COOKING_PREFERENCES = 'UserCookingPreferences'
ALWAYS_COOKING = 'cook every day'
SOMETIMES_COOKING = 'occasionally cook'
NEVER_COOKING = 'cannot be trusted in the kitchen'

USER_SHOWER_TIMES = 'UserShowerTimes'
MORNING_SHOWER = 'shower in the morning'
MIDDAY_SHOWER = 'shower midday'
NIGHT_SHOWER = 'shower at night'

USER_ALCOHOL_PREFERENCES = 'UserAlcoholPreferences'
COMFORTABLE_WITH_ALCOHOL = 'comfortable with alcohol present'
SEMI_COMFORTABLE_WITH_ALCOHOL = 'comfortable with alcohol but not in my space'
UNCOMFORTABLE_WITH_ALCOHOL = 'not comfortable with alcohol present'

ROOMMATE_FIELDS = {
    USER_GRADES: {
        TITLE: USER_GRADES,
        TYPE: DATA,
        DATA: {
            1: FRESHMAN,
            2: SOPHOMORE,
            3: JUNIOR,
            4: SENIOR,
            5: GRAD
        }
    },
    USER_BEDTIMES: {
        TITLE: USER_BEDTIMES,
        TYPE: DATA,
        DATA: {
            1: EARLY_BEDTIME,
            2: LATER_BEDTIME,
            3: LATE_BEDTIME
        }
    },
    USER_GUEST_PREFERENCES: {
        TITLE: USER_GUEST_PREFERENCES,
        TYPE: DATA,
        DATA: {
            1: NO_GUESTS,
            2: FEW_GUESTS,
            3: NO_GUEST_PREFERENCE
        }
    },
    USER_CLEANING_PREFERENCES: {
        TITLE: USER_CLEANING_PREFERENCES,
        TYPE: DATA,
        DATA: {
            1: CLEAN_TIDY,
            2: CLEAN_MESSY,
            3: MESSY
        }
    },
    USER_SHARING_PREFERENCES: {
        TITLE: USER_SHARING_PREFERENCES,
        TYPE: DATA,
        DATA: {
            1: SHARING,
            2: NO_SHARING,
            3: SOME_SHARING
        }
    },
    USER_DORM_FREQUENCY: {
        TITLE: USER_DORM_FREQUENCY,
        TYPE: DATA,
        DATA: {
            1: NEVER_AT_DORM,
            2: OFTEN_AT_DORM,
            3: ALWAYS_AT_DORM
        }
    },
    USER_GENDER_PREFERENCES: {
        TITLE: USER_GENDER_PREFERENCES,
        TYPE: DATA,
        DATA: {
            1: MALE,
            2: FEMALE,
            3: ANY_GENDER
        }
    },
    USER_ANIMAL_PREFERENCES: {
        TITLE: USER_ANIMAL_PREFERENCES,
        TYPE: DATA,
        DATA: {
            1: COMFORTABLE_WITH_ANIMAL,
            2: UNCOMFORTABLE_WITH_ANIMAL
        }
    },
    USER_COOKING_PREFERENCES: {
        TITLE: USER_COOKING_PREFERENCES,
        TYPE: DATA,
        DATA: {
            1: ALWAYS_COOKING,
            2: SOMETIMES_COOKING,
            3: NEVER_COOKING
        }
    },
    USER_SHOWER_TIMES: {
        TITLE: USER_SHOWER_TIMES,
        TYPE: DATA,
        DATA: {
            1: MORNING_SHOWER,
            2: MIDDAY_SHOWER,
            3: NIGHT_SHOWER
        }
    },
    USER_ALCOHOL_PREFERENCES: {
        TITLE: USER_ALCOHOL_PREFERENCES,
        TYPE: DATA,
        DATA: {
            1: COMFORTABLE_WITH_ALCOHOL,
            2: SEMI_COMFORTABLE_WITH_ALCOHOL,
            3: UNCOMFORTABLE_WITH_ALCOHOL
        }
    }
}


def get_field(field_name):
    return ROOMMATE_FIELDS[field_name]
