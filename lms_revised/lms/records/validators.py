from . import literals
from django.contrib import messages
from datetime import date, datetime

data_errors = dict()
def validate_date(raw_date):
    print("================validaiting date")
    parsed_date = None
    try:
        parsed_date = datetime.strptime(raw_date, "%Y-%m-%d")
        parsed_date = raw_date
    except:
        try:
            parsing = datetime.strptime(raw_date, '%Y/%m/%d')
            parsed_date = datetime.strftime(parsing, '%Y-%m-%d')
        except:
            parsed_date == None

    if parsed_date == None:
        data_errors['date'] = 'invalid date format(Action: skip)'
        return False
    else:
        return parsed_date


def validate_stat_1(stat):
    print("================validaiting stat1")
    stat_one_data = [
        literals.STAT_ONE_CHOICE_ONE,
        literals.STAT_ONE_CHOICE_TWO,
        literals.STAT_ONE_CHOICE_THREE,
        literals.STAT_ONE_CHOICE_FOUR,
        literals.STAT_ONE_CHOICE_FIVE,
    ]
    if stat in stat_one_data:
        return stat
    else:
        return literals.STAT_ONE_CHOICE_NOT_SPECIFIED


def validate_stat_2(stat):
    print("================validaiting stat2")
    stat_two_data = [
        literals.STAT_TWO_CHOICE_ONE,
        literals.STAT_TWO_CHOICE_TWO,
        literals.STAT_TWO_CHOICE_THREE
    ]
    if stat in stat_two_data:
        return stat
    else:
        return literals.STAT_TWO_CHOICE_NOT_SPECIFIED


def validate_rating(rating):
    print("================validaiting rating")
    rating = float(rating)
    if 1.0<=rating<=5.0:
        return round(float(rating*1.000),1)
    else:
        data_errors['rating'] = 'rating out of range(Action: False)'
        return False


def validate_score(score):
    print("================validaiting score")
    score = float(score)
    if 0<=score<=50:
        return int(score)
    else:
        data_errors['score'] = 'score out of range(Action: False)'
        return False


def validate_and_clean(obj, data):
    if obj == 'thing':
        data['date'] = validate_date(data['date'])
        data['stat_one'] = validate_stat_1(data['stat_one'])
        data['stat_two'] = validate_stat_2(data['stat_two'])

    else:
        data['rating'] = validate_rating(data['rating'])
        data['score'] = validate_score(data['score'])

    return data, data_errors
