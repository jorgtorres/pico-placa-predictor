#!/usr/bin/env python
import datetime

class PicoYPlaca():
    def __init__(self, license, date, time):
        self.license = license
        self.date = date
        self.time = time

    def CanItBeOnRoad(self):
        moment = datetime.datetime.strptime("{0} {1}".format(self.date, self.time), '%Y-%m-%d %H:%M')
        last_digit = int(self.getLicense().strip()[-1])
        day = moment.weekday()
        if (moment.time() >= datetime.time(7, 0) and moment.time() <= datetime.time(9, 30)) \
        or (moment.time() >= datetime.time(16, 0) and moment.time() <= datetime.time(19, 30)):
            if (day == 0 and (last_digit == 1 or last_digit == 2)) or (day == 1 and (last_digit == 3 or last_digit == 4)) \
            or (day == 2 and (last_digit == 5 or last_digit == 6)) or (day == 3 and (last_digit == 7 or last_digit == 8)) \
            or (day == 4 and (last_digit == 9 or last_digit == 0)):
                return False
        return True

    def getLicense(self):
        return self.license