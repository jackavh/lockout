import sys
import time
import ctypes
from ctypes import wintypes
import datetime


def lockout(t):
    """
    Locks out system for *t*, requires admin priv
    t: t in seconds to lockout
    """
    BlockInput = ctypes.windll.user32.BlockInput
    BlockInput.argtypes = [wintypes.BOOL]
    BlockInput.restype = wintypes.BOOL

    blocked = BlockInput(True)
    print("Blocking inputs for %d seconds" % t)
    countdown(t)
    blocked = BlockInput(False)
    print("Unblocking!")


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


def countdown(t):
    while t: 
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t-= 1


def __main__():
    t = time_calc()
    print("Lockout for " + str(t))
    confirm = input("Are you sure? Y/n: ")
    if confirm.casefold() == 'y':
        print()
        lockout(t)
    elif confirm == 'test':
        print()
        lockout(int(input("Test val: ")))
    else:
        sys.exit("Cancelled!")

__main__()