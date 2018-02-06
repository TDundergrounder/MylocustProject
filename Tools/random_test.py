# from random import randint
import datetime
import random

def random_date():
    y = random.randint(1999,datetime.datetime.now().year)
    m = random.randint(1,12)
    x = 1
    d = random.randint(1,x)
    if m<10:
        m = '0%s'%m
        if m == 2:
            if y%4 == 0:
                x = 29
            else:
                x = 28            
        else:
            if m == 4 or m ==6 or m == 9:
                x = 30
            else:
                x = 31
    else:
        if m == 11:
            x = 30
        else:
            x = 31    
    if d<10:
        d = '0%s'%d
    date = '%s%s%s'%(y,m,d)
    return date


def random_days():
    days = random.randint(1,366)
    return days


def random_PhoneNO():
    area_NO = ['187','186','159','158','155','153','152','139','138','137','135','132','131','130']
    area_Nu = choice(area_NO)
    seed="1234567890"
    sa = []
    for i in range(8):
        sa.append(choice(seed))
    lasteight_NO =''.join(sa)

    return area_Nu+lasteight_NO

def random_fromType():
    from_t = random.randint(1,2)
    print from_t
    return from_t

# def random_innName():
#     first_user = 'locustTester_'
#     seed = "1234567890"
#     sa = []
#     for i in range(2):
#         sa.append(choice(seed))
#         last_num = ''.join(sa)
#     return first_user + last_num

