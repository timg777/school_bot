#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from datetime import datetime
import time
import requests
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
import json
import re
import os
import sys
import traceback

classes = ['11А', '11Б', '11В', '11Г']
class_iter = ['11А.txt', '11Б.txt', '11В.txt', '11Г.txt']
weekdays = ['понедельник', 'вторник' , 'среда', 'четверг', 'пятница']
id_database = []

with open('data.txt', 'r') as inp:
    inp = inp.read().split()
    gr_id = inp[0]
    gr_name = inp[1]
    your_id = inp[2]
    gr_token = inp[3]
    changed_gr_id = inp[4]

def load_data():
    bot_session = vk_api.VkApi(
        token=gr_token)
    bot_api = bot_session.get_api()
    return bot_session, bot_api
bot_session, bot_api = load_data()

def bells(num, today):
    hour = datetime.now().hour + 5
    minute = datetime.now().minute
    if num == 1:
        if today:
            if hour == 8 and 40 > minute >= 0:
                return '\t\t\t\t\t\t\t\t\t\t\t[¶] 1 - [  8:00 - 8:40  ] '
            else:
                return '\t\t\t\t\t\t\t\t\t\t\t[ ] 1 - [  8:00 - 8:40  ] '

        else:
            return '\t\t\t\t\t\t\t\t\t\t\t[¶] 1 - [  8:00 - 8:40  ] '

    elif num == 1.5:
        if hour == 8 and 40 <= minute < 50:
            return 'shift -> [¶]'
        else:
            return 'shift -> [ ]'


    elif num == 2:
        if today:
            if (hour == 8 and minute >= 50) or (hour == 9 and 30 > minute > 0):
                return '\t\t\t\t\t\t\t\t\t\t\t[¶] 2 - [  8:50 - 9:30  ] '
            else:
                return '\t\t\t\t\t\t\t\t\t\t\t[ ] 2 - [  8:50 - 9:30  ] '
        else:
            return '\t\t\t\t\t\t\t\t\t\t\t[¶] 2 - [  8:50 - 9:30  ] '

    elif num == 2.5:
        if hour == 9 and 30 <= minute < 40:
            return 'shift -> [¶]'
        else:
            return 'shift -> [ ]'

    elif num == 3:
        if today:
            if (hour == 9 and minute >= 40) or (hour == 10 and 0 <= minute < 20):
                return '\t\t\t\t\t\t\t\t\t\t\t[¶] 3 - [ 9:40 - 10:20 ] '
            else:
                return '\t\t\t\t\t\t\t\t\t\t\t[ ] 3 - [ 9:40 - 10:20 ] '
        else:
            return '\t\t\t\t\t\t\t\t\t\t\t[¶] 3 - [ 9:40 - 10:20 ] '

    elif num == 3.5:
        if hour == 10 and 20 <= minute < 35:
            return 'shift -> [¶]'
        else:
            return 'shift -> [ ]'

    elif num == 4:
        if today:
            if (hour == 10 and minute >= 35) or (hour == 11 and 0 <= minute < 15):
                return '\t\t\t\t\t\t\t\t\t\t\t[¶] 4 - [10:35 - 11:15] '
            else:
                return '\t\t\t\t\t\t\t\t\t\t\t[ ] 4 - [10:35 - 11:15] '
        else:
            return '\t\t\t\t\t\t\t\t\t\t\t[¶] 4 - [10:35 - 11:15] '

    elif num == 4.5:
        if hour == 11 and 15 <= minute < 30:
            return 'shift -> [¶]'
        else:
            return 'shift -> [ ]'

    elif num == 5:
        if today:
            if (hour == 11 and minute >= 30) or (hour == 12 and 0 <= minute < 12):
                return '\t\t\t\t\t\t\t\t\t\t\t[¶] 5 - [11:30 - 12:10] '
            else:
                return '\t\t\t\t\t\t\t\t\t\t\t[ ] 5 - [11:30 - 12:10] '
        else:
            return '\t\t\t\t\t\t\t\t\t\t\t[¶] 5 - [11:30 - 12:10] '

    elif num == 5.5:
        if hour == 12 and 10 <= minute < 20:
            return 'shift -> [¶]'
        else:
            return 'shift -> [ ]'

    elif num == 6:
        if today:
            if hour == 12 and minute >= 20:
                return '\t\t\t\t\t\t\t\t\t\t\t[¶] 6 - [12:20 - 13:00] '
            else:
                return '\t\t\t\t\t\t\t\t\t\t\t[ ] 6 - [12:20 - 13:00] '
        else:
            return '\t\t\t\t\t\t\t\t\t\t\t[¶] 6 - [12:20 - 13:00] '

    elif num == 6.5:
        if hour == 13 and 0 <= minute < 5:
            return 'shift -> [¶]'
        else:
            return 'shift -> [ ]'

    elif num == 7:
        if today:
            if hour == 13 and 5 <= minute < 45:
                return '\t\t\t\t\t\t\t\t\t\t\t[¶] 7 - [13:05 - 13:45] '
            else:
                return '\t\t\t\t\t\t\t\t\t\t\t[ ] 7 - [13:05 - 13:45] '
        else:
            return '\t\t\t\t\t\t\t\t\t\t\t[¶] 7 - [13:05 - 13:45] '

    elif num == 7.5:
        if hour == 13 and 40 <= minute:
            return 'shift -> [¶]'
        else:
            return 'shift -> [ ]'

    elif num == 8:
        if today:
            if hour == 14 and 0 <= minute < 40:
                return '\t\t\t\t\t\t\t\t\t\t\t[¶] 8 - [14:00 - 14:40] '
            else:
                return '\t\t\t\t\t\t\t\t\t\t\t[ ] 8 - [14:00 - 14:0] '
        else:
            return '\t\t\t\t\t\t\t\t\t\t\t[¶] 8 - [14:00 - 14:40] '

