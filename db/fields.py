
TYPE = 'Type'
DATA = 'Data'
TITLE = 'Title'

USER_GRADES = 'UserGrades'
FRESHMAN = 'freshman'
SOPHOMORE = 'sophomore'
JUNIOR = 'junior'
SENIOR = 'senior'
GRAD = 'graduate student'

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
    }
}


def get_field(field_name):
    return ROOMMATE_FIELDS[field_name]
