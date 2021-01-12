from datetime import * 

def diffDate(x):
    try:
        now = datetime.date(datetime.now())
        x = x.split('-')
        x = date(int(x[0]),int(x[1]),int(x[2]))
        result = x - now
        result = result.days
        print('Date Now           : ', now)
        print('Date Given         : ', x)
        print('Difference of Days : ', result, 'days')
    except ValueError:
        result = False
    return result

diffDate('2021-01-13')