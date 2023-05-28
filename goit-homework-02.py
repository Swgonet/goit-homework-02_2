from datetime import datetime, timedelta

weeks = {'Monday': [], 'Tuesday': [], 'Wednesday': [],
         'Thursday': [], 'Friday': [], 'Saturday': [], 'Sunday': []}

def result(s):
    for k, v in weeks.items():
        if v:
            print(f'{k}: {", ".join(v)}')

def get_birthdays_per_week(a):
    now = datetime.now()
    interval = timedelta(days=9)
    res = now + interval
    for i in a: 
        for k, v in i.items():
            x = datetime.strptime(v, '%d-%m-%Y')
            # print(res.day, res. month, x.day, x.month)
            if res.day == x.day and res.month == x.month:
                if res.strftime('%A') == 'Saturday' or res.strftime('%A') == 'Sunday':
                    weeks['Monday'].append(k)
                else:
                    weeks[res.strftime('%A')].append(k)
    return result(weeks)

x = get_birthdays_per_week([{"petro": '30-05-2011'},
         {'vasya': '4-06-1999'},
         {'mykola': '6-06-1575'},
         {'kapw': '5-06-1490'}])
print(x)