class ALL_CLASSES_AND_FUNCTIONS:

    #def news(response, event):
        ##############################################################################################################################################

    def wr_id_database():

        global id_database

        with open('id_database.txt', 'r') as inp:
            inp = inp.readlines()
            id_database += inp

    def check_and_delete_hw():

            w = datetime.now().weekday()
            [os.system(f'python3 clear_home_dump.py {iter} {w}') for iter in class_iter]
            print('_HomeWork cleared_')
            os.system('python3 bot.py')

    def write_dumps(response, ANS, event):

        global weekdays, classes

        try:
            if response.split()[0] in classes and response.split()[1] in weekdays:
                with open('homewk_mess_dump.txt', 'a') as ouf:
                    ouf.writelines(ANS)
                    ouf.writelines('\n\n')
            else:
                with open('mess_dump.txt', 'a') as ouf:
                    ouf.writelines(ANS)
                    ouf.writelines('\n\n')
        except:
            with open('mess_dump.txt', 'a') as ouf:
                ouf.writelines(ANS)
                ouf.writelines('\n\n')
        print('-' * 45, '')

        id = str(event.obj['message']['from_id'])

        if response[:7].lower() == '/report' and response[7] == ' ':
            with open('report.txt', 'a') as ouf:
                ouf.write('[ ' + response[8:] + f' ]  |  id: {id} |  time: ' +  str(datetime.strftime(datetime.now(),  "%H:%M:%S  |  date: ")) +  f'{year}-{month}-{day}')
                ouf.write('\n\n')

    def check_files():

        if os.stat("11Б.txt").st_size != 0:

            with open('11Б.txt', 'r') as inp:
                FILE = inp.readlines()
                event = ''
                for elem in FILE:
                    try:
                        elem = elem.split()
                        class_ = '11Б'
                        weekday = elem[0]
                        subject = elem[1]
                        home_work = elem[2:-6]
                        str_home_work = ''
                        for item in home_work:
                            str_home_work += re.sub(',', ' ', item.replace("'", '').replace(']', '').replace('[', ''), 1)
                            str_home_work = re.sub(' ,', ', ', str_home_work)

                        response = f'{class_} {weekday} {subject} {str_home_work}'
                        ALL_CLASSES_AND_FUNCTIONS.home_work.write_homework(response, event, True)
                    except:
                        pass

        if os.stat("11А.txt").st_size != 0:

            with open('11А.txt', 'r') as inp:
                FILE = inp.readlines()
                event = ''
                for elem in FILE:
                    try:
                        elem = elem.split()
                        class_ = '11А'
                        weekday = elem[0]
                        subject = elem[1]
                        home_work = elem[2:-6]
                        str_home_work = ''
                        for item in home_work:
                            str_home_work += re.sub(',', ' ', item.replace("'", '').replace(']', '').replace('[', ''), 1)
                            str_home_work = re.sub(' ,', ', ', str_home_work)
                        response = f'{class_} {weekday} {subject} {str_home_work}'
                        ALL_CLASSES_AND_FUNCTIONS.home_work.write_homework(response, event, True)
                    except:
                        pass

        if os.stat("11В.txt").st_size != 0:

            with open('11В.txt', 'r') as inp:
                FILE = inp.readlines()
                event = ''
                for elem in FILE:
                    try:
                        elem = elem.split()
                        class_ = '11В'
                        weekday = elem[0]
                        subject = elem[1]
                        home_work = elem[2:-6]
                        str_home_work = ''
                        for item in home_work:
                            str_home_work += re.sub(',', ' ', item.replace("'", '').replace(']', '').replace('[', ''), 1)
                            str_home_work = re.sub(' ,', ', ', str_home_work)
                        response = f'{class_} {weekday} {subject} {str_home_work}'
                        ALL_CLASSES_AND_FUNCTIONS.home_work.write_homework(response, event, True)
                    except:
                        pass

        if os.stat("11Г.txt").st_size != 0:

            with open('11Г.txt', 'r') as inp:
                FILE = inp.readlines()
                event = ''
                for elem in FILE:
                    try:
                        elem = elem.split()
                        class_ = '11Г'
                        weekday = elem[0]
                        subject = elem[1]
                        home_work = elem[2:-6]
                        str_home_work = ''
                        for item in home_work:
                            str_home_work += re.sub(',', ' ', item.replace("'", '').replace(']', '').replace('[', ''), 1)
                            str_home_work = re.sub(' ,', ', ', str_home_work)
                        response = f'{class_} {weekday} {subject} {str_home_work}'
                        ALL_CLASSES_AND_FUNCTIONS.home_work.write_homework(response, event, True)
                    except:
                        pass

    def data():

        global start_
        global yes
        global start_lessons
        global monitor_bells_access
        global trap
        global kb_added
        global a11, b11, d11, g11
        global c
        global homework_B_11, homework_A_11, homework_V_11, homework_G_11

        start_ = False
        print('server started\n', '-' * 45, '\n')
        yes = True
        start_lessons = False
        monitor_bells_access = False
        trap = False
        kb_added = False
        c = 0
        a11, b11, d11, g11 = False, False, False, False
        homework_B_11 = {
            'понедельник': {
                'инфа': [],
                'литра': [],
                'обж': [],
                'физика': []
            },
            'вторник': {
                'химия': [],
                'русский': [],
                'матан': [],
                'био': [],
                'физика': []
            },
            'среда': {
                'история': [],
                'родной': [],
                'англ': [],
                'инфа': [],
                'матан': []
            },
            'четверг': {
                'англ': [],
                'физика': [],
                'общество': [],
                'матан': [],
            },
            'пятница': {
                'матан': [],
                'физика': [],
                'литра': [],
                'англ': [],
            }
        }
        homework_A_11 = {
            'понедельник': {
                'физика': [],
                'литра': [],
                'био': [],
                'матан': [],
                'англ': [],
            },
            'вторник': {
                'обж': [],
                'литра': [],
                'нем': [],
                'англ': [],
                'русский': [],
            },
            'среда': {
                'матан': [],
                'физика': [],
                'англ': [],
                'нем': [],
                'литра': [],
                'история': [],
                'родной': [],
            },
            'четверг': {
                'химия': [],
                'общество': [],
                'литра': [],
                'англ': [],
                'нем': [],
            },
            'пятница': {
                'русский': [],
                'матан': [],
                'литра': [],
                'англ': []
            }
        }
        homework_V_11 = {
            'понедельник': {
                'англ': [],
                'обж': [],
                'матан': [],
                'физика': [],
                'литра': [],
                'химия': [],
            },
            'вторник': {
                'история': [],
                'матан': [],
                'химия': [],
            },
            'среда': {
                'англ': [],
                'матан': [],
                'био': [],
                'русский': [],
                'литра': [],
                'физика': [],
            },
            'четверг': {
                'литра': [],
                'общество': [],
                'био': [],
                'история': [],
            },
            'пятница': {
                'общество': [],
                'химия': [],
                'англ': [],
                'матан': [],
            }
        }
        homework_G_11 = {
            'понедельник': {
                'химия': [],
                'био':[],
                'физика': [],
                'общество': [],
                'англ': []
            },
            'вторник': {
                'матан': [],
                'история': [],
                'литра': [],
                'русский': [],
                'родной': []
            },
            'среда': {
                'литра': [],
                'англ': [],
                'физика': [],
                'геогр': [],
                'матан': []
            },
            'четверг': {
                'англ': [],
                'литра': [],
                'русский': [],
                'история': [],
                'матан': []
            },
            'пятница': {
                'русский': [],
                'обж': [],
                'инфа': [],
                'общество': [],
                'матан': []
            }
        }

    class classes_:

        class B_11:

            def today(weekday, event, today):

                tab = '\t\t'
                year, day, month = datetime.now().year, datetime.now().day, datetime.now().month
                data = f'{year}-{month}-{day}'

                if weekday == 0:
                    ALL_CLASSES_AND_FUNCTIONS.keyboards.B_11_kb_1(event)
                    if today:
                        return f'{data},    ПОНЕДЕЛЬНИК\n\n{bells(1, today)} •|инфа|•\n{tab}{bells(1.5, today)}\n{bells(2, today)} •|инфа|•\n{tab}{bells(2.5, today)}\n{bells(3, today)} •|литра|•\n{tab}{bells(3.5, today)}\n{bells(4, today)} •|литра|•\n{tab}{bells(4.5, today)}\n{bells(5, today)} •|обж|•\n{tab}{bells(5.5, today)}\n{bells(6, today)}•|физика|•\n{tab}{bells(6.5, today)}\n{bells(7, today)} •|физика|•'
                    else:
                        return f'ПОНЕДЕЛЬНИК\n\n{bells(1, today)} •|инфа|•\n{bells(2, today)} •|инфа|•\n{bells(3, today)} •|литра|•\n{bells(4, today)} •|литра|•\n{bells(5, today)} •|обж|•\n{bells(6, today)}•|физика|•\n{bells(7, today)} •|физика|•'
                elif weekday == 1:
                    ALL_CLASSES_AND_FUNCTIONS.keyboards.B_11_kb_1(event)
                    if today:
                        return f'{data},    ВТОРНИК\n\n{bells(1, today)} •|химия|•\n{tab}{bells(1.5, today)}\n{bells(2, today)} •|рузге|•\n{tab}{bells(2.5, today)}\n{bells(3, today)} •|матан|•\n{tab}{bells(3.5, today)}\n{bells(4, today)} •|матан|•\n{tab}{bells(4.5, today)}\n{bells(5, today)} •|биолоджи|•\n{tab}{bells(5.5, today)}\n{bells(6, today)} •|физра|•'
                    else:
                        return f'ВТОРНИК\n\n{bells(1, today)} •|химия|•\n{bells(2, today)} •|рузге|•\n{bells(3, today)} •|матан|•\n{bells(4, today)} •|матан|•\n{bells(5, today)} •|биолоджи|•\n{bells(6, today)} •|физра|•'
                elif weekday == 2:
                    ALL_CLASSES_AND_FUNCTIONS.keyboards.B_11_kb_1(event)
                    if today:
                        return f'{data},    СРЕДА\n\n{bells(1, today)} •|история|•\n{tab}{bells(1.5, today)}\n{bells(2, today)} •|история|•\n{tab}{bells(2.5, today)}\n{bells(3, today)} •|родной|•\n{tab}{bells(3.5, today)}\n{bells(4, today)} •|англ|•\n{tab}{bells(4.5, today)}\n{bells(5, today)}•|инфа|•\n{tab}{bells(5.5, today)}\n{bells(6, today)} •|инфа|•\n{tab}{bells(6.5, today)}\n{bells(7, today)} •|матан|•'
                    else:
                        return f'СРЕДА\n\n{bells(1, today)} •|история|•\n{bells(2, today)} •|история|•\n{bells(3, today)} •|родной|•\n{bells(4, today)} •|англ|•\n{bells(5, today)}•|инфа|•\n{bells(6, today)} •|инфа|•\n{bells(7, today)} •|матан|•'
                elif weekday == 3:
                    ALL_CLASSES_AND_FUNCTIONS.keyboards.B_11_kb_1(event)
                    if today:
                        return f'{data},    ЧЕТВЕРГ\n\n{bells(1, today)} •|англ|•\n{tab}{bells(1.5, today)}\n{bells(2, today)} •|физика|•\n{tab}{bells(2.5, today)}\n{bells(3, today)} •|общество|•\n{tab}{bells(3.5, today)}\n{bells(4, today)} •|матан|•\n{tab}{bells(4.5, today)}\n{bells(5, today)} •|матан|•\n{tab}{bells(5.5, today)}\n{bells(6, today)} •|физра|•\n{tab}{bells(6.5, today)}\n{bells(7, today)} •|общество|•'
                    else:
                        return f'ЧЕТВЕРГ\n\n{bells(1, today)} •|англ|•\n{bells(2, today)} •|физика|•\n{bells(3, today)} •|общество|•\n{bells(4, today)} •|матан|•\n{bells(5, today)} •|матан|•\n{bells(6, today)} •|физра|•\n{bells(7, today)} •|общество|•'
                elif weekday == 4:
                    ALL_CLASSES_AND_FUNCTIONS.keyboards.B_11_kb_1(event)
                    if today:
                        return f'{data},    ПЯТНИЦА\n\n{bells(1, today)} •|матан|•\n{tab}{bells(1.5, today)}\n{bells(2, today)} •|матан|•\n{tab}{bells(2.5, today)}\n{bells(3, today)} •|физика|•\n{tab}{bells(3.5, today)}\n{bells(4, today)} •|физика|•\n{tab}{bells(4.5, today)}\n{bells(5, today)} •|англ|•\n{tab}{bells(5.5, today)}\n{bells(6, today)} •|литра|•\n{tab}{bells(6.5, today)}\n{bells(7, today)} •|физра|•'
                    else:
                        return f'ПЯТНИЦА\n\n{bells(1, today)} •|матан|•\n{bells(2, today)} •|матан|•\n{bells(3, today)} •|физика|•\n{bells(4, today)} •|физика|•\n{bells(5, today)} •|англ|•\n{bells(6, today)} •|литра|•\n{bells(7, today)} •|физра|•'
                elif weekday == 5:
                    ALL_CLASSES_AND_FUNCTIONS.keyboards.B_11_kb_1(event)
                    return f'дожить бы до этого дня без расписания :('

                elif weekday == 6:
                    ALL_CLASSES_AND_FUNCTIONS.keyboards.B_11_kb_1(event)
                    return f'сон никто не отменял в воскресенье :)'

            def tomorrow(weekday, event, today):

                if weekday == 7:
                    return ALL_CLASSES_AND_FUNCTIONS.classes_.B_11.today(0, event, today)
                else:
                    return ALL_CLASSES_AND_FUNCTIONS.classes_.B_11.today(weekday, event, today)

        class A_11:

            def today(weekday, event, today):

                tab = '\t\t'
                year, day, month = datetime.now().year, datetime.now().day, datetime.now().month
                data = f'{year}-{month}-{day}'

                if weekday == 0:
                    ALL_CLASSES_AND_FUNCTIONS.keyboards.A_11_kb_1(event)
                    if today:
                        return f'{data},    ПОНЕДЕЛЬНИК\n\n{bells(1, today)} •| - |•\n{tab}{bells(1.5, today)}\n{bells(2, today)} •|литра|•\n{tab}{bells(2.5, today)}\n{bells(3, today)} •|биология|•\n{tab}{bells(3.5, today)}\n{bells(4, today)} •|матан|•\n{tab}{bells(4.5, today)}\n{bells(5, today)} •|физика|•\n{tab}{bells(5.5, today)}\n{bells(6, today)} •|англ|•\n{tab}{bells(6.5, today)}\n{bells(7, today)} •|англ|•'
                    else:
                        return f'ПОНЕДЕЛЬНИК\n\n{bells(1, today)} •| - |•\n{bells(2, today)} •|литра|•\n{bells(3, today)} •|биология|•\n{bells(4, today)} •|матан|•\n{bells(5, today)} •|физика|•\n{bells(6, today)} •|англ|•\n{bells(7, today)} •|англ|•'

                elif weekday == 1:
                    ALL_CLASSES_AND_FUNCTIONS.keyboards.A_11_kb_1(event)
                    if today:
                        return f'{data},    ВТОРНИК\n\n{bells(1, today)} •|родной|• \n{tab}{bells(1.5, today)}\n{bells(2, today)} •|обж|•\n{tab}{bells(2.5, today)}\n{bells(3, today)} •|литра|•\n{tab}{bells(3.5, today)}\n{bells(4, today)} •|литра|•\n{tab}{bells(4.5, today)}\n{bells(5, today)} •|англ/нем|•\n{tab}{bells(5.5, today)}\n{bells(6, today)} •|русский|•\n{tab}{bells(6.5, today)}\n{bells(7, today)} •|физра|•'
                    else:
                        return f'ВТОРНИК\n\n{bells(1, today)} •|родной|• \n{bells(2, today)} •|обж|•\n{bells(3, today)} •|литра|•\n{bells(4, today)} •|литра|•\n{bells(5, today)} •|англ/нем|•\n{bells(6, today)} •|русский|•\n{bells(7, today)} •|физра|•'

                elif weekday == 2:
                    ALL_CLASSES_AND_FUNCTIONS.keyboards.A_11_kb_1(event)
                    if today:
                        return f'{data},    СРЕДА\n\n{bells(1, today)} •|матан|•\n{tab}{bells(1.5, today)}\n{bells(2, today)} •|физика|•\n{tab}{bells(2.5, today)}\n{bells(3, today)} •|англ/нем|•\n{tab}{bells(3.5, today)}\n{bells(4, today)} •|русский|•\n{tab}{bells(4.5, today)}\n{bells(5, today)} •|история|•\n{tab}{bells(5.5, today)}\n{bells(6, today)} •|история|•\n{tab}{bells(6.5, today)}\n{bells(7, today)} •|родной|•'
                    else:
                        return f'СРЕДА\n\n{bells(1, today)} •|матан|•\n{bells(2, today)} •|физика|•\n{bells(3, today)} •|англ/нем|•\n{bells(4, today)} •|русский|•\n{bells(5, today)} •|история|•\n{bells(6, today)} •|история|•\n{bells(7, today)} •|родной|•'

                elif weekday == 3:
                    ALL_CLASSES_AND_FUNCTIONS.keyboards.A_11_kb_1(event)
                    if today:
                        return f'{data},    ЧЕТВЕРГ\n\n{bells(1, today)} •|химия|•\n{tab}{bells(1.5, today)}\n{bells(2, today)} •|общество|•\n{tab}{bells(2.5, today)}\n{bells(3, today)} •|литра|•\n{tab}{bells(3.5, today)}\n{bells(4, today)} •|общество|•\n{tab}{bells(4.5, today)}\n{bells(5, today)} •|физра|•\n{tab}{bells(5.5, today)}\n{bells(6, today)} •|англ/нем|•\n{tab}{bells(6.5, today)}\n{bells(7, today)} •|англ/нем|•'
                    else:
                        return f'ЧЕТВЕРГ\n\n{bells(1, today)} •|химия|•\n{bells(2, today)} •|общество|•\n{bells(3, today)} •|литра|•\n{bells(4, today)} •|общество|•\n{bells(5, today)} •|физра|•\n{bells(6, today)} •|англ/нем|•\n{bells(7, today)} •|англ/нем|•'

                elif weekday == 4:
                    ALL_CLASSES_AND_FUNCTIONS.keyboards.A_11_kb_1(event)
                    if today:
                        return f'{data},    ПЯТНИЦА\n\n{bells(1, today)} •|литра|•\n{tab}{bells(1.5, today)}\n{bells(2, today)} •|матан|•\n{tab}{bells(2.5, today)}\n{bells(3, today)} •|литра|•\n{tab}{bells(3.5, today)}\n{bells(4, today)} •|матан|•\n{tab}{bells(4.5, today)}\n{bells(5, today)} •|физра|•\n{tab}{bells(5.5, today)}\n{bells(6, today)} •|англ|•\n{tab}{bells(6.5, today)}\n{bells(7, today)} •|англ|•'
                    else:
                        return f'ПЯТНИЦА\n\n{bells(1, today)} •|литра|•\n{bells(2, today)} •|матан|•\n{bells(3, today)} •|литра|•\n{bells(4, today)} •|матан|•\n{bells(5, today)} •|физра|•\n{bells(6, today)} •|англ|•\n{bells(7, today)} •|англ|•'

                elif weekday == 5:
                    ALL_CLASSES_AND_FUNCTIONS.keyboards.A_11_kb_1(event)
                    return f'дожить бы до этого дня без расписания :('

                elif weekday == 6:
                    ALL_CLASSES_AND_FUNCTIONS.keyboards.A_11_kb_1(event)
                    return f'сон никто не отменял в воскресенье :)'

            def tomorrow(weekday, event, today):

                if weekday == 7:
                    return ALL_CLASSES_AND_FUNCTIONS.classes_.A_11.today(0, event, today)
                else:
                    return ALL_CLASSES_AND_FUNCTIONS.classes_.A_11.today(weekday, event, today)

        class V_11:

            def today(weekday, event, today):

                tab = '\t\t'
                year, day, month = datetime.now().year, datetime.now().day, datetime.now().month
                data = f'{year}-{month}-{day}'

                if weekday == 0:
                    ALL_CLASSES_AND_FUNCTIONS.keyboards.V_11_kb_1(event)
                    if today:
                        return f'{data},    ПОНЕДЕЛЬНИК\n\n{bells(1, today)} •|англ|•\n{tab}{bells(1.5, today)}\n{bells(2, today)} •|обж|•\n{tab}{bells(2.5, today)}\n{bells(3, today)} •|матан|•\n{tab}{bells(3.5, today)}\n{bells(4, today)} •|физика|•\n{tab}{bells(4.5, today)}\n{bells(5, today)} •|литра|•\n{tab}{bells(5.5, today)}\n{bells(6, today)} •|литра|•\n{tab}{bells(6.5, today)}\n{bells(7, today)} •|химия|•'
                    else:
                        return f'ПОНЕДЕЛЬНИК\n\n{bells(1, today)} •|англ|•\n{bells(2, today)} •|обж|•\n{bells(3, today)} •|матан|•\n{bells(4, today)} •|физика|•\n{bells(5, today)} •|литра|•\n{bells(6, today)} •|литра|•\n{bells(7, today)} •|химия|•'

                elif weekday == 1:
                    ALL_CLASSES_AND_FUNCTIONS.keyboards.V_11_kb_1(event)
                    if today:
                        return f'{data},    ВТОРНИК\n\n{bells(1, today)} •|история|• \n{tab}{bells(1.5, today)}\n{bells(2, today)} •|матан|•\n{tab}{bells(2.5, today)}\n{bells(3, today)} •|матан|•\n{tab}{bells(3.5, today)}\n{bells(4, today)} •|химия|•\n{tab}{bells(4.5, today)}\n{bells(5, today)} •|химия|•\n{tab}{bells(5.5, today)}\n{bells(6, today)} •|физра|•'
                    else:
                        return f'ВТОРНИК\n\n{bells(1, today)} •|история|• \n{bells(2, today)} •|матан|•\n{bells(3, today)} •|матан|•\n{bells(4, today)} •|химия|•\n{bells(5, today)} •|химия|•\n{bells(6, today)} •|физра|•'

                elif weekday == 2:
                    ALL_CLASSES_AND_FUNCTIONS.keyboards.V_11_kb_1(event)
                    if today:
                        return f'{data},    СРЕДА\n\n{bells(1, today)} •|англ|•\n{tab}{bells(1.5, today)}\n{bells(2, today)} •|матан|•\n{tab}{bells(2.5, today)}\n{bells(3, today)} •|био|•\n{tab}{bells(3.5, today)}\n{bells(4, today)} •|био|•\n{tab}{bells(4.5, today)}\n{bells(5, today)} •|русский|•\n{tab}{bells(5.5, today)}\n{bells(6, today)} •|литра|•\n{tab}{bells(6.5, today)}\n{bells(7, today)} •|физика|•'
                    else:
                        return f'СРЕДА\n\n{bells(1, today)} •|англ|•\n{bells(2, today)} •|матан|•\n{bells(3, today)} •|био|•\n{bells(4, today)} •|био|•\n{bells(5, today)} •|русский|•\n{bells(6, today)} •|литра|•\n{bells(7, today)} •|физика|•'

                elif weekday == 3:
                    ALL_CLASSES_AND_FUNCTIONS.keyboards.V_11_kb_1(event)
                    if today:
                        return f'{data},    ЧЕТВЕРГ\n\n{bells(1, today)} •|литра|•\n{tab}{bells(1.5, today)}\n{bells(2, today)} •|литра|•\n{tab}{bells(2.5, today)}\n{bells(3, today)} •|общество|•\n{tab}{bells(3.5, today)}\n{bells(4, today)} •|био|•\n{tab}{bells(4.5, today)}\n{bells(5, today)} •|био|•\n{tab}{bells(5.5, today)}\n{bells(6, today)} •|физра|•\n{tab}{bells(6.5, today)}\n{bells(7, today)} •|история|•'
                    else:
                        return f'ЧЕТВЕРГ\n\n{bells(1, today)} •|литра|•\n{bells(2, today)} •|литра|•\n{bells(3, today)} •|общество|•\n{bells(4, today)} •|био|•\n{bells(5, today)} •|био|•\n{bells(6, today)} •|физра|•\n{bells(7, today)} •|история|•'

                elif weekday == 4:
                    ALL_CLASSES_AND_FUNCTIONS.keyboards.V_11_kb_1(event)
                    if today:
                        return f'{data},    ПЯТНИЦА\n\n{bells(1, today)} •|общество|•\n{tab}{bells(1.5, today)}\n{bells(2, today)} •|химия|•\n{tab}{bells(2.5, today)}\n{bells(3, today)} •|химия|•\n{tab}{bells(3.5, today)}\n{bells(4, today)} •|англ|•\n{tab}{bells(4.5, today)}\n{bells(5, today)} •|матан|•\n{tab}{bells(5.5, today)}\n{bells(6, today)} •|матан|•\n{tab}{bells(6.5, today)}\n{bells(7, today)} •|физра|•'
                    else:
                        return f'ПЯТНИЦА\n\n{bells(1, today)} •|общество|•\n{bells(2, today)} •|химия|•\n{bells(3, today)} •|химия|•\n{bells(4, today)} •|англ|•\n{bells(5, today)} •|матан|•\n{bells(6, today)} •|матан|•\n{bells(7, today)} •|физра|•'

                elif weekday == 5:
                    ALL_CLASSES_AND_FUNCTIONS.keyboards.V_11_kb_1(event)
                    return f'дожить бы до этого дня без расписания :('

                elif weekday == 6:
                    ALL_CLASSES_AND_FUNCTIONS.keyboards.V_11_kb_1(event)
                    return f'сон никто не отменял в воскресенье :)'

            def tomorrow(weekday, event, today):

                if weekday == 7:
                    return ALL_CLASSES_AND_FUNCTIONS.classes_.V_11.today(0, event, today)
                else:
                    return ALL_CLASSES_AND_FUNCTIONS.classes_.V_11.today(weekday, event, today)

        class G_11:

            def today(weekday, event, today):

                tab = '\t\t'
                year, day, month = datetime.now().year, datetime.now().day, datetime.now().month
                data = f'{year}-{month}-{day}'

                if weekday == 0:
                    ALL_CLASSES_AND_FUNCTIONS.keyboards.G_11_kb_1(event)
                    if today:
                        return f'{data},    ПОНЕДЕЛЬНИК\n\n{bells(1, today)} •|химия|•\n{tab}{bells(1.5, today)}\n{bells(2, today)} •|био|•\n{tab}{bells(2.5, today)}\n{bells(3, today)} •|физика|•\n{tab}{bells(3.5, today)}\n{bells(4, today)} •|общество|•\n{tab}{bells(4.5, today)}\n{bells(5, today)} •|англ|•\n{tab}{bells(5.5, today)}\n{bells(6, today)} •|общество|•\n{tab}{bells(6.5, today)}\n{bells(7, today)} •|физра|•'
                    else:
                        return f'ПОНЕДЕЛЬНИК\n\n{bells(1, today)} •|химия|•\n{bells(2, today)} •|био|•\n{bells(3, today)} •|физика|•\n{bells(4, today)} •|общество|•\n{bells(5, today)} •|англ|•\n{bells(6, today)} •|общество|•\n{bells(7, today)} •|физра|•'

                elif weekday == 1:
                    ALL_CLASSES_AND_FUNCTIONS.keyboards.G_11_kb_1(event)
                    if today:
                        return f'{data},    ВТОРНИК\n\n{bells(1, today)} •|матан|• \n{tab}{bells(1.5, today)}\n{bells(2, today)} •|матан|•\n{tab}{bells(2.5, today)}\n{bells(3, today)} •|история|•\n{tab}{bells(3.5, today)}\n{bells(4, today)} •|история|•\n{tab}{bells(4.5, today)}\n{bells(5, today)} •|литра|•\n{tab}{bells(5.5, today)}\n{bells(6, today)} •|руссиий|•\n{tab}{bells(6.5, today)}\n{bells(7, today)} •|родной|•'
                    else:
                        return f'ВТОРНИК\n\n{bells(1, today)} •|матан|• \n{bells(2, today)} •|матан|•\n{bells(3, today)} •|история|•\n{bells(4, today)} •|история|•\n{bells(5, today)} •|литра|•\n{bells(6, today)} •|руссиий|•\n{bells(6, today)} •|родной|•'

                elif weekday == 2:
                    ALL_CLASSES_AND_FUNCTIONS.keyboards.G_11_kb_1(event)
                    if today:
                        return f'{data},    СРЕДА\n\n{bells(1, today)} •|литра|•\n{tab}{bells(1.5, today)}\n{bells(2, today)} •|англ|•\n{tab}{bells(2.5, today)}\n{bells(3, today)} •|физика|•\n{tab}{bells(3.5, today)}\n{bells(4, today)} •|география|•\n{tab}{bells(4.5, today)}\n{bells(5, today)} •|матан|•\n{tab}{bells(5.5, today)}\n{bells(6, today)} •|матан|•\n{tab}{bells(6.5, today)}\n{bells(7, today)} •|физра|•'
                    else:
                        return f'СРЕДА\n\n{bells(1, today)} •|литра|•\n{bells(2, today)} •|англ|•\n{bells(3, today)} •|физика|•\n{bells(4, today)} •|география|•\n{bells(5, today)} •|матан|•\n{bells(6, today)} •|матан|•\n{bells(7, today)} •|физра|•'

                elif weekday == 3:
                    ALL_CLASSES_AND_FUNCTIONS.keyboards.G_11_kb_1(event)
                    if today:
                        return f'{data},    ЧЕТВЕРГ\n\n {tab*13}[-None-]{tab*4}•| None |•\n{tab}{bells(1.5, today)}\n{bells(2, today)} •|англ|•\n{tab}{bells(2.5, today)}\n{bells(3, today)} •|литра|•\n{tab}{bells(3.5, today)}\n{bells(4, today)} •|русский|•\n{tab}{bells(4.5, today)}\n{bells(5, today)} •|история|•\n{tab}{bells(5.5, today)}\n{bells(6, today)} •|матан|•\n{tab}{bells(6.5, today)}\n{bells(7, today)} •|матан|•'
                    else:
                        return f'ЧЕТВЕРГ\n\n {tab*13}[-None-]{tab*4}•| None |•\n{bells(2, today)} •|англ|•\n{bells(3, today)} •|литра|•\n{bells(4, today)} •|русский|•\n{bells(5, today)} •|история|•\n{bells(6, today)} •|матан|•\n{bells(7, today)} •|матан|•'

                elif weekday == 4:
                    ALL_CLASSES_AND_FUNCTIONS.keyboards.G_11_kb_1(event)
                    if today:
                        return f'{data},    ПЯТНИЦА\n\n{bells(1, today)} •|русский|•\n{tab}{bells(1.5, today)}\n{bells(2, today)} •|обж|•\n{tab}{bells(2.5, today)}\n{bells(3, today)} •|инфа|•\n{tab}{bells(3.5, today)}\n{bells(4, today)} •|инфа|•\n{tab}{bells(4.5, today)}\n{bells(5, today)} •|общество|•\n{tab}{bells(5.5, today)}\n{bells(6, today)} •|физра|•\n{tab}{bells(6.5, today)}\n{bells(7, today)} •|матан|•\n{tab}{bells(7.5, today)}\n{bells(8, today)} •|физра|•'
                    else:
                        return f'ПЯТНИЦА\n\n{bells(1, today)} •|русский|•\n{bells(2, today)} •|обж|•\n{bells(3, today)} •|инфа|•\n{bells(4, today)} •|инфа|•\n{bells(5, today)} •|общество|•\n{bells(6, today)} •|физра|•\n{bells(7, today)} •|матан|•\n{bells(8, today)} •|физра|•'

                elif weekday == 5:
                    ALL_CLASSES_AND_FUNCTIONS.keyboards.G_11_kb_1(event)
                    return f'дожить бы до этого дня без расписания :('

                elif weekday == 6:
                    ALL_CLASSES_AND_FUNCTIONS.keyboards.G_11_kb_1(event)
                    return f'сон никто не отменял в воскресенье :)'

            def tomorrow(weekday, event, today):

                if weekday == 7:
                    return ALL_CLASSES_AND_FUNCTIONS.classes_.G_11.today(0, event, today)
                else:
                    return ALL_CLASSES_AND_FUNCTIONS.classes_.G_11.today(weekday, event, today)

    class main:

        def data(response, obj):
            weekday, year, day, month = datetime.now().weekday(), datetime.now().year, datetime.now().day, datetime.now().month

            print('received at : ' + str(datetime.strftime(datetime.now(), "%H:%M:%S |")), f'{year}-{month}-{day}')
            print(response, '<-- <-- <-- user received message')
            print(obj, '<-- <-- <-- user id')

        def get_button(label, color, payload=""):
            return {
                'action': {
                    'type': 'text',
                    'payload': json.dumps(payload),
                    'label': label
                },
                'color': color
            }

        def add_kb(keyboard, mon):
            keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
            keyboard = str(keyboard.decode('utf-8'))
            if int(mon) == 7:
                ALL_CLASSES_AND_FUNCTIONS.main.send_keyboard(event.obj['message']['peer_id'], keyboard, '[ ∆ Main_menu ∆! ]')

        def send_keyboard(peer_id, keyboard, message):
            bot_api.messages.send(
                peer_id=peer_id,
                message=message,
                keyboard=keyboard,
                random_id=get_random_id(),
            )

        def main_kb(yes):
            ALL_CLASSES_AND_FUNCTIONS.main.add_kb(yes)

        def kill_kb(yes):
            keyboard = {
                'one_time': True,
                'buttons': [
                ]
            }

            keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
            keyboard = str(keyboard.decode('utf-8'))
            killed_kb = True
            ALL_CLASSES_AND_FUNCTIONS.main.send_keyboard(event.obj['message']['peer_id'], keyboard, 'Keyboard killed!')
            ALL_CLASSES_AND_FUNCTIONS.main.send_keyboard(event.obj['message']['peer_id'], keyboard,
                               '[\t\t/update\t\t] \t\tyour bot to resurrect keyboard.')

        def send_message(peer_id, message):
            bot_api.messages.send(
                peer_id=peer_id,
                message=message,
                random_id=get_random_id()
            )

    class keyboards:

        def B_11_kb_1(event):

            keyboard = {
                'one_time': False,
                'buttons': [
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11Б] - НА СЕГОДНЯ - [11Б]", color='secondary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11Б] - НА ЗАВТРА - [11Б]", color='secondary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11Б] - НА ОПРЕДЕЛЁННЫЙ ДЕНЬ - [11Б]", color='default')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11Б] - ДЗ - [11Б]", color='positive')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label='[11Б] - ВЫБРАТЬ ДРУГОЙ КЛАСС - [11Б]', color='negative')]
                ],
                'inline': False
            }

            keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
            keyboard = str(keyboard.decode('utf-8'))

            ALL_CLASSES_AND_FUNCTIONS.main.send_keyboard(event.obj['message']['peer_id'], keyboard, '< Choose schedule type! >')

        def B_11_kb_2(event):

            keyboard = {
                'one_time': False,
                'buttons': [
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11Б] - ПОНЕДЕЛЬНИК - [11Б]", color='primary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11Б] - ВТОРНИК - [11Б]", color='primary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11Б] - СРЕДА - [11Б]", color='primary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label='[11Б] - ЧЕТВЕРГ - [11Б]', color='primary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label='[11Б] - ПЯТНИЦА - [11Б]', color='primary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label='[11Б] - ВЫБРАТЬ ДРУГОЙ КЛАСС - [11Б]', color='negative')]
                ],
                'inline': False
            }

            keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
            keyboard = str(keyboard.decode('utf-8'))

            ALL_CLASSES_AND_FUNCTIONS.main.send_keyboard(event.obj['message']['peer_id'], keyboard, '< Choose any day! >')

        def B_11_kb_3(event):

            keyboard = {
                'one_time': False,
                'buttons': [
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11Б] - НА ПОНЕДЕЛЬНИК - [11Б]", color='primary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11Б] - НА ВТОРНИК - [11Б]", color='primary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11Б] - НА СРЕДУ - [11Б]", color='primary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label='[11Б] - НА ЧЕТВЕРГ - [11Б]', color='primary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label='[11Б] - НА ПЯТНИЦУ - [11Б]', color='primary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label='[11Б] - НАЗАД - [11Б]', color='negative')]
                ],
                'inline': False
            }

            keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
            keyboard = str(keyboard.decode('utf-8'))

            ALL_CLASSES_AND_FUNCTIONS.main.send_keyboard(event.obj['message']['peer_id'], keyboard, '< Choose any day! >')

        def A_11_kb_1(event):

            keyboard = {
                'one_time': False,
                'buttons': [
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11А] - НА СЕГОДНЯ - [11А]", color='secondary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11А] - НА ЗАВТРА - [11А]", color='secondary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11А] - НА ОПРЕДЕЛЁННЫЙ ДЕНЬ - [11А]", color='default')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11А] - ДЗ - [11А]", color='positive')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label='[11А] - ВЫБРАТЬ ДРУГОЙ КЛАСС - [11А]', color='negative')]
                ],
                'inline': False
            }

            keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
            keyboard = str(keyboard.decode('utf-8'))

            ALL_CLASSES_AND_FUNCTIONS.main.send_keyboard(event.obj['message']['peer_id'], keyboard, '< Choose schedule type! >')

        def A_11_kb_2(event):

            keyboard = {
                'one_time': False,
                'buttons': [
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11А] - ПОНЕДЕЛЬНИК - [11А]", color='primary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11А] - ВТОРНИК - [11А]", color='primary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11А] - СРЕДА - [11А]", color='primary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label='[11А] - ЧЕТВЕРГ - [11А]', color='primary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label='[11А] - ПЯТНИЦА - [11А]', color='primary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label='[11А] - ВЫБРАТЬ ДРУГОЙ КЛАСС - [11А]', color='negative')]
                ],
                'inline': False
            }

            keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
            keyboard = str(keyboard.decode('utf-8'))

            ALL_CLASSES_AND_FUNCTIONS.main.send_keyboard(event.obj['message']['peer_id'], keyboard, '< Choose any day! >')

        def A_11_kb_3(event):

            keyboard = {
                'one_time': False,
                'buttons': [
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11А] - НА ПОНЕДЕЛЬНИК - [11А]", color='primary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11А] - НА ВТОРНИК - [11А]", color='primary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11А] - НА СРЕДУ - [11А]", color='primary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label='[11А] - НА ЧЕТВЕРГ - [11А]', color='primary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label='[11А] - НА ПЯТНИЦУ - [11А]', color='primary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label='[11А] - НАЗАД - [11А]', color='negative')]
                ],
                'inline': False
            }

            keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
            keyboard = str(keyboard.decode('utf-8'))

            ALL_CLASSES_AND_FUNCTIONS.main.send_keyboard(event.obj['message']['peer_id'], keyboard, '< Choose any day! >')

        def V_11_kb_1(event):

            keyboard = {
                'one_time': False,
                'buttons': [
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11В] - НА СЕГОДНЯ - [11В]", color='secondary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11В] - НА ЗАВТРА - [11В]", color='secondary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11В] - НА ОПРЕДЕЛЁННЫЙ ДЕНЬ - [11В]", color='default')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11В] - ДЗ - [11В]", color='positive')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label='[11В] - ВЫБРАТЬ ДРУГОЙ КЛАСС - [11В]', color='negative')]
                ],
                'inline': False
            }

            keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
            keyboard = str(keyboard.decode('utf-8'))

            ALL_CLASSES_AND_FUNCTIONS.main.send_keyboard(event.obj['message']['peer_id'], keyboard, '< Choose schedule type! >')

        def V_11_kb_2(event):

            keyboard = {
                'one_time': False,
                'buttons': [
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11В] - ПОНЕДЕЛЬНИК - [11В]", color='primary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11В] - ВТОРНИК - [11В]", color='primary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11В] - СРЕДА - [11В]", color='primary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label='[11В] - ЧЕТВЕРГ - [11В]', color='primary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label='[11В] - ПЯТНИЦА - [11В]', color='primary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label='[11В] - ВЫБРАТЬ ДРУГОЙ КЛАСС - [11В]', color='negative')]
                ],
                'inline': False
            }

            keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
            keyboard = str(keyboard.decode('utf-8'))

            ALL_CLASSES_AND_FUNCTIONS.main.send_keyboard(event.obj['message']['peer_id'], keyboard, '< Choose any day! >')

        def V_11_kb_3(event):

            keyboard = {
                'one_time': False,
                'buttons': [
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11В] - НА ПОНЕДЕЛЬНИК - [11В]", color='primary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11В] - НА ВТОРНИК - [11В]", color='primary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11В] - НА СРЕДУ - [11В]", color='primary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label='[11В] - НА ЧЕТВЕРГ - [11В]', color='primary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label='[11В] - НА ПЯТНИЦУ - [11В]', color='primary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label='[11В] - НАЗАД - [11В]', color='negative')]
                ],
                'inline': False
            }

            keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
            keyboard = str(keyboard.decode('utf-8'))

            ALL_CLASSES_AND_FUNCTIONS.main.send_keyboard(event.obj['message']['peer_id'], keyboard, '< Choose any day! >')

        def G_11_kb_1(event):

            keyboard = {
                'one_time': False,
                'buttons': [
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11Г] - НА СЕГОДНЯ - [11Г]", color='secondary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11Г] - НА ЗАВТРА - [11Г]", color='secondary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11Г] - НА ОПРЕДЕЛЁННЫЙ ДЕНЬ - [11Г]", color='default')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11Г] - ДЗ - [11Г]", color='positive')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label='[11Г] - ВЫБРАТЬ ДРУГОЙ КЛАСС - [11Г]', color='negative')]
                ],
                'inline': False
            }

            keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
            keyboard = str(keyboard.decode('utf-8'))

            ALL_CLASSES_AND_FUNCTIONS.main.send_keyboard(event.obj['message']['peer_id'], keyboard, '< Choose schedule type! >')

        def G_11_kb_2(event):

            keyboard = {
                'one_time': False,
                'buttons': [
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11Г] - ПОНЕДЕЛЬНИК - [11Г]", color='primary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11Г] - ВТОРНИК - [11Г]", color='primary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11Г] - СРЕДА - [11Г]", color='primary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label='[11Г] - ЧЕТВЕРГ - [11Г]', color='primary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label='[11Г] - ПЯТНИЦА - [11Г]', color='primary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label='[11Г] - ВЫБРАТЬ ДРУГОЙ КЛАСС - [11Г]', color='negative')]
                ],
                'inline': False
            }

            keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
            keyboard = str(keyboard.decode('utf-8'))

            ALL_CLASSES_AND_FUNCTIONS.main.send_keyboard(event.obj['message']['peer_id'], keyboard, '< Choose any day! >')

        def G_11_kb_3(event):

            keyboard = {
                'one_time': False,
                'buttons': [
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11Г] - НА ПОНЕДЕЛЬНИК - [11Г]", color='primary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11Г] - НА ВТОРНИК - [11Г]", color='primary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11Г] - НА СРЕДУ - [11Г]", color='primary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label='[11Г] - НА ЧЕТВЕРГ - [11Г]', color='primary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label='[11Г] - НА ПЯТНИЦУ - [11Г]', color='primary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label='[11Г] - НАЗАД - [11Г]', color='negative')]
                ],
                'inline': False
            }

            keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
            keyboard = str(keyboard.decode('utf-8'))

            ALL_CLASSES_AND_FUNCTIONS.main.send_keyboard(event.obj['message']['peer_id'], keyboard, '< Choose any day! >')

    class monitor:

        def monitor_bells_one_time(event, weekday):

            global start_lessons
            hour = datetime.now().hour + 5
            minute = datetime.now().minute + 2
            weekday = datetime.now().weekday()

            if (((13 > hour >= 8 and 59 <= minute <= 0) or (hour == 13 and 0 <= minute <= 45)) and 0 <= weekday < 4) or (weekday == 4 and ((8 <= hour < 14 and 0 <= minute <= 59) or (hour == 14 and 0 <= minute <= 40))):
                start_lessons = True

            elif hour >= 13 and minute >= 45:
                start_lessons = False

            if not start_lessons:
                if 60 - minute < 10:
                    minute = '0' + str(60 - minute)

                    if abs((23 - hour) + 8) < 24:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До начала уроков осталось\n              [ ' + str(abs((23 - hour) + 8)) + ' ч -  ' + minute + ' мин ]')
                    else:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До начала уроков осталось\n              [ ' + str(abs(7 - hour)) + ' ч -  ' + minute + ' мин ]')
                else:
                    if abs((23 - hour) + 8) < 24:

                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До начала уроков осталось\n              [ ' + str(abs((23 - hour) + 8)) + ' ч -  ' + str(60 - minute) + ' мин ]')
                    else:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До начала уроков осталось\n              [ ' + str(abs(7 - hour)) + ' ч -  ' + str(60 - minute) + ' мин ]')
            else:

                if 0 <= weekday < 4:
                    ALL_CLASSES_AND_FUNCTIONS.monitor.mon_unlim_7(event, hour, minute)
                elif weekday == 4:
                    ALL_CLASSES_AND_FUNCTIONS.monitor.mon_unlim_8(event, hour, minute)
                else:
                    ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Завтра суббота, откисай!')

        def time_find(minute):

            a = [1, 21, 31, 41]
            b = [2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54]
            c = list(range(5, 21)) + list(range(25, 31)) + list(range(35, 41)) + list(range(45, 51)) + list(range(55, 60))

            if minute in a:
                return ' минута!'
            elif minute in b:
                return ' минуты!'
            elif minute in c:
                return ' минут!'

        def mon_unlim_7(event, hour, minute):

            if hour == 8 and minute == 0:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Уроки начались - 1 урок!')
            elif hour == 8 and minute < 40:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца урока осталось: ' + str(40 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(40 - minute))

            elif hour == 8 and 50 > minute >= 40:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Перемена!')
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца перемены осталось: ' + str(50 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(50 - minute))

            elif hour == 8 and minute == 50:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Начался 2 урок!')
            elif hour == 8 and minute > 50:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца урока осталось: ' + str((60 - minute) + 30) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(60 - minute + 30))
            elif hour == 9 and minute < 30:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца урока осталось: ' + str(30 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(30 - minute))

            elif hour == 9 and 40 > minute >= 30:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Перемена!')
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца перемены осталось: ' + str(40 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(40 - minute))

            elif hour == 9 and minute == 40:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Начался 3 урок!')
            elif hour == 9 and minute > 40:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца урока осталось: ' + str((60 - minute) + 20) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(60 - minute + 20))
            elif hour == 10 and minute < 20:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца урока осталось: ' + str(20 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(20 - minute))

            elif hour == 10 and 30 > minute >= 20:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Перемена!')
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца перемены осталось: ' + str(35 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(35 - minute))
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Бегом в столовую)')

            elif hour == 10 and 35 > minute >= 30:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца перемены осталось: ' + str(35 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(35 - minute))
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Бегом на урок!')

            elif hour == 10 and minute == 35:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Начался 4 урок!')
            elif hour == 10 and minute > 35:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца урока осталось: ' + str((60 - minute) + 15) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(60 - minute + 15))
            elif hour == 11 and minute < 15:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца урока осталось: ' + str(15 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(15 - minute))

            elif hour == 11 and 25 > minute >= 15:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Перемена!')
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'У тебя ' + str(30 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(30 - minute) + ', чтобы подкрепиться!')

            elif hour == 11 and 25 <= minute < 30:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'У тебя ' + str(30 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(30 - minute) + ', чтобы добраться до класса!')

            elif hour == 11 and minute == 30:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Начался 5 урок!')
            elif hour == 11 and minute > 30:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца урока осталось: ' + str((60 - minute) + 10) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(60 - minute + 10))
            elif hour == 12 and minute < 10:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца урока осталось: ' + str(10 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(10 - minute))

            elif hour == 12 and 20 > minute >= 10:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Перемена!')
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца перемены осталось: ' + str(20 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(20 - minute))

            elif hour == 12 and minute == 20:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Начался 6 урок!')
            elif hour == 12 and minute > 20:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца урока осталось: ' + str(60 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(60 - minute))

            elif hour == 13 and 5 > minute >= 0:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Перемена!')
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца перемены осталось: ' + str(5 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(5 - minute))

            elif hour == 13 and minute == 5:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Начался 7 урок!')
            elif hour == 13 and minute < 45:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца урока осталось: ' + str(45 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(45 - minute))
            elif hour == 13 and minute == 45 or minute == 46 or minute == 47:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Пора домой!')

        def mon_unlim_8(event, hour, minute):

            if hour == 8 and minute == 0:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Уроки начались - 1 урок!')
            elif hour == 8 and minute < 40:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца урока осталось: ' + str(40 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(40 - minute))

            elif hour == 8 and 50 > minute >= 40:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Перемена!')
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца перемены осталось: ' + str(50 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(50 - minute))

            elif hour == 8 and minute == 50:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Начался 2 урок!')
            elif hour == 8 and minute > 50:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца урока осталось: ' + str((60 - minute) + 30) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(60 - minute + 30))
            elif hour == 9 and minute < 30:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца урока осталось: ' + str(30 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(30 - minute))

            elif hour == 9 and 40 > minute >= 30:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Перемена!')
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца перемены осталось: ' + str(40 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(40 - minute))

            elif hour == 9 and minute == 40:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Начался 3 урок!')
            elif hour == 9 and minute > 40:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца урока осталось: ' + str((60 - minute) + 20) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(60 - minute + 20))
            elif hour == 10 and minute < 20:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца урока осталось: ' + str(20 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(20 - minute))

            elif hour == 10 and 30 > minute >= 20:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Перемена!')
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца перемены осталось: ' + str(35 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(35 - minute))
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Бегом в столовую)')

            elif hour == 10 and 35 > minute >= 30:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца перемены осталось: ' + str(35 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(35 - minute))
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Бегом на урок!')

            elif hour == 10 and minute == 35:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Начался 4 урок!')
            elif hour == 10 and minute > 35:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца урока осталось: ' + str((60 - minute) + 15) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(60 - minute + 15))
            elif hour == 11 and minute < 15:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца урока осталось: ' + str(15 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(15 - minute))

            elif hour == 11 and 25 > minute >= 15:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Перемена!')
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'У тебя ' + str(30 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(30 - minute) + ', чтобы подкрепиться!')

            elif hour == 11 and 25 <= minute < 30:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'У тебя ' + str(30 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(30 - minute) + ', чтобы добраться до класса!')

            elif hour == 11 and minute == 30:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Начался 5 урок!')
            elif hour == 11 and minute > 30:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца урока осталось: ' + str((60 - minute) + 10) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(60 - minute + 10))
            elif hour == 12 and minute < 10:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца урока осталось: ' + str(10 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(10 - minute))

            elif hour == 12 and 20 > minute >= 10:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Перемена!')
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца перемены осталось: ' + str(20 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(20 - minute))

            elif hour == 12 and minute == 20:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Начался 6 урок!')
            elif hour == 12 and minute > 20:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца урока осталось: ' + str(60 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(60 - minute))

            elif hour == 13 and 5 > minute >= 0:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Перемена!')
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца перемены осталось: ' + str(5 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(5 - minute))

            elif hour == 13 and minute == 5:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Начался 7 урок!')
            elif hour == 13 and minute < 45:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца урока осталось: ' + str(45 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(45 - minute))

            elif hour == 13 and 45 >= minute:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Перемена!')
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца перемены осталось: ' + str(60 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(60 - minute))

            elif hour == 14 and minute == 0:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Начался 8 урок!')
            elif hour == 14 and minute < 40:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца урока осталось: ' + str(60 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(60 - minute))
            elif hour == 14 and minute == 40 or minute == 41 or minute == 42:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Пора домой!')

        def mon_unlim_6(event, hour, minute):

            if hour == 8 and minute == 0:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Уроки начались - 1 урок!')
            elif hour == 8 and minute < 40:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца урока осталось: ' + str(40 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(40 - minute))

            elif hour == 8 and 50 > minute >= 40:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Перемена!')
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца перемены осталось: ' + str(50 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(50 - minute))

            elif hour == 8 and minute == 50:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Начался 2 урок!')
            elif hour == 8 and minute > 50:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца урока осталось: ' + str((60 - minute) + 30) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(60 - minute + 30))
            elif hour == 9 and minute < 30:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца урока осталось: ' + str(30 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(30 - minute))

            elif hour == 9 and 40 > minute >= 30:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Перемена!')
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца перемены осталось: ' + str(40 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(40 - minute))

            elif hour == 9 and minute == 40:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Начался 3 урок!')
            elif hour == 9 and minute > 40:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца урока осталось: ' + str((60 - minute) + 20) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(60 - minute + 20))
            elif hour == 10 and minute < 20:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца урока осталось: ' + str(20 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(20 - minute))

            elif hour == 10 and 30 > minute >= 20:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Перемена!')
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца перемены осталось: ' + str(35 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(35 - minute))
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Бегом в столовую)')

            elif hour == 10 and 35 > minute >= 30:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца перемены осталось: ' + str(35 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(35 - minute))
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Бегом на урок!')

            elif hour == 10 and minute == 35:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Начался 4 урок!')
            elif hour == 10 and minute > 35:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца урока осталось: ' + str((60 - minute) + 15) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(60 - minute + 15))
            elif hour == 11 and minute < 15:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца урока осталось: ' + str(15 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(15 - minute))

            elif hour == 11 and 25 > minute >= 15:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Перемена!')
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'У тебя ' + str(30 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(30 - minute) + ', чтобы подкрепиться!')

            elif hour == 11 and 25 <= minute < 30:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'У тебя ' + str(30 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(30 - minute) + ', чтобы добраться до класса!')

            elif hour == 11 and minute == 30:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Начался 5 урок!')
            elif hour == 11 and minute > 30:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца урока осталось: ' + str((60 - minute) + 10) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(60 - minute + 10))
            elif hour == 12 and minute < 10:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца урока осталось: ' + str(10 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(10 - minute))

            elif hour == 12 and 20 > minute >= 10:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Перемена!')
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца перемены осталось: ' + str(20 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(20 - minute))

            elif hour == 12 and minute == 20:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Начался 6 урок!')
            elif hour == 12 and minute > 20:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'До конца урока осталось: ' + str(60 - minute) + ALL_CLASSES_AND_FUNCTIONS.monitor.time_find(60 - minute))

            elif hour == 13 and 3 >= minute >= 0:
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Пора домой!!!')

    class schedule:

        def if_today(response, event, weekday):

            if response == '[11Б] - НА СЕГОДНЯ - [11Б]':
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], ALL_CLASSES_AND_FUNCTIONS.classes_.B_11.today(weekday, event, True))

            elif response == '[11А] - НА СЕГОДНЯ - [11А]':
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], ALL_CLASSES_AND_FUNCTIONS.classes_.A_11.today(weekday, event, True))

            elif response == '[11В] - НА СЕГОДНЯ - [11В]':
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], ALL_CLASSES_AND_FUNCTIONS.classes_.V_11.today(weekday, event, True))

            elif response == '[11Г] - НА СЕГОДНЯ - [11Г]':
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], ALL_CLASSES_AND_FUNCTIONS.classes_.G_11.today(weekday, event, True))

        def if_tomorrow(response, event, weekday):

            if response == '[11Б] - НА ЗАВТРА - [11Б]':
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], ALL_CLASSES_AND_FUNCTIONS.classes_.B_11.tomorrow(weekday + 1, event, False))

            elif response == '[11А] - НА ЗАВТРА - [11А]':
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], ALL_CLASSES_AND_FUNCTIONS.classes_.A_11.tomorrow(weekday + 1, event, False))

            elif response == '[11В] - НА ЗАВТРА - [11В]':
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], ALL_CLASSES_AND_FUNCTIONS.classes_.V_11.tomorrow(weekday + 1, event, False))

            elif response == '[11Г] - НА ЗАВТРА - [11Г]':
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], ALL_CLASSES_AND_FUNCTIONS.classes_.G_11.tomorrow(weekday + 1, event, False))

        def if_day(response, event, weekday):

            if response == '[11Б] - НА ОПРЕДЕЛЁННЫЙ ДЕНЬ - [11Б]':
                ALL_CLASSES_AND_FUNCTIONS.keyboards.B_11_kb_2(event)

            elif response == '[11А] - НА ОПРЕДЕЛЁННЫЙ ДЕНЬ - [11А]':
                ALL_CLASSES_AND_FUNCTIONS.keyboards.A_11_kb_2(event)

            elif response == '[11В] - НА ОПРЕДЕЛЁННЫЙ ДЕНЬ - [11В]':
                ALL_CLASSES_AND_FUNCTIONS.keyboards.V_11_kb_2(event)

            elif response == '[11Г] - НА ОПРЕДЕЛЁННЫЙ ДЕНЬ - [11Г]':
                ALL_CLASSES_AND_FUNCTIONS.keyboards.G_11_kb_2(event)

        def if_day_chosen(response, event):

            if response == '[11Б] - ПОНЕДЕЛЬНИК - [11Б]':
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], ALL_CLASSES_AND_FUNCTIONS.classes_.B_11.today(0, event, False))
            elif response == '[11Б] - ВТОРНИК - [11Б]':
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], ALL_CLASSES_AND_FUNCTIONS.classes_.B_11.today(1, event, False))
            elif response == '[11Б] - СРЕДА - [11Б]':
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], ALL_CLASSES_AND_FUNCTIONS.classes_.B_11.today(2, event, False))
            elif response == '[11Б] - ЧЕТВЕРГ - [11Б]':
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], ALL_CLASSES_AND_FUNCTIONS.classes_.B_11.today(3, event, False))
            elif response == '[11Б] - ПЯТНИЦА - [11Б]':
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], ALL_CLASSES_AND_FUNCTIONS.classes_.B_11.today(4, event, False))

            if response == '[11А] - ПОНЕДЕЛЬНИК - [11А]':
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], ALL_CLASSES_AND_FUNCTIONS.classes_.A_11.today(0, event, False))
            elif response == '[11А] - ВТОРНИК - [11А]':
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], ALL_CLASSES_AND_FUNCTIONS.classes_.A_11.today(1, event, False))
            elif response == '[11А] - СРЕДА - [11А]':
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], ALL_CLASSES_AND_FUNCTIONS.classes_.A_11.today(2, event, False))
            elif response == '[11А] - ЧЕТВЕРГ - [11А]':
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], ALL_CLASSES_AND_FUNCTIONS.classes_.A_11.today(3, event, False))
            elif response == '[11А] - ПЯТНИЦА - [11А]':
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], ALL_CLASSES_AND_FUNCTIONS.classes_.A_11.today(4, event, False))

            if response == '[11В] - ПОНЕДЕЛЬНИК - [11В]':
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], ALL_CLASSES_AND_FUNCTIONS.classes_.V_11.today(0, event, False))
            elif response == '[11В] - ВТОРНИК - [11В]':
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], ALL_CLASSES_AND_FUNCTIONS.classes_.V_11.today(1, event, False))
            elif response == '[11В] - СРЕДА - [11В]':
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], ALL_CLASSES_AND_FUNCTIONS.classes_.V_11.today(2, event, False))
            elif response == '[11В] - ЧЕТВЕРГ - [11В]':
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], ALL_CLASSES_AND_FUNCTIONS.classes_.V_11.today(3, event, False))
            elif response == '[11В] - ПЯТНИЦА - [11В]':
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], ALL_CLASSES_AND_FUNCTIONS.classes_.V_11.today(4, event, False))

            if response == '[11Г] - ПОНЕДЕЛЬНИК - [11Г]':
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], ALL_CLASSES_AND_FUNCTIONS.classes_.G_11.today(0, event, False))
            elif response == '[11Г] - ВТОРНИК - [11Г]':
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], ALL_CLASSES_AND_FUNCTIONS.classes_.G_11.today(1, event, False))
            elif response == '[11Г] - СРЕДА - [11Г]':
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], ALL_CLASSES_AND_FUNCTIONS.classes_.G_11.today(2, event, False))
            elif response == '[11Г] - ЧЕТВЕРГ - [11Г]':
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], ALL_CLASSES_AND_FUNCTIONS.classes_.G_11.today(3, event, False))
            elif response == '[11Г] - ПЯТНИЦА - [11Г]':
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], ALL_CLASSES_AND_FUNCTIONS.classes_.G_11.today(4, event, False))

    def choose_another_class(response, monitor_bells_access):

        if response == '[11Б] - ВЫБРАТЬ ДРУГОЙ КЛАСС - [11Б]':

            if monitor_bells_access:
                keyboard = {
                    'one_time': False,
                    'buttons': [
                        [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="∆ ВАЖНОЕ ∆", color='positive')],
                        [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="Ω 11Б", color='primary'),
                         ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="Ω 11A", color='primary'),
                         ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="Ω 11В", color='primary'),
                         ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="Ω 11Г", color='primary')],
                        [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="∆ - ПРЯМОЙ МОНИТОРИНГ ЗВОНКОВ - ∆", color='positive')],
                        [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="• ПОМОЩЬ •", color='secondary')]
                    ],
                    'inline': False
                }
                ALL_CLASSES_AND_FUNCTIONS.main.add_kb(keyboard, 7)

            else:
                keyboard = {
                    'one_time': False,
                    'buttons': [
                        [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="∆ ВАЖНОЕ ∆", color='positive')],
                        [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="Ω 11Б", color='primary'),
                         ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="Ω 11A", color='primary'),
                         ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="Ω 11В", color='primary'),
                         ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="Ω 11Г", color='primary')],
                        [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="∆ - ПРЯМОЙ МОНИТОРИНГ ЗВОНКОВ - ∆", color='positive')],
                        [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="• ПОМОЩЬ •", color='secondary')]
                    ],
                    'inline': False
                }
                ALL_CLASSES_AND_FUNCTIONS.main.add_kb(keyboard, 7)


        elif response == '[11А] - ВЫБРАТЬ ДРУГОЙ КЛАСС - [11А]':

            if monitor_bells_access:
                keyboard = {
                    'one_time': False,
                    'buttons': [
                        [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="∆ ВАЖНОЕ ∆", color='positive')],
                        [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="Ω 11Б", color='primary'),
                         ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="Ω 11A", color='primary'),
                         ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="Ω 11В", color='primary'),
                         ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="Ω 11Г", color='primary')],
                        [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="∆ - ПРЯМОЙ МОНИТОРИНГ ЗВОНКОВ - ∆", color='positive')],
                        [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="• ПОМОЩЬ •", color='secondary')]
                    ],
                    'inline': False
                }
                ALL_CLASSES_AND_FUNCTIONS.main.add_kb(keyboard, 7)

            else:
                keyboard = {
                    'one_time': False,
                    'buttons': [
                        [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="∆ ВАЖНОЕ ∆", color='positive')],
                        [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="Ω 11Б", color='primary'),
                         ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="Ω 11A", color='primary'),
                         ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="Ω 11В", color='primary'),
                         ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="Ω 11Г", color='primary')],
                        [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="∆ - ПРЯМОЙ МОНИТОРИНГ ЗВОНКОВ - ∆", color='positive')],
                        [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="• ПОМОЩЬ •", color='secondary')]
                    ],
                    'inline': False
                }
                ALL_CLASSES_AND_FUNCTIONS.main.add_kb(keyboard, 7)

        elif response == '[11В] - ВЫБРАТЬ ДРУГОЙ КЛАСС - [11В]':

            if monitor_bells_access:
                keyboard = {
                    'one_time': False,
                    'buttons': [
                        [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="∆ ВАЖНОЕ ∆", color='positive')],
                        [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="Ω 11Б", color='primary'),
                         ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="Ω 11A", color='primary'),
                         ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="Ω 11В", color='primary'),
                         ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="Ω 11Г", color='primary')],
                        [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="∆ - ПРЯМОЙ МОНИТОРИНГ ЗВОНКОВ - ∆", color='positive')],
                        [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="• ПОМОЩЬ •", color='secondary')]
                    ],
                    'inline': False
                }
                ALL_CLASSES_AND_FUNCTIONS.main.add_kb(keyboard, 7)

            else:
                keyboard = {
                    'one_time': False,
                    'buttons': [
                        [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="∆ ВАЖНОЕ ∆", color='positive')],
                        [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="Ω 11Б", color='primary'),
                         ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="Ω 11A", color='primary'),
                         ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="Ω 11В", color='primary'),
                         ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="Ω 11Г", color='primary')],
                        [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="∆ - ПРЯМОЙ МОНИТОРИНГ ЗВОНКОВ - ∆", color='positive')],
                        [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="• ПОМОЩЬ •", color='secondary')]
                    ],
                    'inline': False
                }
                ALL_CLASSES_AND_FUNCTIONS.main.add_kb(keyboard, 7)

        elif response == '[11Г] - ВЫБРАТЬ ДРУГОЙ КЛАСС - [11Г]':

            if monitor_bells_access:
                keyboard = {
                    'one_time': False,
                    'buttons': [
                        [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="∆ ВАЖНОЕ ∆", color='positive')],
                        [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="Ω 11Б", color='primary'),
                         ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="Ω 11A", color='primary'),
                         ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="Ω 11В", color='primary'),
                         ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="Ω 11Г", color='primary')],
                        [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="∆ - ПРЯМОЙ МОНИТОРИНГ ЗВОНКОВ - ∆", color='positive')],
                        [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="• ПОМОЩЬ •", color='secondary')]
                    ],
                    'inline': False
                }
                ALL_CLASSES_AND_FUNCTIONS.main.add_kb(keyboard, 7)

            else:
                keyboard = {
                    'one_time': False,
                    'buttons': [
                        [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="∆ ВАЖНОЕ ∆", color='positive')],
                        [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="Ω 11Б", color='primary'),
                         ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="Ω 11A", color='primary'),
                         ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="Ω 11В", color='primary'),
                         ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="Ω 11Г", color='primary')],
                        [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="∆ - ПРЯМОЙ МОНИТОРИНГ ЗВОНКОВ - ∆", color='positive')],
                        [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="• ПОМОЩЬ •", color='secondary')]
                    ],
                    'inline': False
                }
                ALL_CLASSES_AND_FUNCTIONS.main.add_kb(keyboard, 7)

    def back(response, event):

        if response == '[11Б] - НАЗАД - [11Б]':

            keyboard = {
                'one_time': False,
                'buttons': [
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11Б] - НА СЕГОДНЯ - [11Б]", color='secondary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11Б] - НА ЗАВТРА - [11Б]", color='secondary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11Б] - НА ОПРЕДЕЛЁННЫЙ ДЕНЬ - [11Б]", color='default')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11Б] - ДЗ - [11Б]", color='positive')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label='[11Б] - ВЫБРАТЬ ДРУГОЙ КЛАСС - [11Б]', color='negative')]
                ],
                'inline': False
            }

            keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
            keyboard = str(keyboard.decode('utf-8'))

            ALL_CLASSES_AND_FUNCTIONS.main.send_keyboard(event.obj['message']['peer_id'], keyboard, '< Choose schedule type! >')


        elif response == '[11А] - НАЗАД - [11А]':
            keyboard = {
                'one_time': False,
                'buttons': [
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11А] - НА СЕГОДНЯ - [11А]", color='secondary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11А] - НА ЗАВТРА - [11А]", color='secondary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11А] - НА ОПРЕДЕЛЁННЫЙ ДЕНЬ - [11А]", color='default')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11А] - ДЗ - [11А]", color='positive')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label='[11А] - ВЫБРАТЬ ДРУГОЙ КЛАСС - [11А]', color='negative')]
                ],
                'inline': False
            }

            keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
            keyboard = str(keyboard.decode('utf-8'))

            ALL_CLASSES_AND_FUNCTIONS.main.send_keyboard(event.obj['message']['peer_id'], keyboard, '< Choose schedule type! >')

        elif response == '[11В] - НАЗАД - [11В]':
            keyboard = {
                'one_time': False,
                'buttons': [
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11В] - НА СЕГОДНЯ - [11В]", color='secondary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11В] - НА ЗАВТРА - [11В]", color='secondary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11В] - НА ОПРЕДЕЛЁННЫЙ ДЕНЬ - [11В]", color='default')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11В] - ДЗ - [11В]", color='positive')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label='[11В] - ВЫБРАТЬ ДРУГОЙ КЛАСС - [11В]', color='negative')]
                ],
                'inline': False
            }

            keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
            keyboard = str(keyboard.decode('utf-8'))

            ALL_CLASSES_AND_FUNCTIONS.main.send_keyboard(event.obj['message']['peer_id'], keyboard, '< Choose schedule type! >')

        elif response == '[11Г] - НАЗАД - [11Г]':
            keyboard = {
                'one_time': False,
                'buttons': [
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11Г] - НА СЕГОДНЯ - [11Г]", color='secondary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11Г] - НА ЗАВТРА - [11Г]", color='secondary')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11Г] - НА ОПРЕДЕЛЁННЫЙ ДЕНЬ - [11Г]", color='default')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="[11Г] - ДЗ - [11Г]", color='positive')],
                    [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label='[11Г] - ВЫБРАТЬ ДРУГОЙ КЛАСС - [11Г]', color='negative')]
                ],
                'inline': False
            }

            keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
            keyboard = str(keyboard.decode('utf-8'))

            ALL_CLASSES_AND_FUNCTIONS.main.send_keyboard(event.obj['message']['peer_id'], keyboard, '< Choose schedule type! >')

    class important:

        def help(response, event):

            if response == '• ПОМОЩЬ •':
                answer = '<ВНИМАНИЕ>\n\nКорректировка по времени использована в соответствиии со звонками!\n\n' \
                         'ИСПОЛЬЗОВАТЬ БОТА ЛУЧШЕ В ЛС! В СИЛУ ЕГО НЕБОЛЬШОГО СПАМА(Все вопросы к разрабам вк)\n\n' \
                         '-----------------------------------------------------------------\n\n' \
                         '<ПРЯМОЙ МОНИТОРИНГ>\n\n позволяет контроллировать время до конца, ' \
                         'а также до начала урока(всё автоматизированно, нужно лишь нажать на кнопку, ' \
                         'чтобы бот отправил информацию о звонке :)\n' \
                         'Иногда может врать по той простой причине, что сервер в мухосранске, а мы в новой Атланте!\n\n' \
                         '-----------------------------------------------------------------\n\n' \
                         '<РАСПИСАНИЕ>\n\n\t\t' \
                         '[¶] 1 - [  8:00 - 8:40  ] •|англ|•\n' \
                         'означает, что на ДАННЫЙ МОМЕНТ идёт урок именно АНГЛИЙСКОГО ЯЗЫКА\n' \
                         '(1 - первый урок)\n\n\t[ shift -> [¶] ] - ПЕРЕМЕНА\n' \
                         'Аналогично без значков " ¶ "\n(нет значка - нет действующего(-щей) урока/перемены)\n[ не пишите про суперпозицию :) ]   \n\n' \
                         'Если выбор пал на определённый или завтрашний день, то значки " ¶ " будут отображаться по умолчанию.\n\n' \
                         '-----------------------------------------------------------------\n\n' \
                         '<ДЗ>\n\n' \
                         'Форма добавления дз:\n' \
                         '[КЛАСС] [ДЕНЬ НЕДЕЛИ] [ПРЕДМЕТ] [ДЗ]\n' \
                         'ПРИМЕР:\n11Б понедельник инфа что-то задали\n\n' \
                         '||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n' \
                         '† УБЕДИТЕЛЬНАЯ ПРОСЬБА НЕ ДОБАВЛЯТЬ ДЗ К ЧУЖИМ КЛАССАМ †\n' \
                         '||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n\n' \
                         'Для особо умных персон прибудет божий DDoS на 2 ТБ/с 😁 (и естественно это будет делать не бот)\n\n' \
                         '!НАИМЕНОВАНИЕ ПРЕДМЕТОВ!\n\n' \
                         '[НАЗВАНИЕ ПРЕДМЕТА ДЛЯ БОТА - (ИСТИННОЕ НАЗВАНИЕ ПРЕДМЕТА)]\n\n' \
                         '[русский - (русский)\n[англ - (английский)]\n[матан - (математика)]\n' \
                         '[литра - (литература)]\n[физика - (физика)]\n[геогр - (география)]\n[нем - (немецкий)]\n' \
                         '[родной - (родной)]\n[химия - (химия)]\n[обж - (обж)], [история - (история)]\n[общество - (обществознание)]\n' \
                         '[био - (биология)]\n[инфа - (информатика)]\n\n' \
                         '-----------------------------------------------------------------\n\n' \
                         '<ОГРОМНАЯ ПРОСЬБА>\n' \
                         'Вовремя сообщить о косяках, так как все косяки я самостоятельно отследить не смогу ввиду того, что задача бота работать во время школы, а в школе дебажить бота крайне сложно.\n' \
                         'Напиши боту /report и ваше сообщение о проблеме\nНапример: /report что-то сломалось\n' \
                         'Если проблему описать сложно или имиеются скрины, то напишите мне в личку об ошибках, которые вы увидели(со скринами, чтобы я понял, что делать).\n\n' \
                         '-----------------------------------------------------------------\n\n' \
                         'Your faithfully https://vk.com/firemansky ...'
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], answer)

        def time_find(minute):

            minute = int(minute)

            a = [1, 21, 31, 41]
            b = [2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54]
            c = list(range(5, 21)) + list(range(25, 31)) + list(range(35, 41)) + list(range(45, 51)) + list(range(55, 60))

            if minute in a:
                return ' ДЕНЬ!'
            elif minute in b:
                return ' ДНЯ!'
            elif minute in c:
                return ' ДНЕЙ!'

        def piece(response, event):

            if response == '∆ ВАЖНОЕ ∆':

                now = datetime.now()

                target_ban = datetime(2020, 5, 26)
                target_weekends = datetime(2020, 3, 24)

                delta_ban = abs((target_ban - now).days)
                delta_weekends = abs((target_weekends - now).days)

                print(delta_ban, ALL_CLASSES_AND_FUNCTIONS.important.time_find(int(delta_ban)))

                bot_answer = 'ДО ВЕЛИКОГО БАНА ОСТАЛОСЬ ' + str(delta_ban) + ' д'
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], bot_answer)
                bot_answer = 'ДО НАЧАЛА КАНИКУЛ ОСТАЛОСЬ ' + str(delta_weekends) + ' д'
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], bot_answer)

        def update_bot(response, event):

            global kb_added
            global monitor_bells_access

            if response == '/update':
                keyboard = {
                    'one_time': False,
                    'buttons': [
                        [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="∆ ВАЖНОЕ ∆", color='positive')],
                        [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="Ω 11Б", color='primary'),
                         ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="Ω 11A", color='primary'),
                         ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="Ω 11В", color='primary'),
                         ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="Ω 11Г", color='primary')],
                        [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="∆ - ПРЯМОЙ МОНИТОРИНГ ЗВОНКОВ - ∆", color='positive')],
                        [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="∞ РАЗРЕШИТЬ ПОСТОЯННЫЙ МОНИТОРИНГ ∞", color='positive')],
                        [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label="• ПОМОЩЬ •", color='secondary')]
                        # [ALL_CLASSES_AND_FUNCTIONS.main.get_button(label='/del', color='negative')]
                    ],
                    'inline': False
                }
                kb_added = True
                ALL_CLASSES_AND_FUNCTIONS.monitor_bells_access = False
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], "< Let's get it started! >")
                ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], "< Читайте мою документацию >\n<   --> • ПОМОЩЬ • <--   >")
                ALL_CLASSES_AND_FUNCTIONS.main.add_kb(keyboard, 7)

        def del_kb(response, yes, kb_added):

            if response == '/del':
                kb_added = False
                ALL_CLASSES_AND_FUNCTIONS.main.kill_kb(yes)

    class if_monitor:

        def one_mon(response, event):

            weekday = datetime.now().weekday()
            hour = datetime.now().hour + 5
            minute = datetime.now().minute + 2

            if response == '∆ - ПРЯМОЙ МОНИТОРИНГ ЗВОНКОВ - ∆':
                if 0 <= weekday < 4:
                    ALL_CLASSES_AND_FUNCTIONS.monitor.monitor_bells_one_time(event, weekday)
                elif weekday == 4 and ((0 <= hour <= 13 and 0 <= minute <= 59) or (hour == 14 and minute < 40)):
                    ALL_CLASSES_AND_FUNCTIONS.monitor.monitor_bells_one_time(event, weekday)

                elif weekday == 4 and ((hour >= 14 and minute >= 40) or (hour >= 15)):
                    ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Завтра выходной, откисай!')

                elif 5 <= weekday <= 6:
                    ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Сегодня выходной, спи!')

    class if_classes:

        def class_(response, event):

            global b11
            global a11
            global v11
            global g11

            if response == 'Ω 11Б':
                b11 = True
                ALL_CLASSES_AND_FUNCTIONS.keyboards.B_11_kb_1(event)

            elif response == 'Ω 11A':
                a11 = True
                ALL_CLASSES_AND_FUNCTIONS.keyboards.A_11_kb_1(event)

            elif response == 'Ω 11В':
                v11 = True
                ALL_CLASSES_AND_FUNCTIONS.keyboards.V_11_kb_1(event)

            elif response == 'Ω 11Г':
                g11 = True
                ALL_CLASSES_AND_FUNCTIONS.keyboards.G_11_kb_1(event)

    class home_work:

        def write_homework(response, event, from_dump):

            global homework_B_11, homework_A_11, homework_V_11, homework_G_11

            try:
                if response[:3] == '11Б' or response[:3] == '11А' or response[:3] == '11В' or response[:3] == '11Г':
                    response = response.lower().split()
                    if response[0].upper() == '11Б':
                        day1, day2 = response[1], response[2]
                        del response[0:3]
                        HOME = [item for item in response]
                        try:


                            homework_B_11[day1][day2].append(HOME)
                            DATE_AND_TIME = str(datetime.now().day) + ':' + str(datetime.now().month) + ':' + str(
                                    datetime.now().year) + ' [date] | at ' + str(datetime.now().hour) + ':' + str(
                                    datetime.now().minute) + ' [time]'

                            if not from_dump:
                                BACKUP_HOMEWORK = open('11Б.txt', 'a')
                                BACKUP_HOMEWORK.writelines(day1 + ' ' + day2 + ' ' + str(HOME) + ' ' + DATE_AND_TIME + '\n')
                                BACKUP_HOMEWORK.close()
                        except KeyError:
                            ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                        'Wrong subject or nonexistent!')

                    if response[0].upper() == '11А':
                        day1, day2 = response[1], response[2]
                        del response[0:3]
                        HOME = [item for item in response]
                        try:


                            homework_A_11[day1][day2].append(HOME)
                            DATE_AND_TIME = str(datetime.now().day) + ':' + str(datetime.now().month) + ':' + str(
                                    datetime.now().year) + ' [date] | at ' + str(datetime.now().hour) + ':' + str(
                                    datetime.now().minute) + ' [time]'

                            if not from_dump:
                                BACKUP_HOMEWORK = open('11А.txt', 'a')
                                BACKUP_HOMEWORK.writelines(day1 + ' ' + day2 + ' ' + str(HOME) + ' ' + DATE_AND_TIME + '\n')
                                BACKUP_HOMEWORK.close()
                        except KeyError:
                            ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                        'Wrong subject or nonexistent!')

                    if response[0].upper() == '11В':
                        day1, day2 = response[1], response[2]
                        del response[0:3]
                        HOME = [item for item in response]
                        try:


                            homework_V_11[day1][day2].append(HOME)

                            DATE_AND_TIME = str(datetime.now().day) + ':' + str(datetime.now().month) + ':' + str(
                                datetime.now().year) + ' [date] | at ' + str(datetime.now().hour) + ':' + str(
                                datetime.now().minute) + ' [time]'
                            if not from_dump:
                                BACKUP_HOMEWORK = open('11В.txt', 'a')
                                BACKUP_HOMEWORK.writelines(day1 + ' ' + day2 + ' ' + str(HOME) + ' ' + DATE_AND_TIME + '\n')
                                BACKUP_HOMEWORK.close()
                        except KeyError:
                            ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                        'Wrong subject or nonexistent!')

                    if response[0].upper() == '11Г':
                        day1, day2 = response[1], response[2]
                        del response[0:3]
                        HOME = [item for item in response]
                        try:


                            homework_G_11[day1][day2].append(HOME)

                            DATE_AND_TIME = str(datetime.now().day) + ':' + str(datetime.now().month) + ':' + str(
                                datetime.now().year) + ' [date] | at ' + str(datetime.now().hour) + ':' + str(
                                datetime.now().minute) + ' [time]'
                            if not from_dump:
                                BACKUP_HOMEWORK = open('11Г.txt', 'a')
                                BACKUP_HOMEWORK.writelines(day1 + ' ' + day2 + ' ' + str(HOME) + ' ' + DATE_AND_TIME + '\n')
                                BACKUP_HOMEWORK.close()
                        except KeyError:
                            ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                        'Wrong subject or nonexistent!')
                    # else:
                    #     ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'Please text the class command correctly!')
            except IndexError:
                pass

        def open_homework_table(response, event):

            if response == '[11Б] - ДЗ - [11Б]':
                ALL_CLASSES_AND_FUNCTIONS.keyboards.B_11_kb_3(event)
            elif response == '[11А] - ДЗ - [11А]':
                ALL_CLASSES_AND_FUNCTIONS.keyboards.A_11_kb_3(event)
            elif response == '[11В] - ДЗ - [11В]':
                ALL_CLASSES_AND_FUNCTIONS.keyboards.V_11_kb_3(event)
            elif response == '[11Г] - ДЗ - [11Г]':
                ALL_CLASSES_AND_FUNCTIONS.keyboards.G_11_kb_3(event)

        def check_homework_and_print(response, event):

            global homework_B_11, homework_A_11, homework_V_11, homework_G_11

            if response[:5] == '[11Б]':

                if response == '[11Б] - НА ПОНЕДЕЛЬНИК - [11Б]':

                    if not homework_B_11['понедельник']['инфа']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ИНФА')
                    else:
                        text = ''
                        for item in homework_B_11['понедельник']['инфа']:
                            for char in item:
                                 if char[11:17] == '[date]':
                                    break
                                 else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], text + '\n\n <-- ИНФА')

                    if not homework_B_11['понедельник']['литра']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ЛИТРА')
                    else:
                        text = ''
                        for item in homework_B_11['понедельник']['литра']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], text + '\n\n <-- ЛИТРА')


                    if not homework_B_11['понедельник']['обж']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ОБЖ ')
                    else:
                        text = ''
                        for item in homework_B_11['понедельник']['обж']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], text + '\n\n <-- ОБЖ')


                    if not homework_B_11['понедельник']['физика']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ФИЗИКА')
                    else:
                        text = ''
                        for item in homework_B_11['понедельник']['физика']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], text + '\n\n <-- ФИЗИКА')


                elif response == '[11Б] - НА ВТОРНИК - [11Б]':

                    if not homework_B_11['вторник']['химия']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ХИИМИЯ')
                    else:
                        text = ''
                        for item in homework_B_11['вторник']['химия']:
                            for char in item:
                                 if char[11:17] == '[date]':
                                    break
                                 else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], text + '\n\n <-- ХИМИЯ')

                    if not homework_B_11['вторник']['русский']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- РУССКИЙ')
                    else:
                        text = ''
                        for item in homework_B_11['вторник']['русский']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], text + '\n\n <-- РУССКИЙ')

                    if not homework_B_11['вторник']['матан']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- МАТАН')
                    else:
                        text = ''
                        for item in homework_B_11['вторник']['матан']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], text + '\n\n <-- МАТАН')

                    if not homework_B_11['вторник']['био']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- БИО')
                    else:
                        text = ''
                        for item in homework_B_11['вторник']['био']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], text + '\n\n <-- БИО')

                    if not homework_B_11['вторник']['физика']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ФИЗИКА')
                    else:
                        text = ''
                        for item in homework_B_11['вторник']['физика']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], text + '\n\n <-- ФИЗИКА')

                elif response == '[11Б] - НА СРЕДУ - [11Б]':

                    if not homework_B_11['среда']['история']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ИСТОРИЯ')
                    else:
                        text = ''
                        for item in homework_B_11['среда']['история']:
                            for char in item:
                                 if char[11:17] == '[date]':
                                    break
                                 else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], text + '\n\n <-- ИСТОРИЯ')

                    if not homework_B_11['среда']['родной']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- РОДНОЙ')
                    else:
                        text = ''
                        for item in homework_B_11['среда']['родной']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], text + '\n\n <-- РОДНОЙ')

                    if not homework_B_11['среда']['англ']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- АНГЛ')
                    else:
                        text = ''
                        for item in homework_B_11['среда']['англ']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], text + '\n\n <-- АНГЛ')

                    if not homework_B_11['среда']['инфа']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ИНФА')
                    else:
                        text = ''
                        for item in homework_B_11['среда']['инфа']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], text + '\n\n <-- ИНФА')

                    if not homework_B_11['среда']['матан']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- МАТАН')
                    else:
                        text = ''
                        for item in homework_B_11['среда']['матан']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], text + '\n\n <-- МАТАН')

                elif response == '[11Б] - НА ЧЕТВЕРГ - [11Б]':

                    if not homework_B_11['четверг']['англ']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- АНГЛ')
                    else:
                        text = ''
                        for item in homework_B_11['четверг']['англ']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], text + '\n\n <-- АНГЛ')

                    if not homework_B_11['четверг']['физика']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ФИЗИКА')
                    else:
                        text = ''
                        for item in homework_B_11['четверг']['физика']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], text + '\n\n <-- ФИЗИКА')

                    if not homework_B_11['четверг']['общество']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ОБЩЕСТВО')
                    else:
                        text = ''
                        for item in homework_B_11['четверг']['общество']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], text + '\n\n <-- ОБЩЕСТВО')

                    if not homework_B_11['четверг']['матан']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- МАТАН')
                    else:
                        text = ''
                        for item in homework_B_11['четверг']['матан']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], text + '\n\n <-- МАТАН')

                elif response == '[11Б] - НА ПЯТНИЦУ - [11Б]':

                    if not homework_B_11['пятница']['матан']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- МАТАН')
                    else:
                        text = ''
                        for item in homework_B_11['пятница']['матан']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], text + '\n\n <-- МАТАН')

                    if not homework_B_11['пятница']['физика']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ФИЗИКА')
                    else:
                        text = ''
                        for item in homework_B_11['пятница']['физиика']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], text + '\n\n <-- ФИЗИКА')

                    if not homework_B_11['пятница']['литра']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ЛИТРА')
                    else:
                        text = ''
                        for item in homework_B_11['пятница']['литра']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], text + '\n\n <-- ЛИТРА')

                    if not homework_B_11['пятница']['англ']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- АНГЛ')
                    else:
                        text = ''
                        for item in homework_B_11['пятница']['англ']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], text + '\n\n <-- АНГЛ')



            elif response[:5] == '[11А]':

                if response == '[11А] - НА ПОНЕДЕЛЬНИК - [11А]':

                    if not homework_A_11['понедельник']['литра']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ЛИТРА')
                    else:
                        text = ''
                        for item in homework_A_11['понедельник']['литра']:
                            for char in item:
                                 if char[11:17] == '[date]':
                                    break
                                 else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], text + '\n\n <-- ЛИТРА')

                    if not homework_A_11['понедельник']['био']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- БИО')
                    else:
                        text = ''
                        for item in homework_A_11['понедельник']['био']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], text + '\n\n <-- БИО')


                    if not homework_A_11['понедельник']['матан']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- МАТАН')
                    else:
                        text = ''
                        for item in homework_A_11['понедельник']['матан']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], text + '\n\n <-- МАТАН')

                    if not homework_A_11['понедельник']['физика']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ФИЗИКА')
                    else:
                        text = ''
                        for item in homework_A_11['понедельник']['физика']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], text + '\n\n <-- ФИЗИКА')

                    if not homework_A_11['понедельник']['англ']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- АНГЛ')
                    else:
                        text = ''
                        for item in homework_A_11['понедельник']['англ']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break



                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], text + '\n\n <-- АНГЛ')




                elif response == '[11А] - НА ВТОРНИК - [11А]':

                    if not homework_A_11['вторник']['родной']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- РОДНОЙ')
                    else:
                        text = ''
                        for item in homework_A_11['вторник']['родной']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], text + '\n\n <-- РОДНОЙ')

                    if not homework_A_11['вторник']['обж']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ОБЖ')
                    else:
                        text = ''
                        for item in homework_A_11['вторник']['обж']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], text + '\n\n <-- ОБЖ')

                    if not homework_A_11['вторник']['литра']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ЛИТРА')
                    else:
                        text = ''
                        for item in homework_A_11['вторник']['литра']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], text + '\n\n <-- ЛИТРА')

                    if not homework_A_11['вторник']['нем']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-НЕМЕЦКИЙ')
                    else:
                        text = ''
                        for item in homework_A_11['вторник']['нем']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], text + '\n\n <-- НЕМЕЦКИЙ')

                    if not homework_A_11['вторник']['англ']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- АНГЛ')
                    else:
                        text = ''
                        for item in homework_A_11['вторник']['англ']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], text + '\n\n <-- АНГЛ')
                    if not homework_A_11['вторник']['русский']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- РУССКИЙ')
                    else:
                        text = ''
                        for item in homework_A_11['вторник']['русский']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], text + '\n\n <-- РУССКИЙ')

                elif response == '[11А] - НА СРЕДУ - [11А]':

                    if not homework_A_11['среда']['матан']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- МАТАН')
                    else:
                        text = ''
                        for item in homework_A_11['среда']['матан']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- МАТАН')

                    if not homework_A_11['среда']['физика']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ФИЗИКА')
                    else:
                        text = ''
                        for item in homework_A_11['среда']['физика']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- ФИЗИКА')

                    if not homework_A_11['среда']['англ']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-АНГЛ')
                    else:
                        text = ''
                        for item in homework_A_11['среда']['англ']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- АНГЛ')

                    if not homework_A_11['среда']['нем']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- НЕМЕЦКИЙ')
                    else:
                        text = ''
                        for item in homework_A_11['среда']['нем']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- НЕМЕЦКИЙ')
                    if not homework_A_11['среда']['русский']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- РУССКИЙ')
                    else:
                        text = ''
                        for item in homework_A_11['среда']['русский']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- РУССКИЙ')
                    if not homework_A_11['среда']['история']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ИСТОРИЯ')
                    else:
                        text = ''
                        for item in homework_A_11['среда']['история']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- ИСТОРИЯ')
                    if not homework_A_11['среда']['матан']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- МАТАН')
                    else:
                        text = ''
                        for item in homework_A_11['среда']['матан']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- МАТАН')

                elif response == '[11А] - НА ЧЕТВЕРГ - [11А]':

                    if not homework_A_11['четверг']['химия']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ХИМИЯ')
                    else:
                        text = ''
                        for item in homework_A_11['четверг']['химия']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- ХИМИЯ')

                    if not homework_A_11['четверг']['общество']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ОБЩЕСТВО')
                    else:
                        text = ''
                        for item in homework_A_11['четверг']['общество']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- ОБЩЕСТВО')

                    if not homework_A_11['четверг']['литра']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-ЛИТРА')
                    else:
                        text = ''
                        for item in homework_A_11['четверг']['литра']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- ЛИТРА')

                    if not homework_A_11['четверг']['общество']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    'None <-- ОБЩЕСТВО')
                    else:
                        text = ''
                        for item in homework_A_11['четверг']['общество']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- ОБЩЕСТВО')

                    if not homework_A_11['четверг']['англ']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- АНГЛ')
                    else:
                        text = ''
                        for item in homework_A_11['четверг']['англ']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- АНГЛ')

                    if not homework_A_11['четверг']['нем']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- НЕМЕЦКИЙ')
                    else:
                        text = ''
                        for item in homework_A_11['четверг']['нем']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- НЕМЕЦКИЙ')

                elif response == '[11А] - НА ПЯТНИЦУ - [11А]':

                    if not homework_A_11['пятница']['литра']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ЛИТРА')
                    else:
                        text = ''
                        for item in homework_A_11['пятница']['литра']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- ЛИТРА')

                    if not homework_A_11['пятница']['матан']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    'None <-- МАТАН')
                    else:
                        text = ''
                        for item in homework_A_11['пятница']['матан']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- МАТАН')

                    if not homework_A_11['пятница']['литра']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-ЛИТРА')
                    else:
                        text = ''
                        for item in homework_A_11['пятница']['литра']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- ЛИТРА')

                    if not homework_A_11['пятница']['англ']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    'None <-- АНГЛ')
                    else:
                        text = ''
                        for item in homework_A_11['пятница']['англ']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- АНГЛ')

            elif response[:5] == '[11В]':

                if response == '[11В] - НА ПОНЕДЕЛЬНИК - [11В]':

                    if not homework_V_11['понедельник']['англ']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- АНГЛ')
                    else:
                        text = ''
                        for item in homework_V_11['понедельник']['англ']:
                            for char in item:
                                 if char[11:17] == '[date]':
                                    break
                                 else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], text + '\n\n <-- АНГЛ')


                    if not homework_V_11['понедельник']['обж']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ОБЖ')
                    else:
                        text = ''
                        for item in homework_V_11['понедельник']['обж']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], text + '\n\n <-- ОБЖ')


                    if not homework_V_11['понедельник']['матан']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- МАТАН')
                    else:
                        text = ''
                        for item in homework_V_11['понедельник']['матан']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], text + '\n\n <-- МАТАН')


                    if not homework_V_11['понедельник']['физика']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ФИЗИКА')
                    else:
                        text = ''
                        for item in homework_V_11['понедельник']['физика']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], text + '\n\n <-- ФИЗИКА')

                    if not homework_V_11['понедельник']['литра']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ЛИТРА')
                    else:
                        text = ''
                        for item in homework_V_11['понедельник']['литра']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- ЛИТРА')


                    if not homework_V_11['понедельник']['химия']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ХИМИЯ')
                    else:
                        text = ''
                        for item in homework_V_11['понедельник']['химия']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- ХИМИЯ')

                elif response == '[11В] - НА ВТОРНИК - [11В]':

                    if not homework_V_11['вторник']['история']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ИСТОРИЯ')
                    else:
                        text = ''
                        for item in homework_V_11['вторник']['история']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- ИСТОРИЯ')

                    if not homework_V_11['вторник']['матан']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- МАТАН')
                    else:
                        text = ''
                        for item in homework_V_11['вторник']['матан']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- МАТАН')

                    if not homework_V_11['вторник']['химия']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ХИМИЯ')
                    else:
                        text = ''
                        for item in homework_V_11['вторник']['химия']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- ХИМИЯ')

                elif response == '[11В] - НА СРЕДУ - [11В]':

                    if not homework_V_11['среда']['англ']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- АНГЛ')
                    else:
                        text = ''
                        for item in homework_V_11['среда']['англ']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- АНГЛ')

                    if not homework_V_11['среда']['матан']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- МАТАН')
                    else:
                        text = ''
                        for item in homework_V_11['среда']['матан']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- МАТАН')

                    if not homework_V_11['среда']['био']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- БИО')
                    else:
                        text = ''
                        for item in homework_V_11['среда']['био']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- БИО')

                    if not homework_V_11['среда']['русский']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- РУССКИЙ')
                    else:
                        text = ''
                        for item in homework_V_11['среда']['русский']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- РУССКИЙ')

                    if not homework_V_11['среда']['литра']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ЛИТРА')
                    else:
                        text = ''
                        for item in homework_V_11['среда']['литра']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- ЛИТРА')

                elif response == '[11В] - НА ЧЕТВЕРГ - [11В]':

                    if not homework_V_11['четверг']['литра']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ЛИТРА')
                    else:
                        text = ''
                        for item in homework_V_11['четверг']['литра']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- ЛИТРА')

                    if not homework_V_11['четверг']['общество']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ОБЩЕСТВО')
                    else:
                        text = ''
                        for item in homework_V_11['четверг']['общество']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- ОБЩЕСТВО')

                    if not homework_V_11['четверг']['био']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- БИО')
                    else:
                        text = ''
                        for item in homework_V_11['четверг']['био']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- БИО')

                    if not homework_V_11['четверг']['история']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ИСТОРИЯ')
                    else:
                        text = ''
                        for item in homework_V_11['четверг']['история']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- ИСТОРИЯ')

                elif response == '[11В] - НА ПЯТНИЦУ - [11В]':

                    if not homework_V_11['пятница']['общество']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ОБЩЕСТВО')
                    else:
                        text = ''
                        for item in homework_V_11['пятница']['общество']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- ОБЩЕСТВО')

                    if not homework_V_11['пятница']['химия']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ХИМИЯ')
                    else:
                        text = ''
                        for item in homework_V_11['пятница']['химия']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- ХИМИЯ')

                    if not homework_V_11['пятница']['англ']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- АНГЛ')
                    else:
                        text = ''
                        for item in homework_V_11['пятница']['англ']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- АНГЛ')

                    if not homework_V_11['пятница']['матан']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- МАТАН')
                    else:
                        text = ''
                        for item in homework_V_11['пятница']['матан']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- МАТАН')

            elif response[:5] == '[11Г]':

                if response == '[11Г] - НА ПОНЕДЕЛЬНИК - [11Г]':

                    if not homework_G_11['понедельник']['химия']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ХИМИЯ')
                    else:
                        text = ''
                        for item in homework_G_11['понедельник']['химия']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- ХИМИЯ')

                    if not homework_G_11['понедельник']['био']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- БИО')
                    else:
                        text = ''
                        for item in homework_G_11['понедельник']['био']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- БИО')

                    if not homework_G_11['понедельник']['физика']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ФИЗИКА')
                    else:
                        text = ''
                        for item in homework_G_11['понедельник']['физика']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- ФИЗИКА')

                    if not homework_G_11['понедельник']['общество']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ОБЩЕСТВО')
                    else:
                        text = ''
                        for item in homework_G_11['понедельник']['общество']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- ОБЩЕСТВО')

                    if not homework_G_11['понедельник']['англ']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- АНГЛ')
                    else:
                        text = ''
                        for item in homework_G_11['понедельник']['англ']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- АНГЛ')


                elif response == '[11Г] - НА ВТОРНИК - [11Г]':

                    if not homework_G_11['вторник']['матан']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- МАТАН')
                    else:
                        text = ''
                        for item in homework_G_11['вторник']['матан']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- МАТАН')

                    if not homework_G_11['вторник']['история']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ИСТОРИЯ')
                    else:
                        text = ''
                        for item in homework_G_11['вторник']['история']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- ИСТОРИЯ')

                    if not homework_G_11['вторник']['литра']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ЛИТРА')
                    else:
                        text = ''
                        for item in homework_G_11['вторник']['литра']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- ЛИТРА')

                    if not homework_G_11['вторник']['русский']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- РУССКИЙ')
                    else:
                        text = ''
                        for item in homework_G_11['вторник']['русский']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- РУССКИЙ')

                    if not homework_G_11['вторник']['родной']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- РОДНОЙ')
                    else:
                        text = ''
                        for item in homework_G_11['вторник']['родной']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- РОДНОЙ')

                elif response == '[11Г] - НА СРЕДУ - [11Г]':

                    if not homework_G_11['среда']['литра']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ЛИТРА')
                    else:
                        text = ''
                        for item in homework_G_11['среда']['литра']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- ЛИТРА')

                    if not homework_G_11['среда']['англ']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- АНГЛ')
                    else:
                        text = ''
                        for item in homework_G_11['среда']['англ']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- АНГЛ')

                    if not homework_G_11['среда']['физика']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ФИЗИКА')
                    else:
                        text = ''
                        for item in homework_G_11['среда']['физика']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- ФИЗИКА')

                    if not homework_G_11['среда']['геогр']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ГЕОГР')
                    else:
                        text = ''
                        for item in homework_G_11['среда']['геогр']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- ГЕОГР')

                    if not homework_G_11['среда']['матан']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- МАТАН')
                    else:
                        text = ''
                        for item in homework_G_11['среда']['матан']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- МАТАН')

                elif response == '[11Г] - НА ЧЕТВЕРГ - [11Г]':

                    if not homework_G_11['четверг']['англ']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- АНГЛ')
                    else:
                        text = ''
                        for item in homework_G_11['четверг']['англ']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- АНГЛ')

                    if not homework_G_11['четверг']['литра']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ЛИТРА')
                    else:
                        text = ''
                        for item in homework_G_11['четверг']['литра']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- ЛИТРА')

                    if not homework_G_11['четверг']['русский']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- РУССКИЙ')
                    else:
                        text = ''
                        for item in homework_G_11['четверг']['русский']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- РУССКИЙ')

                    if not homework_G_11['четверг']['история']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ИСТОРИЯ')
                    else:
                        text = ''
                        for item in homework_G_11['четверг']['история']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- ИСТОРИЯ')

                    if not homework_G_11['четверг']['матан']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- МАТАН')
                    else:
                        text = ''
                        for item in homework_G_11['четверг']['матан']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- МАТАН')

                elif response == '[11Г] - НА ПЯТНИЦУ - [11Г]':

                    if not homework_G_11['пятница']['русский']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- РУССКИЙ')
                    else:
                        text = ''
                        for item in homework_G_11['пятница']['русский']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- РУССКИЙ')

                    if not homework_G_11['пятница']['обж']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ОБЖ')
                    else:
                        text = ''
                        for item in homework_G_11['пятница']['обж']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- ОБЖ')

                    if not homework_G_11['пятница']['инфа']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ИНФА')
                    else:
                        text = ''
                        for item in homework_G_11['пятница']['инфа']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- ИНФА')

                    if not homework_G_11['пятница']['общество']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- ОБЩЕСТВО')
                    else:
                        text = ''
                        for item in homework_G_11['пятница']['общество']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- ОБЩЕСТВО')

                    if not homework_G_11['пятница']['матан']:
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], 'None <-- МАТАН')
                    else:
                        text = ''
                        for item in homework_G_11['пятница']['матан']:
                            for char in item:
                                if char[11:17] == '[date]':
                                    break
                                else:
                                    text += char + ' '
                            text += '\n'
                        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'],
                                                                    text + '\n\n <-- МАТАН')

