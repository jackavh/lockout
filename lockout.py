import time
import ctypes
from ctypes import wintypes
import datetime


def lock():
    """Locks the keyboard and mouse using ctypes.windll.user32.BlockInput. Undo with lockout.unblock()"""
    BlockInput = ctypes.windll.user32.BlockInput
    BlockInput.argtypes = [wintypes.BOOL]
    BlockInput.restype = wintypes.BOOL
    blocked = BlockInput(True)

    return blocked


def unlock():
    """Unlocks the keyboard and mouse using ctypes.windll.user32.BlockInput."""
    BlockInput = ctypes.windll.user32.BlockInput
    BlockInput.argtypes = [wintypes.BOOL]
    BlockInput.restype = wintypes.BOOL
    blocked = BlockInput(False)

    return blocked


def time_dist(t):
    """
    Calculates the amount of seconds until a datetime from now().
    Lower bound four integer return is 0.
    Ex, if distance is negative, return 0.
    Requires datetime module
    
    t: Distance to calculate from
    """
    start_date = datetime.datetime.now()
    end_date = t
    secs = int((end_date - start_date).total_seconds())

    return secs


def time_calc():
    """
    Returns the amount of seconds until 6AM tomorrow
    """
    start_date = datetime.datetime.now()
    end_date = start_date + datetime.timedelta(days=1)
    time_string = ("%d-%d-%d 06" % (end_date.year, end_date.month, end_date.day))
    adj_end_date = datetime.datetime.strptime(time_string, "%Y-%m-%d %H")
    t = int((adj_end_date - start_date).total_seconds())

    return t


class countdownTimer(object):
    """
    A class that keeps track of how many seconds have elapsed, counting down from seconds.
    """


    def __init__(self, secs):
        self.init_time = datetime.datetime.now()
        self.end_time = self.init_time + datetime.timedelta(seconds=secs)


    def get_init(self):
        return self.init_time

    
    def get_end(self):
        return self.end_time

    
    def remaining(self):
        """ Returns time remaining in seconds """
        return int((self.end_time - datetime.datetime.now()).total_seconds())


    def countdown(self):
        """ Returns a string formatted in 00:00:00, converted from self.remaining() """
        t = self.remaining()
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        str = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)

        return str