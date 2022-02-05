# He is an example

from datetime import date

week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
def day_phrase():
    today = date.today()
    return week_days[today.weekday()] + ',\n' + str(today.strftime("%B %d"))