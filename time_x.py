import datetime

def choose_plural(n, noun):
    if n % 10 == 1 and n % 100 != 11:
        res = noun[0]
    elif 1 < n % 10 < 5 and (n % 100 < 10 or n % 100 >= 20):
        res = noun[1]
    else:
        res = noun[2]
    return n, res

try:
    datetime_str = input('Введите дату/время в формате ДД.ММ.ГГГГ ЧЧ:ММ ')
    date_x = datetime.datetime.strptime(datetime_str, '%d.%m.%Y %H:%M')
    date_now = datetime.datetime.now().replace(second=0, microsecond=0)

    if date_x > date_now:
        delta = date_x - date_now
        days = delta.days
        hours = delta.seconds // 3600 % 24
        minutes = delta.seconds // 60 % 60
        res_d = choose_plural(days, ('день', 'дня', 'дней'))
        res_h = choose_plural(hours, ('час', 'часа', 'часов'))
        res_m = choose_plural(minutes, ('минута', 'минуты', 'минут'))
        if days:
            if hours:
                print(f'До часа "Икс" {res_d[0]} {res_d[1]} и {res_h[0]} {res_h[1]}')
            else:
                print(f'До часа "Икс" {res_d[0]} {res_d[1]}')
        elif hours:
            if minutes:
                print(f'До часа "Икс" {res_h[0]} {res_h[1]} и {res_m[0]} {res_m[1]}')
            else:
                print(f'До часа "Икс" {res_h[0]} {res_h[1]}')
        elif minutes:
            print(f'До часа "Икс" {res_m[0]} {res_m[1]}')
    else:
        print('Ошибка')

except ValueError:
    print('Ошибка')