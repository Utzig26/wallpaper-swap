# He is an example
import random
from datetime import date

week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
def day_phrase():
    today = date.today()
    return week_days[today.weekday()] + ',\n' + str(today.strftime("%B %d"))

def raul_genival_phrase():
    with open('lyrics/lyrics_raul.txt', 'r', encoding='utf8') as f:
        lyrics_raul = f.readlines()
    f.close()

    with open('lyrics/lyrics_genival.txt', 'r', encoding='utf8') as f:
        lyrics_genivaldo = f.readlines()
    f.close()

    choice = random.randrange(1,2)
    if choice == 1:
        quote = str(random.choice(lyrics_raul) + random.choice(lyrics_genivaldo))
    else:
        quote = str(random.choice(lyrics_genival) + random.choice(lyrics_raul))

    return quote