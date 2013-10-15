#-*- coding: utf-8 -*-

import os
import time
from daemon import runner


# Create the daemon object
def main():
    notifier = Runner()
    daemon_runner = runner.DaemonRunner(notifier)
    daemon_runner.do_action()


# Function to notify
def notification():
    os.system('notify-send \'1 hora de utilização\' \'Descansar.\'')


# Function to shows the succeed to activate the notification
def success():
    os.system('notify-send \'Notificador ativado\'')


class Runner():

    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path = '/tmp/foo.pid'
        self.pidfile_timeout = 5

    def run(self):
        success()
        while(True):
            time.sleep(3600)
            notification()


if __name__ == '__main__':
    main()