def MAIN(response, event, weekday, monitor_bells_access, yes, kb_added, from_dump, ANS):

    h = datetime.now().hour + 5
    m = datetime.now().minute
    s = datetime.now().second

    if h == 8 and m == 0 and s == 0:

        ALL_CLASSES_AND_FUNCTIONS.check_and_delete_hw()

    ALL_CLASSES_AND_FUNCTIONS.write_dumps(response, ANS, event)

    ALL_CLASSES_AND_FUNCTIONS.back(response, event)

    ALL_CLASSES_AND_FUNCTIONS.home_work.check_homework_and_print(response, event)

    ALL_CLASSES_AND_FUNCTIONS.home_work.write_homework(response, event, from_dump)

    ALL_CLASSES_AND_FUNCTIONS.home_work.open_homework_table(response, event)

    ALL_CLASSES_AND_FUNCTIONS.important.del_kb(response, yes, kb_added)

    ALL_CLASSES_AND_FUNCTIONS.important.update_bot(response, event)

    ALL_CLASSES_AND_FUNCTIONS.if_classes.class_(response, event)

    ALL_CLASSES_AND_FUNCTIONS.if_monitor.one_mon(response, event)

    ALL_CLASSES_AND_FUNCTIONS.choose_another_class(response, monitor_bells_access)

    ALL_CLASSES_AND_FUNCTIONS.important.piece(response, event)

    ALL_CLASSES_AND_FUNCTIONS.important.help(response, event)

    ALL_CLASSES_AND_FUNCTIONS.schedule.if_today(response, event, weekday)

    ALL_CLASSES_AND_FUNCTIONS.schedule.if_tomorrow(response, event, weekday)

    ALL_CLASSES_AND_FUNCTIONS.schedule.if_day(response, event, weekday)

    ALL_CLASSES_AND_FUNCTIONS.schedule.if_day_chosen(response, event)

    return response

