from datetime import datetime, timedelta
from collections import defaultdict


def get_birthdays_per_week(users):
    dates_future_week = []
    weeks_dict = defaultdict(list)


    if datetime.now().strftime('%A') == 'Monday':
        for i in range(7):
            dates_future_week.append(datetime.now().date() + timedelta(days=5) + timedelta(days=i))
    if datetime.now().strftime('%A') == 'Tuesday':
        for i in range(7):
            dates_future_week.append(datetime.now().date() + timedelta(days=4) + timedelta(days=i))
    if datetime.now().strftime('%A') == 'Wednesday':
        for i in range(7):
            dates_future_week.append(datetime.now().date() + timedelta(days=3) + timedelta(days=i))
    if datetime.now().strftime('%A') == 'Thursday':
        for i in range(7):
            dates_future_week.append(datetime.now().date() + timedelta(days=2) + timedelta(days=i))
    if datetime.now().strftime('%A') == 'Friday':
        for i in range(7):
            dates_future_week.append(datetime.now().date() + timedelta(days=1) + timedelta(days=i))
    if datetime.now().strftime('%A') == 'Saturday':
        for i in range(7):
            dates_future_week.append(datetime.now().date() + timedelta(days=i))
    if datetime.now().strftime('%A') == 'Sunday':
        for i in range(7):
            dates_future_week.append(datetime.now().date() + timedelta(days=6) + timedelta(days=i))

    for user in users:
        if user['birthday'].strftime('%B %d') == dates_future_week[0].strftime('%B %d') or user['birthday'].strftime('%B %d') == dates_future_week[1].strftime('%B %d') or user['birthday'].strftime('%B %d') == dates_future_week[2].strftime('%B %d'):
            weeks_dict['Monday'].append(user['name'])
        if user['birthday'].strftime('%B %d') == dates_future_week[3].strftime('%B %d'):
            weeks_dict['Tuesday'].append(user['name'])
        if user['birthday'].strftime('%B %d') == dates_future_week[4].strftime('%B %d'):
            weeks_dict['Wednesday'].append(user['name'])
        if user['birthday'].strftime('%B %d') == dates_future_week[5].strftime('%B %d'):
            weeks_dict['Thursday'].append(user['name'])
        if user['birthday'].strftime('%B %d') == dates_future_week[6].strftime('%B %d'):
            weeks_dict['Friday'].append(user['name'])


    sorted_weeks_dict = {"Monday" if weeks_dict["Monday"] else "": weeks_dict["Monday"],
                         "Tuesday" if weeks_dict["Tuesday"] else "": weeks_dict["Tuesday"],
                         "Wednesday" if weeks_dict["Wednesday"] else "": weeks_dict["Wednesday"],
                         "Thursday" if weeks_dict["Thursday"] else "": weeks_dict["Thursday"],
                         "Friday" if weeks_dict["Friday"] else "": weeks_dict["Friday"],
                         }

    for key, value in sorted_weeks_dict.items():
        if key:
            str_ = ", ".join(value)
            print(f"{key}: {str_}")


get_birthdays_per_week([{'name':'Nataly', 'birthday': datetime(year = 1987, month = 12, day = 23)},
         {'name':'Andrey', 'birthday': datetime(year = 1991, month = 12, day = 18)},
         {'name':'Julia', 'birthday': datetime(year = 1974, month = 12, day = 22)},
         {'name':'Luda', 'birthday': datetime(year = 1974, month = 12, day = 22)},
         {'name':'Sergey', 'birthday': datetime(year = 1974, month = 12, day = 21)}])