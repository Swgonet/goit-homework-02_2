from datetime import datetime, timedelta

users = [{"petro": '29-05-2011'},
         {'vasya': '3-06-1999'},
         {'mykola': '5-12-1555'},
         {'kapw': '30-01-1490'}]
weeks = {'Monday': [], 'Tuesday': [], 'Wednesday': [],
         'Thursday': [], 'Friday': [], 'Saturday': [], 'Sunday': []}

def get_birthdays_per_week(a):
    now = datetime.now()
    interval = timedelta(days=7)
    res = now + interval
    for i in a: 
        for k, v in i.items():
            x = datetime.strptime(v, '%d-%m-%Y')
            if (res.day or res.month) == (x.day or x.month):
                if res.day == 'Saturday' or 'Sunday':
                    weeks['Monday'].append(k)
                else:
                    weeks[res.strftime('%A')].append(k)

get_birthdays_per_week(users)

for k, v in weeks.items():
    if v:
        print(f'{k}: {", ".join(v)}')