ALL_CLASSES_AND_FUNCTIONS.data()

ALL_CLASSES_AND_FUNCTIONS.check_files()

ALL_CLASSES_AND_FUNCTIONS.wr_id_database()

def response_convert(event):

    if event.from_user:
        response = event.object['message']['text']
    elif event.from_chat:

        if event.object['message']['text'][:18] == f'[club{gr_id}|{gr_name}]':
            response = event.object['message']['text'][19:]
        elif event.object['message']['text'][:28] == f'[club{gr_id}|@{changed_gr_id}]':
            response = event.object['message']['text'][29:]

        else:
            response = event.object['message']['text']
    return response

def log(response, event):

    day = datetime.now().day
    month = datetime.now().month
    year = datetime.now().year

    h = datetime.now().hour + 5
    m = datetime.now().minute + 2
    s = datetime.now().second

    ANS =  'mess:[ '+ response + ' ]\tid:  vk.com/id' + str(event.obj['message']['from_id']) + '\t\t' + f'{h}:{m}:{s}' + f'{year}-{month}-{day}'
    print('mess:[ '+ response + ' ]\tid:  'f'vk.com/id{id}  \t\t', f'{h}:{m}:{s}', f'{year}-{month}-{day}')

    return ANS

def add_id(event):

    id = str(event.obj['message']['from_id'])
    id = f'vk.com/id{id}'
    with open('id_database.txt', 'r') as inp:
        inp = inp.read().split()
        if id not in id_database:
            id_database.append(id)
            with open('id_database.txt', 'a') as ouf:
                ouf.write(f'{id}\n')

while True:
    longpoll = VkBotLongPoll(bot_session, gr_id)

    try:
        for event in longpoll.listen():

            if event.type == VkBotEventType.MESSAGE_NEW:

                add_id(event)

                response = response_convert(event)

                response = MAIN(response, event, datetime.now().weekday(), monitor_bells_access, yes, kb_added, False, log(response, event))

                response = 'quit()'

    except KeyboardInterrupt:
        sys.exit()
    except requests.exceptions.ReadTimeout as timeout:
        continue
    except:
        ALL_CLASSES_AND_FUNCTIONS.main.send_message(event.obj['message']['peer_id'], '[ Someone summon the green rubbit...]\n       <      (vk server shuts down)     >')
        with open('err.txt', 'a') as ouf:
            ouf.write('Ошибка:\n' + traceback.format_exc())
            ALL_CLASSES_AND_FUNCTIONS.main.send_message(your_id, traceback.format_exc())
            os.system('python3 sending_traceback_to_email.py')
            os.system('./clear_traceback.txt')
